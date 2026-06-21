# Infection-control & waste logs

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/IPC-LOGS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a staff member, I want to keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal, so that we evidence safe practice.
Sterilisation/single-use, sharps & clinical-waste disposal logs, all audited (REQ-FAC-2, C20). Fuller v2 adds manifests + sterilisation register.

## Requirements

- To keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Sterilisation/single-use and sharps/clinical-waste disposals can be logged and are audited.
- [ ] Logs are retrievable for inspection (feeds PRD-08 pack).
- [ ] A twice-daily cold-chain log with a breach pathway is supported (links PRD-04 cold-chain).
- [ ] Waste manifests/sterilisation register are captured for v2 expansion.

## UI designs / screenshots

prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
