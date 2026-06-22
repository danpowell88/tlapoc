# Recall / recare worklist

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/RECALL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a front desk, I want a recall worklist of clients due to rebook and automatic recall nudges at the treatment interval, so that clients return on cadence and the book stays full.
Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall worklist for front desk (REQ-NOTIF-3).

## How it works

A scheduled job creates a RecallTask when a client passes the treatment interval with no future booking (reason: interval), or when a treatment plan has an unbooked recommended session (reason: unbooked_plan). The task carries due_at, status and last_nudge_at. The client receives an automatic recall nudge over the channels (SMS + email per the 'Recall — anti-wrinkle (~12 wks)' automation) with a rebook link — gated on consent for the marketing-style nudge — and the task lands in the front-desk worklist.
Recall tasks merge into the unified Follow-ups queue as 'Recall' jobs (e.g. 'Rebook Olivia Brown — toxin 14 wks overdue · due this week'), so staff work recalls alongside replies, callbacks and stock. Booking the next visit (CHECKOUT-ASSIST / PRD-06 rebooking, PRD-02 calendar) resolves the task. Unbooked recommended sessions prompt a rebook the same way.

## Requirements

- A recall worklist of clients due to rebook and automatic recall nudges at the treatment interval.

## Acceptance Criteria

- [ ] A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- [ ] An unbooked recommended session (treatment plan, PRD-05) prompts a rebook.
- [ ] Front desk can work the recall/rebook worklist (recall tasks appear in the Follow-ups queue).
- [ ] Recall integrates with treatment plans (PRD-05) and rebooking (PRD-06/PRD-02).

## UI designs / screenshots

- Prototype: Follow-ups — recall/rebook worklist of clients due (e.g. 'Rebook Olivia Brown — toxin 14 wks overdue', 'Win-back Mia Chen — lapsed 5 mo'), shown as 'Recall' jobs with assignee + due; automatic recall nudges via the channels.
- Unbooked recommended sessions prompt a rebook.

![followups — prototype screen](../screens/followups.png)

## Suggested data model

- **RecallTask** — id, tenant_id, client_id, due_at, reason(interval|unbooked_plan), status(open|done), last_nudge_at
  - _Generated at the interval by a scheduled job; projects into the Follow-ups queue as a Recall Job._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **RecallTask model + interval/unbooked-plan generation (migrations)**
  Model RecallTask (tenant_id + RLS): client_id, due_at, reason (interval|unbooked_plan), status, last_nudge_at.
  - Configurable interval per treatment type (toxin ~12 wks default).
  - A RecallTask projects into the Job queue (FOLLOWUPS) as a 'recall' Job.
- [ ] **Recall scheduler + nudge + worklist API**
  Server-side.
  - Scheduled job: find toxin clients past the interval with no future booking -> create a RecallTask + recall Job; find treatment plans (PRD-05) with unbooked recommended sessions -> create RecallTask (unbooked_plan).
  - Send the recall nudge via INotifier (marketing-style — consent + suppression gated) with a rebook link; stamp last_nudge_at; avoid re-nudging.
  - Resolve the task when a future booking exists (PRD-02/PRD-06). Worklist query feeds the Follow-ups recall jobs.
