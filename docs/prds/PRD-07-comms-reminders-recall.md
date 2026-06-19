# PRD-07 — Communications, Reminders & Recall

> **▸ Option A alignment (rev 2, 2026-06-19).** The prototype builds the **omnichannel inbox** (IG/FB/SMS/email) with categorisation, **client linking**, **templated/keyword suggested replies** (no AI) and the advertising linter — previously a §2 non-goal, now **scoped as Phase 2** under **REQ-NOTIF-6 / ADR-0018/0019**. **🔬 Feasibility:** Meta's **24-h window**, **App Review/Business Verification** and **no cold-DM** mean **marketing DMs are out** — IG/FB/WhatsApp are **reactive/service** channels while **proactive marketing stays on SMS/email**. The **v1 scope here is unchanged** (reminders, aftercare, recall + linter + Spam-Act consent). See [requirements §12](../02-requirements.md#12-option-a-prototype-alignment--feasibility-register).

> **Phase:** 1 · **Status:** Draft
> **Requirements:** REQ-NOTIF-1…5 · **Compliance:** C9 (advertising), C23 (Spam Act)
> **ADRs:** 0012 (integration adapters) · **Depends on:** PRD-01, PRD-02

## 1. Summary
The engine that keeps the book full and clients coming back at the right cadence: reminders,
pre-/after-care sequences, and **recall** (~12-week toxin re-care), delivered over SMS/email/push —
with built-in **advertising compliance** (no S4 references in public/marketing content) and
**Spam Act** consent/unsubscribe baked in.

## 2. Goals & non-goals
**Goals:** appointment reminders/confirmations; pre-care + aftercare sequences (multi-touch, timed
per treatment); recall/recare + unbooked-rebook prompts; an **advertising-compliance linter**; opt-in
marketing consent + functional unsubscribe.
**Non-goals (v1):** full campaign builder/segmentation; referrals; unified inbox/missed-call text-back;
AI message generation (all Phase 2+).

## 3. Users
Client (recipient), front desk/owner (templates, recall worklist), system (scheduled sends).

## 4. User stories
- As a **client**, I get timely **reminders** (confirm/decline) and **aftercare** instructions appropriate to my treatment.
- As a **client**, ~12 weeks after toxin I get a **recall** nudge to rebook; if I had an unbooked recommended session, I'm prompted.
- As **front desk**, I work a **recall/rebook worklist** of clients due.
- As an **owner**, any outbound public/marketing content is **linted** so it can't reference S4 (brands, "anti-wrinkle injections", prices, #botox, promotional imagery).
- As a **client**, I only receive marketing if I **opted in**, and every message lets me **unsubscribe**.

## 5. Key flow
```mermaid
flowchart TD
  A[Trigger: booking / visit / interval] --> B{Message type}
  B -- transactional\n(reminder/aftercare) --> C[Send per template\n(SMS/email/push)]
  B -- marketing/recall --> D{Opt-in consent?}
  D -- no --> E[Suppress]
  D -- yes --> F[Advertising linter\n(block S4 refs C9)]
  F --> G[Send + unsubscribe footer C23]
  C --> H[Log to comms history]
  G --> H
```

## 6. Functional scope
- **Channels** (REQ-NOTIF-1, ADR-0012): `INotifier` over AU SMS provider + email + app push; per-tenant templates.
- **Reminders & care** (REQ-NOTIF-2): appointment reminders/confirmations; pre-care + aftercare sequences (multi-touch, timed per treatment type).
- **Recall** (REQ-NOTIF-3): recare at treatment interval (toxin ~12 weeks) + unbooked-rebook prompts; recall worklist.
- **Advertising linter** (REQ-NOTIF-4, C9): scans campaign + public booking-page content; blocks direct/indirect S4 references (brands, nicknames, generic "anti-wrinkle"/"dermal filler" terms, price promotions, banned hashtags, promotional S4 imagery); inserts mandatory warnings where permitted. Uses the catalog `schedule` flag (ADR-0014).
- **Marketing consent** (REQ-NOTIF-5, C23): opt-in for commercial electronic messages; sender identification; functional unsubscribe; suppression on withdrawal. Transactional messages (reminders/aftercare) are exempt and always send.

## 7. Data & entities
`MessageTemplate`, `NotificationLog`, `Sequence`/`SequenceStep`, `RecallTask`, `MarketingConsent`,
`SuppressionList`. Reuses catalog `schedule` for linting.

## 8. Acceptance criteria
- **AC1 (C23):** A marketing message sends only to opted-in clients and always includes a working unsubscribe; unsubscribing suppresses future marketing immediately.
- **AC2 (C9):** Content containing an S4 brand, banned term, price promotion, banned hashtag or promotional S4 image is **blocked** by the linter with the offending element identified.
- **AC3 (transactional):** Reminders/aftercare send regardless of marketing opt-in (and have no unsubscribe-gating), but still avoid S4 references.
- **AC4 (recall):** A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- **AC5:** All sends are logged to the client's comms history.

## 9. Dependencies & sequencing
After PRD-01/02. Reward/incentive comms come from PRD-06 but flow through this linter. SMS provider via PRD-10/ADR-0012.

## 10. Out of scope
Campaign builder, segmentation, referrals, unified inbox, AI copy (Phase 2+).

## 11. Open questions
- AU SMS provider choice (MessageMedia / ClickSend / Twilio).
- Aftercare/recall cadence defaults per treatment.
