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

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Administration — id, tenant_id, client_id, prescription_id, product_id, lot_id, units, site, depth, administrator_id, at (Immutable (ADR-0010); requires valid unconsumed Rx (same client) + current consent + in-date lot; appears in register.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
  - Rule: It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
  - Rule: A blocked attempt shows the reason and writes an audit event.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/PRESCRIPTION, PRD-04/STOCK-RECEIVE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C8 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
  - It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
  - A blocked attempt shows the reason and writes an audit event.
