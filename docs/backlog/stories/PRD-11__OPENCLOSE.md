# Daily open/close checklist & fridge log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/OPENCLOSE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a staff member, I want a daily open/close checklist and a twice-daily fridge-temperature log, so that the clinic opens/closes safely and cold-chain is evidenced.

The prototype's Operations → Open/close & fridge log (openFridge/saveFridge) is a twice-daily routine: an open/close checklist plus a manual fridge-temperature log with a breach pathway.

## Requirements

- A daily open/close checklist and a twice-daily fridge-temperature log.
- Traces to requirement(s): REQ-FAC-2.
- Must satisfy compliance obligation(s): C13, C20.

## Acceptance Criteria

- [ ] Configurable open and close checklists are completed and recorded with who/when.
- [ ] A twice-daily fridge log captures temperature; an out-of-range reading triggers the breach pathway (quarantine lot + job).
- [ ] Logs are audited and feed the inspection pack (PRD-08).
- [ ] Ties into automated temperature monitors (PRD-11/TEMP-MONITORS, PRD-04/COLD-CHAIN).

## UI designs / screenshots

prototype.html — Operations → Open/close & fridge log; backroom.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0026 (see docs/adr/decision-log.md).
Depends on: PRD-04/COLD-CHAIN.

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/OPENCLOSE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C13, C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C13, C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Operations → Open/close & fridge log; backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
