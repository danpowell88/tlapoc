# Offline queue & sync for room-side charting

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/OFFLINE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-OFFLINE`, `PRD-05/IMMUTABILITY`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want my notes and photos to queue locally and sync when back online if the room loses Wi-Fi, so that I never lose work mid-treatment.

If Wi-Fi drops mid-visit, notes/photos queue locally (encrypted) and sync on reconnect with no loss; finalisation is server-side (REQ-CLIN/APP, ADR-0015).

## Requirements

- My notes and photos to queue locally and sync when back online if the room loses Wi-Fi.
- Traces to requirement(s): REQ-APP-3.

## Acceptance Criteria

- [ ] With connectivity dropped, notes/photos queue locally (encrypted) and sync on reconnect with no loss.
- [ ] Drafts use last-write-wins; finalisation occurs server-side.
- [ ] A sync/offline indicator shows queued count + last-sync time; finalise disabled until synced.
- [ ] Built on SPIKE-OFFLINE.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0015, ADR-0010 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/SPIKE-OFFLINE, PRD-05/IMMUTABILITY.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/OFFLINE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Offline queue + sync handling** — Encrypted local queue; finalise server-side.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
