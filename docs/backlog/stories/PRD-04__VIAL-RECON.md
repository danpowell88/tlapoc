# Vial / unit reconciliation

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/VIAL-RECON`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a owner, I want vial/unit reconciliation across draws and wastage, so that stock, billing and the medicine register always agree.
Units drawn vs vial size + wastage must reconcile so stock, billing and the register agree (C8).

## How it works

Vial/unit reconciliation tracks units drawn vs vial size plus wastage, so stock, billing and the medicine register always agree. Each administration decrements the selected lot; discrepancies are surfaced and feed reporting (PRD-08).
Partial-vial handling is supported (one vial may treat several patients).

## Requirements

- Vial/unit reconciliation across draws and wastage.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
- [ ] Discrepancies are surfaced.
- [ ] Reconciliation data feeds reporting (PRD-08).
- [ ] Partial-vial handling is supported.

## UI designs / screenshots

- Prototype: Stock & medicines (stock.png) — per-lot on-hand vs received vs wasted columns; usage history; reconciliation surfaced when draws don't match.
- Charting finalise deducts charted units from the lot (see charting.png).

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockLedger** — id, lot_id, movement(receive|administer|waste|adjust), units, ref(administration_id?), at, actor_id
  - _Sum reconciles on_hand; partial-vial waste recorded; discrepancies flagged (C8)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - StockLedger — id, lot_id, movement(receive|administer|waste|adjust), units, ref(administration_id?), at, actor_id (Sum reconciles on_hand; partial-vial waste recorded; discrepancies flagged (C8).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
  - Rule: Discrepancies are surfaced.
  - Rule: Reconciliation data feeds reporting (PRD-08).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/ADMIN-GATE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C8 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
