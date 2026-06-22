# Resources: calendar exposure + conflict-flagging

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/RESOURCE-CALENDAR`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`, `PRD-02/CALENDAR`

## Background

As a manager, I want resources exposed to the calendar with conflict-flagging, so that scheduling avoids double-booking a room or device.
Plainly: make the rooms/chairs/devices register available to the booking calendar so a device can't be double-booked into two rooms at once. Where it fits: a follow-up to the rooms & devices register (PRD-11/ROOMS-DEVICES) that wires resources into the booking calendar (PRD-02); availability reflects each resource's status in real time and PRD-02/WALKINS surfaces a conflict before confirm.

## How it works

Make resources available to the PRD-02 calendar for booking and conflict-flagging: a device resource can't be assigned to two concurrent appointments / two rooms at once (PRD-02/WALKINS surfaces the conflict before confirm). Availability reflects each resource's status in real time.
This builds on the resource register (PRD-11/ROOMS-DEVICES), turning the register into live scheduling capacity. The out-of-service status that removes a resource from availability is its own follow-up (RESOURCE-SERVICE).

## Requirements

- Resources exposed to the calendar with conflict-flagging.

## Acceptance Criteria

- [ ] Resources are available to the PRD-02 calendar for booking and conflict-flagging.
- [ ] A device resource can't be assigned to two concurrent appointments / two rooms at once.
- [ ] PRD-02/WALKINS surfaces the conflict before confirm.
- [ ] Availability reflects each resource's status in real time.

## UI designs / screenshots

- Prototype: Operations → Rooms & devices feeds the PRD-02 calendar; calendar flags conflicts (a device can't be in two rooms).
- Availability reflects resource status in real time; conflict surfaced before confirm (WALKINS).

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) Resource** — (shared with PRD-02) exposed for booking + conflict-flagging
  - _Extends ROOMS-DEVICES; PRD-02 calendar books against it; conflict surfaced before confirm._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Expose resources to the calendar + conflict-flagging**
  Behaviour: make resources available to the PRD-02 calendar for booking and conflict-flagging. Requirements: a device resource can't be assigned to two concurrent appointments / two rooms at once (PRD-02/WALKINS surfaces the conflict before confirm); availability reflects each resource's status in real time.
