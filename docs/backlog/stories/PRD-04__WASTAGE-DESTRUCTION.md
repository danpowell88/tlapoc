# Wastage, disposal & destruction records

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/WASTAGE-DESTRUCTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want to record wastage, disposal and destruction (including partial vials) with certificates, so that we evidence lawful disposal of S4 medicine.
Wastage and destruction (incl. partial vials) must be recorded via a licensed/RUM pathway with certificates (C16).

## How it works

Wastage and destruction (including partial vials) are recorded via a licensed/RUM pathway with certificate references (C16). Records capture quantity, reason, pathway and certificate, are immutable and audited.
Closes the medicines loop alongside reconciliation and stocktake.

## Requirements

- To record wastage, disposal and destruction (including partial vials) with certificates.
- Compliance: [C16](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Wastage/destruction records capture quantity, reason, pathway and certificate reference.
- [ ] Partial-vial destruction is supported.
- [ ] Licensed/RUM disposal pathway is recorded.
- [ ] Records are immutable and audited.

## UI designs / screenshots

- Prototype: Stock & medicines -> record wastage/destruction (stock.png) — quantity, reason, pathway, certificate ref; also surfaced in the back-office waste log (backroom.png).

## Suggested data model

- **StockDestruction** — id, lot_id, units, reason, pathway(RUM|licensed), certificate_ref, at, actor_id
  - _Partial-vial supported; immutable + audited (C16)._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C16); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
