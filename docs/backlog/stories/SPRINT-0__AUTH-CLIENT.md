# Client identity: Entra External ID (social / email / OTP) wiring

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUTH-CLIENT`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/SPIKE-AUTH`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a client, I want to create an account and sign in with social login, email+password, or a one-time code, so that I can access booking, intake and my records easily and securely.

Clients create accounts with Google/Apple, email+password, or email/SMS OTP via Entra External ID (CIAM).

## Requirements

- To create an account and sign in with social login, email+password, or a one-time code.

## Acceptance Criteria

- [ ] Entra External ID configured for social, local (email+password) and OTP flows.
- [ ] Client app and public web complete each of the three sign-in methods.
- [ ] Client identities are tenant-scoped and distinct from staff identities.
- [ ] Account recovery (password reset / OTP resend) works.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0004 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/SPIKE-AUTH.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/AUTH-CLIENT.
Phase: 0 · Priority: P0 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Client identity: Entra External ID (social / email / OTP) wiring**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
