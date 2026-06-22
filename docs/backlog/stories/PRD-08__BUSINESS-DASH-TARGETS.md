# Business dashboards: owner Targets editor

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-TARGETS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want to set, apply and reset the targets my dashboard measures against, so that variance colouring and insights reflect the goals I actually set.
Plainly: the editable row of owner targets (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) that drives every tile's variance colouring and the Insights callouts. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that makes the comparison targets editable and persistent. Targets persist per clinic (the prototype's 'saved in this browser only' becomes real per-tenant persistence); the editor is owner-only (.fin).

## How it works

The Targets editor is the editable row of owner-set targets — MRR (Monthly Recurring Revenue) target, Active members, Conversion %, Retention %, Rebooking %, No-show max — with Apply targets / Reset controls. These targets are the comparison the whole dashboard measures against.
Targets persist as ClinicTarget per tenant — the prototype's 'saved in this browser only' becomes real per-clinic persistence. Applying re-colours every tile's variance (across the GROWTH/PERFORMANCE/FINANCE bands) and regenerates the Insights callouts so the whole screen reflects the goals the owner actually set. The editor is owner-only behind the owner-only financial (.fin) capability, and the note states figures are saved per clinic.

## Requirements

- To set, apply and reset the targets my dashboard measures against.

## Acceptance Criteria

- [ ] An editable row of owner targets (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) with Apply targets / Reset.
- [ ] Targets persist as ClinicTarget per tenant.
- [ ] Applying re-colours every tile's variance and regenerates the Insights callouts.
- [ ] The editor is owner-only (.fin); the note states figures are saved per clinic.

## UI designs / screenshots

- Prototype: Reports — the Targets editor row (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) with Apply targets / Reset.
- Applying re-colours every tile's variance and regenerates Insights; editor owner-only (.fin); the note states figures are saved per clinic (real per-tenant persistence).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **ClinicTarget** — tenant_id, mrr_target, active_member_target, conversion_target, retention_target, rebooking_target, no_show_ceiling
  - _Owner-set; persisted per tenant; drives variance colouring + Insights callouts across the bands._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Owner Targets editor (set, apply, reset; persisted per clinic)**
  Behaviour: an editable row of owner targets (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) with Apply targets / Reset. Requirements: persists ClinicTarget per tenant; applying re-colours every tile's variance and regenerates the Insights callouts; the editor is owner-only and the note states figures are saved per clinic (the prototype's 'saved in this browser only' becomes real per-tenant persistence).
