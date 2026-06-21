# Client app: account, privacy & access/correction

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-PRIVACY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-01/PRIVACY-RIGHTS`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a client, I want an account area where I can see my data, know it stays in Australia, and request access or correction, so that I'm in control of my information.

The Account area exposes profile, balances, card-on-file and a 'Your data & privacy' surface (residency note, access copy, request correction) (C21).

## Requirements

- An account area where I can see my data, know it stays in Australia, and request access or correction.
- Traces to requirement(s): REQ-APP-1.
- Must satisfy compliance obligation(s): C21.

## Acceptance Criteria

- [ ] Account shows profile, balances and card-on-file.
- [ ] 'Your data & privacy' shows the residency note and access-copy/correction actions (PRD-01).
- [ ] Requests are tracked to resolution.
- [ ] Actions are audited.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter client app.
Depends on: PRD-01/PRIVACY-RIGHTS.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/CLIENT-PRIVACY.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C21.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
