# Equipment & maintenance register (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`

## Background

As a owner, I want a register of equipment with their service/validation/calibration schedules, so that I can see each device's cadence and when it's next due.
Plainly: a register of the clinic's serviceable equipment with each item's service/validation/calibration cadence and last/next-due dates. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core, promoted from the FAC-WORKFLOWS placeholder; this basic slice is the Equipment entity (linked to its bookable device), the MaintenanceRecord schedules and the register table, with due/overdue alerts and evidence-logging added as follow-ups. The prototype's Operations → Equipment & maintenance tracks servicing with due dates.

## How it works

An equipment & maintenance register tracking servicing/validation/calibration with a standard/cadence and last/next-due dates: autoclave validation + spore testing (AS 5369:2023), laser service/calibration — e.g. Autoclave (Melag) · spore weekly · next due Oct 2026 · OK; Candela GentleLase · service + calibration · next due Aug 2026 · Due soon. The register table surfaces on Operations; Equipment links to a bookable Resource (device) from ROOMS-DEVICES. Optional per clinic.
Due/overdue alerts (EQUIPMENT-ALERTS) and logging service events with evidence (EQUIPMENT-EVIDENCE) are added by the follow-ups. Keeps a register of devices and their schedules (promoted from the FAC-WORKFLOWS placeholder).

## Requirements

- A register of equipment with their service/validation/calibration schedules.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Equipment records (linked to a bookable device Resource) hold service/validation/calibration schedules (e.g. autoclave validation, spore testing, laser service).
- [ ] MaintenanceRecord holds the standard/cadence and derives due/overdue against done_at.
- [ ] The register table (Equipment · Standard/cadence · Last · Next due · Status OK / Due soon) surfaces on Operations; 'Optional per clinic' is shown.
- [ ] Due/overdue alerts and evidence-logged service events are added by the follow-ups (EQUIPMENT-ALERTS, EQUIPMENT-EVIDENCE).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations → Equipment & maintenance (ops-equipment) — table Equipment · Standard/cadence · Last · Next due · Status (OK / Due soon); 'Optional per clinic'.
- Due/overdue alerts + evidence-logged service events are the follow-ups (EQUIPMENT-ALERTS, EQUIPMENT-EVIDENCE).

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **Equipment** — id, tenant_id, location_id, name, type, linked_resource_id?
  - _Links to a bookable Resource (device); optional per clinic._
- **MaintenanceRecord** — id, equipment_id, kind(service|validation|calibration|spore_test), standard, due_at, done_at, evidence_ref, status
  - _Holds the cadence + derives due/overdue; alerts + evidence-logging in the follow-ups._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Equipment entity + link to bookable Resource**
  Behaviour: model the clinic's serviceable equipment and tie each device to its bookable identity. Requirements: model Equipment (tenant_id, location_id, name, type, linked_resource_id?); link a device Equipment record to its bookable Resource (ROOMS-DEVICES) so the same physical device has one identity across booking and servicing; optional per clinic (not every clinic runs an autoclave/laser).
- [ ] **MaintenanceRecord: service/validation/calibration/spore schedules**
  Behaviour: hold each item's servicing/validation/calibration cadence and compute when it's due. Requirements: model MaintenanceRecord (equipment_id, kind[service|validation|calibration|spore_test], standard, due_at, done_at, evidence_ref, status) holding the standard/cadence (e.g. AS 5369:2023 spore weekly) and deriving due/overdue against done_at; supports autoclave validation + spore testing and laser service/calibration.
- [ ] **Equipment & maintenance register table UI**
  Behaviour: the Equipment & maintenance register table (Equipment · Standard/cadence · Last · Next due · Status OK / Due soon) on Operations. Requirements: lists each item with its derived due/overdue status; 'Optional per clinic' is shown; renew/log actions are reachable from the row (the log action is built in EQUIPMENT-EVIDENCE).
