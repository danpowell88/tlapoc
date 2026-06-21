# Equipment & maintenance register

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/ROOMS-DEVICES`

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a owner, I want to track equipment servicing, validation and calibration with reminders, so that devices stay safe, validated and within service.

The prototype's Operations → Equipment & maintenance tracks sterilisation/equipment servicing (autoclave validation, spore testing, laser service/calibration) with due dates — promoted from the FAC-WORKFLOWS placeholder.

## Requirements

- To track equipment servicing, validation and calibration with reminders.
- Traces to requirement(s): REQ-FAC-2, REQ-FAC-4.
- Must satisfy compliance obligation(s): C20.

## Acceptance Criteria

- [ ] Equipment records hold service/validation/calibration schedules (e.g. autoclave validation, spore testing, laser service).
- [ ] Due/overdue items raise alerts and surface on the operations view.
- [ ] Service events are logged with evidence and audited.
- [ ] Feeds the inspection-readiness pack (PRD-08).

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0026 (see docs/adr/decision-log.md).
Depends on: PRD-11/ROOMS-DEVICES.

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/EQUIPMENT.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
