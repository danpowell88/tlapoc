# Treatment plans: project upcoming sessions as recall jobs

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/TREATMENT-PLANS-RECALL`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/TREATMENT-PLANS`

## Background

As a injector / reception, I want each upcoming plan session to project a recall job at its due date, so that clients are rebooked on cadence without relying on memory.
Plainly: this keeps a client on cadence — each upcoming plan session automatically creates a recall task at its due date, so reception rebooks them at the right time instead of relying on memory. Where it fits: a follow-up to PRD-05/TREATMENT-PLANS that connects plans to the recall worklist in comms (PRD-07). The plan structure already schedules sessions; this story projects them into the shared follow-up queue as recall jobs.

## How it works

This follow-up connects plans to the recall worklist. Each upcoming PlanSession projects a recall Job at its due date (ADR-0023) into the PRD-07 worklist, so reception/comms rebook the client at the right cadence rather than relying on memory.
As sessions are charted (a ChartEntry is finalised against a plan session), the session is marked done and the next becomes the active recall; a skipped or rescheduled session updates its projected job accordingly.
The recall job carries the client, plan and the service due so the rebook lands on the right treatment at the right interval.

## Requirements

- Each upcoming plan session to project a recall job at its due date.

## Acceptance Criteria

- [ ] Each upcoming plan session projects a recall Job at its due date into the shared follow-up worklist (PRD-07).
- [ ] As a session is charted (its ChartEntry is finalised), the session is marked done and the next session becomes the active recall.
- [ ] A skipped or rescheduled session updates its projected recall job accordingly.
- [ ] Recall jobs carry the client, plan and the service due so reception can rebook at the right cadence.

## UI designs / screenshots

- Charting: the close-out's recall toggle (rebook ~12 wks) projects the rebook Job (closeoutGo) aligned to the plan's next session.
- Upcoming plan sessions appear in the PRD-07 recall worklist at their due dates.
- Charting a session advances the plan and the active recall to the next session.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Job (recall, referenced, ADR-0023)** — type=recall, client_id, plan_id, session_id, service_id, due
  - _Extends the basic's PlanSession — no new entity; upcoming sessions project recall Jobs into the PRD-07 worklist._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Recall-job projection from plan sessions**
  Behaviour: each upcoming PlanSession projects a recall Job at its due date (ADR-0023) into the PRD-07 worklist; charting a session marks it done and advances the next to the active recall; a skipped/rescheduled session updates its projected job. Requirements: jobs carry client/plan/session/service-due; emit domain events so the worklist stays in sync.
