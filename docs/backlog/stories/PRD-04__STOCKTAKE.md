# Stocktake, discrepancy & loss/theft reporting

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCKTAKE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a owner, I want to run a stocktake and have discrepancies surfaced with a loss/theft reporting path, so that stock integrity is provable and losses are reported.

Stocktakes and discrepancy handling, with loss/theft reporting, close the medicines-governance loop (C17).

## Requirements

- To run a stocktake and have discrepancies surfaced with a loss/theft reporting path.
- Traces to requirement(s): REQ-MED-10.
- Must satisfy compliance obligation(s): C17.

## Acceptance Criteria

- [ ] A stocktake compares expected vs counted stock per lot.
- [ ] Discrepancies are recorded; a discrepancy can trigger a loss/theft report.
- [ ] Expiry alerts surface near-expiry lots.
- [ ] Stocktake results feed the compliance dashboard (PRD-08).

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/CUSTODY-STORAGE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/STOCKTAKE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C17.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C17); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
