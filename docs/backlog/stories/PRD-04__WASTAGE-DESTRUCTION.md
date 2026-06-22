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

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockDestruction** — id, lot_id, units, reason, pathway(RUM|licensed), certificate_ref, at, actor_id
  - _Partial-vial supported; immutable + audited (C16)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - StockDestruction — id, lot_id, units, reason, pathway(RUM|licensed), certificate_ref, at, actor_id (Partial-vial supported; immutable + audited (C16).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Wastage/destruction records capture quantity, reason, pathway and certificate reference.
  - Rule: Partial-vial destruction is supported.
  - Rule: Licensed/RUM disposal pathway is recorded.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/CUSTODY-STORAGE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C16 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Records are immutable and audited.
