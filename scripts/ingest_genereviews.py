#!/usr/bin/env python3
"""Crawl GeneReviews chapters from NCBI Bookshelf into the Medical LLM wiki.

Conservative mode:
- Stores concise, attributed raw extracts rather than full chapter reproduction.
- Creates one concise factual entity page per GeneReviews chapter.
- Adds source/copyright attribution to every raw and synthesized page.
- Is resumable via _meta/genereviews_ingest_state.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Tag

WIKI = Path(__file__).resolve().parents[1]
BASE_URL = "https://www.ncbi.nlm.nih.gov/books/NBK1116/?lang=es"
BOOK_CANONICAL = "https://www.ncbi.nlm.nih.gov/books/NBK1116/"
COPYRIGHT = "GeneReviews® chapters are owned by the University of Washington, Seattle, © 1993-2026. Source: NCBI Bookshelf/GeneReviews, https://www.ncbi.nlm.nih.gov/books/NBK1116/."
USER_AGENT = "Medical-LLM-wiki crawler (+https://www.ncbi.nlm.nih.gov/books/NBK1116/)"
STATE_PATH = WIKI / "_meta" / "genereviews_ingest_state.json"
RAW_DIR = WIKI / "raw" / "articles"
ENTITY_DIR = WIKI / "entities"

SKIP_TOC_TEXTS = {
    "Bookshelf", "Browse Titles", "Advanced", "Help", "Disclaimer", "Next >", "GeneReviews Advanced Search",
    "Glossary", "Resource Materials", "For Current/Prospective Authors", "here", "GeneReviews® Copyright Notice and Usage Disclaimer",
    "New in GeneReviews", "Author List", "Download/Link to GeneReviews", "Contact Us",
}

UTILITY_PATH_SEGMENTS = {
    "advanced", "helpadvsearch", "glossary", "resource_mats", "archived_chapters", "updates", "authors",
    "howto_linkin", "contact_us", "GRcopyright_permiss", "GRrevprocesses", "GRpersonnel",
}

UTILITY_TITLE_RE = re.compile(
    r"\b(?:gene(reviews)?\s+(advanced\s+search|copyright|resource|author|contact|download|link|help|updates)|"
    r"glossary|resource materials|for current/prospective authors|contact us|author list|download/link)\b",
    re.I,
)

TAG_SET = {"pathology", "diagnosis", "genetics", "therapeutics", "guideline", "evidence"}
# `genetics` is not currently in SCHEMA.md. The script will avoid it unless SCHEMA is updated.
ALLOWED_TAGS: set[str] = set()

@dataclass
class Chapter:
    title: str
    url: str
    slug_hint: str


def today() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d")


def now_stamp() -> str:
    return dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")


def slugify(text: str, max_len: int = 90) -> str:
    text = html.unescape(text)
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    text = re.sub(r"-+", "-", text)
    return text[:max_len].strip("-") or "untitled"


def yaml_quote(s: str) -> str:
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def req(url: str) -> requests.Response:
    r = requests.get(url, timeout=45, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()
    return r


def load_allowed_tags() -> set[str]:
    schema = (WIKI / "SCHEMA.md").read_text(encoding="utf-8")
    tags = set()
    for line in schema.splitlines():
        m = re.match(r"^-\s+([a-z0-9-]+)\s*$", line.strip())
        if m:
            tags.add(m.group(1))
    return tags


def toc_chapters() -> list[Chapter]:
    soup = BeautifulSoup(req(BASE_URL).text, "lxml")
    chapters: list[Chapter] = []
    seen = set()
    for a in soup.find_all("a", href=True):
        text = " ".join(a.get_text(" ", strip=True).split())
        href = a["href"]
        if not text or text in SKIP_TOC_TEXTS:
            continue
        if UTILITY_TITLE_RE.search(text):
            continue
        if "/books/n/gene/" not in href:
            continue
        url = urljoin("https://www.ncbi.nlm.nih.gov", href)
        parsed_path = urlparse(url).path.rstrip("/")
        path_parts = set(parsed_path.split("/"))
        path = parsed_path.split("/")[-1]
        if path in UTILITY_PATH_SEGMENTS or path.startswith("GR") or path_parts.intersection(UTILITY_PATH_SEGMENTS):
            continue
        key = (text, url)
        if key in seen:
            continue
        seen.add(key)
        # Slug hint from path segment if available.
        chapters.append(Chapter(text, url, path))
    return chapters


def clean_text(s: str) -> str:
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    # Remove citation-only bracket clutter from concise summaries.
    s = re.sub(r"\s*\[\s*[^\]]{1,120}\s*(?:et al|PubMed|PMC free article|CrossRef|Google Scholar|[0-9,\- ]+)\s*[^\]]{0,80}\]\s*", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def clean_author_text(s: str) -> str:
    s = clean_text(s)
    s = re.sub(r"\s+Email:.*$", "", s)
    s = re.sub(r"\s+(?:University|Hospital|Children's|Cone Health|Mission|Department|Division|Center|Centre|Clinic|Institute|School|College|Medical|Seattle|Greensboro|Asheville|Boston|New York|Philadelphia|Baltimore|Houston|Chicago|Los Angeles|San Francisco|London|Paris|Toronto|Vancouver|Australia|Netherlands|Germany|France|Italy|Spain|Japan|China|Korea|Canada|United Kingdom)\b.*$", "", s)
    s = re.sub(r"\s+,\s*([A-Z]{2,6})(?:\s|$).*", r", \1", s)
    return s.strip(" ,")


def element_text(el: Tag) -> str:
    for sup in el.find_all(["sup", "script", "style"]):
        sup.decompose()
    return clean_text(el.get_text(" ", strip=True))


def first_sentences(text: str, limit: int = 2, max_chars: int = 700) -> str:
    text = clean_text(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    out = " ".join(parts[:limit]).strip()
    if len(out) > max_chars:
        out = out[:max_chars].rsplit(" ", 1)[0].rstrip(".;,") + "."
    return out


def table_to_markdown(table: Tag, max_rows: int = 8) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [clean_text(c.get_text(" ", strip=True)) for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows[:max_rows]]
    header = rows[0]
    body = rows[1:]
    if not body:
        return ""
    def fmt(r): return "| " + " | ".join(c.replace("|", "\\|")[:180] for c in r) + " |"
    return "\n".join([fmt(header), "| " + " | ".join(["---"] * width) + " |"] + [fmt(r) for r in body])


def extract_chapter(ch: Chapter) -> dict:
    # Printable page is more stable for parsing, but final URL gives canonical NBK ID.
    r = req(ch.url.rstrip("/") + "/?report=printable")
    final = r.url.replace("?report=printable", "")
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.select_one("div.main-content") or soup.select_one("div.content") or soup.body
    if content is None:
        raise RuntimeError("Could not locate main content")
    title_el = content.find("h1")
    title = clean_text(title_el.get_text(" ", strip=True)) if title_el else ch.title
    body = content.select_one("div.body-content") or content

    # Publication metadata.
    all_text = clean_text(content.get_text(" ", strip=True))
    initial = re.search(r"Initial Posting:\s*([^.;]+)", all_text)
    last_update = re.search(r"Last Update:\s*([^.;]+)", all_text)
    authors = []
    for div in content.select("div.contrib"):
        t = clean_author_text(div.get_text(" ", strip=True))
        if t:
            authors.append(t)
    authors = authors[:6]

    sections: dict[str, list[str]] = {}
    current = None
    for node in body.descendants:
        if isinstance(node, Tag) and node.name in ["h2", "h3"]:
            current = clean_text(node.get_text(" ", strip=True)).rstrip(".")
            sections.setdefault(current, [])
        elif isinstance(node, Tag) and node.name == "p" and current:
            txt = element_text(node)
            if txt and not txt.startswith("View in own window"):
                sections.setdefault(current, []).append(txt)

    # Find useful table summaries.
    tables = []
    for div in body.select("div.table")[:6]:
        cap_el = div.select_one("div.caption") or div.find(["h3", "h4"])
        cap = clean_text(cap_el.get_text(" ", strip=True)) if cap_el else "Table"
        tbl = div.find("table")
        md = table_to_markdown(tbl) if tbl else ""
        if md:
            tables.append((cap, md))

    def sec_summary(name: str, fallback_names: Iterable[str] = ()) -> str:
        paras = []
        for key in (name, *fallback_names):
            for k, vals in sections.items():
                if k.lower() == key.lower() or k.lower().startswith(key.lower()):
                    paras.extend(vals)
                    break
        return first_sentences(" ".join(paras), 3, 900)

    summary = sec_summary("Summary")
    diagnosis = sec_summary("Diagnosis", ["Suggestive Findings", "Establishing the Diagnosis"])
    clinical = sec_summary("Clinical Characteristics", ["Clinical Description"])
    management = sec_summary("Management", ["Evaluations Following Initial Diagnosis", "Treatment of Manifestations", "Surveillance"])
    genetic_counseling = sec_summary("Genetic Counseling", ["Mode of Inheritance", "Risk to Family Members"])

    if not summary and not clinical:
        raise RuntimeError(f"Could not extract summary/clinical text for {title}")

    return {
        "toc_title": ch.title,
        "title": title,
        "source_url": final,
        "printable_url": r.url,
        "authors": authors,
        "initial_posting": clean_text(initial.group(1)) if initial else "",
        "last_update": clean_text(last_update.group(1)) if last_update else "",
        "summary": summary,
        "diagnosis": diagnosis,
        "clinical_characteristics": clinical,
        "management": management,
        "genetic_counseling": genetic_counseling,
        "tables": tables[:3],
    }


def raw_markdown(data: dict, raw_rel: str) -> str:
    body = []
    body.append(f"# {data['title']} — GeneReviews Extract")
    body.append("")
    body.append(f"Source URL: {data['source_url']}")
    body.append(f"Book source: {BOOK_CANONICAL}")
    body.append(f"Copyright/usage attribution: {COPYRIGHT}")
    if data.get("authors"):
        body.append(f"Authors: {', '.join(data['authors'])}")
    if data.get("initial_posting") or data.get("last_update"):
        body.append(f"Publication details: Initial posting {data.get('initial_posting') or 'not extracted'}; last update {data.get('last_update') or 'not extracted'}.")
    body.append("")
    body.append("This raw ingest is a concise factual extract prepared for noncommercial research/study wiki synthesis, not a full reproduction of the GeneReviews chapter.")
    body.append("")
    for heading, key in [
        ("Summary", "summary"),
        ("Diagnosis", "diagnosis"),
        ("Clinical Characteristics", "clinical_characteristics"),
        ("Management", "management"),
        ("Genetic Counseling", "genetic_counseling"),
    ]:
        if data.get(key):
            body.append(f"## {heading}")
            body.append(data[key])
            body.append("")
    for cap, md in data.get("tables", []):
        body.append(f"## Extracted Table: {cap}")
        body.append(md)
        body.append("")
    body_text = "\n".join(body).rstrip() + "\n"
    sha = hashlib.sha256(body_text.encode("utf-8")).hexdigest()
    fm = f"---\nsource_url: {data['source_url']}\ningested: {today()}\nsha256: {sha}\n---\n"
    return fm + body_text


def entity_markdown(data: dict, raw_rel: str, slug: str, existing_created: str | None = None) -> str:
    date = today()
    created = existing_created or date
    title = data["title"]
    sources = f"[{raw_rel}]"
    # Only use tags present in schema. genetics is intentionally omitted unless schema supports it.
    tags = ["pathology", "diagnosis", "therapeutics", "evidence"]
    tags = [t for t in tags if t in ALLOWED_TAGS]
    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f"created: {created}",
        f"updated: {date}",
        "type: entity",
        "tags: [" + ", ".join(tags) + "]",
        f"sources: {sources}",
        "confidence: medium",
        "clinical_evidence: educational",
        "regulatory_status: not-applicable",
        "---",
        "",
        f"# {title}",
        "",
        f"{title} is a GeneReviews-covered hereditary or genetic condition. This page summarizes a concise, attributed extract from GeneReviews for research and study context; it is not medical advice, diagnosis, or treatment guidance.",
        "",
        "## Source and attribution",
        "",
        f"- Primary source: GeneReviews chapter, {data['source_url']}",
        f"- Book source: {BOOK_CANONICAL}",
        f"- Copyright/usage attribution: {COPYRIGHT}",
    ]
    if data.get("authors"):
        lines.append(f"- Authors: {', '.join(data['authors'])}")
    if data.get("initial_posting") or data.get("last_update"):
        lines.append(f"- Publication details: initial posting {data.get('initial_posting') or 'not extracted'}; last update {data.get('last_update') or 'not extracted'}.")
    lines += ["", "## Overview", ""]
    lines.append(data.get("summary") or data.get("clinical_characteristics") or "GeneReviews provides disease-focused clinical, diagnostic, management, and genetic counseling information for this condition.")
    if data.get("clinical_characteristics"):
        lines += ["", "## Clinical characteristics", "", data["clinical_characteristics"]]
    if data.get("diagnosis"):
        lines += ["", "## Diagnosis", "", data["diagnosis"]]
    if data.get("management"):
        lines += ["", "## Management and surveillance", "", data["management"]]
    if data.get("genetic_counseling"):
        lines += ["", "## Genetic counseling", "", data["genetic_counseling"]]
    lines += [
        "",
        "## Related concepts",
        "",
        "- [[diagnosis]]",
        "- [[therapeutics]]",
        "- [[pathology]]",
        "",
        "## Notes",
        "",
        f"- This page is based on the raw extract `{raw_rel}` and links to the original GeneReviews source for full clinical detail.",
        "- Because the source is educational reference material, clinical decisions should rely on qualified professional judgment and current guidelines rather than this wiki summary alone.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def extract_created(path: Path) -> str | None:
    if not path.exists():
        return None
    txt = path.read_text(encoding="utf-8", errors="ignore")[:500]
    m = re.search(r"^created:\s*(\d{4}-\d{2}-\d{2})", txt, re.M)
    return m.group(1) if m else None


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"completed": {}, "failed": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def update_index_entry(entity_slug: str, title: str, summary: str) -> None:
    path = WIKI / "index.md"
    text = path.read_text(encoding="utf-8")
    entry = f"- [[{entity_slug}]] — {first_sentences(summary, 1, 170) or 'GeneReviews-covered hereditary or genetic condition.'}"
    # Remove existing entry for this slug.
    lines = [ln for ln in text.splitlines() if not ln.startswith(f"- [[{entity_slug}]]")]
    text = "\n".join(lines) + "\n"
    marker = "## Entities\n\n<!-- Alphabetical within section -->\n"
    if marker not in text:
        raise RuntimeError("index.md Entities marker not found")
    before, after = text.split(marker, 1)
    # Entities section ends before Concepts.
    ent_body, rest = after.split("\n## Concepts", 1)
    entries = [ln for ln in ent_body.splitlines() if ln.strip().startswith("- [[")]
    entries.append(entry)
    entries = sorted(set(entries), key=lambda s: s.lower())
    new_ent = "\n".join(entries)
    new_text = before + marker + ("\n" + new_ent + "\n" if new_ent else "") + "\n## Concepts" + rest
    # Update header count/date.
    page_count = 0
    for d in ["entities", "concepts", "comparisons", "queries"]:
        page_count += len(list((WIKI / d).glob("*.md")))
    new_text = re.sub(r"> Last updated: .*? \| Total pages: \d+", f"> Last updated: {today()} | Total pages: {page_count}", new_text)
    path.write_text(new_text, encoding="utf-8")


def append_log(title: str, source_url: str, raw_rel: str, entity_rel: str) -> None:
    path = WIKI / "log.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if f"Raw extract saved: `{raw_rel}`" in existing:
        return
    entry = f"\n## [{today()}] ingest | GeneReviews: {title}\n- Source: GeneReviews/NCBI Bookshelf chapter, {BOOK_CANONICAL}\n- Chapter URL: {source_url}\n- Raw extract saved: `{raw_rel}`\n- Created/updated entity page: `{entity_rel}`\n- Notes: Concise factual chapter summary with GeneReviews source and copyright attribution.\n"
    with path.open("a", encoding="utf-8") as f:
        f.write(entry)


def update_readme(title: str, raw_rel: str, entity_rel: str) -> None:
    path = WIKI / "README.md"
    text = path.read_text(encoding="utf-8")
    if f"`{raw_rel}`" in text:
        return
    if "## Ingest History" not in text:
        text += "\n## Ingest History\n"
    bullet = f"- {now_stamp()} — Ingested: GeneReviews chapter: {title}. Content: Concise factual summary of clinical characteristics, diagnosis, management, and genetic counseling context with source/copyright attribution. Updated: `{raw_rel}`, `{entity_rel}`, `index.md`, `log.md`."
    text = text.replace("## Ingest History\n\n", "## Ingest History\n\n" + bullet + "\n", 1)
    path.write_text(text, encoding="utf-8")


def process_chapter(ch: Chapter, force: bool = False) -> str:
    state = load_state()
    if not force and ch.url in state.get("completed", {}):
        return "skipped"
    data = extract_chapter(ch)
    slug = slugify(data["title"])
    raw_rel = f"raw/articles/genereviews-{slug}.md"
    ent_rel = f"entities/{slug}.md"
    raw_path = WIKI / raw_rel
    ent_path = WIKI / ent_rel
    raw_path.write_text(raw_markdown(data, raw_rel), encoding="utf-8")
    ent_path.write_text(entity_markdown(data, raw_rel, slug, extract_created(ent_path)), encoding="utf-8")
    update_index_entry(slug, data["title"], data.get("summary") or data.get("clinical_characteristics") or "")
    append_log(data["title"], data["source_url"], raw_rel, ent_rel)
    update_readme(data["title"], raw_rel, ent_rel)
    state.setdefault("completed", {})[ch.url] = {"title": data["title"], "slug": slug, "when": now_stamp(), "source_url": data["source_url"]}
    state.get("failed", {}).pop(ch.url, None)
    save_state(state)
    return data["title"]


def verify_wiki_quick() -> None:
    bad_hash = []
    for p in (WIKI / "raw").rglob("*.md"):
        txt = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
        if not m:
            continue
        fm, body = m.groups()
        hm = re.search(r"^sha256:\s*([a-f0-9]+)", fm, re.M)
        if hm and hashlib.sha256(body.encode("utf-8")).hexdigest() != hm.group(1):
            bad_hash.append(str(p.relative_to(WIKI)))
    pages = {p.stem: p for d in ["entities", "concepts", "comparisons", "queries"] for p in (WIKI / d).glob("*.md")}
    broken = []
    for p in pages.values():
        for link in re.findall(r"\[\[([^\]|#]+)", p.read_text(encoding="utf-8")):
            if link not in pages:
                broken.append((str(p.relative_to(WIKI)), link))
    idx = (WIKI / "index.md").read_text(encoding="utf-8")
    indexed = set(re.findall(r"\[\[([^\]]+)\]\]", idx))
    missing = [str(p.relative_to(WIKI)) for slug, p in pages.items() if slug not in indexed]
    if bad_hash or broken or missing:
        raise RuntimeError(f"verification failed: bad_hash={bad_hash[:5]}, broken={broken[:5]}, missing_index={missing[:5]}")


def git_commit_push_chapter(title: str, raw_rel: str, ent_rel: str) -> None:
    verify_wiki_quick()
    paths = ["README.md", "index.md", "log.md", "_meta/genereviews_ingest_state.json", raw_rel, ent_rel]
    subprocess.run(["git", "add", *paths], cwd=WIKI, check=True)
    diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=WIKI)
    if diff_check.returncode == 0:
        return
    safe_title = title.replace("\n", " ")[:80]
    subprocess.run(["git", "commit", "-m", f"docs: ingest GeneReviews chapter {safe_title}"], cwd=WIKI, check=True)
    subprocess.run(["git", "push", "origin", "HEAD"], cwd=WIKI, check=True)


def main() -> int:
    global ALLOWED_TAGS
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.5)
    ap.add_argument("--commit-each", action="store_true")
    args = ap.parse_args()
    ALLOWED_TAGS = load_allowed_tags()
    chapters = toc_chapters()
    if args.list:
        for i, ch in enumerate(chapters):
            print(f"{i+1}\t{ch.title}\t{ch.url}")
        print(f"TOTAL\t{len(chapters)}")
        return 0
    subset = chapters[args.start:]
    if args.limit is not None:
        subset = subset[:args.limit]
    state = load_state()
    for ch in subset:
        try:
            result = process_chapter(ch, force=args.force)
            if result == "skipped":
                print(f"Skipped completed chapter {ch.title}", flush=True)
            else:
                print(f"Completed the chapter {result}", flush=True)
                if args.commit_each:
                    slug = slugify(result)
                    git_commit_push_chapter(result, f"raw/articles/genereviews-{slug}.md", f"entities/{slug}.md")
                    print(f"Committed and pushed the chapter {result}", flush=True)
            time.sleep(args.sleep)
        except Exception as e:
            state = load_state()
            state.setdefault("failed", {})[ch.url] = {"title": ch.title, "error": repr(e), "when": now_stamp()}
            save_state(state)
            print(f"ERROR processing chapter {ch.title}: {e}", file=sys.stderr, flush=True)
            return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
