# Spike — offline queue & sync integrity (provider app)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-OFFLINE`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

As a mobile engineer, I want a spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts, so that the offline-tolerant charting design is viable.
Treatment rooms drop Wi-Fi, and the provider app must queue notes and photos without losing data, with finalisation done server-side — an encrypted local queue that syncs cleanly on reconnect (ADR-0015/0010), and photos that never persist on device beyond a transient sync cache (C14/ADR-0009). The spike proves this before PRD-05/09 depend on it.  Output feeds PRD-05/OFFLINE and PRD-09 provider-offline: a proven offline queue + sync approach with last-write-wins drafts and verified no-loss behaviour.

## How it works

A Flutter prototype queues draft chart edits plus a photo offline in an encrypted local store, then syncs cleanly on reconnect with no data loss. It demonstrates conflict handling — last-write-wins for drafts — and that finalisation is server-side (a draft becomes an immutable finalised record only on the server, ADR-0010), so the device never holds the authoritative final record.
Critically, it proves photos never persist on device beyond a transient, encrypted sync cache that is purged once synced (C14/ADR-0009) — the known competitor failure mode of lost/retained photos is exactly what this guards against. The interplay with MEDIA-STORAGE's signed-URL upload is part of what's validated.
Go/no-go bar: drafts + a photo queue offline encrypted and sync with no loss; last-write-wins drafts and server-side finalisation work; photos leave no device residue after sync. It's a spike — document the approach for PRD-05/09 and discard the prototype.

## Requirements

- A spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Prototype queues drafts + a photo offline (encrypted) and syncs cleanly on reconnect with no loss.
- [ ] Conflict handling (last-write-wins for drafts) demonstrated; finalisation is server-side.
- [ ] Photos never persist on device beyond a transient sync cache (C14/ADR-0009).
- [ ] Approach documented; feeds PRD-05 / PRD-09.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0015](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)
- Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Define the spike scope, questions and go/no-go criteria**
  Frame the offline-integrity risk and the bar charting needs cleared.
  - Questions: can an encrypted local queue hold drafts + a photo offline and sync with NO loss; does last-write-wins for drafts + server-side finalisation work; do photos leave NO device residue after sync (C14/ADR-0009)?
  - Go/no-go bar: all hold, including verified no-loss sync and purge-after-sync for photos.
  - Time-box and the hand-off (PRD-05 OFFLINE / PRD-09).
- [ ] **Build the throwaway offline-queue prototype**
  Prove encrypted queue, lossless sync and photo non-retention.
  - Queue draft chart edits + a photo offline in an encrypted local store; sync cleanly on reconnect with no loss.
  - Demonstrate last-write-wins drafts and that finalisation happens server-side (device never holds the authoritative final record).
  - Prove photos persist only in a transient encrypted cache purged after sync; validate the hand-off to MEDIA-STORAGE signed-URL upload. Disposable code.
- [ ] **Document the proven offline/sync approach**
  Capture what PRD-05/OFFLINE and PRD-09 should build on.
  - The encrypted-queue + sync design, the conflict (last-write-wins) and server-side finalisation model, and the photo no-retention guarantee.
  - The go/no-go and any caveats.
  - ADR only if a real decision emerged.
