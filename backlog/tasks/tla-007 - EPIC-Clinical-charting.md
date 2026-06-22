---
id: TLA-007
title: 'EPIC: Clinical charting'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - 'area:api'
  - mvp
  - compliance
  - 'milestone:M3'
dependencies: []
references:
  - docs/prds/PRD-05-clinical-charting.md
priority: high
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The treatment record itself. Injection mapping (where, what product, how many units/mL, which batch) on a body/face canvas, before/after photography, the structured treatment note, and aftercare. The charting captures what was actually administered and ties each unit back to the S4 batch it came from.

Derived from PRD-05. Built on the consult/prescribing epic (what was authorised) and feeds reporting and recall (what was given, to whom, from which batch).

**MVP:** yes. **Surface:** web (staff) · provider app (chairside) · API. Compliance: C8, C12, C14.
<!-- SECTION:DESCRIPTION:END -->
