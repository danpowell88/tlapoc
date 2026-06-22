# Omnichannel inbox + lead/reviews (placeholder)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/INBOX`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

As a staff member, I want a unified inbox with lead tracking and review management, so that all client conversations live in one place.
The omnichannel inbox (IG/FB/SMS/email), lead/prospect CRM and reviews/reputation are scoped to Phase 2; marketing DMs are out (Meta 24-h window). Placeholder (REQ-NOTIF-6/8/9, ADR-0018/0019/0032/0033).

## How it works

Placeholder (Phase 2). An omnichannel inbox (IG/FB/SMS/email) with category tagging, client linking and templated/keyword suggested replies (no AI). Inbound arrives via provider webhooks and replies go out via the providers' Send/Conversations APIs behind an IMessagingChannel port (ADR-0018). A flagged or complaint conversation raises a Job into Follow-ups; a lead conversation feeds the Lead CRM.
Feasibility to validate before build: Meta App Review + Business Verification, the 24-hour customer-service window, and the no-cold-DM rule — which is why marketing DMs are out of scope and these stay reactive/service channels. The data model is captured so the unified queue and lead CRM stay inbox-ready.

## Requirements

- A unified inbox with lead tracking and review management.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2; IG/FB/WhatsApp are reactive/service channels only (no cold-DM marketing).
- [ ] Inbox categorisation, client linking and templated/keyword suggested replies (no AI) captured; flag -> Job, lead -> CRM.
- [ ] Meta feasibility (App Review, Business Verification, 24-h window) flagged for validation before build.

## UI designs / screenshots

- Prototype: Comms -> Inbox — conversation list with channel + category, client linking, flag, templated/keyword replies (scanInbox / openConvo / sendMsg / linkConvo / flagConvo).

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Conversation** — id, tenant_id, channel(ig|fb|sms|email), client_id?, category, status, last_at
  - _Phase 2; reactive channels only (Meta 24-h window)._
- **Message** — id, conversation_id, direction(in|out), body, at
  - _Inbound via webhooks; flag -> Job (Follow-ups)._

## Technical notes (high level)

- Architecture decisions: [ADR-0018](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0032](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0033](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1. When pulled in: validate Meta feasibility first (App Review, Business Verification, 24-h messaging window, no cold-DM) — these constrain IG/FB/WhatsApp to reactive/service channels; proactive marketing stays on SMS/email. Then design IMessagingChannel (ADR-0018) with inbound webhooks + provider Send/Conversations APIs, the rules/keyword categoriser (no AI), client linking, flag -> Job (Follow-ups) and the Lead-CRM projection. Break down accordingly.
