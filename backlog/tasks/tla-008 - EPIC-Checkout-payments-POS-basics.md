---
id: TLA-008
title: 'EPIC: Checkout & payments (POS basics)'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - 'area:api'
  - mvp
  - 'milestone:M4'
dependencies: []
references:
  - docs/prds/PRD-06-payments-memberships-rewards.md
priority: high
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Closing out a visit: take payment in person at the front desk, produce an invoice/receipt, and tie the transaction to the visit and client. The minimum needed for staff to check a client out after treatment — in-person card/cash tender, itemised charges (service + any products/units), refunds/voids, and an end-of-day view. Memberships, autopay, packages and loyalty are a separate later epic.

Derived from the in-person POS subset of PRD-06. Money figures honour the owner-only financial-gating rule.

**MVP:** yes (basic checkout only). **Surface:** web (staff) · API · payments provider (Square AU). Compliance: C9, C23.
<!-- SECTION:DESCRIPTION:END -->
