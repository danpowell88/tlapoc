# Back-office / bench tablet surface

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/BACKOFFICE-TABLET`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/OPENCLOSE`, `PRD-07/FOLLOWUPS`

## Background

As a clinic staff, I want a bench-tablet view of the day's operational jobs, so that behind-the-scenes work (logs, stock, handover) is quick at the bench.
Plainly: a back-room bench tablet pulling the day's operational jobs into one place — open/close, fridge/cold-chain (the unbroken temperature-controlled storage required for medicines), stock, the controlled-drug register, waste log, tasks and handover. Where it fits: a late surface that composes existing module views (PRD-04 medicines, PRD-11 operations, PRD-07 jobs) rather than re-implementing them. The prototype's backroom surface is a bench tablet for behind-the-scenes work: open/close, cold-chain, stock on hand, S4 drug register, waste/disposal log, tasks and shift handover — a focused operations view.

## How it works

A bench tablet for behind-the-scenes work, opening on a 'Good morning' hub that shows the morning's attention items (open/close progress, cold-chain, expiring stock, last handover). Panels: open/close checklist, cold-chain (fridge) log, stock on hand, Schedule 4 (S4, prescription-only medicine) drug register, waste & disposal log, tasks and shift handover — each re-using the underlying module (PRD-04 medicines, PRD-11 operations, PRD-07 jobs, PRD-11 handover) rather than duplicating data.
Role/financial gating applies (owner-only money stays gated via .fin); actions are audited; shared-device session handling attributes actions to the acting staff member. A focused operations view for the back room.

## Requirements

- A bench-tablet view of the day's operational jobs.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Surfaces open/close checklist, cold-chain log, stock on hand, S4 register, waste log, tasks and shift handover.
- [ ] Each panel reuses the underlying modules (PRD-04 medicines, PRD-11 operations, PRD-07 jobs).
- [ ] Role/financial gating applies; actions are audited.
- [ ] Usable on a shared device with appropriate session handling.

## UI designs / screenshots

_Prototype screen: backroom.html._

- Prototype: backroom — 'Good morning, Tessa' hub with morning attention items; tabs Today · Open & close · Cold chain · Stock · S4 register · Waste log · Tasks & handover.
- Shared-device session handling; financial figures stay owner-only (gated).

![backroom — prototype screen](../screens/backroom.png)

## Suggested data model

- **(reuses) OpenCloseChecklist/FridgeLog** — PRD-11 — open/close + cold-chain panels
  - _Aggregates operations._
- **(reuses) StockItem/StockLedger/S4 register/StockDestruction** — PRD-04 — stock on hand, S4 register, waste/disposal
  - _Aggregates medicines._
- **(reuses) Job/ShiftHandover** — PRD-07 jobs + PRD-11 handover — tasks + handover panels
  - _Aggregates jobs + handover._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Bench-tablet shell + 'Good morning' hub + shared-device sessions**
  Behaviour: a back-office web/tablet surface with a left rail (Today · Open & close · Cold chain · Stock · S4 register · Waste log · Tasks & handover) opening on a 'Good morning' hub that pulls the morning's attention items (open/close progress, cold-chain status, expiring stock, last handover) into one glance. Requirements: composes existing module views (does NOT re-implement them); shared-device session handling attributes every action to the acting staff member; role/financial gating applies (owner-only money stays behind the .fin capability); all actions audited.
- [ ] **Open/close checklist + cold-chain (fridge) log panels (PRD-11)**
  Behaviour: the Open & close panel renders today's checklist (tick items, each recording who/when, with the responsible role) and the Cold chain panel logs AM/PM fridge temperatures with in-range / breach states. Requirements: reuses PRD-11/OPENCLOSE + TEMP-MONITORS — an out-of-2–8°C reading raises the breach pathway (quarantine the affected lot (the manufacturer's batch of a medicine vial) + a job); no parallel data store; audited.
- [ ] **Stock-on-hand + S4 register + waste-log panels (PRD-04)**
  Behaviour: the Stock panel shows on-hand levels with par lines, expiry watch and one-tap reorder/receive; the S4 register reconciles received vs administered vs wasted against a physical count; the Waste log records witnessed disposal of partial/expired S4 (Schedule 4 prescription-only medicine) vials. Requirements: reuses the PRD-04 StockItem/StockLedger/S4 register/StockDestruction entities (batch + expiry tracked); the register is append-only and reconciled; witnessed-disposal capture is required for traceability; no money figures shown to non-owner roles (.fin).
- [ ] **Tasks panel (PRD-07) + shift-handover panel (PRD-11)**
  Behaviour: the Tasks & handover panel shows the team's to-dos / restock nudges / compliance dates (PRD-07 jobs) alongside the shift-to-shift handover note (PRD-11). Requirements: reuses PRD-07/FOLLOWUPS jobs and PRD-11/SHIFT-HANDOVER (add/read, timestamped + attributed); outstanding jobs surface next to the handover so the incoming shift sees both together; the last handover note also appears on the hub.
