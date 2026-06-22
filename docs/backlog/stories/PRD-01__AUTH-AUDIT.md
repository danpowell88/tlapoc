# Authentication & authorisation audit events

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUTH-AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`, `PRD-01/RBAC`

## Background

As a compliance officer, I want an audit of authentication and authorisation events, including blocked out-of-scope attempts, so that we can investigate access and prove the gates work.
Beyond data-access audit, security needs a record of authentication and authorisation events: sign-in success/failure, lockouts, MFA/step-up, role switches and every scope-block (a blocked out-of-scope action).

## How it works

Beyond data-access audit, security needs a record of authentication/authorisation events: sign-in success/failure, lockouts, MFA/step-up, role switches and every scope-block (a blocked out-of-scope or lapsed-registration attempt, with the reason).
Queryable/exportable alongside the data-access audit; can seed the breach workflow on suspicious patterns.

## Requirements

- An audit of authentication and authorisation events, including blocked out-of-scope attempts.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Sign-in success/failure, lockout, MFA/step-up and role-switch events are recorded.
- [ ] Every blocked out-of-scope or lapsed-registration action writes an audit event with the reason.
- [ ] These events are queryable/exportable alongside the data-access audit.
- [ ] Suspicious patterns can feed the breach workflow (PRD-01/BREACH).

## UI designs / screenshots

- Surfaces in the admin audit viewer / Governance audit pack filtered to auth + authorisation events.

## Suggested data model

- **AuthEvent** — id, tenant_id, actor_id, kind(signin_ok|signin_fail|lockout|mfa|stepup|role_switch|scope_block), reason, at
  - _Peer of AuditEvent; scope_block records the blocked capability._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - AuthEvent — id, tenant_id, actor_id, kind(signin_ok|signin_fail|lockout|mfa|stepup|role_switch|scope_block), reason, at (Peer of AuditEvent; scope_block records the blocked capability.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Sign-in success/failure, lockout, MFA/step-up and role-switch events are recorded.
  - Rule: Every blocked out-of-scope or lapsed-registration action writes an audit event with the reason.
  - Rule: These events are queryable/exportable alongside the data-access audit.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/AUDIT, PRD-01/RBAC.
- [ ] **Enforce compliance gate + audit events**
  Enforce C10, C4, C19 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Every blocked out-of-scope or lapsed-registration action writes an audit event with the reason.
