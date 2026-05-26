# Medical LLM Wiki

An Obsidian-compatible markdown knowledge base for medical LLMs and clinical AI systems.

This repository uses the Karpathy-style LLM wiki pattern: raw sources are preserved, synthesized pages are interlinked, and the index/log keep the knowledge base navigable over time.

## Scope

The wiki covers medical LLMs and clinical AI systems, including:

- medical foundation models and multimodal clinical AI systems
- clinical language-model applications and healthcare agents
- biomedical datasets, benchmarks, and evaluation methods
- safety, privacy, bias, robustness, and monitoring concerns
- regulatory and deployment considerations for clinical settings
- evidence about performance in real-world care workflows

This wiki is for research and engineering synthesis. It is not medical advice, diagnosis, or treatment guidance.

## Start Here

- `SCHEMA.md` — domain, frontmatter, tag taxonomy, and operating rules
- `index.md` — catalog of wiki pages
- `log.md` — append-only activity log
- `raw/` — immutable ingested sources
- `entities/` — models, organizations, datasets, benchmarks, regulators, and other entities
- `concepts/` — medical LLM concepts and topic pages
- `comparisons/` — side-by-side analyses
- `queries/` — saved substantial query answers

## Repository Layout

```text
.
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/
├── concepts/
├── comparisons/
├── queries/
├── _meta/
└── _archive/
```

## Conventions

- Store wiki pages and raw ingests in English. Translate non-English sources before writing them into the wiki.
- Use lowercase kebab-case filenames, for example `clinical-llm-evaluation.md`.
- Preserve raw sources as immutable evidence under `raw/`.
- Add synthesized pages to `index.md` and append every meaningful action to `log.md`.
- Use Obsidian-style `[[wikilinks]]` for cross-references.

## Ingest History

- 2026-05-26 15:12 CST — Ingested: EMS Zones of Care (StatPearls/NCBI Bookshelf). Content: EMS Hot/Warm/Cold zones of care and their implications for high-threat clinical workflow, mass casualty triage, and clinical AI safety constraints. Updated: `raw/articles/ems-zones-of-care-statpearls-2025.md`, `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, `concepts/mass-casualty-triage.md`, `index.md`, `log.md`.
