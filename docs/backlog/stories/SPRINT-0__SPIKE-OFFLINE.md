# Spike — offline queue & sync integrity (provider app)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-OFFLINE`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

As a mobile engineer, I want a spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts, so that the offline-tolerant charting design is viable.
Treatment rooms drop Wi-Fi; the provider app must queue notes/photos encrypted and sync without loss, with server-side finalisation (ADR-0015/0010). De-risk before PRD-05/09.

## How it works

Spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts, with server-side finalisation and photos never persisted on device beyond a transient cache (C14/ADR-0009/0015). De-risks offline-tolerant charting (PRD-05/09).

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

- [ ] **Define spike scope, questions & success criteria**
  List the unknowns to resolve and the pass/fail bar before building; time-box it.
- [ ] **Build a throwaway prototype**
  Smallest end-to-end slice that answers the questions (not production code); measure the risky bits.
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
  What worked, the gotchas, the chosen approach + its impact on the dependent stories.
