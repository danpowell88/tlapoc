# Offline queue & sync for room-side charting

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/OFFLINE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-OFFLINE`, `PRD-05/IMMUTABILITY`

## Background

As a injector, I want my notes and photos to queue locally and sync when back online if the room loses Wi-Fi, so that I never lose work mid-treatment.
If Wi-Fi drops mid-visit, notes/photos queue locally (encrypted) and sync on reconnect with no loss; finalisation is server-side (REQ-CLIN/APP, ADR-0015).

## Requirements

- My notes and photos to queue locally and sync when back online if the room loses Wi-Fi.

## Acceptance Criteria

- [ ] With connectivity dropped, notes/photos queue locally (encrypted) and sync on reconnect with no loss.
- [ ] Drafts use last-write-wins; finalisation occurs server-side.
- [ ] A sync/offline indicator shows queued count + last-sync time; finalise disabled until synced.
- [ ] Built on SPIKE-OFFLINE.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0015](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Offline queue + sync handling** — Encrypted local queue; finalise server-side.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
