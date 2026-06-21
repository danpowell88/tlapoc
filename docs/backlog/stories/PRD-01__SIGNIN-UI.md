# Sign-in / sign-out screens & session management

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/SIGNIN-UI`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`

## Background

As a user, I want clear sign-in and sign-out screens and a session that behaves safely, so that I can authenticate and trust my session.
The prototype demos a login/persona screen; the real product needs proper sign-in/out UI for staff (Entra) and clients (External ID), plus session lifecycle — built on the Sprint 0 auth wiring.

## How it works

The real sign-in sits on the Sprint-0 Entra wiring: staff sign in via Microsoft 365 SSO; clients via social / email+password / OTP with account recovery. Sign-out clears the session everywhere; idle-timeout + absolute limits apply and expiry returns to sign-in without losing in-progress work.
Every sign-in, sign-out and failed attempt is an auth audit event.

## Requirements

- Clear sign-in and sign-out screens and a session that behaves safely.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Staff sign-in via Entra SSO; client sign-in/up via social, email+password and OTP, with account recovery.
- [ ] Sign-out clears the session everywhere; token refresh is seamless.
- [ ] Idle-timeout and absolute session limits apply; expiry returns to sign-in without data loss.
- [ ] Sign-in, sign-out and failed attempts are recorded as auth audit events.

## UI designs / screenshots

_Prototype screen: prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings._

- Staff: an Entra SSO sign-in screen; clients: social/email/OTP sign-in + sign-up + recovery (the prototype persona picker stands in for this).
- Session-expiry returns to sign-in, preserving unsaved drafts where possible.

## Suggested data model

- **Session** — id, user_id, tenant_id, started_at, last_seen, expires_at, device
  - _Idle + absolute limits; revoked on sign-out._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Web UI** — prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.
