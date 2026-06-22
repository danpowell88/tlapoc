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

- [ ] **Automation model over Sequence (migrations)**
  Model Automation (tenant_id + RLS (row-level security)): trigger, treatment_type, sequence_id, kind (transactional|marketing), enabled.
  - A thin wrapper over Sequence (REMINDERS-CARE) — does not duplicate the engine.
  - kind carries through to the consent gate.
- [ ] **Automation toggle/edit API + engine wiring**
  Server-side.
  - Endpoints to list/enable/disable/edit automations per treatment type; toggling enabled gates whether the linked Sequence triggers.
  - Marketing-kind automations gate on consent + suppression (C23); transactional always send.
  - Stats (sent/booked/returned) read from NotificationLog + outcomes.
- [ ] **Automations web UI (cards + toggles)**
  Angular per the screenshot.
  - Automation cards with channel + audience + live stats and an on/off toggle (toggleAuto); per-treatment editing; the 'all respect opt-in & unsubscribe' note.
  - Owner/front-desk gated; loading/empty/error states.
