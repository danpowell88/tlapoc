# Complaints register with AHPRA pathway

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a manager, I want to log a complaint against a client/treatment and have the system surface the AHPRA pathway, so that complaints are handled correctly and retained.

A complaints/adverse-outcome register linked to client/treatment that surfaces complaint mechanisms incl. AHPRA (NDA doesn't remove the right), feeds retention (complaint → indefinite) and reporting (REQ-CLI-4, C24).

## Requirements

- To log a complaint against a client/treatment and have the system surface the AHPRA pathway.
- Traces to requirement(s): REQ-CLI-4.
- Must satisfy compliance obligation(s): C24, C18.

## Acceptance Criteria

- [ ] A complaint links to the client/treatment and surfaces complaint mechanisms incl. AHPRA (noting NDA doesn't remove the right).
- [ ] A complaint flag drives indefinite retention of the related record (C18, PRD-01).
- [ ] Complaints feed the register/reporting (PRD-08).
- [ ] A complaint can be raised from a conversation (links PRD-07).

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/COMPLAINTS.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C24, C18.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C24, C18); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
