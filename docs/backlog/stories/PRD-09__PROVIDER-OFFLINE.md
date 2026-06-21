# Provider app: offline-tolerant workflows + sync indicator

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-OFFLINE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/OFFLINE`

## Background

As a injector, I want the app to keep working offline and clearly show my sync state, so that treatment-room Wi-Fi drops never cost me data.
Charting/photos queue locally encrypted and sync on reconnect with no loss; a persistent sync/offline indicator shows queued count + last sync (REQ-APP-3, ADR-0015).

## How it works

The provider app keeps working offline: charting/photos queue locally (encrypted) and sync on reconnect with no loss; a persistent indicator shows queued count + last-sync, and finalise is disabled until synced (ADR-0015, built on SPIKE-OFFLINE + PRD-05/OFFLINE).
Treatment-room Wi-Fi drops never cost the clinician data.

## Requirements

- The app to keep working offline and clearly show my sync state.

## Acceptance Criteria

- [ ] Charting/photos queue locally (encrypted) offline and sync on reconnect with no loss.
- [ ] Persistent indicator shows queued-items count + last-sync time.
- [ ] Finalise is disabled until synced.
- [ ] Built on SPIKE-OFFLINE and PRD-05/OFFLINE.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: provider app (treatment-room.png) — a persistent sync/offline indicator; queued-items count + last-sync; finalise disabled until synced.

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses)** — LocalQueue (PRD-05/OFFLINE) on-device
  - _Encrypted; last-write-wins drafts; server-side finalise._

## Technical notes (high level)

- Architecture decisions: [ADR-0015](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Offline queue + sync handling** — Encrypted local queue; finalise server-side.
