# Open/close: manual fridge-temp log + breach pathway

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/OPENCLOSE-FRIDGE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/OPENCLOSE`, `PRD-04/COLD-CHAIN`

## Background

As a staff member, I want a twice-daily manual fridge-temperature log with an automatic breach pathway, so that cold-chain is evidenced and a warm fridge quarantines stock and raises a job.
Plainly: the twice-daily manual fridge-temperature log that hangs off the open/close routine, where an out-of-range reading quarantines the affected stock and raises a job. Where it fits: a follow-up to the open/close basic (PRD-11/OPENCLOSE) that adds the cold-chain (the unbroken temperature-controlled storage required for medicines) manual log; it is the fallback alongside the automated monitors (PRD-11/TEMP-MONITORS) and reconciles with the medicines module (PRD-04) into one evidenced cold-chain record. The breach pathway is safety-critical and must stay intact regardless of source.

## How it works

Per-fridge AM/PM manual temperature entry (openFridge → modal → saveFridge) recording temp, period, actor and time, with 'in range' / 'warm spike — recovered' states. This manual log is the fallback alongside the live monitor feed (TEMP-MONITORS); both reconcile into one cold-chain (the unbroken temperature-controlled storage required for medicines) record per fridge.
A reading outside the safe band (toxin 2–8°C) is a breach: set breach=true, quarantine the affected lot (the manufacturer's batch of a medicine vial) via PRD-04 cold-chain, and raise a job (PRD-07) automatically. The reconciled record feeds the PRD-08 inspection-readiness pack (C13); the breach path must stay intact regardless of source (manual or monitor).

## Requirements

- A twice-daily manual fridge-temperature log with an automatic breach pathway.

## Acceptance Criteria

- [ ] A twice-daily manual fridge log per fridge captures temperature with 'in range' / 'warm spike — recovered' states.
- [ ] A reading outside the safe band (toxin 2–8°C) is a breach: quarantine the affected lot (PRD-04) + raise a job (PRD-07) automatically.
- [ ] Manual + device readings reconcile into one evidenced cold-chain record (C13); logs feed the inspection pack (PRD-08).
- [ ] The breach path stays intact regardless of source (manual or monitor).

## UI designs / screenshots

- Prototype: Operations → Open / close & fridge log (ops-openclose); also on the back-office tablet (backroom).
- Per-fridge AM/PM 'Manual log' temp entry; 'in range' / 'warm spike — recovered'; breach → quarantine lot + job (openFridge/saveFridge).

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **FridgeLog** — id, tenant_id, location_id, fridge_id, period(am|pm), temp, at, actor_id, breach(bool)
  - _Extends OPENCLOSE; out-of-range → quarantine lot + Job (PRD-04/PRD-07); reconciles with TEMP-MONITORS._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Twice-daily manual fridge-temp log (openFridge/saveFridge)**
  Behaviour: per-fridge AM/PM manual temperature entry (openFridge → modal → saveFridge) recording temp, period, actor and time, with 'in range' / 'warm spike — recovered' states. Requirements: model FridgeLog (fridge_id, period[am|pm], temp, at, actor_id, breach); this manual log is the fallback alongside the live monitor feed (TEMP-MONITORS) and both reconcile into one cold-chain (the unbroken temperature-controlled storage required for medicines) record.
- [ ] **Fridge breach pathway (quarantine lot + job) + inspection feed**
  Behaviour: a reading outside the safe band (toxin 2–8°C) is a breach. Requirements: set breach=true, quarantine the affected lot (the manufacturer's batch of a medicine vial) via PRD-04 cold-chain, and raise a job (PRD-07) automatically; reconcile manual + device readings into one evidenced cold-chain record (C13); feed logs to the PRD-08 inspection-readiness pack; the breach path must stay intact regardless of source (manual or monitor).
