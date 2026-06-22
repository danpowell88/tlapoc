# Custody & secure storage

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CUSTODY-STORAGE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/STOCK-RECEIVE`

## Background

As a owner, I want stock custody limited to an on-site prescriber and bound to a secure, access-logged location, so that S4 custody meets the exclusive-custody rule.
Only NP/prescriber roles may take custody; stock is bound to a secure, access-logged location. Mode-A custodian must physically work at the clinic with exclusive custody (C7/C15).

## How it works

Only NP/prescriber roles may take custody; stock is bound to a secure, access-logged location. The Mode-A custodian must physically work at the clinic and hold exclusive custody — a remote prescriber consigning stock is flagged non-compliant (C7/C15).
A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.

## Requirements

- Stock custody limited to an on-site prescriber and bound to a secure, access-logged location.
- Compliance: [C7](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C15](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Only NP/prescriber roles can take custody of stock.
- [ ] Stock is bound to a secure location; access is logged.
- [ ] A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.
- [ ] A remote prescriber consigning stock is flagged non-compliant.

## UI designs / screenshots

- Prototype: Stock & medicines header (stock.png) shows 'custody Dr Lee NP · locked fridge'; the custodian + secure-location binding is visible; access is logged.
- Custody-change is capability-gated and audited.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockLocation** — id, tenant_id, name(locked cabinet/fridge), custodian_id, exclusive_custody_attested(bool), store_contact
  - _Custody limited to on-site prescriber (C7); access logged._
- **AccessLog** — id, location_id, actor_id, at, event(open|close|tamper)
  - _Feeds the optional ESP32 cabinet sensor + audit._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - StockLocation — id, tenant_id, name(locked cabinet/fridge), custodian_id, exclusive_custody_attested(bool), store_contact (Custody limited to on-site prescriber (C7); access logged.)
  - AccessLog — id, location_id, actor_id, at, event(open|close|tamper) (Feeds the optional ESP32 cabinet sensor + audit.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Only NP/prescriber roles can take custody of stock.
  - Rule: Stock is bound to a secure location; access is logged.
  - Rule: A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/STOCK-RECEIVE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C7, C15 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Only NP/prescriber roles can take custody of stock.
