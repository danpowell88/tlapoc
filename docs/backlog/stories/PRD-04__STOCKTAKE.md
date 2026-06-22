# Stocktake, discrepancy & loss/theft reporting

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCKTAKE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want to run a stocktake and have discrepancies surfaced with a loss/theft reporting path, so that stock integrity is provable and losses are reported.
Stocktakes and discrepancy handling, with loss/theft reporting, close the medicines-governance loop (C17).

## How it works

Stocktakes compare expected vs counted stock per lot; discrepancies are recorded and a discrepancy can trigger a loss/theft report. Near-expiry lots surface via expiry alerts. Results feed the compliance dashboard (C17).
Keeps stock integrity provable and losses reported.

## Requirements

- To run a stocktake and have discrepancies surfaced with a loss/theft reporting path.
- Compliance: [C17](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A stocktake compares expected vs counted stock per lot.
- [ ] Discrepancies are recorded; a discrepancy can trigger a loss/theft report.
- [ ] Expiry alerts surface near-expiry lots.
- [ ] Stocktake results feed the compliance dashboard (PRD-08).

## UI designs / screenshots

- Prototype: Stock & medicines (stock.png) — a stocktake action comparing counted vs expected per lot; discrepancies highlighted with a loss/theft report path; expiry alerts on near-expiry lots.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **Stocktake** — id, tenant_id, at, actor_id, lines[]{lot_id, expected, counted, variance}
  - _Variance -> discrepancy._
- **LossReport** — id, stocktake_id, lot_id, units, kind(loss|theft), reported_at
  - _Triggerable from a discrepancy (C17)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Stocktake — id, tenant_id, at, actor_id, lines[]{lot_id, expected, counted, variance} (Variance -> discrepancy.)
  - LossReport — id, stocktake_id, lot_id, units, kind(loss|theft), reported_at (Triggerable from a discrepancy (C17).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A stocktake compares expected vs counted stock per lot.
  - Rule: Discrepancies are recorded; a discrepancy can trigger a loss/theft report.
  - Rule: Expiry alerts surface near-expiry lots.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/CUSTODY-STORAGE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C17 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
