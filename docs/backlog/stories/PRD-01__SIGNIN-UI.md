# Sign-in / sign-out screens & session management

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/SIGNIN-UI`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a user, I want clear sign-in and sign-out screens and a session that behaves safely, so that I can authenticate and trust my session.

The prototype demos a login/persona screen; the real product needs proper sign-in/out UI for staff (Entra) and clients (External ID), plus session lifecycle — built on the Sprint 0 auth wiring.

## Requirements

- Clear sign-in and sign-out screens and a session that behaves safely.
- Traces to requirement(s): REQ-TEN-2.
- Must satisfy compliance obligation(s): C10.

## Acceptance Criteria

- [ ] Staff sign-in via Entra SSO; client sign-in/up via social, email+password and OTP, with account recovery.
- [ ] Sign-out clears the session everywhere; token refresh is seamless.
- [ ] Idle-timeout and absolute session limits apply; expiry returns to sign-in without data loss.
- [ ] Sign-in, sign-out and failed attempts are recorded as auth audit events.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0004 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/SIGNIN-UI.
Phase: 0 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Web UI** — prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
