# Facility: accreditation expiry alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY-ALERTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/FACILITY`

## Background

As a owner, I want to be alerted before a facility accreditation expires, so that we renew in time and never lapse.
Plainly: get warned ahead of an accreditation lapsing so renewal happens in time. Where it fits: a follow-up to the facility accreditation register (PRD-11/FACILITY) that adds scheduled expiry alerts; it reads the FacilityAccreditation record and raises a job/notification via the jobs scheduler. The clinic never operates silently out of accreditation.

## How it works

Warn ahead of an accreditation lapsing: schedule expiry alerts (configurable lead-time before expiry) via the jobs scheduler, raising a job/notification so renewal happens in time. The alert reads the FacilityAccreditation.expiry from the register (PRD-11/FACILITY) — no parallel store.
The clinic never operates silently out of accreditation. Whether a lapse blocks or merely warns is the enforcement follow-up (FACILITY-ENFORCE); this story is the warning itself.

## Requirements

- To be alerted before a facility accreditation expires.

## Acceptance Criteria

- [ ] Expiry alerts fire ahead of an accreditation lapsing, on a configurable lead-time.
- [ ] An alert raises a job/notification via the jobs scheduler.
- [ ] The alert reads the FacilityAccreditation expiry (no parallel store).
- [ ] The clinic never operates silently out of accreditation.

## UI designs / screenshots

- Prototype: Operations / facility profile — expiry alerts ahead of lapse on each accreditation row.
- Configurable lead-time; raises a job/notification.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) FacilityAccreditation** — PRD-11/FACILITY — reads expiry to schedule alerts
  - _Extends FACILITY; alert raises a Job/Notification via the scheduler._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Accreditation expiry alerts (scheduled)**
  Behaviour: warn ahead of an accreditation lapsing. Requirements: schedule expiry alerts (configurable lead-time before expiry) via the jobs scheduler, raising a job/notification so renewal happens in time; never operate silently out of accreditation.
