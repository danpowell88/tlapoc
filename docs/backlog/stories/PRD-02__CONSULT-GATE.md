# Consult gate on injectable appointments

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CONSULT-GATE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a system, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.
An injectable appointment cannot move to charting without a linked Consult — the booking-side half of the moat (REQ-BOOK-5).

## How it works

The booking-side half of the moat: an injectable appointment cannot progress to charting until a synchronous Consult is linked (REQ-BOOK-5). Server-enforced, surfaced via the blocked-action banner.
This guarantees no S4 treatment can begin without the consult, complementing the consent gate (PRD-03) and the Rx gate (PRD-04).

## Requirements

- To block a checked-in injectable appointment from opening charting unless a consult is linked.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A checked-in injectable appointment with no linked consult cannot open the charting screen.
- [ ] The blocked-action banner explains what's missing and who can resolve it.
- [ ] Once a consult is recorded the gate clears (handoff to PRD-04).
- [ ] The block is server-enforced, not just UI.

## UI designs / screenshots

- Prototype: the Charting screen (charting.png) shows the gate chips (Consult / Consent / screening) and the Consult & prescription card; a checked-in injectable with no consult cannot open charting and shows why.
- On the schedule/Today board, an injectable visit shows its gate status.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Appointment.consult_id** — FK Consult (PRD-04), nullable until consult recorded
  - _Charting open is blocked while null for S4 services._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Appointment.consult_id — FK Consult (PRD-04), nullable until consult recorded (Charting open is blocked while null for S4 services.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A checked-in injectable appointment with no linked consult cannot open the charting screen.
  - Rule: The blocked-action banner explains what's missing and who can resolve it.
  - Rule: Once a consult is recorded the gate clears (handoff to PRD-04).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/ONLINE-BOOK.
- [ ] **Enforce compliance gate + audit events**
  Enforce C1 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A checked-in injectable appointment with no linked consult cannot open the charting screen.
  - The blocked-action banner explains what's missing and who can resolve it.
  - Once a consult is recorded the gate clears (handoff to PRD-04).
