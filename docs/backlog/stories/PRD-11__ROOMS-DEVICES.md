# Rooms & devices register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/ROOMS-DEVICES`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a manager, I want to manage the clinic's rooms, chairs and devices as bookable resources, so that scheduling reflects real capacity and avoids conflicts.
The prototype's Operations → Rooms & devices manages the bookable rooms/chairs/devices that the calendar schedules against (resource conflict-flagging in PRD-02).

## Requirements

- To manage the clinic's rooms, chairs and devices as bookable resources.

## Acceptance Criteria

- [ ] Rooms/chairs/devices can be created/edited with attributes (type, location, status).
- [ ] Resources are available to the calendar for booking + conflict-flagging (PRD-02/WALKINS).
- [ ] Out-of-service status removes a resource from availability.
- [ ] Device records link to equipment maintenance (PRD-11/EQUIPMENT).

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
