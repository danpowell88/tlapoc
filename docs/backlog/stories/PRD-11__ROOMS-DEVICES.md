# Rooms & devices register (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/ROOMS-DEVICES`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a manager, I want to manage the clinic's rooms, chairs and devices as resources, so that there's one register of real capacity to schedule against.
Plainly: keep the clinic's rooms, chairs and devices on file as bookable resources with their attributes and utilisation. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; this basic slice is the resource register itself (the same entity the booking calendar schedules against), with calendar exposure + conflict-flagging and the out-of-service/equipment-link added as follow-ups. The prototype's Operations → Rooms & devices manages the bookable rooms/chairs/devices (PRD-02).

## How it works

Manage the clinic's rooms, chairs and devices as bookable resources: create/edit with attributes (type, location, status); the prototype shows Room 1/2/3 and devices (Candela GentleLase · Class 4 laser · QLD laser licence, Lumecca IPL (intense pulsed light device) · TAS IPL only) with utilisation. This basic CRUDs the shared Resource entity — the SAME entity the PRD-02 calendar books against (no duplicate model).
Exposing resources to the calendar for conflict-flagging (RESOURCE-CALENDAR) and the out-of-service status + equipment-maintenance link (RESOURCE-SERVICE) are added by the follow-ups. Keeps one honest register of real capacity.

## Requirements

- To manage the clinic's rooms, chairs and devices as resources.

## Acceptance Criteria

- [ ] Rooms/chairs/devices can be created/edited with attributes (type, location, status, optional licence note).
- [ ] Cards show utilisation; devices carry a licence note (e.g. Candela GentleLase · Class 4 laser · QLD laser licence).
- [ ] CRUD the SAME shared Resource entity the PRD-02 calendar books against (no duplicate model); tenant-scoped.
- [ ] Calendar exposure + conflict-flagging and the out-of-service/equipment-link are added by the follow-ups (RESOURCE-CALENDAR, RESOURCE-SERVICE).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations → Rooms & devices (ops-resources) — cards for rooms (Treatment/Skin) and devices (utilisation bars, licence notes); create/edit (type, location, status).
- Calendar conflict-flagging + out-of-service/equipment-link are the follow-ups (RESOURCE-CALENDAR, RESOURCE-SERVICE).

![ops-resources — prototype screen](../screens/ops-resources.png)

## Suggested data model

- **Resource** — (shared with PRD-02) id, tenant_id, type(room|chair|device), name, location_id, status, licence_note?
  - _The SAME entity the PRD-02 calendar books against; calendar exposure + equipment link in the follow-ups._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Resource register: rooms/chairs/devices CRUD + utilisation**
  Behaviour: manage rooms, chairs and devices as bookable resources on Operations → Rooms & devices (cards with utilisation bars; devices carry a licence note, e.g. Candela GentleLase · Class 4 laser · QLD laser licence). Requirements: CRUD the shared Resource entity (type[room|chair|device], name, location_id, status, optional licence_note) — the SAME entity the PRD-02 calendar books against (no duplicate model); tenant-scoped.
