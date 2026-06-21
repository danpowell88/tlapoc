# Custody & secure storage

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CUSTODY-STORAGE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/STOCK-RECEIVE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a owner, I want stock custody limited to an on-site prescriber and bound to a secure, access-logged location, so that S4 custody meets the exclusive-custody rule.

Only NP/prescriber roles may take custody; stock is bound to a secure, access-logged location. Mode-A custodian must physically work at the clinic with exclusive custody (C7/C15).

## Requirements

- Stock custody limited to an on-site prescriber and bound to a secure, access-logged location.
- Traces to requirement(s): REQ-MED-2, REQ-MED-8.
- Must satisfy compliance obligation(s): C7, C15.

## Acceptance Criteria

- [ ] Only NP/prescriber roles can take custody of stock.
- [ ] Stock is bound to a secure location; access is logged.
- [ ] A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.
- [ ] A remote prescriber consigning stock is flagged non-compliant.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/STOCK-RECEIVE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/CUSTODY-STORAGE.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C7, C15.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C7, C15); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
