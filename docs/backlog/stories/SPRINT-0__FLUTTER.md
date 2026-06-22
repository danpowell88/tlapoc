# Flutter app shells (client + provider) + shared packages

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/FLUTTER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/AUTH-CLIENT`, `SPRINT-0/DESIGN`

## Background

As a mobile developer, I want client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage, so that the two apps are built from one codebase with consistent plumbing.
One Flutter codebase, two flavours (client, provider), sharing auth, the API client and the design system (ADR-0006).

## How it works

One Flutter codebase produces two flavours. The client app shell has bottom-tab navigation Home / Book / My care / Membership / Account (matching client-app.png), and the provider app shell has Schedule / Patient / Medicines / Tasks (the room-side flow in treatment-room.png) — empty screens at this stage, just the navigable frame and theme.
Both apps authenticate through the shared auth package: the provider flavour signs in with Entra ID (staff) and the client flavour with External ID, and both call the sample API endpoint via the OPENAPI-generated client to prove the round-trip. Auth tokens are kept in platform secure storage (keychain/keystore), never plain storage, and the design-system theme/tokens are applied so both apps look like the product from day one.
CI builds installable artifacts for internal distribution for both flavours (signing/store channels are APP-DISTRIBUTION's job). This shell is the base the offline-tolerant charting (PRD-05/09) and the injection-mapping canvas build on — de-risked separately by SPIKE-OFFLINE and SPIKE-CANVAS.

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

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build both app shells: tab nav, shared auth/API/design packages, secure token storage, themed**
  Stand up the client and provider flavours from one codebase with shared plumbing.
  - Client shell tabs Home/Book/My care/Membership/Account; provider shell tabs Schedule/Patient/Medicines/Tasks (empty screens, navigable frame).
  - Shared auth package: provider signs in with Entra (AUTH-STAFF), client with External ID (AUTH-CLIENT); both call the sample endpoint via the OPENAPI-generated client.
  - Tokens stored in platform secure storage (keychain/keystore); design-system theme/tokens (DESIGN) applied.
  - CI builds installable artifacts per flavour for internal distribution (channels deferred to APP-DISTRIBUTION).
- [ ] **Document the Flutter flavour/package structure and build/run/distribution basics**
  Write the mobile-base guide so SPIKE-CANVAS/SPIKE-OFFLINE and PRD-09 build consistently.
  - Flavour configuration (client vs provider) and the shared packages (auth, api-client, design-system) layout.
  - How each flavour authenticates (different audiences) and where secure token storage lives.
  - How CI produces artifacts and the hand-off to APP-DISTRIBUTION for real distribution.
