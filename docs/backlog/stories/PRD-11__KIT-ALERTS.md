# Emergency kit: expiry alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/KIT-ALERTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/EMERGENCY-KIT`

## Background

As a owner, I want to be alerted before an emergency-kit item expires, so that a time-critical drug is never found expired in an emergency.
Plainly: flag a lapsing emergency-kit item before it expires, so a time-critical drug like adrenaline is never found expired during an emergency. Where it fits: a follow-up to the emergency kit register (PRD-11/EMERGENCY-KIT) that adds scheduled expiry alerts; it reads the EmergencyKitItem expiry and raises an alert via the jobs scheduler.

## How it works

Flag a lapsing kit item before it expires: schedule expiry alerts (configurable lead-time) via the jobs scheduler so a time-critical item (e.g. adrenaline) is never found expired during an emergency. The alert reads the EmergencyKitItem.expiry from the register (PRD-11/EMERGENCY-KIT) — no parallel store.
This mirrors the facility accreditation alerts pattern (FACILITY-ALERTS) but for the emergency kit. It complements the register basic by keeping the kit current.

## Requirements

- To be alerted before an emergency-kit item expires.

## Acceptance Criteria

- [ ] A lapsing kit item raises an expiry alert before it expires, on a configurable lead-time.
- [ ] Alerts are scheduled via the jobs scheduler.
- [ ] The alert reads the EmergencyKitItem.expiry from the register (no parallel store).
- [ ] A time-critical item (e.g. adrenaline) is never found expired during an emergency.

## UI designs / screenshots

- Prototype: Clinical → Complication protocols — expiry flag/alert on each kit item near lapse.
- Configurable lead-time; raises a job/notification via the scheduler.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) EmergencyKitItem** — PRD-11/EMERGENCY-KIT — reads expiry to schedule alerts
  - _Extends EMERGENCY-KIT; alert raises a Job/Notification via the scheduler._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Emergency-kit expiry alerts (scheduled)**
  Behaviour: flag a lapsing kit item before it expires. Requirements: schedule expiry alerts (configurable lead-time) via the jobs scheduler so a time-critical item (e.g. adrenaline) is never found expired during an emergency.
