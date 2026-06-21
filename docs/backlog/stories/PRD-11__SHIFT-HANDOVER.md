# Shift handover notes

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/SHIFT-HANDOVER`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a staff member, I want to record and read shift-handover notes, so that the next shift knows outstanding tasks and issues.

The prototype's back-office tablet includes a shift-handover panel so the team passes on what the next shift needs to know.

## Requirements

- To record and read shift-handover notes.
- Traces to requirement(s): REQ-FAC-2.

## Acceptance Criteria

- [ ] Handover notes can be added and are visible to the next shift, tenant/location-scoped.
- [ ] Outstanding follow-ups/jobs are surfaced alongside the handover.
- [ ] Handover entries are timestamped and attributed.
- [ ] Accessible from the back-office tablet (PRD-09/BACKOFFICE-TABLET).

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-07/FOLLOWUPS.

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/SHIFT-HANDOVER.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
