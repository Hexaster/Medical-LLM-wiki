# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, merge
> When this file exceeds 500 entries, rotate: rename to `log-YYYY.md` and start fresh.

## [2026-05-26] update | Correct wiki scope
- Corrected repository scope: this is an LLM-generated and LLM-maintained wiki about medicine and healthcare, not a wiki primarily about medical LLMs or clinical AI.
- Updated operating rules in `SCHEMA.md` and `README.md` to prevent irrelevant LLM/AI framing.
- Removed irrelevant LLM/AI relevance sections from `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, and `concepts/mass-casualty-triage.md`.
- Updated navigation summaries in `index.md`.

## [2026-05-26] ingest | EMS Zones of Care
- Source: https://www.ncbi.nlm.nih.gov/books/NBK436017/
- Raw source saved: `raw/articles/ems-zones-of-care-statpearls-2025.md`
- Created concept pages: `concepts/ems-zones-of-care.md`, `concepts/clinical-workflow-in-high-threat-care.md`, `concepts/mass-casualty-triage.md`
- Updated navigation: `index.md`
- Notes: Source is StatPearls educational content about EMS Hot/Warm/Cold zones of care. It was integrated as medical workflow context for high-threat prehospital care and mass casualty triage.

## [2026-05-26] create | Medical LLM wiki initialized
- Domain: LLM-generated and LLM-maintained wiki about medicine and healthcare.
- Location: `/home/zzz010122/Medical-LLM-wiki`
- Structure created with `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `_meta/`, and `_archive/`.
- Convention: store wiki content and raw ingests in English; translate non-English sources before writing them.
