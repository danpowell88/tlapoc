# Facility accreditation & expiry alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a owner, I want to record facility accreditation and be alerted before it expires, so that we never lapse on accreditation.

Per-location accreditation status + expiry alerts before lapse (REQ-FAC-1, C20).

## Requirements

- To record facility accreditation and be alerted before it expires.
- Traces to requirement(s): REQ-FAC-1.
- Must satisfy compliance obligation(s): C20.

## Acceptance Criteria

- [ ] Per-location accreditation status recorded.
- [ ] Expiry alerts fire before lapse.
- [ ] Whether accreditation is blocking or advisory is configurable (open question).
- [ ] Records are audited.

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/FACILITY.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
