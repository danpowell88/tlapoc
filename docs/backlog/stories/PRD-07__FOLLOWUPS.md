# Unified follow-up / job queue

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/FOLLOWUPS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a staff member, I want one follow-up queue that merges recalls, needs-attention items and flagged messages, so that nothing falls through the cracks.

Scattered recall / needs-attention / unanswered-comms items merge into one queue; staff can flag any message; inbound comms auto-categorise into jobs (rules/keyword, no AI) (REQ-NOTIF-7, ADR-0023).

## Requirements

- One follow-up queue that merges recalls, needs-attention items and flagged messages.
- Traces to requirement(s): REQ-NOTIF-7.

## Acceptance Criteria

- [ ] Recall, needs-attention and unanswered-comms items merge into a single queue.
- [ ] Any message can be flagged so it isn't lost.
- [ ] Inbound comms auto-categorise into jobs by rules/keyword (no AI).
- [ ] A no-show (PRD-02) and negative reviews raise jobs into this queue.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0023 (see docs/adr/decision-log.md).
Depends on: PRD-07/CHANNELS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/FOLLOWUPS.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
