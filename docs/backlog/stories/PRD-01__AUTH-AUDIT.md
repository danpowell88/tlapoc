# Authentication & authorisation audit events

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUTH-AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`, `PRD-01/RBAC`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a compliance officer, I want an audit of authentication and authorisation events, including blocked out-of-scope attempts, so that we can investigate access and prove the gates work.

Beyond data-access audit, security needs a record of authentication and authorisation events: sign-in success/failure, lockouts, MFA/step-up, role switches and every scope-block (a blocked out-of-scope action).

## Requirements

- An audit of authentication and authorisation events, including blocked out-of-scope attempts.
- Traces to requirement(s): REQ-SEC-3.
- Must satisfy compliance obligation(s): C10, C4, C19.

## Acceptance Criteria

- [ ] Sign-in success/failure, lockout, MFA/step-up and role-switch events are recorded.
- [ ] Every blocked out-of-scope or lapsed-registration action writes an audit event with the reason.
- [ ] These events are queryable/exportable alongside the data-access audit.
- [ ] Suspicious patterns can feed the breach workflow (PRD-01/BREACH).

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0010 (see docs/adr/decision-log.md).
Depends on: PRD-01/AUDIT, PRD-01/RBAC.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/AUTH-AUDIT.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C10, C4, C19.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10, C4, C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
