# Campaigns (external-tool handoff) (placeholder)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CAMPAIGNS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a owner, I want campaign capability, so that I can run promotions.

The prototype shows a Comms → Campaigns screen, but advertising/campaign tooling was withdrawn from scope (ADR-0034 withdrawn) — email campaigns and social belong in the clinic's external tools (Mailchimp, Meta Business Suite). Tracked as a placeholder to reconcile prototype vs scope.

## Requirements

- Campaign capability.
- Must satisfy compliance obligation(s): C9, C23.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — advertising/campaign content is produced in external tools, not the platform.
- [ ] The platform exposes consented audience export / segments for those tools where appropriate (C23).
- [ ] If ever built in-app, it must honour TGA/AHPRA advertising rules and the no-public-S4-pricing rule (C9).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0034 (see docs/adr/decision-log.md).

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/CAMPAIGNS.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.
Compliance criteria: C9, C23.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
