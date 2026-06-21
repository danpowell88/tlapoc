# Flutter app shells (client + provider) + shared packages

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/FLUTTER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`, `SPRINT-0/DESIGN`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a mobile developer, I want client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage, so that the two apps are built from one codebase with consistent plumbing.

One Flutter codebase, two flavours (client, provider), sharing auth, the API client and the design system (ADR-0006).

## Requirements

- Client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage.

## Acceptance Criteria

- [ ] Client app shell has the Home/Book/My care/Membership/Account tabs; provider app shell has Schedule/Patient/Medicines/Tasks tabs (empty screens).
- [ ] Both apps sign in (client = External ID, provider = Entra) and call the sample endpoint.
- [ ] Auth tokens stored in secure storage; design-system theme applied.
- [ ] Builds are produced by CI for internal distribution.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Flutter client app; Flutter provider app.
Architecture decisions: ADR-0004, ADR-0006 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT, SPRINT-0/DESIGN.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/FLUTTER.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Flutter app shells (client + provider) + shared packages**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
