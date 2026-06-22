# Staff Follow-ups: view / call back / resolve a concern

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CONCERN-TRIAGE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CONCERN`, `PRD-07/FOLLOWUPS`

## Background

As a clinic staff, I want to view a reported concern in Follow-ups, call the client back and resolve it, so that concerns are worked and closed, most urgent first.
Plainly: the staff side of the safety channel — a reported concern shows up in Follow-ups where staff view it, call the client back and resolve it. Where it fits: a follow-up to the concern basic (PRD-09/CLIENT-CONCERN) that adds the staff triage workflow; it works the Job the concern raises in the follow-ups/job-queue (PRD-07), surfacing urgency so the most pressing concerns are worked first.

## How it works

In staff Follow-ups, render the concern job (prototype openConcern 'View report') with the client and treatment linked; surface urgency so the most pressing concerns are worked first. Staff call the client back and resolve it (concernCall → 'Marked as actioned — client called back', job → done).
Resolving updates the Concern status and closes the linked Job (PRD-07); the exchange is recorded and audited. Escalation to an adverse event / complaint is its own follow-up (CONCERN-ESCALATE).

## Requirements

- To view a reported concern in Follow-ups, call the client back and resolve it.

## Acceptance Criteria

- [ ] In staff Follow-ups, the concern job renders ('View report' → openConcern) with its urgency surfaced.
- [ ] Staff can call the client back and resolve it (concernCall → 'Marked as actioned — client called back', job → done).
- [ ] Resolving updates the Concern status and the linked Job.
- [ ] The exchange is recorded and audited.

## UI designs / screenshots

- Prototype: staff Follow-ups — concern job ('View report' → openConcern; 'client called back' → concernCall → 'Marked as actioned').
- Urgency surfaced; resolving sets the job to done.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Concern/Job** — status transitions (open → actioned/done); call-back recorded
  - _Extends CLIENT-CONCERN; works the Job the concern raised; audited._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Staff Follow-ups: view / call back / resolve a concern**
  In staff Follow-ups, render the concern job (prototype openConcern 'View report'); let staff call the client back and resolve it (concernCall → 'Marked as actioned — client called back', job → done). Surface urgency.
