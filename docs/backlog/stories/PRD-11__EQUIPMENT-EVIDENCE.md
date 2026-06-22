# Equipment: log service events with evidence

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EQUIPMENT-EVIDENCE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/EQUIPMENT`

## Background

As a owner, I want to log a completed service event with its evidence, so that a regulator can see devices are validated and in-service.
Plainly: log a completed service event with proof (service report / spore-test result) so a regulator can see devices are validated and in-service. Where it fits: a follow-up to the equipment register (PRD-11/EQUIPMENT) that adds evidence-logging; setting done_at attaches the evidence and is audited, feeding the inspection-readiness pack (PRD-08).

## How it works

Log a completed service event with proof: setting done_at attaches evidence_ref (service report / spore-test result) and is audited. Equipment status + evidence feed the PRD-08 inspection-readiness pack so a regulator can see devices are validated and in-service.
This builds on the equipment register (PRD-11/EQUIPMENT) by closing out a maintenance item with evidence, and complements the due/overdue alerts (EQUIPMENT-ALERTS) — logging a service resets the next-due cadence. Reachable from the register row.

## Requirements

- To log a completed service event with its evidence.

## Acceptance Criteria

- [ ] Setting done_at on a MaintenanceRecord attaches evidence_ref (service report / spore-test result).
- [ ] The service event is audited.
- [ ] Equipment status + evidence feed the PRD-08 inspection-readiness pack.
- [ ] Logging is reachable from the register row.

## UI designs / screenshots

- Prototype: Operations → Equipment & maintenance — log a service event from the row, attaching evidence (report / spore result).
- Setting done_at + evidence feeds the PRD-08 inspection pack; audited.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) MaintenanceRecord** — PRD-11/EQUIPMENT — done_at + evidence_ref (service report / spore-test result)
  - _Extends EQUIPMENT; logging a service event is audited and feeds the inspection pack._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Log service events with evidence + inspection feed**
  Behaviour: log a completed service event with proof. Requirements: setting done_at attaches evidence_ref (service report / spore-test result) and is audited; equipment status + evidence feed the PRD-08 inspection-readiness pack so a regulator can see devices are validated and in-service.
