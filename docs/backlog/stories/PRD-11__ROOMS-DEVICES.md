# Rooms & devices register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/ROOMS-DEVICES`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a manager, I want to manage the clinic's rooms, chairs and devices as bookable resources, so that scheduling reflects real capacity and avoids conflicts.
Plainly: keep the clinic's rooms, chairs and devices as bookable resources so the calendar reflects real capacity and flags conflicts. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; these resources are what the booking calendar (PRD-02) schedules against. The prototype's Operations → Rooms & devices manages the bookable rooms/chairs/devices that the calendar schedules against (resource conflict-flagging in PRD-02).

## How it works

Manage the clinic's rooms, chairs and devices as bookable resources the calendar schedules against (conflict-flagging in PRD-02 — a device can't be in two rooms at once). Create/edit with attributes (type, location, status); prototype shows Room 1/2/3 and devices (Candela GentleLase · Class 4 laser · QLD laser licence, Lumecca IPL (intense pulsed light device) · TAS IPL only) with utilisation. Out-of-service status removes a resource from availability; device records link to equipment maintenance (PRD-11/EQUIPMENT).
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

- Prototype: Operations → Rooms & devices (ops-resources) — cards for rooms (Treatment/Skin) and devices (utilisation bars, licence notes); create/edit (type, location, status); out-of-service toggles availability.
- Calendar flags conflicts (a device can't be in two rooms).

![ops-resources — prototype screen](../screens/ops-resources.png)

## Suggested data model

- **Resource** — (shared with PRD-02) id, tenant_id, type(room|chair|device), name, location_id, status, licence_note?
  - _Out-of-service removes from availability; device links to Equipment._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Resource register: rooms/chairs/devices CRUD**
  Manage the shared Resource entity (type[room|chair|device], name, location_id, status, optional licence_note). CRUD on Operations → Rooms & devices; show utilisation. Same entity the PRD-02 calendar books against.
- [ ] **Expose resources to calendar + conflict-flagging**
  Make resources available to the PRD-02 calendar for booking and conflict-flagging (PRD-02/WALKINS): a device resource can't be assigned to two concurrent appointments / two rooms at once.
- [ ] **Out-of-service status + link to equipment maintenance**
  Out-of-service status removes a resource from availability (can't be scheduled while down). A device Resource carries an optional link to its Equipment maintenance record (PRD-11/EQUIPMENT) — same physical device.
