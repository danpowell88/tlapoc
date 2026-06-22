---
id: TLA-006
title: 'EPIC: Consult, prescribing & S4 medicines'
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
  - docs/prds/PRD-04-consult-prescribing-s4.md
priority: high
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The clinical and regulatory moat. The prescriber consult that authorises treatment, the prescription record, the product catalogue, and Schedule-4 (prescription-only) medicines governance: custody and storage of S4 stock, cold-chain monitoring, stock movements, batch tracking, recall lookup/execution, and destruction records. Bookings for injectables cannot proceed to charting without a valid consult by an authorised prescriber.

Derived from PRD-04 — the highest-risk, highest-differentiation area. Hardware monitors (fridge temp, S4 cabinet) feed cold-chain and custody.

**MVP:** yes. **Surface:** web (staff/prescriber) · API · hardware feeds. Compliance: C1, C2, C7, C8, C11, C13, C15, C16, C17.
<!-- SECTION:DESCRIPTION:END -->
