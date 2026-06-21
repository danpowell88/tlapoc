# MFA & step-up authentication for sensitive actions

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MFA-STEPUP`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/SIGNIN-UI`

## Background

As a security-conscious clinic, I want MFA for staff and step-up re-authentication on the most sensitive actions, so that high-risk operations can't be performed on a walk-up or hijacked session.
Staff MFA is required; sensitive clinical/medicines/financial actions (e.g. prescribing, S4 custody changes, destruction, data export) may require step-up re-auth. Client MFA policy is an open question.

## How it works

Staff sign-in enforces MFA (via Entra). The most sensitive actions — prescribing, S4 custody changes, destruction, data export — require a recent/step-up re-auth or are blocked with a clear prompt. Client MFA policy is configurable per clinic.
Step-up events are audited.

## Requirements

- MFA for staff and step-up re-authentication on the most sensitive actions.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Staff sign-in enforces MFA (via Entra).
- [ ] Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
- [ ] Step-up events are audited.
- [ ] Client MFA policy (optional vs required for sensitive actions) is configurable (open question resolved per clinic).

## UI designs / screenshots

- A step-up prompt appears when a configured sensitive action is attempted without recent strong auth; otherwise invisible.

## Suggested data model

- **AuthAssurance** — session_id, mfa_at, stepup_at, methods[]
  - _Sensitive actions check recency of stepup_at._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
