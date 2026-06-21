# Equipment & maintenance register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`

## Background

As a owner, I want to track equipment servicing, validation and calibration with reminders, so that devices stay safe, validated and within service.
The prototype's Operations → Equipment & maintenance tracks sterilisation/equipment servicing (autoclave validation, spore testing, laser service/calibration) with due dates — promoted from the FAC-WORKFLOWS placeholder.

## How it works

An equipment & maintenance register tracking servicing/validation/calibration (autoclave validation, spore testing, laser service/calibration) with due dates; due/overdue items raise alerts and service events are logged with evidence and audited. Feeds the inspection pack.
Keeps devices safe, validated and in-service (promoted from the FAC-WORKFLOWS placeholder).

## Requirements

- To track equipment servicing, validation and calibration with reminders.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Equipment records hold service/validation/calibration schedules (e.g. autoclave validation, spore testing, laser service).
- [ ] Due/overdue items raise alerts and surface on the operations view.
- [ ] Service events are logged with evidence and audited.
- [ ] Feeds the inspection-readiness pack (PRD-08).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations -> Equipment & maintenance (ops-equipment.png) — equipment list with service/validation schedules + due/overdue alerts.

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **Equipment** — id, tenant_id, location_id, name, type, linked_resource_id?
  - _Links to a bookable Resource (device)._
- **MaintenanceRecord** — id, equipment_id, kind(service|validation|calibration|spore_test), due_at, done_at, evidence_ref
  - _Due/overdue alerts; inspection evidence._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
