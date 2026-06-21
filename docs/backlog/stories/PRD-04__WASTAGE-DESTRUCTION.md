# Wastage, disposal & destruction records

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/WASTAGE-DESTRUCTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a owner, I want to record wastage, disposal and destruction (including partial vials) with certificates, so that we evidence lawful disposal of S4 medicine.

Wastage and destruction (incl. partial vials) must be recorded via a licensed/RUM pathway with certificates (C16).

## Requirements

- To record wastage, disposal and destruction (including partial vials) with certificates.
- Traces to requirement(s): REQ-MED-9.
- Must satisfy compliance obligation(s): C16.

## Acceptance Criteria

- [ ] Wastage/destruction records capture quantity, reason, pathway and certificate reference.
- [ ] Partial-vial destruction is supported.
- [ ] Licensed/RUM disposal pathway is recorded.
- [ ] Records are immutable and audited.

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/CUSTODY-STORAGE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/WASTAGE-DESTRUCTION.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C16.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C16); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
