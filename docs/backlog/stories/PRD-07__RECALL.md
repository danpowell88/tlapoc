# Recall / recare worklist

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/RECALL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a front desk, I want a recall worklist of clients due to rebook and automatic recall nudges at the treatment interval, so that clients return on cadence and the book stays full.
Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall worklist for front desk (REQ-NOTIF-3).

## How it works

Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall/rebook worklist for front desk. A toxin client with no future booking enters the worklist at the configured interval and receives the nudge.
Integrates with treatment plans (PRD-05) and rebooking (PRD-06); keeps the book full and clients on cadence.

## Requirements

- A recall worklist of clients due to rebook and automatic recall nudges at the treatment interval.

## Acceptance Criteria

- [ ] A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- [ ] Unbooked recommended sessions prompt a rebook.
- [ ] Front desk can work the recall/rebook worklist.
- [ ] Recall integrates with treatment plans (PRD-05) and rebooking (PRD-06).

## UI designs / screenshots

- Prototype: Follow-ups (followups.png) includes the recall/rebook worklist of clients due; automatic recall nudges via the channels.
- Unbooked recommended sessions prompt a rebook.

![followups — prototype screen](../screens/followups.png)

## Suggested data model

- **RecallTask** — id, tenant_id, client_id, due_at, reason(interval|unbooked_plan), status, last_nudge_at
  - _Generated at interval by a scheduled job; works the worklist._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - RecallTask — id, tenant_id, client_id, due_at, reason(interval|unbooked_plan), status, last_nudge_at (Generated at interval by a scheduled job; works the worklist.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
  - Rule: Unbooked recommended sessions prompt a rebook.
  - Rule: Front desk can work the recall/rebook worklist.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-07/CHANNELS.
