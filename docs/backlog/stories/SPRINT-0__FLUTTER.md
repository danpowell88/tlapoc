# Flutter app shells (client + provider) + shared packages

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/FLUTTER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`, `SPRINT-0/DESIGN`

## Background

As a mobile developer, I want client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage, so that the two apps are built from one codebase with consistent plumbing.
One Flutter codebase, two flavours (client, provider), sharing auth, the API client and the design system (ADR-0006).

## How it works

Client + provider app shells (bottom-tab nav) from one Flutter codebase, sharing auth (Entra staff / External ID clients), the generated API client and the design system, with secure token storage; CI produces internal builds (ADR-0004/0006). The base PRD-09 builds on.

## Requirements

- Client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage.

## Acceptance Criteria

- [ ] Client app shell has the Home/Book/My care/Membership/Account tabs; provider app shell has Schedule/Patient/Medicines/Tasks tabs (empty screens).
- [ ] Both apps sign in (client = External ID, provider = Entra) and call the sample endpoint.
- [ ] Auth tokens stored in secure storage; design-system theme applied.
- [ ] Builds are produced by CI for internal distribution.

## UI designs / screenshots

_Prototype screen: Non-UI / platform scaffolding — no prototype screen._

- Client tabs Home/Book/My care/Membership/Account and provider tabs Schedule/Patient/Medicines/Tasks (empty shells) — see client-app.png / treatment-room.png.

## Technical notes (high level)

- Stack: Flutter client app; Flutter provider app
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Flutter app shells (client + provider) + shared packages**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
