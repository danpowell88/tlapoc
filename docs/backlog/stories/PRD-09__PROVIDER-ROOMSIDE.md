# Provider app: room-side charting, camera & finalise

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-ROOMSIDE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/MAPPING`, `PRD-05/PHOTOS`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a injector, I want to map injections, capture photos and finalise the chart room-side, so that the full clinical record is captured at the chair.

Map injections, capture photos via signed URLs (never on device), record consult/link script and finalise — all surfacing PRD-04/05 (REQ-APP-2, C14/ADR-0009).

## Requirements

- To map injections, capture photos and finalise the chart room-side.
- Traces to requirement(s): REQ-APP-2.
- Must satisfy compliance obligation(s): C14.

## Acceptance Criteria

- [ ] Provider app surfaces PRD-05 mapping/photos and PRD-04 consult/Rx/administration.
- [ ] Photos capture to central storage via signed URLs; none persist on device after sync (C14).
- [ ] Finalisation is server-side; once finalised the entry is read-only.
- [ ] Thumb-first, gloves-on usability (UX §1).

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0009 (see docs/adr/decision-log.md).
Depends on: PRD-05/MAPPING, PRD-05/PHOTOS.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/PROVIDER-ROOMSIDE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C14.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
