---
title: Mass Casualty Triage
created: 2026-05-26
updated: 2026-05-26
type: concept
tags: [triage, clinical-workflow, safety, human-factors, deployment]
sources: [raw/articles/ems-zones-of-care-statpearls-2025.md]
confidence: medium
clinical_evidence: none
regulatory_status: unknown
---

# Mass Casualty Triage

Mass casualty triage is the prioritization and routing of patients when incident scale, hazards, or resource constraints exceed ordinary care capacity. In high-threat prehospital incidents, formal triage may occur only after casualties reach a safer Cold Zone; Hot and Warm Zone activity prioritizes extraction and immediate life-saving interventions. This makes mass casualty triage tightly connected to [[ems-zones-of-care]] and [[clinical-workflow-in-high-threat-care]].

## AI-relevant considerations

For medical LLMs and clinical AI, mass casualty triage raises distinct design and safety issues:

- Triage recommendations must reflect operational context, not just patient-level clinical severity.
- Systems should separate Hot/Warm Zone life-saving priorities from Cold Zone formal triage and transport planning.
- Handoff summaries should preserve interventions already performed under duress, such as tourniquets, airway maneuvers, chest seals, or needle decompression.
- Patient tracking and family reunification workflows may require coordination across EMS, fire services, hospitals, and incident command.
- Lower-acuity transport decisions may be system-level decisions intended to avoid overwhelming nearby facilities.

## Evidence and limitations

The current source is a StatPearls educational review of EMS zones of care. It provides workflow context but does not evaluate any medical LLM or clinical AI tool. Claims on this page should therefore be treated as background for designing or evaluating AI systems in emergency-care workflows.

## Related pages

- [[ems-zones-of-care]]
- [[clinical-workflow-in-high-threat-care]]
