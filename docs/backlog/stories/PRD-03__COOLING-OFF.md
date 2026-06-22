# Cooling-off & under-18 payment block

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/CLIENT-CORE`, `PRD-03/CONSENT`

## Background

As a system, I want to enforce a 7-day cooling-off and payment block for under-18s and record a second consultation, so that minors are protected per the rules.
Under-18s require ≥7 days between consent and procedure plus a payment block (except the consult) and a recorded second consultation; an optional adult cooling-off is configurable (C6).

## How it works

For under-18s the system enforces >=7 days between consent and procedure and blocks payment (except the consult) until it elapses, and records a second-consultation offer. An optional adult cooling-off is configurable (default per legal read).
The payment block coordinates with PRD-06; the booking deposit/hold is suppressed during cooling-off (F14 invariant).

## Requirements

- To enforce a 7-day cooling-off and payment block for under-18s and record a second consultation.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
- [ ] A second-consultation offer is recorded.
- [ ] Optional adult cooling-off is configurable (default per legal read).
- [ ] Payment block coordinates with PRD-06.

## UI designs / screenshots

- Patient header shows an 'under-18 cooling-off' chip with the elapse date; checkout is blocked (except consult) until then.
- A recorded second-consultation offer appears on the client timeline.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **CoolingOffTimer** — id, client_id, appointment_id, consent_at, eligible_at, payment_blocked(bool), second_consult_offered_at
  - _Under-18 mandatory 7d; adult optional/config._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - CoolingOffTimer — id, client_id, appointment_id, consent_at, eligible_at, payment_blocked(bool), second_consult_offered_at (Under-18 mandatory 7d; adult optional/config.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
  - Rule: A second-consultation offer is recorded.
  - Rule: Optional adult cooling-off is configurable (default per legal read).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/CLIENT-CORE, PRD-03/CONSENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C6 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
  - Payment block coordinates with PRD-06.
