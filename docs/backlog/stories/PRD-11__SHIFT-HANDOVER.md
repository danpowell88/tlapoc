# Shift handover notes

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/SHIFT-HANDOVER`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a staff member, I want to record and read shift-handover notes, so that the next shift knows outstanding tasks and issues.
The prototype's back-office tablet includes a shift-handover panel so the team passes on what the next shift needs to know.

## How it works

Shift-handover notes so the team passes on what the next shift needs to know; notes are timestamped, attributed, tenant/location-scoped, and shown alongside outstanding follow-ups/jobs. Accessible from the back-office tablet.
Smooth, safe shift transitions.

## Requirements

- To record and read shift-handover notes.

## Acceptance Criteria

- [ ] Handover notes can be added and are visible to the next shift, tenant/location-scoped.
- [ ] Outstanding follow-ups/jobs are surfaced alongside the handover.
- [ ] Handover entries are timestamped and attributed.
- [ ] Accessible from the back-office tablet (PRD-09/BACKOFFICE-TABLET).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: back-office tablet -> Shift handover (backroom.png) — add/read handover notes; outstanding jobs surfaced alongside.

![backroom — prototype screen](../screens/backroom.png)

## Suggested data model

- **ShiftHandover** — id, tenant_id, location_id, note, created_by, at
  - _Shown with outstanding Jobs (PRD-07)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ShiftHandover — id, tenant_id, location_id, note, created_by, at (Shown with outstanding Jobs (PRD-07).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Handover notes can be added and are visible to the next shift, tenant/location-scoped.
  - Rule: Outstanding follow-ups/jobs are surfaced alongside the handover.
  - Rule: Handover entries are timestamped and attributed.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-07/FOLLOWUPS.
- [ ] **Web UI**
  Build on the Angular web app: the backroom per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: back-office tablet -> Shift handover (backroom.png) — add/read handover notes; outstanding jobs surfaced alongside.
