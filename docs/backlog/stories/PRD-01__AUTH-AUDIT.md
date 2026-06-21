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

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10, C4, C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
