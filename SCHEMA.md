# Wiki Schema

## Domain

Medical LLMs and clinical AI systems: medical foundation models, clinical language-model applications, healthcare agents, biomedical evaluation benchmarks, medical datasets, safety and regulatory issues, deployment patterns, and evidence about performance in real-world care settings.

The wiki is for research synthesis and engineering context. It is not a source of medical advice, diagnosis, or treatment recommendations.

## Conventions

- Language: all wiki pages and raw ingests should be stored in English. Translate non-English sources to English before writing them into the wiki.
- File names: lowercase, kebab-case, no spaces (for example, `clinical-llm-evaluation.md`).
- Every wiki page starts with YAML frontmatter matching the schema below.
- Use `[[wikilinks]]` to connect pages. Each non-stub wiki page should have at least 2 outbound links when possible.
- Wikilinks should use filename slugs, not display-title aliases, unless the link scanner is updated to normalize aliases.
- When updating a page, bump the `updated` date.
- Every new page must be added to `index.md` under the correct section, alphabetically.
- Every action must be appended to `log.md`.
- Preserve raw sources as immutable evidence. Do not edit files under `raw/` after ingest; corrections belong in entity, concept, comparison, or query pages.
- For medical claims, distinguish reported benchmark results, retrospective findings, prospective clinical evidence, regulatory claims, and expert opinion.
- Do not present model outputs or wiki syntheses as clinical recommendations. Flag patient-safety, privacy, and regulatory uncertainty explicitly.
- Provenance markers: on pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]` or `^[raw/papers/source-file.md]` at the end of paragraphs whose claims come from a specific source. Optional on single-source pages where the `sources:` frontmatter is enough.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
clinical_evidence: none | benchmark | retrospective | prospective | deployed
regulatory_status: unknown | research | cleared | approved | non-medical
---
```

Use `confidence: low` or `medium` for single-source, opinion-heavy, fast-moving, or clinically sensitive claims. Use `clinical_evidence` to clarify whether claims are backed only by benchmark studies or by clinical deployment/evaluation evidence.

### Raw source frontmatter

Raw sources must include a small frontmatter block so re-ingests can detect drift:

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content body below this frontmatter>
---
```

Compute `sha256` over the body only, not the frontmatter. On re-ingest of the same URL, recompute and compare before updating.

## Tag Taxonomy

Every tag used in page frontmatter must appear here. Add new tags to this taxonomy before using them.

### Models and systems
- model
- foundation-model
- multimodal
- agent
- clinical-decision-support
- medical-device

### Clinical and biomedical scope
- clinical-workflow
- diagnosis
- triage
- documentation
- patient-communication
- biomedical-research
- radiology
- pathology
- genomics
- pharmacology

### Data and evaluation
- dataset
- benchmark
- evaluation
- evidence
- validation
- bias
- robustness

### Safety, governance, and deployment
- safety
- privacy
- security
- regulation
- compliance
- deployment
- monitoring
- human-factors

### Organizations and people
- company
- lab
- hospital
- regulator
- person
- open-source

### Methods and infrastructure
- training
- fine-tuning
- retrieval
- prompting
- inference
- interoperability
- standards

### Meta
- comparison
- timeline
- controversy
- prediction
- query
- survey

## Page Thresholds

- Create a page when an entity, model, dataset, benchmark, clinical workflow, regulatory issue, or concept appears in 2+ sources, or is central to one important source.
- Add to an existing page when a source mentions something already covered.
- Do not create pages for passing mentions, minor product names, isolated institutions, or out-of-domain medical details unless they are central to medical LLM usage.
- Split a page when it exceeds about 200 lines, or when it mixes distinct clinical, technical, and regulatory topics.
- Archive a page when its content is fully superseded: move it to `_archive/`, remove it from `index.md`, and update inbound links.

## Entity Pages

One page per notable entity: model, system, organization, dataset, benchmark, regulator, person, or major project. Include:

- Overview / what it is
- Key facts and dates
- Evidence level and limitations
- Relationships to other entities via `[[wikilinks]]`
- Source references

## Concept Pages

One page per concept or topic. Include:

- Definition / explanation
- Relevance to medical LLMs or clinical AI
- Current state of knowledge
- Safety, privacy, regulatory, and clinical-evidence considerations where relevant
- Open questions or debates
- Related concepts via `[[wikilinks]]`

## Comparison Pages

Side-by-side analyses. Include:

- What is being compared and why
- Dimensions of comparison, preferably as a table
- Evidence basis and limits
- Practical implications
- Verdict or synthesis
- Sources

## Query Pages

Save only substantial answers that would be painful to re-derive. Query pages should include:

- The question answered
- Short synthesis
- Pages and sources consulted
- Open uncertainties

## Update Policy

When new information conflicts with existing content:

1. Check publication and access dates. Newer sources may supersede older ones, but clinical claims require stronger evidence than recency alone.
2. If genuinely contradictory, note both positions with dates and sources.
3. Mark unresolved contradictions in frontmatter with `contested: true` and `contradictions: [page-slug]`.
4. Prefer cautious language for clinical performance, safety, and regulatory claims.
5. Flag contradictions and low-confidence clinical claims in lint reports.

## Recommended Seed Topics

Good first pages or ingests include:

- Medical LLM evaluation benchmarks and their limitations
- Clinical deployment patterns for LLMs
- Safety risks in medical LLMs
- Privacy and data-governance issues
- Multimodal medical foundation models
- Regulatory pathways for AI/ML-enabled medical devices
