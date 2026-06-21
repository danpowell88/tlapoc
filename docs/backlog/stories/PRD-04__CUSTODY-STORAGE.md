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

## Suggested data model

- **StockLocation** — id, tenant_id, name(locked cabinet/fridge), custodian_id, exclusive_custody_attested(bool), store_contact
  - _Custody limited to on-site prescriber (C7); access logged._
- **AccessLog** — id, location_id, actor_id, at, event(open|close|tamper)
  - _Feeds the optional ESP32 cabinet sensor + audit._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C7, C15); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
