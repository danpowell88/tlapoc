# Staff identity: Entra ID SSO + MFA wiring

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUTH-STAFF`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/SPIKE-AUTH`

## Background

As a staff member, I want to sign in to the web and provider app with my Microsoft 365 account and MFA, so that I use one secure corporate identity and no extra password.
Staff sign in with the clinic's existing Microsoft 365 accounts via Entra ID with MFA (ADR-0004). This is the plumbing; the RBAC/scope rules are PRD-01.

## Requirements

- To sign in to the web and provider app with my Microsoft 365 account and MFA.

## Acceptance Criteria

- [ ] Entra ID app registration configured; web + provider app complete SSO + MFA.
- [ ] Tokens carry the tenant and a stable user id usable by the API.
- [ ] Sign-out and token refresh work across web and app.
- [ ] Sessions are scoped to a single tenant.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Staff identity: Entra ID SSO + MFA wiring**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
