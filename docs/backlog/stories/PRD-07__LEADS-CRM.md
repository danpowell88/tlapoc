# Lead / prospect CRM

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/LEADS-CRM`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a front desk / owner, I want to track leads/prospects through to booking, so that enquiries don't get lost and convert better.

The prototype's Growth → Leads (CRM) screen tracks enquiries who haven't booked yet, over the inbox (ADR-0033).

## Requirements

- To track leads/prospects through to booking.
- Traces to requirement(s): REQ-NOTIF-8.
- Must satisfy compliance obligation(s): C23.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Leads are captured with source, status and next action.
- [ ] A lead can convert to a client/booking, preserving history.
- [ ] Lead follow-ups surface in the Follow-ups queue.
- [ ] Marketing to leads respects Spam-Act consent (C23).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0033 (see docs/adr/decision-log.md).
Depends on: PRD-07/FOLLOWUPS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/LEADS-CRM.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.
Compliance criteria: C23.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
