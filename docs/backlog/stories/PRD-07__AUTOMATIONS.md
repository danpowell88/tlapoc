# Automation builder (triggers → timed messages)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

As a owner / front desk, I want to configure automations that send the right message at the right time per trigger, so that reminders, aftercare and recall run hands-off.
Reminders, aftercare and recall shouldn't need a human to remember them. The Automations screen is the management UI over the sequence engine: each automation maps a trigger (booking, visit, interval) to a timed sequence of messages, and can be switched on/off and tuned per treatment type — so the right message goes out at the right time, hands-off. It drives the same engine as REMINDERS-CARE and RECALL.  The prototype's Comms → Automations screen (toggleAuto) configures the reminder/aftercare/recall sequences as toggleable automations. This is the management UI over PRD-07's sequence engine.

## How it works

An Automation is a thin, toggleable wrapper over a Sequence: trigger + treatment_type + sequence_id + enabled. The screen lists the clinic's automations as cards (Recall — anti-wrinkle ~12 wks, Aftercare sequence, Win-back lapsed 90d, Birthday offer, No-show follow-up, Review request) each showing its channel, audience and live stats ('42 sent · 18 booked'), with an on/off toggle and per-treatment editing.
The compliance split is explicit and shown on-screen — 'Flows run automatically on the right trigger. All respect opt-in & unsubscribe (Spam Act).' Marketing automations (recall nudge, win-back, birthday, review request) gate on consent + suppression (C23); transactional ones (reminders, aftercare) always send. Toggling an automation off stops the underlying sequence from triggering. This is UI + orchestration only — it doesn't reimplement the engine, it configures REMINDERS-CARE / RECALL.

## Requirements

- To configure automations that send the right message at the right time per trigger.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Automations map a trigger (booking, visit, interval) to a timed sequence of messages.
- [ ] Each automation can be enabled/disabled and edited per treatment type.
- [ ] Marketing automations respect opt-in/unsubscribe (C23); transactional ones always send.
- [ ] Automations drive the same sequence engine as REMINDERS-CARE and RECALL.

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Comms -> Automations — 'Flows run automatically on the right trigger. All respect opt-in & unsubscribe (Spam Act)'; automation cards (Recall ~12 wks, Aftercare, Win-back lapsed 90d, Birthday offer, No-show follow-up, Review request) with channel + audience + live stats + an on/off toggle (toggleAuto), per-treatment editing; Review request shown off by default.

![marketing-auto — prototype screen](../screens/marketing-auto.png)

## Suggested data model

- **Automation** — id, tenant_id, trigger(booking|visit|interval), treatment_type, sequence_id, kind(transactional|marketing), enabled(bool)
  - _UI over Sequence; marketing kind respects consent (C23)._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Automation model over Sequence + on/off toggle**
  Behaviour: an Automation is a thin, toggleable wrapper over a Sequence — trigger (booking|visit|interval) + treatment_type + sequence_id + kind (transactional|marketing) + enabled. Toggling an automation off stops the underlying Sequence from triggering; toggling on resumes it. Requirements: tenant-scoped with RLS (row-level security); does NOT duplicate the sequence engine (REMINDERS-CARE/RECALL) — it configures it; kind carries through to the consent gate.
- [ ] **Per-treatment-type editing of automations**
  Behaviour: each automation can be edited per treatment type so a filler client and a skin client get the right cadence/content (e.g. Recall — anti-wrinkle ~12 wks vs a different interval for filler). Requirements: editing changes the linked Sequence's steps/offsets/templates; changes are owner/front-desk gated; the default set matches the prototype cards (Recall, Aftercare, Win-back, Birthday, No-show follow-up, Review request).
- [ ] **Transactional vs marketing consent split (C23)**
  Behaviour: the screen states 'Flows run automatically on the right trigger. All respect opt-in & unsubscribe (Spam Act).' Marketing automations (recall nudge, win-back, birthday, review request) gate on marketing consent + suppression; transactional ones (reminders, aftercare) always send. Requirements: the kind flag drives the gate via MARKETING-CONSENT; a marketing automation never sends to a non-consented/suppressed contact; content never names/prices S4 (Schedule 4 prescription-only medicine) (C9). Review request is off by default.
- [ ] **Automation live stats (sent / booked / returned)**
  Behaviour: each automation card shows live stats — e.g. 'Recall 42 sent · 18 booked', 'Aftercare 96 sent (30d)', 'Win-back 128 sent · 11 returned', 'No-show 9 sent · 5 rebooked'. Requirements: stats read from NotificationLog (sends) joined to outcomes (bookings/returns) over a rolling window; computed server-side, not hand-entered.
- [ ] **Automations web UI (cards + toggles)**
  Behaviour: the Automations screen renders automation cards with channel + audience + live stats and an on/off toggle (toggleAuto), plus per-treatment editing and the 'all respect opt-in & unsubscribe (Spam Act)' note. Requirements: owner/front-desk gated; Review request shown off by default; loading/empty/error states.
