# Equipment & maintenance register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`

## Background

As a owner, I want to track equipment servicing, validation and calibration with reminders, so that devices stay safe, validated and within service.
The prototype's Operations → Equipment & maintenance tracks sterilisation/equipment servicing (autoclave validation, spore testing, laser service/calibration) with due dates — promoted from the FAC-WORKFLOWS placeholder.

## How it works

An equipment & maintenance register tracking servicing/validation/calibration with a standard/cadence and last/next-due dates: autoclave validation + spore testing (AS 5369:2023), laser service/calibration — e.g. Autoclave (Melag) · spore weekly · next due Oct 2026 · OK; Candela GentleLase · service + calibration · next due Aug 2026 · Due soon. Due/overdue items raise alerts (facility jobs) and service events are logged with evidence (report/spore result) and audited. Feeds the inspection pack (PRD-08); Equipment links to a bookable Resource (device) from ROOMS-DEVICES. Optional per clinic.
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

- Prototype: Operations → Equipment & maintenance (ops-equipment) — table Equipment · Standard/cadence · Last · Next due · Status (OK / Due soon); 'Optional per clinic'.
- Due/overdue raise facility jobs; service events logged with evidence; feeds the inspection pack.

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **Equipment** — id, tenant_id, location_id, name, type, linked_resource_id?
  - _Links to a bookable Resource (device); optional per clinic._
- **MaintenanceRecord** — id, equipment_id, kind(service|validation|calibration|spore_test), standard, due_at, done_at, evidence_ref, status
  - _Due/overdue alerts; inspection evidence; audited._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Equipment entity + link to bookable Resource**
  Model Equipment (tenant_id, location_id, name, type, linked_resource_id?). Link a device Equipment record to its bookable Resource (ROOMS-DEVICES) so the same physical device has one identity. Optional per clinic (not every clinic runs an autoclave/laser).
- [ ] **MaintenanceRecord: schedules (service/validation/calibration/spore)**
  Model MaintenanceRecord (equipment_id, kind[service|validation|calibration|spore_test], standard, due_at, done_at, evidence_ref, status). Hold cadence/standard (e.g. AS 5369:2023 spore weekly) and compute due/overdue against done_at.
- [ ] **Equipment & maintenance register UI + due/overdue alerts**
  Register table (Equipment · Standard/cadence · Last · Next due · Status OK/Due soon). Due/overdue items raise alerts (facility jobs via the scheduler) and surface on the operations view.
- [ ] **Log service events with evidence + inspection feed**
  Log a service event (sets done_at, attaches evidence_ref — service report / spore-test result), audited. Feed equipment status + evidence into the PRD-08 inspection-readiness pack.
