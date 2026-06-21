# Reviews & reputation (request, acknowledge, flag, auto-follow-up)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REVIEWS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a owner, I want to request reviews and manage replies, with negative ones auto-raising follow-ups, so that reputation is managed and problems are caught early.

The prototype's Growth → Reviews screen (scanReviews/reviewReply/reviewFlag/reviewAck) requests reviews, replies/acknowledges, and auto-raises follow-up jobs for negative reviews (≤3★) — with a staff caution against resharing an S4-endorsing review as a prohibited testimonial.

## Requirements

- To request reviews and manage replies, with negative ones auto-raising follow-ups.
- Traces to requirement(s): REQ-NOTIF-9.
- Must satisfy compliance obligation(s): C9, C23.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Review requests sent to consented clients; replies/acknowledge supported.
- [ ] Negative reviews (≤3★) and complaint matches auto-raise review jobs into the Follow-ups queue.
- [ ] A caution warns against resharing an S4-endorsing review as a testimonial (C9).
- [ ] No sentiment-gating of who is asked (request-all).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0032 (see docs/adr/decision-log.md).
Depends on: PRD-07/FOLLOWUPS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/REVIEWS.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.
Compliance criteria: C9, C23.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
