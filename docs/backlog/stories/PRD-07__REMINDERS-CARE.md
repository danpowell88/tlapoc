# Reminders, confirmations & care sequences

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REMINDERS-CARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a client, I want timely reminders I can confirm/decline and pre-/after-care instructions for my treatment, so that I'm prepared and cared for around my visit.
Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type) (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

## How it works

Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type). Confirm/decline updates the appointment (PRD-02). Transactional messages send regardless of marketing opt-in and avoid S4 references.
Keeps clients prepared and cared-for around each visit.

## Requirements

- Timely reminders I can confirm/decline and pre-/after-care instructions for my treatment.

## Acceptance Criteria

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment (PRD-02).
- [ ] Pre-care + aftercare sequences are multi-touch and timed per treatment type.
- [ ] Transactional messages send regardless of marketing opt-in and avoid S4 references.
- [ ] Sends are logged to comms history.

## UI designs / screenshots

- Prototype: Comms -> Automations (marketing-auto.png) configures the reminder/aftercare sequences; sends appear in the client's comms history.
- Reminder includes confirm/decline + reschedule links (PRD-02 REMINDERS).

![marketing-auto — prototype screen](../screens/marketing-auto.png)

## Suggested data model

- **Sequence** — id, tenant_id, trigger(booking|visit), treatment_type, steps[]{offset, channel, template_key}
  - _Multi-touch, timed per treatment._
- **SequenceRun** — id, sequence_id, client_id, appointment_id, step_status[]
  - _Transactional; exempt from opt-in._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
