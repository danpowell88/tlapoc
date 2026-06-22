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

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Equipment — id, tenant_id, location_id, name, type, linked_resource_id? (Links to a bookable Resource (device).)
  - MaintenanceRecord — id, equipment_id, kind(service|validation|calibration|spore_test), due_at, done_at, evidence_ref (Due/overdue alerts; inspection evidence.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Equipment records hold service/validation/calibration schedules (e.g. autoclave validation, spore testing, laser service).
  - Rule: Due/overdue items raise alerts and surface on the operations view.
  - Rule: Service events are logged with evidence and audited.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-11/ROOMS-DEVICES.
- [ ] **Enforce compliance gate + audit events**
  Enforce C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Equipment records hold service/validation/calibration schedules (e.g. autoclave validation, spore testing, laser service).
- [ ] **Web UI**
  Build on the Angular web app: the ops-equipment per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations -> Equipment & maintenance (ops-equipment.png) — equipment list with service/validation schedules + due/overdue alerts.
