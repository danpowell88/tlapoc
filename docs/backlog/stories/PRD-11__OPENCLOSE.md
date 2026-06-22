# Daily open/close checklist (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/OPENCLOSE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a staff member, I want a daily open/close checklist that's recorded with who/when, so that the clinic opens and closes safely with an audit trail.
Plainly: the daily safe-open/safe-close routine at its core — a configurable checklist that's ticked off and recorded with who/when. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; this basic slice is the checklist model + the open/close run + the log, with the manual fridge-temperature log and its breach pathway added as follow-ups (which reconcile into one cold-chain (the unbroken temperature-controlled storage required for medicines) record with the medicines module, PRD-04). The daily open/close discipline.

## How it works

A daily routine: a configurable open and close checklist (items attributed to a role — e.g. 'Fridge 1 AM temp logged' · Reception, 'Autoclave run & cycle logged' · Lead Nurse) completed and recorded with who/when. Each daily instance is independent and audited; some items deep-link to the relevant log (cold chain, S4 register).
Logs are audited and feed the inspection pack (PRD-08); completion state surfaces on the back-office hub's morning attention items. The manual fridge-temperature log and its breach pathway are added by the follow-up (OPENCLOSE-FRIDGE), which reconciles into one cold-chain record with the automated monitors (TEMP-MONITORS). The daily safe open/close discipline.

## Requirements

- A daily open/close checklist that's recorded with who/when.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Configurable open and close checklists are completed and recorded with who/when.
- [ ] Each tick attributes to the acting staff member + timestamp; overall completion is shown.
- [ ] Logs are audited and feed the inspection pack (PRD-08).
- [ ] The manual fridge-temperature log and its breach pathway are added by the follow-up (OPENCLOSE-FRIDGE).

## UI designs / screenshots

_Prototype screen: prototype.html — Operations → Open/close & fridge log; backroom.html._

- Prototype: Operations → Open / close & fridge log (ops-openclose); also on the back-office tablet (backroom).
- Checklist items with done-state + role; recording who/when; overall completion shown. The fridge-temp log + breach are the follow-up (OPENCLOSE-FRIDGE).

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **OpenCloseChecklist** — id, tenant_id, location_id, type(open|close), items[]{label, done, role}, completed_by, at
  - _Configurable checklist; audited._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Configurable open/close checklist templates + daily instances**
  Behaviour: per-clinic open and close checklist templates (items each carrying a responsible role, e.g. 'Fridge 1 AM temp logged' · Reception, 'Autoclave run & cycle logged' · Lead Nurse) instantiated per day and type. Requirements: model OpenCloseChecklist (type[open|close], items[]{label, done, role}, completed_by, at) tenant/location-scoped under RLS (row-level security); templates are editable; each daily instance is independent and audited.
- [ ] **Open/close checklist UI (tick, attribute, complete)**
  Behaviour: today's open/close checklist on Operations (ops-openclose) and the back-office tablet — tick each item, with the role label, recording who/when, and show overall completion. Requirements: each tick attributes to the acting staff member + timestamp; completion state surfaces on the back-office hub's morning attention items; some items deep-link to the relevant log (cold chain, S4 register).
