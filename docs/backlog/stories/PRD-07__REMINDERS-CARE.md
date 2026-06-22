# Reminders, confirmations & care sequences

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REMINDERS-CARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a client, I want timely reminders I can confirm/decline and pre-/after-care instructions for my treatment, so that I'm prepared and cared for around my visit.
Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type) (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

## How it works

A Sequence is a multi-touch flow bound to a trigger (booking or visit) and a treatment_type, with ordered steps {offset, channel, template_key}. A SequenceRun tracks one client's progress through a sequence for a given appointment, recording per-step status. Reminders/confirmations send per template (via INotifier); a confirm/decline action updates the appointment (PRD-02) and a reschedule link routes back into booking.
Pre-care (e.g. avoid blood thinners before toxin) and aftercare (day-0 + day-3 care tips) are sequences keyed by treatment type, so a filler client and a skin-needling client get the right cadence and content. Because reminders and aftercare are transactional (Spam Act exempt), they send regardless of marketing opt-in and have no unsubscribe-gating — but they still must not name or price S4 items (C9). Recall/marketing sequences (RECALL, win-back, birthday) are the consented path. All sends log to the comms history.

## Requirements

- Timely reminders I can confirm/decline and pre-/after-care instructions for my treatment.

## Acceptance Criteria

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment and a reschedule link routes to booking (PRD-02).
- [ ] Pre-care and aftercare sequences are multi-touch and timed per treatment type.
- [ ] Transactional messages send regardless of marketing opt-in (no unsubscribe-gating) and avoid S4 references.
- [ ] All sends are logged to the comms history.

## UI designs / screenshots

- Prototype: Comms -> Automations configures the reminder/aftercare sequences (e.g. 'Aftercare sequence — Day 0 + day 3 care tips after each visit · SMS · Post-treatment'); sends appear in the client's comms history.
- Reminder messages include confirm/decline + reschedule links (PRD-02 REMINDERS).

![marketing-auto — prototype screen](../screens/marketing-auto.png)

## Suggested data model

- **Sequence** — id, tenant_id, trigger(booking|visit), treatment_type, kind(transactional|marketing), steps[]{offset, channel, template_key}
  - _Multi-touch, timed per treatment._
- **SequenceRun** — id, sequence_id, client_id, appointment_id, step_status[]{step, status, sent_at}
  - _Transactional runs are opt-in exempt; per-step status tracked._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Sequence/SequenceRun model (migrations)**
  Model Sequence + SequenceRun (tenant_id + RLS).
  - Sequence: trigger (booking|visit), treatment_type, kind (transactional|marketing), ordered steps {offset, channel, template_key}.
  - SequenceRun: one per client+appointment with per-step status + sent_at.
  - kind distinguishes the opt-in-exempt transactional path from the consented marketing path.
- [ ] **Sequence engine: trigger -> timed steps, confirm/decline, transactional/consent split**
  Server-side engine (shared with RECALL + AUTOMATIONS).
  - On a trigger (booking made / visit completed), start a SequenceRun and schedule steps at their offsets; dispatch each via INotifier at its time.
  - Reminder confirm/decline updates the Appointment (PRD-02); reschedule link routes to booking.
  - Transactional sequences send regardless of marketing consent; marketing sequences gate on consent + suppression (MARKETING-CONSENT). Either way, content must not name/price S4 (C9).
  - Endpoints to define sequences + query runs; log every send.
