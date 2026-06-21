# Cooling-off & under-18 payment block

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/CLIENT-CORE`, `PRD-03/CONSENT`

## Background

As a system, I want to enforce a 7-day cooling-off and payment block for under-18s and record a second consultation, so that minors are protected per the rules.
Under-18s require ≥7 days between consent and procedure plus a payment block (except the consult) and a recorded second consultation; an optional adult cooling-off is configurable (C6).

## Requirements

- To enforce a 7-day cooling-off and payment block for under-18s and record a second consultation.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
- [ ] A second-consultation offer is recorded.
- [ ] Optional adult cooling-off is configurable (default per legal read).
- [ ] Payment block coordinates with PRD-06.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C6); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
