# Client identity: Entra External ID (social / email / OTP) wiring

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUTH-CLIENT`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/SPIKE-AUTH`

## Background

As a client, I want to create an account and sign in with social login, email+password, or a one-time code, so that I can access booking, intake and my records easily and securely.
Clients create accounts with Google/Apple, email+password, or email/SMS OTP via Entra External ID (CIAM).

## How it works

An Entra External ID (CIAM) tenant is configured with three user flows: social (Google/Apple), local (email + password) and OTP (email/SMS one-time code), each with its sign-up and sign-in experience and account recovery (password reset, OTP resend). The client Flutter app and the public web complete each of the three methods.
Client tokens carry a tenant scope and a stable client identity that is separate from the staff identity namespace, so a client can never be mistaken for staff and vice versa; the API's auth middleware validates client tokens and resolves the same tenant context RLS uses. Account recovery flows are first-class because clients self-serve.
Because handles and contact details are personal data (C21), the identities created here feed the consent/retention model later; this story just establishes the authentication, keeping client and staff audiences cleanly separated for the SaaS-ready design (ADR-0003/0004).

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

- [ ] **Configure Entra External ID user flows (social / email+password / OTP) and complete them on client app + public web**
  Stand up CIAM sign-up/sign-in for clients across all three methods, tenant-scoped and distinct from staff.
  - External ID tenant with three user flows: social (Google/Apple), local (email+password), and email/SMS OTP, each with sign-up, sign-in and account recovery (reset / OTP resend).
  - Client Flutter app and public web complete each method.
  - Client tokens carry tenant scope and a stable client identity in a namespace separate from staff; the API validates them and resolves tenant context for RLS.
  - Social/OTP redirect + provider credentials sourced per environment from config/secrets (SECRETS).
- [ ] **Document client auth flows, recovery and the client-vs-staff identity separation**
  Write the client-identity reference covering the separation that matters for safety and SaaS.
  - Each of the three flows and the recovery paths, plus the token's claims (tenant, stable client id).
  - Why and how client identities are distinct from staff identities (separate audiences/namespaces) and how the API tells them apart.
  - Note that captured handles/contact data are personal data (C21) feeding the consent/retention model — out of scope here but anticipated.
