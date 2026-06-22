# Unified follow-up / job queue — projected signals + lifecycle (core)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/FOLLOWUPS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a staff member, I want one follow-up queue that merges recalls, needs-attention items and unanswered comms, so that nothing falls through the cracks.
Follow-ups used to scatter: a recall worklist here, a dashboard 'needs attention' there, unanswered inbox messages somewhere else — and anything no one replied to could quietly fall through the cracks. This story makes one queue: recall, needs-attention and unanswered-comms items all merge into a single 'what needs doing' list. This is the minimal end-to-end core — the unified Job model, existing signals projecting into it, the lifecycle actions and the queue UI; manual flagging and rules/keyword auto-categorisation are each added as their own follow-ups. It is the single cross-clinic to-do list (ADR-0023). (REQ-NOTIF-7, ADR-0023).

## How it works

A Job has a type (recall / callback / reply / review / concern / consent / stock / restock / admin...), an optional linked client / conversation / appointment, an assignee (role or person), a due, a status (open / snoozed / done) and a source (manual / auto / recall / system). Existing signals project into the same queue rather than living in separate UIs: recall due (RECALL), unanswered conversations (INBOX), negative reviews (REVIEWS), no-shows (PRD-02), stock/expiry alerts, client concern reports (PRD-09). Staff can manually flag any message/client -> a Job; inbound comms auto-categorise by rules/keyword (e.g. a 'Complaint' conversation -> a Lead-Nurse callback job; a 'Booking' enquiry -> a Reception reply-&-book job).
The queue is role-scoped ('Mine') and every status change is audited. Actions: open (jumps to the chat/client/report), mark done, snooze, reopen, reassign (cycles the role), callback. A count badge in the nav and a dashboard list keep it visible. Auto-categorisation is a UX aid, not a safety control — jobs are advisory and human-actioned.

## Requirements

- One follow-up queue that merges recalls, needs-attention items and unanswered comms.

## Acceptance Criteria

- [ ] Recall, needs-attention and unanswered-comms items merge into a single queue (existing signals project in as Jobs, not duplicate tables).
- [ ] Each job supports the lifecycle actions (open / done / snooze / reopen / reassign / callback); every status change is audited.
- [ ] A no-show (PRD-02) and negative reviews (REVIEWS) raise jobs into this queue; the queue is role-scoped ('Mine').
- [ ] Manual flagging and rules/keyword auto-categorisation are added by follow-ups.

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

- [ ] **Unified Job model + signal projections**
  Behaviour: one Job entity backs the whole queue — type (recall|callback|reply|review|concern|consent|stock|restock|admin), optional client/conversation/appointment links, assignee (role|person), status (open|snoozed|done), source (manual|auto|recall|system), due_at. Existing signals project INTO this one queue rather than living in separate UIs: recall due (RECALL), unanswered conversations (INBOX), negative reviews (REVIEWS), no-shows (PRD-02), stock/expiry alerts, client concern reports (PRD-09). Requirements: tenant-scoped with RLS (row-level security); projections don't create duplicate tables — they surface as Jobs; per ADR-0023.
- [ ] **Job lifecycle actions (open / done / snooze / reopen / reassign / callback)**
  Behaviour: each job supports open (jumps to the chat/client/report), mark done, snooze, reopen, reassign (cycles the role) and callback; every status change is audited. Requirements: actions are server-authoritative; reassign cycles through the role set; snooze hides until a due time; all transitions write an AuditEvent (ADR-0010); the queue is role-scoped so 'Mine' shows only the current user's/role's jobs.
- [ ] **Follow-ups web UI (filters, job rows, actions, nav badge)**
  Behaviour: the Follow-ups screen shows filter pills (Open / Mine / Snoozed / Done) with counts; each job row has a type badge, assignee, source tag (recall / system), due + client link, a primary action (open chat / open client / view report), a done checkbox and Snooze / Reassign. A count badge in the nav and a dashboard 'follow-ups' list keep it visible. Requirements: role-scoped 'Mine'; loading/empty ('queue clear')/error states; the nav badge reflects the open count live. (The 'Auto-detect from inbox' action ships with the auto-categorisation follow-up.)
