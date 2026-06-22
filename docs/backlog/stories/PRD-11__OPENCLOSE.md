# Daily open/close checklist & fridge log

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/OPENCLOSE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a staff member, I want a daily open/close checklist and a twice-daily fridge-temperature log, so that the clinic opens/closes safely and cold-chain is evidenced.
Plainly: the twice-daily safe-open/safe-close routine — a checklist plus a manual fridge-temperature log, where an out-of-range reading quarantines the affected stock and raises a job. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; the manual log is the fallback alongside automated monitors and reconciles into one cold-chain (the unbroken temperature-controlled storage required for medicines) record with the medicines module (PRD-04). The prototype's Operations → Open/close & fridge log (openFridge/saveFridge) is a twice-daily routine: an open/close checklist plus a manual fridge-temperature log with a breach pathway.

## How it works

A twice-daily routine: a configurable open and close checklist (items attributed to a role — e.g. 'Fridge 1 AM temp logged' · Reception, 'Autoclave run & cycle logged' · Lead Nurse) completed and recorded with who/when, plus a manual fridge-temperature log per fridge (AM/PM). An out-of-range reading triggers the breach pathway: quarantine the affected lot (PRD-04) + raise a job (PRD-07) automatically; openFridge/saveFridge drive the entry, with 'in range' / 'warm spike — recovered' states.
Logs are audited and feed the inspection pack (PRD-08); the manual log is the fallback alongside automated monitors (TEMP-MONITORS) and reconciles into one cold-chain record (C13). The daily safe open/close discipline.

## Requirements

- A daily open/close checklist and a twice-daily fridge-temperature log.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Configurable open and close checklists are completed and recorded with who/when.
- [ ] A twice-daily fridge log captures temperature; an out-of-range reading triggers the breach pathway (quarantine lot (the manufacturer's batch of a medicine vial) + job).
- [ ] Logs are audited and feed the inspection pack (PRD-08).
- [ ] Ties into automated temperature monitors (PRD-11/TEMP-MONITORS, PRD-04/COLD-CHAIN).

## UI designs / screenshots

_Prototype screen: prototype.html — Operations → Open/close & fridge log; backroom.html._

- Prototype: Operations → Open / close & fridge log (ops-openclose); also on the back-office tablet (backroom).
- Checklist items with done-state + role; per-fridge AM/PM 'Manual log' temp entry; 'in range' / 'warm spike — recovered'; breach → quarantine lot + job (openFridge/saveFridge).

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **OpenCloseChecklist** — id, tenant_id, location_id, type(open|close), items[]{label, done, role}, completed_by, at
  - _Configurable checklist; audited._
- **FridgeLog** — id, tenant_id, location_id, fridge_id, period(am|pm), temp, at, actor_id, breach(bool)
  - _Out-of-range → quarantine lot + Job (PRD-04/PRD-07)._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Configurable open/close checklist templates + daily instances**
  Behaviour: per-clinic open and close checklist templates (items each carrying a responsible role, e.g. 'Fridge 1 AM temp logged' · Reception, 'Autoclave run & cycle logged' · Lead Nurse) instantiated per day and type. Requirements: model OpenCloseChecklist (type[open|close], items[]{label, done, role}, completed_by, at) tenant/location-scoped under RLS (row-level security); templates are editable; each daily instance is independent and audited.
- [ ] **Open/close checklist UI (tick, attribute, complete)**
  Behaviour: today's open/close checklist on Operations (ops-openclose) and the back-office tablet — tick each item, with the role label, recording who/when, and show overall completion. Requirements: each tick attributes to the acting staff member + timestamp; completion state surfaces on the back-office hub's morning attention items; some items deep-link to the relevant log (cold chain, S4 register).
- [ ] **Twice-daily manual fridge-temp log (openFridge/saveFridge)**
  Behaviour: per-fridge AM/PM manual temperature entry (openFridge → modal → saveFridge) recording temp, period, actor and time, with 'in range' / 'warm spike — recovered' states. Requirements: model FridgeLog (fridge_id, period[am|pm], temp, at, actor_id, breach); this manual log is the fallback alongside the live monitor feed (TEMP-MONITORS) and both reconcile into one cold-chain (the unbroken temperature-controlled storage required for medicines) record.
- [ ] **Fridge breach pathway (quarantine lot + job) + inspection feed**
  Behaviour: a reading outside the safe band (toxin 2–8°C) is a breach. Requirements: set breach=true, quarantine the affected lot (the manufacturer's batch of a medicine vial) via PRD-04 cold-chain, and raise a job (PRD-07) automatically; reconcile manual + device readings into one evidenced cold-chain record (C13); feed logs to the PRD-08 inspection-readiness pack; the breach path must stay intact regardless of source (manual or monitor).
