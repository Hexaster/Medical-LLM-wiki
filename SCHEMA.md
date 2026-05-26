# Wiki Schema

## Domain

This is an LLM-generated and LLM-maintained wiki about medicine and healthcare. The phrase "LLM wiki" describes the maintenance method, not the subject matter: pages should explain medical topics themselves rather than forcing an artificial connection to medical LLMs or clinical AI.

The wiki covers medicine broadly, including anatomy, physiology, pathology, diseases, symptoms, diagnostics, therapeutics, procedures, emergency care, clinical workflows, public health, biomedical science, medical devices, health systems, and evidence used in clinical or health-related decision-making.

The wiki is for research synthesis and study context. It is not a source of medical advice, diagnosis, or treatment recommendations.

## Conventions

- Language: all wiki pages and raw ingests should be stored in English. Translate non-English sources to English before writing them into the wiki.
- File names: lowercase, kebab-case, no spaces (for example, `mass-casualty-triage.md`).
- Every wiki page starts with YAML frontmatter matching the schema below.
- Use `[[wikilinks]]` to connect pages. Each non-stub wiki page should have at least 2 outbound links when possible.
- Wikilinks should use filename slugs, not display-title aliases, unless the link scanner is updated to normalize aliases.
- When updating a page, bump the `updated` date.
- Every new page must be added to `index.md` under the correct section, alphabetically.
- Every meaningful action must be appended to `log.md`.
- Preserve raw sources as immutable evidence. Do not edit files under `raw/` after ingest; corrections belong in entity, concept, comparison, or query pages.
- For medical claims, distinguish guideline recommendations, review summaries, retrospective findings, prospective clinical evidence, expert opinion, and operational practice.
- Do not present model outputs or wiki syntheses as clinical recommendations. Flag patient-safety, privacy, and regulatory uncertainty explicitly when relevant.
- Do not add sections about relevance to LLMs, AI, or automation unless the source or page topic is explicitly about AI/LLMs.
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
clinical_evidence: none | educational | guideline | retrospective | prospective | systematic-review
regulatory_status: unknown | not-applicable | cleared | approved | restricted | withdrawn
---
```

Use `confidence: low` or `medium` for single-source, opinion-heavy, fast-moving, or clinically sensitive claims. Use `clinical_evidence` to clarify whether claims are backed by educational summaries, guidelines, retrospective studies, prospective trials, systematic reviews, or no direct clinical evidence.

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

### Clinical domains and body systems
- anatomy
- physiology
- pathology
- diagnosis
- symptoms
- therapeutics
- pharmacology
- surgery
- radiology
- pathology-lab
- emergency-medicine
- critical-care
- primary-care
- public-health

### Care delivery and operations
- clinical-workflow
- triage
- prehospital-care
- mass-casualty-care
- patient-safety
- infection-control
- documentation
- patient-communication
- care-coordination
- human-factors
- deployment

### Evidence and research
- evidence
- guideline
- systematic-review
- clinical-trial
- retrospective-study
- epidemiology
- biomedical-research
- uncertainty

### Safety, governance, and regulation
- safety
- privacy
- security
- regulation
- compliance
- medical-device
- ethics

### Organizations and people
- hospital
- regulator
- professional-society
- public-health-agency
- company
- lab
- person

### Methods, standards, and infrastructure
- measurement
- scoring-system
- protocol
- standards
- interoperability
- monitoring

### Meta
- comparison
- timeline
- controversy
- prediction
- query
- survey

## Page Thresholds

- Create a page when a disease, symptom, diagnostic method, treatment, procedure, clinical workflow, guideline, organization, biomedical concept, public-health topic, or medically relevant entity appears in 2+ sources, or is central to one important source.
- Add to an existing page when a source mentions something already covered.
- Do not create pages for passing mentions, minor product names, isolated institutions, or details outside medicine/healthcare unless they are central to the source being ingested.
- Split a page when it exceeds about 200 lines, or when it mixes distinct clinical, biological, operational, and regulatory topics.
- Archive a page when its content is fully superseded: move it to `_archive/`, remove it from `index.md`, and update inbound links.

## Entity Pages

One page per notable entity: disease, procedure, drug, device, organization, dataset, guideline, regulator, person, or major project. Include:

- Overview / what it is
- Key facts and dates when relevant
- Evidence level and limitations
- Relationships to other entities via `[[wikilinks]]`
- Source references

## Concept Pages

One page per concept or topic. Include:

- Definition / explanation
- Current state of knowledge
- Clinical, biological, operational, or public-health significance where relevant
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

1. Check publication, guideline, and access dates. Newer sources may supersede older ones, but clinical claims require stronger evidence than recency alone.
2. If genuinely contradictory, note both positions with dates and sources.
3. Mark unresolved contradictions in frontmatter with `contested: true` and `contradictions: [page-slug]`.
4. Prefer cautious language for clinical performance, safety, and regulatory claims.
5. Flag contradictions and low-confidence clinical claims in lint reports.

## Recommended Seed Topics

Good first pages or ingests include:

- Core anatomy and physiology concepts
- Common diseases and syndromes
- Diagnostic tests and interpretation principles
- Treatment classes and mechanisms
- Emergency and prehospital care workflows
- Public-health topics and surveillance concepts
- Clinical guidelines and evidence hierarchies
