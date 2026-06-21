# Administration gating & immutable record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/ADMIN-GATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRESCRIPTION`, `PRD-04/STOCK-RECEIVE`

## Background

As a RN, I want to administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry, so that every dose is lawful, traceable and tamper-proof.
An RN can only administer S4 against a valid, unconsumed prescription for that same client, with current consent and a selected in-date lot; the record is immutable once saved (C8).

## How it works

An RN may only administer S4 against a valid, unconsumed prescription for that same client, with current consent and a selected in-date lot; the administration record is immutable once saved (C8). A blocked attempt shows the reason and writes an audit event.
This is the central invariant of the moat — every dose is provably lawful and traceable. It appears in the medicine register and links lot->client for recall.

## Requirements

- To administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
- [ ] It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
- [ ] A blocked attempt shows the reason and writes an audit event.
- [ ] The administration appears in the medicine register.

## UI designs / screenshots

- Prototype: Charting (charting.png) — administration is the act of finalising the injection map against the selected lot; the gate chips (consult/consent) and lot selection must be satisfied first.
- Over-draw or missing prerequisites block finalise with an explanatory banner.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Administration** — id, tenant_id, client_id, prescription_id, product_id, lot_id, units, site, depth, administrator_id, at
  - _Immutable (ADR-0010); requires valid unconsumed Rx (same client) + current consent + in-date lot; appears in register._

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
