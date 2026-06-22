# Equipment: due/overdue maintenance alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT-ALERTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/EQUIPMENT`

## Background

As a owner, I want alerts when equipment maintenance is due or overdue, so that devices stay validated and within service.
Plainly: raise alerts when an equipment service/validation/calibration is due or overdue so devices stay within service. Where it fits: a follow-up to the equipment register (PRD-11/EQUIPMENT) that adds scheduled due/overdue alerts; it reads the MaintenanceRecord due dates and raises facility jobs via the scheduler, surfacing on the operations view.

## How it works

Raise alerts when an equipment service/validation/calibration is due or overdue: due/overdue items raise alerts (facility jobs via the scheduler) and surface on the operations view. The alert reads the MaintenanceRecord due/overdue status from the register (PRD-11/EQUIPMENT) — no parallel store.
This mirrors the facility/kit alerts pattern but for equipment maintenance. It complements the register basic by keeping devices within service; the evidence-logging of a completed service is its own follow-up (EQUIPMENT-EVIDENCE).

## Requirements

- Alerts when equipment maintenance is due or overdue.

## Acceptance Criteria

- [ ] Due/overdue items raise alerts (facility jobs via the scheduler).
- [ ] Alerts surface on the operations view.
- [ ] The alert reads the MaintenanceRecord due/overdue status from the register (no parallel store).
- [ ] Devices don't silently fall out of service.

## UI designs / screenshots

- Prototype: Operations → Equipment & maintenance — due/overdue rows raise facility jobs and surface on the operations view.
- Scheduler-driven alerts read the MaintenanceRecord due dates.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) MaintenanceRecord** — PRD-11/EQUIPMENT — reads due_at/status to raise due/overdue alerts
  - _Extends EQUIPMENT; alert raises a facility Job via the scheduler._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Due/overdue maintenance alerts (scheduled)**
  Behaviour: warn when an equipment service/validation/calibration is due or overdue. Requirements: due/overdue items raise alerts (facility jobs via the scheduler) by reading the MaintenanceRecord due/overdue status and surface on the operations view; devices never silently fall out of service.
