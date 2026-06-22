# Client app: account, privacy & access/correction

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-PRIVACY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-01/PRIVACY-RIGHTS`

## Background

As a client, I want an account area where I can see my data, know it stays in Australia, and request access or correction, so that I'm in control of my information.
The Account area exposes profile, balances, card-on-file and a 'Your data & privacy' surface (residency note, access copy, request correction) (C21).

## How it works

The Account tab exposes profile, the client's own balances and card-on-file, and a 'Your data & privacy' surface: a residency trust note ('your data stays in Australia', APP 8) plus self-service request-a-copy (access), request-correction and request-deletion. Each raises a PRD-01 PrivacyRequest with a ≤30-day DSAR clock, tracked to resolution and audited; staff resolve via Governance.
Puts the client in control of their information (C21, APP 12/13).

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

- Prototype: client-app Account — 'Edit profile', 'Update card on file', 'Request account deletion', and 'Your data & privacy' (residency note + request-a-copy / request-correction).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) PrivacyRequest** — PRD-01 — kind(access|correction|deletion), status, DSAR clock, resolution
  - _Self-service entry point; staff resolve via Governance._
- **(reuses) AuditEvent** — PRD-01 — actor, time, outcome of each privacy action
  - _Evidences APP 12/13._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app: Account tab (profile, balances, card-on-file)**
  Account screen surfacing profile (Edit profile), the client's own balance and the card-on-file (Update card on file → Square tokenisation). Read-only money: the client sees only their own balances/perks, never clinic revenue. Lay out the 'Your data & privacy' entry point beneath the account actions.
- [ ] **Client app: 'Your data & privacy' — access/correction/deletion + residency note**
  Build the privacy surface: static residency trust note ('your data stays in Australia', backed by the APP 8 AU-residency posture) plus three actions that each POST a PRD-01 PrivacyRequest (access/correction/deletion) with the ≤30-day DSAR clock. Show request status tracked to resolution; deliver any export through the secure channel, not client-built. Audit every action (actor/time/outcome). Staff resolve via the Governance DSAR workflow.
