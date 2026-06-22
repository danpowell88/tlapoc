# Shift handover notes

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/SHIFT-HANDOVER`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a staff member, I want to record and read shift-handover notes, so that the next shift knows outstanding tasks and issues.
The prototype's back-office tablet includes a shift-handover panel so the team passes on what the next shift needs to know.

## How it works

Shift-handover notes so the team passes on what the next shift needs to know: add/read notes, timestamped and attributed, tenant/location-scoped, shown alongside outstanding follow-ups/jobs (PRD-07). The back-office hub shows the last handover note with the morning's attention items. Accessible from the back-office tablet (PRD-09/BACKOFFICE-TABLET).
Smooth, safe shift transitions (a lightweight append-style log).

## Requirements

- To record and read shift-handover notes.

## Acceptance Criteria

- [ ] Handover notes can be added and are visible to the next shift, tenant/location-scoped.
- [ ] Outstanding follow-ups/jobs are surfaced alongside the handover.
- [ ] Handover entries are timestamped and attributed.
- [ ] Accessible from the back-office tablet (PRD-09/BACKOFFICE-TABLET).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: back-office tablet → Shift handover (backroom) — add/read handover notes; last handover note on the hub; outstanding jobs/follow-ups surfaced alongside.
- Entries timestamped and attributed.

![backroom — prototype screen](../screens/backroom.png)

## Suggested data model

- **ShiftHandover** — id, tenant_id, location_id, note, created_by, at
  - _Shown with outstanding Jobs (PRD-07)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **ShiftHandover entity + add/read notes**
  Model ShiftHandover (tenant_id, location_id, note, created_by, at) as an append-style log under RLS. Add/read notes, timestamped and attributed, tenant/location-scoped.
- [ ] **Shift-handover panel on the back-office tablet**
  Handover panel on the back-office tablet (BACKOFFICE-TABLET): list recent entries; show the last handover note on the hub alongside the morning's attention items.
- [ ] **Surface outstanding jobs/follow-ups alongside**
  Show outstanding follow-ups/jobs (PRD-07) next to the handover so the incoming shift sees notes and open work together.
