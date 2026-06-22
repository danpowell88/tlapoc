# Omnichannel inbox + lead/reviews (placeholder)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/INBOX`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

As a staff member, I want a unified inbox with lead tracking and review management, so that all client conversations live in one place.
The omnichannel inbox (IG/FB/SMS/email), lead/prospect CRM and reviews/reputation are scoped to Phase 2; marketing DMs are out (Meta 24-h window). Placeholder (REQ-NOTIF-6/8/9, ADR-0018/0019/0032/0033).

## How it works

Placeholder (Phase 2): an omnichannel inbox (IG/FB/SMS/email) with categorisation, client linking and templated/keyword suggested replies (no AI). Meta feasibility (App Review, Business Verification, 24-h window, no cold-DM) means marketing DMs are out — IG/FB/WhatsApp are reactive/service channels while proactive marketing stays on SMS/email.
Inbound webhooks + provider Send/Conversations APIs behind an IMessagingChannel port (ADR-0018).

## Requirements

- A unified inbox with lead tracking and review management.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2; IG/FB/WhatsApp are reactive/service channels only (no cold-DM marketing).
- [ ] Reviews acknowledge/flag/auto-detect-follow-up and the lead CRM are captured for later.
- [ ] Meta feasibility (App Review, Business Verification, 24-h window) flagged for validation.

## UI designs / screenshots

- Prototype: Comms -> Inbox (marketing-inbox.png) — conversation list with channel + category, client linking, flag, templated/keyword replies (scanInbox/openConvo/sendMsg/linkConvo/flagConvo).

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Conversation** — id, tenant_id, channel, client_id?, category, status, last_at
  - _Phase 2; reactive channels only._
- **Message** — id, conversation_id, direction, body, at
  - _Inbound via webhooks; flag -> Job._

## Technical notes (high level)

- Architecture decisions: [ADR-0018](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0032](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0033](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1; confirm it still fits scope/regulatory stance, then break down.
