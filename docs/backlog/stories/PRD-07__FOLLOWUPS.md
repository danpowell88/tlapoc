# Unified follow-up / job queue

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/FOLLOWUPS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a staff member, I want one follow-up queue that merges recalls, needs-attention items and flagged messages, so that nothing falls through the cracks.
Scattered recall / needs-attention / unanswered-comms items merge into one queue; staff can flag any message; inbound comms auto-categorise into jobs (rules/keyword, no AI) (REQ-NOTIF-7, ADR-0023).

## How it works

A Job has a type (recall / callback / reply / review / concern / consent / stock / restock / admin...), an optional linked client / conversation / appointment, an assignee (role or person), a due, a status (open / snoozed / done) and a source (manual / auto / recall / system). Existing signals project into the same queue rather than living in separate UIs: recall due (RECALL), unanswered conversations (INBOX), negative reviews (REVIEWS), no-shows (PRD-02), stock/expiry alerts, client concern reports (PRD-09). Staff can manually flag any message/client -> a Job; inbound comms auto-categorise by rules/keyword (e.g. a 'Complaint' conversation -> a Lead-Nurse callback job; a 'Booking' enquiry -> a Reception reply-&-book job).
The queue is role-scoped ('Mine') and every status change is audited. Actions: open (jumps to the chat/client/report), mark done, snooze, reopen, reassign (cycles the role), callback. A count badge in the nav and a dashboard list keep it visible. Auto-categorisation is a UX aid, not a safety control — jobs are advisory and human-actioned.

## Requirements

- One follow-up queue that merges recalls, needs-attention items and flagged messages.

## Acceptance Criteria

- [ ] Recall, needs-attention and unanswered-comms items merge into a single queue.
- [ ] Any message/client can be flagged so it isn't lost (manual -> Job).
- [ ] Inbound comms auto-categorise into jobs by rules/keyword (no AI).
- [ ] A no-show (PRD-02) and negative reviews (REVIEWS) raise jobs into this queue; the queue is role-scoped and audited.

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Follow-ups — 'One queue for everything that needs a human — recall, replies, consents & stock. Flag a message and it can't get lost'; filter pills Open / Mine / Snoozed / Done; 'Auto-detect from inbox' button; job rows with a type badge, assignee, source (auto-detected / flagged / recall / system), due + client link; actions open chat/client/report, done (checkbox), Snooze, Reassign; a count badge in the nav + dashboard list.

![followups — prototype screen](../screens/followups.png)

## Suggested data model

- **Job** — id, tenant_id, type(recall|callback|reply|review|concern|consent|stock|restock|admin), client_id?, conversation_id?, appointment_id?, source_ref, assignee(role|person), status(open|snoozed|done), source(manual|auto|recall|system), due_at
  - _Merged queue; auto-categorised by rules/keyword (no AI); role-scoped; audited (ADR-0023)._

## Technical notes (high level)

- Architecture decisions: [ADR-0023](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Job model + signal projections (migrations)**
  Model Job (tenant_id + RLS) per ADR-0023: type, optional client/conversation/appointment links, assignee (role|person), status (open|snoozed|done), source (manual|auto|recall|system), due_at.
  - Existing signals project INTO this queue (recall due, unanswered conversation, negative review, no-show, stock/expiry, client concern) rather than separate tables.
  - Role-scoping ('my queue') via the concerns model.
- [ ] **Jobs API: lifecycle, flag, rules/keyword auto-categorise, projections**
  Server-side.
  - Lifecycle endpoints: create/open/done/snooze/reopen/reassign; flag a message/client -> Job.
  - Auto-categorise inbound conversations by rules/keyword (no AI): map category (Complaint -> Lead-Nurse callback; Booking -> Reception reply-&-book; Pricing -> Reception reply) to a Job; idempotent (don't double-create for an already-open conversation job).
  - Project recall (RECALL), reviews (REVIEWS), no-shows (PRD-02), stock/expiry and concerns (PRD-09) into the queue; audit all status changes (ADR-0010).
- [ ] **Follow-ups web UI: filters, job rows, actions, nav badge**
  Angular per the screenshot.
  - Filter pills (Open / Mine / Snoozed / Done) with counts; 'Auto-detect from inbox' action.
  - Job rows: type badge, assignee, source tag, due + client; primary link (open chat / open client / view report) + done checkbox + Snooze / Reassign.
  - Nav count badge + dashboard 'follow-ups' list; role-scoped 'Mine'; loading/empty ('queue clear')/error states.
