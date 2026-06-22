# Sign-in / sign-out screens & session management

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/SIGNIN-UI`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`

## Background

As a user, I want clear sign-in and sign-out screens and a session that behaves safely, so that I can authenticate and trust my session.
Plainly: the real sign-in and sign-out screens and the rules that keep a session safe — staff sign in with their work Microsoft account, clients with social/email/one-time-code. It is a Foundations story built on the Sprint 0 authentication wiring. It is where the clinic's login experience and session safety (timeouts, clean sign-out, not losing half-finished work) actually live, replacing the prototype's simple persona picker. The prototype demos a login/persona screen; the real product needs proper sign-in/out UI for staff (Entra ID (Microsoft's identity service)) and clients (External ID), plus session lifecycle — built on the Sprint 0 auth wiring.

## How it works

The real sign-in sits on the Sprint-0 Entra wiring (ADR-0004, REQ-TEN-2, AC3). Staff sign in via Microsoft 365 / Entra ID SSO (no local password — they're bound to the tenant via TENANT's invite flow). Clients sign in/up via Entra External ID: Google/Apple social, email+password, or email/SMS OTP (one-time passcode sent by email or SMS), with account recovery. The prototype's persona picker ('Switch user') stands in for this in the POC.
Session lifecycle is the substance of this story: sign-out clears the session everywhere (revokes the server session + clears client tokens); token refresh is seamless so an active user isn't bounced mid-task; an idle-timeout and an absolute session limit both apply; and when a session expires the user is returned to sign-in without losing in-progress work (unsaved drafts preserved where possible — e.g. a half-written chart note or booking).
Every sign-in, sign-out and failed attempt is recorded as an auth audit event (AUTH-AUDIT) — this is where C10 auth-trail capture begins. Failed attempts feed lockout (MFA-STEPUP / Entra policy).
Edge cases: a session that expires during a long charting session restores the draft on re-auth; sign-out on one device doesn't silently keep another device signed in (sign-out is per-session, revocation is explicit); a client OTP that times out re-issues rather than failing hard.

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

- Staff: an Entra SSO sign-in screen (redirect to Microsoft, return to the tenant-scoped app). Clients: a sign-in/up screen offering social / email+password / OTP plus account recovery.
- Session-expiry returns to sign-in preserving unsaved drafts where possible; a clear sign-out control in the header user menu.
- The prototype persona picker (showLogin / 'Switch user') is the POC stand-in for these real screens.

## Suggested data model

- **Session** — id, tenant_id, user_id, kind(staff|client), started_at, last_seen, idle_expires_at, absolute_expires_at, device, revoked_at
  - _Idle + absolute limits; revoked on sign-out; one row per device/session so per-session sign-out is precise._

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Staff Entra SSO sign-in/out screens**
  Build the staff sign-in (redirect to Microsoft Entra ID (Microsoft's identity service) ID SSO (single sign-on), return to the tenant-scoped app on success — bound via TENANT) and a clear sign-out in the header user menu. No local staff password. Write a sign-in/sign-out/failed-attempt auth event for each (AUTH-AUDIT).
- [ ] **Client sign-in/up (social / email+password / OTP) + recovery**
  Build client sign-in and sign-up via Entra ID (Microsoft's identity service) External ID covering each of social (Google/Apple), email+password, and email/SMS OTP (one-time passcode sent by email or SMS), plus account recovery (AC3 requires all three methods work). Handle OTP timeout by re-issuing rather than hard-failing. Auth events recorded.
- [ ] **Session lifecycle: idle/absolute limits, seamless refresh, sign-out-everywhere**
  Model Session with idle + absolute expiry and per-device rows. Implement seamless token refresh for active users, an idle-timeout and absolute limit, and sign-out that revokes the server session and clears client tokens for that session (per-session precision; another device isn't silently kept in). Record sign-out and expiry.
- [ ] **Expiry UX: return to sign-in preserving unsaved drafts**
  On session expiry, route the user back to sign-in and, where possible, preserve in-progress work (unsaved chart note / booking draft) so re-auth restores it rather than losing it. Coordinate with the offline/draft behaviour where relevant; finalisation still happens server-side post-auth.
