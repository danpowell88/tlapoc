# Emergency kit & continuity-of-care

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EMERGENCY-KIT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a owner, I want to track the emergency kit with expiry alerts and record a continuity-of-care contact, so that we're prepared for complications and cover when a prescriber is unavailable.

Track the emergency kit (hyaluronidase, anaphylaxis) with expiry alerts and record a continuity-of-care contact (REQ-FAC-3, C20).

## Requirements

- To track the emergency kit with expiry alerts and record a continuity-of-care contact.
- Traces to requirement(s): REQ-FAC-3.
- Must satisfy compliance obligation(s): C20.

## Acceptance Criteria

- [ ] Emergency-kit items (incl. hyaluronidase, anaphylaxis) raise expiry alerts before lapse.
- [ ] A continuity-of-care contact is recorded and visible when the treating practitioner/prescriber is unavailable.
- [ ] Emergency/complication protocol links are surfaced.
- [ ] Ties into the complication-response flow (PRD-05).

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/EMERGENCY-KIT.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
