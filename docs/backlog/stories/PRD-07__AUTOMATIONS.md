# Automation builder — toggleable automations + consent split (core)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

As a owner / front desk, I want to switch automations on/off, with marketing ones respecting consent, so that reminders, aftercare and recall run hands-off and compliantly.
Reminders, aftercare and recall shouldn't need a human to remember them. The Automations screen is the management UI over the sequence engine: each automation maps a trigger (booking, visit, interval) to a timed sequence of messages and can be switched on/off. This is the minimal end-to-end core — the toggleable Automation wrapper, the transactional-vs-marketing consent split (C23) and a basic cards UI; per-treatment-type editing and live stats are each added as their own follow-ups. It drives the same engine as REMINDERS-CARE and RECALL (this is UI + orchestration, not a re-implemented engine). (REQ-NOTIF-2/3, C23).

## How it works

An Automation is a thin, toggleable wrapper over a Sequence: trigger + treatment_type + sequence_id + enabled. The screen lists the clinic's automations as cards (Recall — anti-wrinkle ~12 wks, Aftercare sequence, Win-back lapsed 90d, Birthday offer, No-show follow-up, Review request) each showing its channel, audience and live stats ('42 sent · 18 booked'), with an on/off toggle and per-treatment editing.
The compliance split is explicit and shown on-screen — 'Flows run automatically on the right trigger. All respect opt-in & unsubscribe (Spam Act).' Marketing automations (recall nudge, win-back, birthday, review request) gate on consent + suppression (C23); transactional ones (reminders, aftercare) always send. Toggling an automation off stops the underlying sequence from triggering. This is UI + orchestration only — it doesn't reimplement the engine, it configures REMINDERS-CARE / RECALL.

## Requirements

- To switch automations on/off, with marketing ones respecting consent.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Automations map a trigger (booking, visit, interval) to a timed sequence and can be enabled/disabled (toggling off stops the underlying Sequence from triggering).
- [ ] Marketing automations respect opt-in/unsubscribe (C23); transactional ones always send; content never names/prices S4 (C9).
- [ ] Automations drive the same sequence engine as REMINDERS-CARE and RECALL (no re-implemented engine).
- [ ] Per-treatment-type editing and live stats are added by follow-ups.

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
- [ ] **Transactional vs marketing consent split (C23)**
  Behaviour: the screen states 'Flows run automatically on the right trigger. All respect opt-in & unsubscribe (Spam Act).' Marketing automations (recall nudge, win-back, birthday, review request) gate on marketing consent + suppression; transactional ones (reminders, aftercare) always send. Requirements: the kind flag drives the gate via MARKETING-CONSENT; a marketing automation never sends to a non-consented/suppressed contact; content never names/prices S4 (Schedule 4 prescription-only medicine) (C9). Review request is off by default.
- [ ] **Automations web UI (cards + toggles)**
  Behaviour: the Automations screen renders automation cards with channel + audience and an on/off toggle (toggleAuto), plus the 'all respect opt-in & unsubscribe (Spam Act)' note. Requirements: owner/front-desk gated; Review request shown off by default; loading/empty/error states. (Per-treatment editing and live stats ship with their follow-ups.)
