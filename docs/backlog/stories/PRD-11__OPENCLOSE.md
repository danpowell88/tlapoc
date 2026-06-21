# Daily open/close checklist & fridge log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/OPENCLOSE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a staff member, I want a daily open/close checklist and a twice-daily fridge-temperature log, so that the clinic opens/closes safely and cold-chain is evidenced.
The prototype's Operations → Open/close & fridge log (openFridge/saveFridge) is a twice-daily routine: an open/close checklist plus a manual fridge-temperature log with a breach pathway.

## How it works

A twice-daily routine: a configurable open/close checklist plus a fridge-temperature log. Checklists are completed and recorded with who/when; an out-of-range fridge reading triggers the breach pathway (quarantine lot + job). Logs are audited and feed the inspection pack; ties into automated monitors (TEMP-MONITORS) and PRD-04 cold-chain.
The daily safe open/close discipline.

## Requirements

- A daily open/close checklist and a twice-daily fridge-temperature log.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Configurable open and close checklists are completed and recorded with who/when.
- [ ] A twice-daily fridge log captures temperature; an out-of-range reading triggers the breach pathway (quarantine lot + job).
- [ ] Logs are audited and feed the inspection pack (PRD-08).
- [ ] Ties into automated temperature monitors (PRD-11/TEMP-MONITORS, PRD-04/COLD-CHAIN).

## UI designs / screenshots

_Prototype screen: prototype.html — Operations → Open/close & fridge log; backroom.html._

- Prototype: Operations -> Open / close & fridge log (ops-openclose.png); also on the back-office tablet (backroom.png) — checklist items + a fridge temp entry with breach handling (openFridge/saveFridge).

## Suggested data model

- **OpenCloseChecklist** — id, tenant_id, location_id, type(open|close), items[]{label, done}, completed_by, at
  - _Configurable checklist._
- **FridgeLog** — id, location_id, temp, at, actor_id, breach(bool)
  - _Out-of-range -> quarantine lot + Job (PRD-04/PRD-07)._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C13, C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Operations → Open/close & fridge log; backroom.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
