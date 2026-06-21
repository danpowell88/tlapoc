# Provider app: offline-tolerant workflows + sync indicator

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-OFFLINE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/OFFLINE`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a injector, I want the app to keep working offline and clearly show my sync state, so that treatment-room Wi-Fi drops never cost me data.

Charting/photos queue locally encrypted and sync on reconnect with no loss; a persistent sync/offline indicator shows queued count + last sync (REQ-APP-3, ADR-0015).

## Requirements

- The app to keep working offline and clearly show my sync state.
- Traces to requirement(s): REQ-APP-3.

## Acceptance Criteria

- [ ] Charting/photos queue locally (encrypted) offline and sync on reconnect with no loss.
- [ ] Persistent indicator shows queued-items count + last-sync time.
- [ ] Finalise is disabled until synced.
- [ ] Built on SPIKE-OFFLINE and PRD-05/OFFLINE.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0015 (see docs/adr/decision-log.md).
Depends on: PRD-05/OFFLINE.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/PROVIDER-OFFLINE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Offline queue + sync handling** — Encrypted local queue; finalise server-side.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
