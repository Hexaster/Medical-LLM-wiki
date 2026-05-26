# Medical LLM Wiki

An Obsidian-compatible markdown knowledge base about medicine and healthcare, generated and maintained using the LLM wiki pattern.

This repository uses the Karpathy-style LLM wiki pattern: raw sources are preserved, synthesized pages are interlinked, and the index/log keep the knowledge base navigable over time.

## Scope

The wiki covers medicine and healthcare broadly, including:

- anatomy, physiology, pathology, diseases, symptoms, and syndromes
- diagnostics, therapeutics, procedures, drugs, and medical devices
- emergency medicine, prehospital care, clinical workflows, and health-system operations
- public health, epidemiology, biomedical science, and health policy
- clinical guidelines, evidence hierarchies, patient safety, regulation, and ethics

"LLM wiki" describes how the wiki is generated and maintained. It does not mean the wiki is primarily about medical LLMs. Pages should focus on the medical topic itself unless the source or topic is explicitly about AI/LLMs.

This wiki is for research and study synthesis. It is not medical advice, diagnosis, or treatment guidance.

## Start Here

- `SCHEMA.md` — domain, frontmatter, tag taxonomy, and operating rules
- `index.md` — catalog of wiki pages
- `log.md` — append-only activity log
- `raw/` — immutable ingested sources
- `entities/` — diseases, drugs, procedures, organizations, guidelines, regulators, devices, and other entities
- `concepts/` — medical concepts and topic pages
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
- Use lowercase kebab-case filenames, for example `mass-casualty-triage.md`.
- Preserve raw sources as immutable evidence under `raw/`.
- Add synthesized pages to `index.md` and append every meaningful action to `log.md`.
- Use Obsidian-style `[[wikilinks]]` for cross-references.
- Do not add LLM/AI relevance sections unless the source or topic is explicitly about AI/LLMs.

## Ingest History

- 2026-05-26 15:12 CST — Ingested: EMS Zones of Care (StatPearls/NCBI Bookshelf). Content: EMS Hot/Warm/Cold zones of care and their implications for high-threat clinical workflow and mass casualty triage. Updated: `raw/articles/ems-zones-of-care-statpearls-2025.md`, `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, `concepts/mass-casualty-triage.md`, `index.md`, `log.md`.
