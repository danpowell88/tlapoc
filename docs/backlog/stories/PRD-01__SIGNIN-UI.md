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

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Session — id, user_id, tenant_id, started_at, last_seen, expires_at, device (Idle + absolute limits; revoked on sign-out.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Staff sign-in via Entra SSO; client sign-in/up via social, email+password and OTP, with account recovery.
  - Rule: Sign-out clears the session everywhere; token refresh is seamless.
  - Rule: Idle-timeout and absolute session limits apply; expiry returns to sign-in without data loss.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C10 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the screen per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Staff: an Entra SSO sign-in screen; clients: social/email/OTP sign-in + sign-up + recovery (the prototype persona picker stands in for this).
  - Session-expiry returns to sign-in, preserving unsaved drafts where possible.
