# Provider app: offline-tolerant workflows + sync indicator

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-OFFLINE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/OFFLINE`

## Background

As a injector, I want the app to keep working offline and clearly show my sync state, so that treatment-room Wi-Fi drops never cost me data.
Charting/photos queue locally encrypted and sync on reconnect with no loss; a persistent sync/offline indicator shows queued count + last sync (REQ-APP-3, ADR-0015).

## How it works

The provider app keeps working offline: charting edits and captured photos queue to an encrypted on-device store and sync on reconnect with no loss (ADR-0015, built on SPIKE-OFFLINE + PRD-05/OFFLINE). Drafts reconcile last-write-wins; photos upload via signed URLs on reconnect (bytes held encrypted locally meanwhile, consistent with C14). A persistent indicator shows queued count + last-sync; finalise is disabled until everything has synced.
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

- Prototype: treatment-room — 'Connected to the treatment room' banner (flips to offline/queued in the real app).
- Persistent indicator: queued-items count + last-sync time; finalise disabled until synced.

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses) LocalQueue** — PRD-05/OFFLINE — encrypted on-device queue of draft edits + pending photo bytes
  - _Encrypted; last-write-wins drafts; server-side finalise._
- **(reuses) ChartEntry/Photo** — PRD-05 — records the queue syncs to
  - _Photos upload via signed URLs on reconnect._

## Technical notes (high level)

- Architecture decisions: [ADR-0015](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Provider app: encrypted offline queue + sync engine**
  Encrypted on-device store (encrypted box / SQLCipher, ADR-0015/SPIKE-OFFLINE) holding draft chart edits and pending photo bytes while offline. Sync engine drains the queue on reconnect with no data loss; drafts reconcile last-write-wins; pending photos upload via signed URLs once connectivity returns (bytes held encrypted locally meanwhile, consistent with C14 — never left as plain device media).
- [ ] **Provider app: persistent sync/offline indicator + finalise gating**
  Always-visible indicator subscribing to queue depth and last-sync time (prototype's 'Connected to the treatment room' banner flips to an offline/queued state with counts). Disable finalise whenever the queue is non-empty so a chart can't be sealed with edits/photos still pending — protecting the server-side immutability guarantee.
