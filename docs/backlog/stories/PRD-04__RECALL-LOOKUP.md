# Lot → clients recall lookup & medicine register

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/RECALL-LOOKUP`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a prescriber/owner, I want to enter a lot number and instantly see every client who received it, plus export the medicine register, so that we can run a recall in minutes and evidence the register.

Given a lot, the system must instantly list every client/administration for that lot, and export an audit-ready medicine register (C8).

## Requirements

- To enter a lot number and instantly see every client who received it, plus export the medicine register.
- Traces to requirement(s): REQ-MED-4.
- Must satisfy compliance obligation(s): C8.

## Acceptance Criteria

- [ ] A lot lookup returns all clients/administrations for that lot.
- [ ] The S4 register exports a complete, immutable record of administrations.
- [ ] Recall execution + acknowledgement tracking is available (full hub in PRD-08/11).
- [ ] The register is queryable by date, product, prescriber, administrator.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/ADMIN-GATE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/RECALL-LOOKUP.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C8.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
