# Client app: my care, memberships, rewards & card-on-file

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-06/MEMBERSHIP`, `PRD-05/PHOTOS`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a client, I want to view my photos, memberships, rewards and balance and add a card-on-file, so that I can self-serve my care and payments.

Clients view consented before/after photos, memberships, rewards/perks and balances, and add a card-on-file for autopay (REQ-APP-1).

## Requirements

- To view my photos, memberships, rewards and balance and add a card-on-file.
- Traces to requirement(s): REQ-APP-1.

## Acceptance Criteria

- [ ] Consent-gated before/after photo viewing.
- [ ] Memberships, rewards/perks and balances visible.
- [ ] Card-on-file can be added in-app (feeds PRD-06 autopay).
- [ ] No one-off online checkout is exposed.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter client app.
Depends on: PRD-06/MEMBERSHIP, PRD-05/PHOTOS.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/CLIENT-CARE.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C14.

## Tasks (dev pickup)

- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
