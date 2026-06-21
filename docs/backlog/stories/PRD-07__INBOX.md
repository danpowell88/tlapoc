# Omnichannel inbox + lead/reviews (placeholder)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/INBOX`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a staff member, I want a unified inbox with lead tracking and review management, so that all client conversations live in one place.

The omnichannel inbox (IG/FB/SMS/email), lead/prospect CRM and reviews/reputation are scoped to Phase 2; marketing DMs are out (Meta 24-h window). Placeholder (REQ-NOTIF-6/8/9, ADR-0018/0019/0032/0033).

## Requirements

- A unified inbox with lead tracking and review management.
- Traces to requirement(s): REQ-NOTIF-6, REQ-NOTIF-8, REQ-NOTIF-9.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2; IG/FB/WhatsApp are reactive/service channels only (no cold-DM marketing).
- [ ] Reviews acknowledge/flag/auto-detect-follow-up and the lead CRM are captured for later.
- [ ] Meta feasibility (App Review, Business Verification, 24-h window) flagged for validation.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0018, ADR-0032, ADR-0033 (see docs/adr/decision-log.md).

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/INBOX.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
