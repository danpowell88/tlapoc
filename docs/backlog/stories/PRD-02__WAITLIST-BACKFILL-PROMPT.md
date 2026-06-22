# Waitlist: cancel/no-show backfill prompt

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WAITLIST-BACKFILL-PROMPT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WAITLIST`, `PRD-02/WAITLIST-MATCHING`

## Background

As a front desk, I want a prompt to offer a slot to the waitlist when an appointment cancels or no-shows, so that I can trigger backfill at the moment a slot opens.
Plainly: the prompt that appears on the Schedule when an appointment is cancelled or no-showed, offering to fill the slot from the waitlist. Where it fits: a follow-up to the waitlist basic entries & management (PRD-02/WAITLIST) that adds the desk-facing trigger on top of the matching engine (PRD-02/WAITLIST-MATCHING). It surfaces the matching engine and quiet-window fill suggestions from the calendar's utilisation data. It sits in Reception (PRD-02).

## How it works

The matching engine runs on slot-freed events; this follow-up gives the desk an explicit trigger. When an appointment is cancelled or no-showed, a prompt appears on the Schedule offering to fill the freed slot from the waitlist.
Acting on the prompt triggers the matching engine (PRD-02/WAITLIST-MATCHING) to offer the slot to the best matching waiting entry. Quiet-window fill suggestions also surface from the calendar's utilisation data (the amber cells / quiet-windows panel).
The prompt is reachable from the Schedule so the desk acts at the moment a slot opens, keeping the diary full.

## Requirements

- A prompt to offer a slot to the waitlist when an appointment cancels or no-shows.

## Acceptance Criteria

- [ ] A prompt appears when an appointment is cancelled/no-showed ('offer this slot to the waitlist').
- [ ] The backfill prompt triggers the matching engine.
- [ ] Quiet-window fill suggestions surface from utilisation data.
- [ ] The prompt is reachable from the Schedule.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — a backfill prompt when an appointment cancels/no-shows ('offer this slot to the waitlist'), and quiet-window fill suggestions from utilisation data.
- The prompt triggers the matching engine; reachable from the Schedule.
- Quiet-window suggestions tie to the calendar utilisation data.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends WAITLIST)** — no new entities; the prompt triggers WAITLIST-MATCHING on a cancel/no-show
  - _Reads calendar utilisation for quiet-window suggestions; offers via the matching engine._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Cancel/no-show backfill prompt + quiet-window suggestions**
  Behaviour: a prompt when an appointment is cancelled/no-showed ('offer this slot to the waitlist'), plus quiet-window fill suggestions from utilisation data. Requirements: the backfill prompt triggers the matching engine; the suggestions read the calendar's utilisation data; reachable from the Schedule.
