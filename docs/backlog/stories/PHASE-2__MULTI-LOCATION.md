# Multi-location switching UI (placeholder)

> **Epic:** [PHASE-2 — Phase 2+ / scale (cross-cutting placeholders)](../epics/PHASE-2.md)  ·  **Key:** `PHASE-2/MULTI-LOCATION`  ·  **Type:** Story  ·  **Stage:** M7  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web

## Background

As a owner of multiple sites, I want to switch between locations in one place, so that I run several clinics from one login.
As an owner of multiple sites, I want to switch between locations in one place, so that I run several clinics from one login.  Switching between locations/clinics in one tenant. The data model is location-aware; the switching UX is deferred.

## How it works

Placeholder (Phase 2+): switching between locations/clinics in one tenant. The data model is already location-aware (Location on every relevant entity), so this is the switching UX + cross-location reporting rollups — built on PLATFORM/CLINIC-SWITCH. Captured so reporting/booking stay location-aware.

## Requirements

- To switch between locations in one place.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2+; data model already carries Location.
- [ ] Captured so reporting/booking stay location-aware.

## UI designs / screenshots

Future — not built in the prototype (some shown as concept cards in Settings → Integrations).

## Suggested data model

- **(reuses) Location** — already on tenant-scoped entities
  - _Switching UX + cross-location rollups deferred._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Placeholder: location switching UX + cross-location rollups (Phase 2+)**
  Deferred. Switching UX + cross-location reporting rollups on the already location-aware model; built on PLATFORM/CLINIC-SWITCH. Not built in v1.
