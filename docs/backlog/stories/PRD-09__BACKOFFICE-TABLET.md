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

- [ ] **Back-office bench-tablet operations surface**
  Back-office web/tablet surface composing existing module views (not re-implementing them): a 'Good morning' hub with morning attention items, then panels for open/close checklist + cold-chain log (PRD-11), stock on hand + S4 (Schedule 4 prescription-only medicine) register + waste/disposal (PRD-04), tasks (PRD-07) and shift handover (PRD-11). Apply role gating with the .fin capability so non-owner roles see no money figures; audit every action; shared-device session handling attributes actions to the acting staff member.
