# Resources: out-of-service + equipment-maintenance link

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/RESOURCE-SERVICE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`, `PRD-11/EQUIPMENT`

## Background

As a manager, I want to take a resource out of service and link a device to its maintenance record, so that a device down for service can't be booked and has one identity across booking and servicing.
Plainly: marking a resource out-of-service removes it from availability, and a device resource links to its maintenance record so the same physical device has one identity across booking and servicing. Where it fits: a follow-up to the rooms & devices register (PRD-11/ROOMS-DEVICES) that adds the out-of-service status and the equipment link (PRD-11/EQUIPMENT).

## How it works

Marking a resource out-of-service removes it from availability, and a device resource links to its maintenance record: an out-of-service resource can't be scheduled while down. A device Resource carries an optional link to its Equipment maintenance record (PRD-11/EQUIPMENT) so the same physical device has one identity across booking and servicing.
This builds on the resource register (PRD-11/ROOMS-DEVICES) and complements the calendar exposure (RESOURCE-CALENDAR) by honouring the out-of-service state. Status changes are audited.

## Requirements

- To take a resource out of service and link a device to its maintenance record.

## Acceptance Criteria

- [ ] Marking a resource out-of-service removes it from availability — it can't be scheduled while down.
- [ ] A device Resource carries an optional link to its Equipment maintenance record (PRD-11/EQUIPMENT).
- [ ] The same physical device has one identity across booking and servicing.
- [ ] Status changes are audited.

## UI designs / screenshots

- Prototype: Operations → Rooms & devices (ops-resources) — out-of-service toggles availability; device links to its Equipment maintenance record.
- Out-of-service can't be scheduled; one device identity across booking + servicing.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) Resource + Equipment** — Resource.status=out_of_service removes from availability; device Resource → Equipment maintenance link (PRD-11/EQUIPMENT)
  - _Extends ROOMS-DEVICES; one device identity across booking and servicing._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Out-of-service status + link to equipment maintenance**
  Behaviour: marking a resource out-of-service removes it from availability, and a device resource links to its maintenance record. Requirements: an out-of-service resource can't be scheduled while down; a device Resource carries an optional link to its Equipment maintenance record (PRD-11/EQUIPMENT) so the same physical device has one identity across booking and servicing.
