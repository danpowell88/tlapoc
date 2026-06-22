# Call log: shared follow-up queue (walk-ins / waitlist)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CALL-QUEUE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/CALL-LOG`, `PRD-07/FOLLOWUPS`

## Background

As a front desk, I want walk-ins and waitlist offers to share the same queue as call callbacks, so that I work one worklist instead of several.
Plainly: the front desk works one queue, not several — call callbacks, walk-ins and waitlist offers all land in one worklist. Where it fits: a follow-up to the call log basic (PRD-11/CALL-LOG) that routes walk-ins and waitlist offers through the SAME follow-up queue (PRD-07) as call callbacks. One worklist instead of scattered lists.

## How it works

The front desk works one queue, not several: route walk-ins and waitlist offers through the SAME follow-up queue (PRD-07) as call callbacks so call, walk-in and waitlist actions all land in one worklist.
This builds on the call log basic (PRD-11/CALL-LOG) and the callback bridge (CALL-FOLLOWUP), unifying the front-desk worklist. Each item is tracked to resolution; the queue reuses the PRD-07 follow-up/job model — no parallel store.

## Requirements

- Walk-ins and waitlist offers to share the same queue as call callbacks.

## Acceptance Criteria

- [ ] Walk-ins and waitlist offers route through the SAME follow-up queue as call callbacks.
- [ ] Call, walk-in and waitlist actions all land in one worklist.
- [ ] The queue reuses the PRD-07 follow-up/job model (no parallel store).
- [ ] Each item is tracked to resolution.

## UI designs / screenshots

- Prototype: Operations → Call log (ops-phone) — Walk-in / Offer from waitlist route through the same queue as call callbacks.
- One worklist for call, walk-in and waitlist actions.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) Job** — PRD-07 — walk-ins / waitlist offers / call callbacks share one follow-up queue
  - _Extends CALL-LOG; one worklist, no parallel store; each item tracked to resolution._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Shared follow-up queue (walk-ins / waitlist offers)**
  Behaviour: the front desk works one queue, not several. Requirements: route walk-ins and waitlist offers through the SAME follow-up queue as call callbacks so call, walk-in and waitlist actions all land in one worklist.
