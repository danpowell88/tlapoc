# Call / phone log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CALL-LOG`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a front desk, I want to log phone calls against a client and raise a follow-up if needed, so that phone interactions aren't lost and callbacks happen.

The prototype's Operations → Call log records inbound/outbound phone interactions against clients and raises follow-ups (the phone is still a primary clinic channel).

## Requirements

- To log phone calls against a client and raise a follow-up if needed.
- Traces to requirement(s): REQ-CLI-1.

## Acceptance Criteria

- [ ] Calls can be logged (direction, client link, summary, outcome).
- [ ] A call can raise a follow-up job (PRD-07) and appears in the client's comms history.
- [ ] Logs are tenant-scoped and audited.
- [ ] A missed-call/callback can be tracked to resolution.

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-07/FOLLOWUPS.

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/CALL-LOG.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
