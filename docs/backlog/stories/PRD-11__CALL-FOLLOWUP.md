# Call log: callback job + comms history

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CALL-FOLLOWUP`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/CALL-LOG`, `PRD-07/FOLLOWUPS`

## Background

As a front desk, I want a call to raise a callback and appear in the client's comms history, so that callbacks happen and the call is visible in the client's history.
Plainly: a logged call can spawn a callback job and shows up in the client's comms history, and missed calls auto-text-back and become callback jobs tracked to resolution. Where it fits: a follow-up to the call log basic (PRD-11/CALL-LOG) that bridges calls into the follow-up queue (PRD-07) and the client's comms history. Nothing slips through after a missed call.

## How it works

A call can spawn a callback and is visible in the client's history: a call can raise a follow-up Job (PRD-07); a linked call appears in the client's comms history; missed calls auto-text-back and become callback jobs; a missed-call/callback is tracked to resolution ('Log callback').
This builds on the call log basic (PRD-11/CALL-LOG), bridging calls into the follow-up worklist and the comms timeline. The shared queue that also carries walk-ins/waitlist offers is its own follow-up (CALL-QUEUE).

## Requirements

- A call to raise a callback and appear in the client's comms history.

## Acceptance Criteria

- [ ] A call can raise a follow-up Job (PRD-07).
- [ ] A linked call appears in the client's comms history.
- [ ] Missed calls auto-text-back and become callback jobs.
- [ ] A missed-call/callback is tracked to resolution ('Log callback').

## UI designs / screenshots

- Prototype: Operations → Call log (ops-phone) — missed → text-back sent; 'Log callback'; call appears in comms history.
- A call raises a follow-up; missed-call/callback tracked to resolution.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) CallLog + Job** — PRD-11/CALL-LOG call raises a PRD-07 follow-up Job; linked call shows in comms history
  - _Extends CALL-LOG; missed-call auto-text-back → callback job tracked to resolution._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Call → follow-up job + comms history**
  Behaviour: a call can spawn a callback and is visible in the client's history. Requirements: a call can raise a follow-up Job (PRD-07); a linked call appears in the client's comms history; missed calls auto-text-back and become callback jobs; a missed-call/callback is tracked to resolution ('Log callback').
