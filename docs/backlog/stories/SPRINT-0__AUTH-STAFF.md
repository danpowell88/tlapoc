# Staff identity: Entra ID SSO + MFA wiring

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUTH-STAFF`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/SPIKE-AUTH`

## Background

As a staff member, I want to sign in to the web and provider app with my Microsoft 365 account and MFA, so that I use one secure corporate identity and no extra password.
Staff sign in with the clinic's existing Microsoft 365 accounts via Entra ID with MFA (ADR-0004). This is the plumbing; the RBAC/scope rules are PRD-01.

## How it works

An Entra ID app registration is configured for the web SPA and the Flutter provider app (auth-code + PKCE, appropriate redirect URIs/scopes). Both surfaces complete interactive SSO + MFA against the clinic's tenant. The flow yields access tokens the API can validate and a stable, immutable user id (the Entra object id, not email) the API uses as the actor identity.
Tokens carry the tenant and that stable user id so the API's auth middleware can resolve tenant context for RLS and identify the actor for audit. Sessions are scoped to a single tenant — a token is only ever valid for one clinic — which keeps the multi-tenant boundary intact end to end. Token refresh and sign-out work consistently across web and app (silent refresh on web, secure refresh on device).
For the SaaS path, ADR-0004 anticipates each clinic federating its own Entra tenant for staff; v1 wires the single clinic but keeps tenant resolution claim-driven so federation is additive. Scope-of-practice and registration-currency checks (C4/C19) are explicitly out of scope here — they live in CREDENTIALS/RBAC — but this story ensures the claims they need are present.

## Requirements

- To sign in to the web and provider app with my Microsoft 365 account and MFA.

## Acceptance Criteria

- [ ] Entra ID app registration configured; web + provider app complete SSO + MFA.
- [ ] Tokens carry the tenant and a stable user id usable by the API.
- [ ] Sign-out and token refresh work across web and app.
- [ ] Sessions are scoped to a single tenant.

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Configure Entra ID app registration and complete staff SSO + MFA on web and provider app**
  Stand up workforce sign-in for staff on both staff-facing surfaces, yielding API-usable tokens.
  - App registration(s) for the Angular web app and the Flutter provider app: auth-code + PKCE, redirect URIs, required scopes/audience, MFA enforced.
  - Both surfaces complete interactive SSO + MFA against the clinic's Entra tenant.
  - Tokens carry the tenant and a stable user id (Entra object id) the API validates and RLS reads for tenant context; sessions are scoped to one tenant.
  - Token refresh and sign-out work across web (silent refresh) and app (secure refresh); keep tenant resolution claim-driven so per-tenant Entra federation is additive later.
- [ ] **Document the staff auth setup, claims contract & SaaS-federation path**
  Write the staff-identity reference so API, RBAC and the SaaS roadmap can rely on it.
  - The exact claims the token carries (tenant, stable user id, anything RBAC/credentials will need) and how the API consumes them.
  - App-registration configuration and redirect/scope setup per environment.
  - How per-tenant Entra federation slots in for SaaS, and the explicit note that scope/registration gating (C4/C19) is CREDENTIALS' job, not this story's.
