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

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C6); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
