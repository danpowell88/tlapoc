# Adverse event: follow-up jobs & route to Governance

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/ADVERSE-EVENT-JOBS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

As a injector / lead nurse, I want logging an adverse event to raise the right follow-up jobs and appear on the governance worklist, so that review, mandatory-report checks and client follow-up happen and nothing is dropped.
Plainly: when an adverse event is logged, this makes sure the right follow-up tasks are created and the case shows up on the governance worklist — so nothing is dropped after the event is recorded. Where it fits: a follow-up to PRD-05/ADVERSE-EVENT that adds the work-routing layer on top of capture + DAEN routing. The captured AE record is the source; this story projects the jobs and surfaces the case in Governance, while the full prefilled DAEN submission stays in PRD-08/DAEN.

## How it works

This follow-up adds the work-routing layer on top of the basic's capture + DAEN routing. On AE creation, the system projects the right Jobs (complication follow-up / review, mandatory-report check, client follow-up) into the shared worklist (ADR-0023) so the follow-through is tracked, not remembered.
The AE also surfaces in Governance → Adverse events & DAEN with its seriousness + DAEN (Database of Adverse Event Notifications) target already set, ready for the full submission. Whether the AE was raised directly at the finalise close-out or from a completed complication-response flow (PRD-05/COMPLICATION-LIBRARY), the same jobs are raised.
The full prefilled DAEN submission/export lives in the Governance hub (PRD-08/DAEN); this story just routes the record and the work.

## Requirements

- Logging an adverse event to raise the right follow-up jobs and appear on the governance worklist.

## Acceptance Criteria

- [ ] On AE creation, the right follow-up Jobs are projected into the shared queue: complication follow-up / review, mandatory-report check, and client follow-up.
- [ ] The AE surfaces in Governance → Adverse events & DAEN with its seriousness + DAEN target set.
- [ ] An AE raised from a completed complication-response flow raises the same jobs as one raised at finalise close-out.
- [ ] The full prefilled DAEN submission stays in PRD-08/DAEN; this story routes the record and the work only.

## UI designs / screenshots

- On AE creation, confirm the raised jobs and the route to Governance → Adverse events & DAEN (gov-ae).
- The governance worklist shows the AE with seriousness + DAEN target set.
- Jobs appear in the shared follow-up queue.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Job (referenced, ADR-0023)** — type=ae, linked client/chart, assignee, due, status
  - _Extends the basic's AdverseEvent — no new entity; AE creation projects follow-up jobs (review / mandatory-report check / client follow-up) and surfaces the case in Governance._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Raise follow-up jobs + route to Governance**
  On AE creation, project the right Jobs (complication follow-up/review, mandatory-report check, client follow-up) into the shared queue (ADR-0023) and surface the AE in Governance → Adverse events & DAEN with seriousness + DAEN target set. Keep the full prefilled DAEN submission in PRD-08/DAEN — this task just routes the record and the work.
