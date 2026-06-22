# Follow-ups: manual flag → Job

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/FOLLOWUPS-FLAG`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a staff member, I want to flag any message or client so it becomes a follow-up Job, so that anything that needs a human can't get lost.
Plainly: let staff flag any message or client so it becomes a Job in the queue and can't get lost. Where it fits: a follow-up to the unified queue core (PRD-07/FOLLOWUPS), which merges projected signals; this adds the manual capture path so a human can put anything into the queue. Flagging is available from the inbox and the client record and is idempotent. The queue stays role-scoped and audited.

## How it works

Staff can flag any message or client and it becomes a Job in the unified queue (PRD-07/FOLLOWUPS) so it can't get lost ('Flag a message and it can't get lost'). A manual flag sets source=manual and an appropriate type/assignee.
Flagging is available from the inbox and the client record; it is idempotent — re-flagging an already-open item doesn't duplicate. This extends the unified queue core (PRD-07/FOLLOWUPS); the queue stays role-scoped and audited.

## Requirements

- To flag any message or client so it becomes a follow-up Job.

## Acceptance Criteria

- [ ] Staff can flag any message or client and it becomes a Job ('Flag a message and it can't get lost').
- [ ] A manual flag sets source=manual with an appropriate type/assignee.
- [ ] Flagging is available from the inbox and the client record.
- [ ] Flagging is idempotent — re-flagging an already-open item doesn't duplicate.

## UI designs / screenshots

- Prototype: Follow-ups / inbox / client record — a 'Flag' action that raises a Job with a 'flagged' source tag.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Job (extends PRD-07/FOLLOWUPS)** — source=manual; raised from a message/client
  - _No new entity; manual flag path; idempotent._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Manual flag -> Job (from inbox + client record, idempotent)**
  Behaviour: flagging a message/client raises a Job (source=manual) with an appropriate type/assignee. Requirements: available from the inbox and the client record; idempotent (re-flagging an already-open item doesn't duplicate); role-scoped + audited.
