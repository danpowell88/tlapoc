# PRD-07 — Communications, Reminders & Recall

> **▸ Option A alignment (rev 2, 2026-06-19).** The prototype builds the **omnichannel inbox** (IG/FB/SMS/email) with categorisation, **client linking** and **templated/keyword suggested replies** (no AI) — previously a §2 non-goal, now **scoped as Phase 2** under **REQ-NOTIF-6 / ADR-0018/0019**. **🔬 Feasibility:** Meta's **24-h window**, **App Review/Business Verification** and **no cold-DM** mean **marketing DMs are out** — IG/FB/WhatsApp are **reactive/service** channels while **proactive marketing stays on SMS/email**. The **v1 scope here is unchanged** (reminders, aftercare, recall + Spam-Act consent). It also adds a **unified follow-up / job queue** (**REQ-NOTIF-7 / ADR-0023**): scattered recall / needs-attention / unanswered-comms items **merge into one queue**, staff can **flag any message** so it isn't lost, and inbound comms **auto-categorise into jobs** (rules/keyword, no AI). See [requirements §12](../02-requirements.md#12-option-a-prototype-alignment--feasibility-register).
>
> **▸ Option A alignment (rev 4, 2026-06-20).** Expands into **growth surfaces** (the prototype's Growth area), all sharing **Spam-Act consent (C23)**: a **lead/prospect CRM** over the inbox (ADR-0033) and **reviews/reputation** (request-all with **no sentiment gating**, reply-yes, with a staff **caution** against resharing an S4-endorsing review as a prohibited testimonial — ADR-0032), plus a **public booking widget** with generic service names and **S4 prices withheld by configuration** (REQ-NOTIF-8/9/12, REQ-MEMB-10).
>
> **▸ Scope cut (rev 4.2, 2026-06-20).** **All advertising tooling is withdrawn** — the advertising linter, newsletter builder and social scheduler are out of scope; email campaigns, social posting and advertising compliance belong in the clinic's existing tools (Mailchimp, Meta Business Suite) (**ADR-0034 withdrawn**; **REQ-NOTIF-4/10/11 dropped**; C9 reframed as clinic-owned). The public booking page uses generic names + withheld S4 prices **by configuration**, not a linter. **Reviews** still gain **acknowledge / flag / auto-detect follow-up**: negative reviews (≤3★) and complaint matches auto-raise review jobs into the Follow-ups queue (ADR-0032 extended).

> **Phase:** 1 · **Status:** Draft<br>
> **Requirements:** REQ-NOTIF-1…3, 5 (REQ-NOTIF-4 withdrawn) · **Compliance:** C9 (advertising — clinic-owned), C23 (Spam Act)<br>
> **ADRs:** 0012 (integration adapters) · **Depends on:** PRD-01, PRD-02

## 1. Summary
The engine that keeps the book full and clients coming back at the right cadence: reminders,
pre-/after-care sequences, and **recall** (~12-week toxin re-care), delivered over SMS/email/push —
with **Spam Act** consent/unsubscribe baked in. *(Advertising/marketing content is produced in the
clinic's external tools — the platform has no advertising linter; C9 advertising compliance is clinic-owned.)*

## 2. Goals & non-goals
**Goals:** appointment reminders/confirmations; pre-care + aftercare sequences (multi-touch, timed
per treatment); recall/recare + unbooked-rebook prompts; opt-in
marketing consent + functional unsubscribe.

**Non-goals (v1):** full campaign builder/segmentation; referrals; unified inbox/missed-call text-back;
AI message generation (all Phase 2+).

## 3. Users
Client (recipient), front desk/owner (templates, recall worklist), system (scheduled sends).

## 4. User stories
- As a **client**, I get timely **reminders** (confirm/decline) and **aftercare** instructions appropriate to my treatment.
- As a **client**, ~12 weeks after toxin I get a **recall** nudge to rebook; if I had an unbooked recommended session, I'm prompted.
- As **front desk**, I work a **recall/rebook worklist** of clients due.
- As an **owner**, my public **booking page** uses generic service names with S4 prices withheld (by configuration), so it doesn't reference S4 (brands, "anti-wrinkle injections", prices, #botox).
- As a **client**, I only receive marketing if I **opted in**, and every message lets me **unsubscribe**.

## 5. Key flow
```mermaid
flowchart TD
  A[Trigger: booking / visit / interval] --> B{Message type}
  B -- transactional<br/>(reminder/aftercare) --> C[Send per template<br/>(SMS/email/push)]
  B -- marketing/recall --> D{Opt-in consent?}
  D -- no --> E[Suppress]
  D -- yes --> G[Send + unsubscribe footer C23]
  C --> H[Log to comms history]
  G --> H
```

## 6. Functional scope
- **Channels** (REQ-NOTIF-1, ADR-0012): `INotifier` over AU SMS provider + email + app push; per-tenant templates.
- **Reminders & care** (REQ-NOTIF-2): appointment reminders/confirmations; pre-care + aftercare sequences (multi-touch, timed per treatment type).
- **Recall** (REQ-NOTIF-3): recare at treatment interval (toxin ~12 weeks) + unbooked-rebook prompts; recall worklist.
- **Public booking-page naming** (REQ-NOTIF-12, C9): the booking page uses **generic service names** and **withholds S4 prices** by **configuration** (driven by the catalog `schedule` flag, ADR-0014). *(No advertising linter — advertising/marketing is produced in the clinic's external tools and TGA/AHPRA compliance is the clinic's responsibility; ADR-0034 withdrawn, REQ-NOTIF-4 dropped.)*
- **Marketing consent** (REQ-NOTIF-5, C23): opt-in for commercial electronic messages; sender identification; functional unsubscribe; suppression on withdrawal. Transactional messages (reminders/aftercare) are exempt and always send.

## 7. Data & entities
`MessageTemplate`, `NotificationLog`, `Sequence`/`SequenceStep`, `RecallTask`, `MarketingConsent`,
`SuppressionList`. Reuses catalog `schedule` for linting.

## 8. Acceptance criteria
- **AC1 (C23):** A marketing message sends only to opted-in clients and always includes a working unsubscribe; unsubscribing suppresses future marketing immediately.
- **AC2 (C9):** The public booking page renders **generic service names** and **withholds S4 prices** for any service flagged S4 in the catalog (configuration-driven). *(No advertising linter; advertising compliance is clinic-owned.)*
- **AC3 (transactional):** Reminders/aftercare send regardless of marketing opt-in (and have no unsubscribe-gating), but still avoid S4 references.
- **AC4 (recall):** A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- **AC5:** All sends are logged to the client's comms history.

## 9. Dependencies & sequencing
After PRD-01/02. Reward/incentive comms come from PRD-06 and send via the same channels (opt-in only). SMS provider via PRD-10/ADR-0012.

## 10. Out of scope
Campaign builder, segmentation, referrals, unified inbox, AI copy (Phase 2+).

## 11. Open questions
- AU SMS provider choice (MessageMedia / ClickSend / Twilio).
- Aftercare/recall cadence defaults per treatment.
