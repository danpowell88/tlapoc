# Clinic / location switcher

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/CLINIC-SWITCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a owner / multi-site staff, I want to switch the active clinic/location, so that I work in the right location's data.
The prototype's sidebar switches between clinics/locations (Brisbane, Gold Coast, a locum site). The in-product switcher is demonstrated; full multi-location data depth is PHASE-2/MULTI-LOCATION.

## Requirements

- To switch the active clinic/location.

## Acceptance Criteria

- [ ] A switcher lists the locations the user can access and sets the active location context.
- [ ] Data shown is scoped to the active location (RLS/tenant + location).
- [ ] The active location is reflected in audit and reporting.
- [ ] Builds on PHASE-2/MULTI-LOCATION data model where deeper multi-site features are needed.

## UI designs / screenshots

prototype.html — sidebar clinic switcher.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — sidebar clinic switcher.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
