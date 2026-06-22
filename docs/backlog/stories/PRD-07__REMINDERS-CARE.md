# Appointment reminders & confirmations — basic sequence (core)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REMINDERS-CARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a client, I want timely reminders I can confirm or decline, so that I remember my visit and the book stays accurate.
This is the minimal end-to-end core: appointment reminders/confirmations a client can confirm or decline, sent per template over the sequence engine. The pre-care and aftercare instruction sequences are each added as their own follow-ups. A reminder a client can confirm or decline keeps the book accurate. These are transactional messages — exempt from marketing opt-in, but they still avoid S4 references. Appointment reminders/confirmations on the sequence engine (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

## How it works

A Sequence is a multi-touch flow bound to a trigger (booking or visit) and a treatment_type, with ordered steps {offset, channel, template_key}. A SequenceRun tracks one client's progress through a sequence for a given appointment, recording per-step status. This basic slice ships the reminder/confirmation flow on that engine: reminders/confirmations send per template (via INotifier); a confirm/decline action updates the appointment (PRD-02) and a reschedule link routes back into booking.
Because reminders are transactional (Spam Act exempt), they send regardless of marketing opt-in and have no unsubscribe-gating — but they still must not name or price S4 (Schedule 4 prescription-only medicine) items (C9). Pre-care and aftercare instruction sequences are added as follow-ups on this same engine; recall/marketing sequences (RECALL, win-back, birthday) are the consented path. All sends log to the comms history.

## Requirements

- Timely reminders I can confirm or decline.

## Acceptance Criteria

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment and a reschedule link routes to booking (PRD-02).
- [ ] The Sequence/SequenceRun model backs multi-touch flows; this basic slice ships the reminder/confirmation flow on it.
- [ ] Transactional messages send regardless of marketing opt-in (no unsubscribe-gating) and avoid S4 references.
- [ ] All sends are logged to the comms history.

## UI designs / screenshots

- Prototype: Comms -> Automations configures the reminder sequence; reminder messages include confirm/decline + reschedule links (PRD-02 REMINDERS); sends appear in the client's comms history.

![marketing-auto — prototype screen](../screens/marketing-auto.png)

## Suggested data model

- **Sequence** — id, tenant_id, trigger(booking|visit), treatment_type, kind(transactional|marketing), steps[]{offset, channel, template_key}
  - _Multi-touch, timed per treatment; consumed by the pre-care/aftercare follow-ups too._
- **SequenceRun** — id, sequence_id, client_id, appointment_id, step_status[]{step, status, sent_at}
  - _Transactional runs are opt-in exempt; per-step status tracked._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Sequence/SequenceRun model (migrations)**
  Model Sequence + SequenceRun (tenant_id + RLS (row-level security)).
  - Sequence: trigger (booking|visit), treatment_type, kind (transactional|marketing), ordered steps {offset, channel, template_key}.
  - SequenceRun: one per client+appointment with per-step status + sent_at.
  - kind distinguishes the opt-in-exempt transactional path from the consented marketing path. This model is shared by the pre-care/aftercare follow-ups, RECALL and AUTOMATIONS.
- [ ] **Sequence engine + reminders/confirmations (trigger -> timed steps, confirm/decline)**
  Server-side engine (shared with the care follow-ups, RECALL + AUTOMATIONS), shipped with the reminder/confirmation flow on it.
  - On a trigger (booking made), start a SequenceRun and schedule steps at their offsets; dispatch each via INotifier at its time.
  - Reminder confirm/decline updates the Appointment (PRD-02); reschedule link routes to booking.
  - Transactional sequences send regardless of marketing consent; content must not name/price S4 (Schedule 4 prescription-only medicine) (C9).
  - Endpoints to define sequences + query runs; log every send.
