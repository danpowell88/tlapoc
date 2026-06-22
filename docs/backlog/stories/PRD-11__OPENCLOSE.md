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

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **OpenCloseChecklist** — id, tenant_id, location_id, type(open|close), items[]{label, done}, completed_by, at
  - _Configurable checklist._
- **FridgeLog** — id, location_id, temp, at, actor_id, breach(bool)
  - _Out-of-range -> quarantine lot + Job (PRD-04/PRD-07)._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - OpenCloseChecklist — id, tenant_id, location_id, type(open|close), items[]{label, done}, completed_by, at (Configurable checklist.)
  - FridgeLog — id, location_id, temp, at, actor_id, breach(bool) (Out-of-range -> quarantine lot + Job (PRD-04/PRD-07).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Configurable open and close checklists are completed and recorded with who/when.
  - Rule: A twice-daily fridge log captures temperature; an out-of-range reading triggers the breach pathway (quarantine lot + job).
  - Rule: Logs are audited and feed the inspection pack (PRD-08).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/COLD-CHAIN.
- [ ] **Enforce compliance gate + audit events**
  Enforce C13, C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the ops-openclose per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations -> Open / close & fridge log (ops-openclose.png); also on the back-office tablet (backroom.png) — checklist items + a fridge temp entry with breach handling (openFridge/saveFridge).
