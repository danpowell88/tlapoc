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

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C17); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
