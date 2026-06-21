# Client app: account, privacy & access/correction

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-PRIVACY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-01/PRIVACY-RIGHTS`

## Background

As a client, I want an account area where I can see my data, know it stays in Australia, and request access or correction, so that I'm in control of my information.
The Account area exposes profile, balances, card-on-file and a 'Your data & privacy' surface (residency note, access copy, request correction) (C21).

## How it works

The Account area exposes profile, balances, card-on-file and a 'Your data & privacy' surface: the residency note ('your data stays in Australia'), request a copy, request correction, and request account deletion — tracked to resolution and audited (APP 12/13, PRD-01).
Puts the client in control of their information.

## Requirements

- An account area where I can see my data, know it stays in Australia, and request access or correction.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Account shows profile, balances and card-on-file.
- [ ] 'Your data & privacy' shows the residency note and access-copy/correction actions (PRD-01).
- [ ] Requests are tracked to resolution.
- [ ] Actions are audited.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: client app Account (client-app.png) — 'Edit profile', 'Update card on file', 'Request account deletion', privacy/access-correction; residency trust note.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses)** — PrivacyRequest (PRD-01) — access/correction/deletion with DSAR clock
  - _Self-service entry point; staff resolve via Governance._

## Technical notes (high level)

- Stack: Flutter client app

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
