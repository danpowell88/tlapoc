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

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - AuthAssurance — session_id, mfa_at, stepup_at, methods[] (Sensitive actions check recency of stepup_at.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Staff sign-in enforces MFA (via Entra).
  - Rule: Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
  - Rule: Step-up events are audited.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/SIGNIN-UI.
- [ ] **Enforce compliance gate + audit events**
  Enforce C10 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
