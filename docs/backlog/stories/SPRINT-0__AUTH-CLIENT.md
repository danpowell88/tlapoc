# Client identity: Entra External ID (social / email / OTP) wiring

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUTH-CLIENT`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/SPIKE-AUTH`

## Background

As a client, I want to create an account and sign in with social login, email+password, or a one-time code, so that I can access booking, intake and my records easily and securely.
Clients create accounts with Google/Apple, email+password, or email/SMS OTP via Entra External ID (CIAM).

## How it works

Clients create accounts and sign in via Entra External ID (CIAM) with Google/Apple, email+password, or email/SMS OTP, plus account recovery (ADR-0004). Client identities are tenant-scoped and distinct from staff; de-risked by SPIKE-AUTH.

## Requirements

- To create an account and sign in with social login, email+password, or a one-time code.

## Acceptance Criteria

- [ ] Entra External ID configured for social, local (email+password) and OTP flows.
- [ ] Client app and public web complete each of the three sign-in methods.
- [ ] Client identities are tenant-scoped and distinct from staff identities.
- [ ] Account recovery (password reset / OTP resend) works.

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Client identity: Entra External ID (social / email / OTP) wiring**
  Deliver per the acceptance criteria:
  - Entra External ID configured for social, local (email+password) and OTP flows.
  - Client app and public web complete each of the three sign-in methods.
  - Client identities are tenant-scoped and distinct from staff identities.
  - Account recovery (password reset / OTP resend) works.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
