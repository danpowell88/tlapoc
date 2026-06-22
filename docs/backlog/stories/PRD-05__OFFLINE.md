# Offline queue & sync for room-side charting

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/OFFLINE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-OFFLINE`, `PRD-05/IMMUTABILITY`

## Background

As a injector, I want my notes and photos to queue locally and sync when back online if the room loses Wi-Fi, so that I never lose work mid-treatment.
If Wi-Fi drops mid-visit, notes/photos queue locally (encrypted) and sync on reconnect with no loss; finalisation is server-side (REQ-CLIN/APP, ADR-0015).

## How it works

Treatment rooms drop Wi-Fi, so charting/photos queue locally (encrypted) and sync on reconnect with no loss; drafts use last-write-wins and finalisation occurs server-side (ADR-0015). A persistent sync indicator shows queued count + last-sync time; finalise is disabled until synced.
Primarily a provider-app capability (PRD-09) but the sync model is defined here; built on SPIKE-OFFLINE.

## Requirements

- My notes and photos to queue locally and sync when back online if the room loses Wi-Fi.

## Acceptance Criteria

- [ ] With connectivity dropped, notes/photos queue locally (encrypted) and sync on reconnect with no loss.
- [ ] Drafts use last-write-wins; finalisation occurs server-side.
- [ ] A sync/offline indicator shows queued count + last-sync time; finalise disabled until synced.
- [ ] Built on SPIKE-OFFLINE.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: provider app (treatment-room.png) shows a sync/offline indicator; finalise disabled until synced.
- Queued drafts/photos visibly pending; no data loss on reconnect.

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **LocalQueue (device)** — draft chart edits + pending photos, encrypted; sync cursor
  - _Last-write-wins drafts; server-side finalise (ADR-0010/0015)._

## Technical notes (high level)

- Architecture decisions: [ADR-0015](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - LocalQueue (device) — draft chart edits + pending photos, encrypted; sync cursor (Last-write-wins drafts; server-side finalise (ADR-0010/0015).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: With connectivity dropped, notes/photos queue locally (encrypted) and sync on reconnect with no loss.
  - Rule: Drafts use last-write-wins; finalisation occurs server-side.
  - Rule: A sync/offline indicator shows queued count + last-sync time; finalise disabled until synced.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: SPRINT-0/SPIKE-OFFLINE, PRD-05/IMMUTABILITY.
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the treatment-room per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: provider app (treatment-room.png) shows a sync/offline indicator; finalise disabled until synced.
  - Queued drafts/photos visibly pending; no data loss on reconnect.
- [ ] **Offline queue + sync handling**
  Offline-tolerant capture (provider app):
  - Encrypted on-device queue for drafts + pending media; last-write-wins for drafts.
  - Sync on reconnect with no data loss; finalisation happens server-side.
  - Persistent sync indicator (queued count + last-sync); finalise disabled until synced.
