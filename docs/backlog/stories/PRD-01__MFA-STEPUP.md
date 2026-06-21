# MFA & step-up authentication for sensitive actions

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MFA-STEPUP`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/SIGNIN-UI`

## Background

As a security-conscious clinic, I want MFA for staff and step-up re-authentication on the most sensitive actions, so that high-risk operations can't be performed on a walk-up or hijacked session.
Staff MFA is required; sensitive clinical/medicines/financial actions (e.g. prescribing, S4 custody changes, destruction, data export) may require step-up re-auth. Client MFA policy is an open question.

## Requirements

- MFA for staff and step-up re-authentication on the most sensitive actions.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Staff sign-in enforces MFA (via Entra).
- [ ] Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
- [ ] Step-up events are audited.
- [ ] Client MFA policy (optional vs required for sensitive actions) is configurable (open question resolved per clinic).

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
