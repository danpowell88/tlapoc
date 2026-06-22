# Rooms & devices register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/ROOMS-DEVICES`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a manager, I want to manage the clinic's rooms, chairs and devices as bookable resources, so that scheduling reflects real capacity and avoids conflicts.
The prototype's Operations → Rooms & devices manages the bookable rooms/chairs/devices that the calendar schedules against (resource conflict-flagging in PRD-02).

## How it works

Manage the clinic's rooms, chairs and devices as bookable resources the calendar schedules against (conflict-flagging in PRD-02). Out-of-service status removes a resource from availability; device records link to equipment maintenance.
Keeps scheduling honest about real capacity.

## Requirements

- To manage the clinic's rooms, chairs and devices as bookable resources.

## Acceptance Criteria

- [ ] Rooms/chairs/devices can be created/edited with attributes (type, location, status).
- [ ] Resources are available to the calendar for booking + conflict-flagging (PRD-02/WALKINS).
- [ ] Out-of-service status removes a resource from availability.
- [ ] Device records link to equipment maintenance (PRD-11/EQUIPMENT).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations -> Rooms & devices (ops-resources.png) — create/edit rooms/chairs/devices (type, location, status); out-of-service toggles availability.

![ops-resources — prototype screen](../screens/ops-resources.png)

## Suggested data model

- **Resource** — (shared with PRD-02) id, type(room|chair|device), name, location_id, status
  - _Out-of-service removes from availability; device links to Equipment._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Resource — (shared with PRD-02) id, type(room|chair|device), name, location_id, status (Out-of-service removes from availability; device links to Equipment.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Rooms/chairs/devices can be created/edited with attributes (type, location, status).
  - Rule: Resources are available to the calendar for booking + conflict-flagging (PRD-02/WALKINS).
  - Rule: Out-of-service status removes a resource from availability.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/CALENDAR.
- [ ] **Web UI**
  Build on the Angular web app: the ops-resources per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations -> Rooms & devices (ops-resources.png) — create/edit rooms/chairs/devices (type, location, status); out-of-service toggles availability.
