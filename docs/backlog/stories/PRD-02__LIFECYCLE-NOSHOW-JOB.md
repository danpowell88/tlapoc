# Visit lifecycle: no-show flag → auto follow-up job

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE-NOSHOW-JOB`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a front desk, I want flagging a no-show to automatically raise a follow-up call, so that no missed appointment is ever lost without a recovery attempt.
Plainly: when reception flags a row as a no-show, the system automatically creates a follow-up call task so the client is chased; flagging 'late' just marks the row. Where it fits: a follow-up to the visit lifecycle basic state-machine (PRD-02/LIFECYCLE) that wires the no-show transition to the follow-up/job queue. The created job is handled by Comms (PRD-07). It sits in Reception (PRD-02).

## How it works

The basic state-machine supports the no_show and late transitions; this follow-up gives no-show a consequence. Flagging a row no-show auto-creates a recovery task so the no-show (a client who misses an appointment without notice) is always chased.
A no_show transition creates a follow-up CALL job in the PRD-07 jobs queue (assignee = reception, source = system, due = today); flagging late only marks the row and raises no job.
The job creation is idempotent — re-flagging the same appointment never duplicates the job — so the recovery worklist stays clean.

## Requirements

- Flagging a no-show to automatically raise a follow-up call.

## Acceptance Criteria

- [ ] A no_show transition auto-creates a follow-up CALL job (assignee = reception, source = system, due = today).
- [ ] Flagging 'late' raises no job; it only marks the row.
- [ ] The job-creation is idempotent — re-flagging never duplicates the job.
- [ ] The created job lands in the PRD-07 follow-up/job queue.

## UI designs / screenshots

- Prototype: Today (dashboard.png) — a no-show row links into Follow-ups; Late and No-show are distinct flags.
- Flagging no-show creates a follow-up call; flagging late only marks the row.
- The follow-up appears in the PRD-07 jobs queue.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends LIFECYCLE)** — no new entities; a no_show transition raises a Job (PRD-07)
  - _Idempotent job creation; the Job entity is owned by Comms (PRD-07)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **No-show → auto follow-up call job (late = flag only)**
  Behaviour: flagging a row no-show auto-creates a recovery task; flagging late only marks the row. Requirements: a no_show transition creates a Follow-up CALL job in the PRD-07 jobs queue (assignee=reception, source=system, due=today) so the no-show (a client who misses an appointment without notice) is recovered; late raises no job; idempotent — re-flagging never duplicates the job.
