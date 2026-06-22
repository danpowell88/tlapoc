# Clinic / location switcher

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/CLINIC-SWITCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a owner / multi-site staff, I want to switch the active clinic/location, so that I work in the right location's data.
The prototype's sidebar switches between clinics/locations (Brisbane, Gold Coast, a locum site). The in-product switcher is demonstrated; full multi-location data depth is PHASE-2/MULTI-LOCATION.

## How it works

A switcher lets multi-site owners/staff choose the active clinic/location they're working in. The prototype puts it at the top of the sidebar (setClinic) listing The Lounge — Brisbane, The Lounge — Gold Coast and Skin & Co (locum); selecting one sets the active location (updating the clinic name/location/badge in the shell).
It lists only the locations the user can access, and sets an active-location context on the session. Data shown is then scoped to the active location within the tenant (RLS tenant_id + location_id) — the diary, clients, stock and reports reflect that one location — and the active location is reflected in audit and reporting so 'where did this happen' is recorded.
This is the in-product switcher demonstrated by the prototype; deeper multi-site data depth (cross-location reporting, locum roster, per-location config) builds on PHASE-2/MULTI-LOCATION. v1 is: pick a location, work in its data, have audit/reporting know which one.
Edge cases: a single-location user sees the location label but no real switching; switching location re-scopes the current views (and closes any location-specific in-progress context cleanly); a user without access to a location never sees it in the list.

## Requirements

- To switch the active clinic/location.

## Acceptance Criteria

- [ ] A switcher lists the locations the user can access and sets the active location context.
- [ ] Data shown is scoped to the active location (RLS/tenant + location).
- [ ] The active location is reflected in audit and reporting.
- [ ] Builds on PHASE-2/MULTI-LOCATION data model where deeper multi-site features are needed.

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar clinic switcher._

- Prototype: the sidebar clinic switcher (dashboard.png) — clinic context at the top of the sidebar listing the accessible clinics (Brisbane, Gold Coast, locum site); selecting one sets the active location and updates the shell's clinic name/location/badge.
- Lists only locations the user can access; data + audit + reporting follow the active location.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(session) ActiveLocation** — session.location_id within tenant
  - _Scopes data (RLS tenant + location) + audit + reporting; lists only accessible Locations (TENANT). Deeper multi-site = PHASE-2/MULTI-LOCATION._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Active-location context + scoped switcher**
  Build the sidebar clinic/location switcher (dashboard.png) listing only the Locations the user can access (TENANT) and setting an active location_id on the session. Scope data to the active location within the tenant (RLS tenant + location) so diary/clients/stock/reports reflect it, and stamp the active location on audit + reporting. Switching re-scopes current views cleanly; single-location users see the label without a real switch. Deeper multi-site features build on PHASE-2/MULTI-LOCATION.
