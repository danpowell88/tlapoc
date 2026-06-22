# Walk-ins: resource conflict-flagging before confirm

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS-CONFLICT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WALKINS`

## Background

As a front desk, I want a walk-in or add-on to flag any resource clash before I confirm it, so that we never double-book a room, chair or device.
Plainly: checking that the chosen room/chair/device is free for the whole block before a walk-in or add-on is confirmed, and flagging any clash inline. Where it fits: a follow-up to the walk-ins basic gate-respecting booking (PRD-02/WALKINS) that adds resource conflict-flagging on top of the walk-in/add-on flow. It re-uses the calendar's resource model and feeds utilisation. It sits in Reception (PRD-02).

## How it works

The basic walk-in flow books against an available resource; this follow-up adds explicit conflict-flagging at the confirm step. Before a walk-in or same-day add-on confirms, the chosen room/chair/device is verified free for the whole block including buffers.
Any conflict is surfaced inline and confirmation is blocked until it is resolved, so the desk can't accidentally double-book a resource under time pressure.
The check feeds resource utilisation and the conflicts are rendered visually unmistakably, consistent with how the calendar flags clashes.

## Requirements

- A walk-in or add-on to flag any resource clash before I confirm it.

## Acceptance Criteria

- [ ] Before a walk-in/add-on confirms, the chosen room/chair/device is verified free for the whole block including buffers.
- [ ] Any conflict is surfaced inline.
- [ ] Confirmation is blocked until the conflict is resolved.
- [ ] The check feeds resource utilisation; conflicts are visually unmistakable.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — resource conflicts flagged before confirm on a walk-in/add-on.
- The confirm action is blocked while a conflict stands; the clash is shown inline.
- The check feeds resource utilisation.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Resource (ref, extends WALKINS)** — free/busy for the block incl. buffers
  - _Conflict-checked before a walk-in/add-on confirms; surfaces utilisation._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Resource conflict-flagging before confirm**
  Behaviour: before a walk-in/add-on confirms, verify the chosen room/chair/device is free for the whole block including buffers and surface any conflict inline. Requirements: confirmation is blocked until the conflict is resolved; the check feeds resource utilisation; conflicts are visually unmistakable.
