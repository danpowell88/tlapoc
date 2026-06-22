# Staff booking wizard: confirm with policy & reminder scheduling

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/BOOKING-WIZARD-CONFIRM`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/BOOKING-WIZARD`

## Background

As a front desk, I want the confirm step to show the cancellation policy and schedule a reminder, so that the client knows the policy and gets a reminder without me doing anything extra.
Plainly: enriching the wizard's confirm step so it shows the cancellation policy and schedules the appointment reminder when the booking is created. Where it fits: a follow-up to the staff booking wizard basic scope-aware flow (PRD-02/BOOKING-WIZARD), whose confirm step just creates the booking. The reminder is scheduled via Comms (PRD-07) and the policy is read from the cancellation policy settings (PRD-02/REMINDERS-POLICY). It sits in Reception (PRD-02).

## How it works

The basic wizard's confirm step commits the booking; this follow-up enriches it. The summary now shows the cancellation policy (read from PRD-02/REMINDERS-POLICY) so the client is informed at booking time.
On confirm, the appointment reminder is scheduled (PRD-07, e.g. 24h prior) and the intake/consent send is triggered if the checkbox was set, with the confirmation showing 'Intake + consent sent · Reminder scheduled'.
The created Appointment remains identical to an online or walk-in booking — this story only adds the policy display and reminder scheduling to the confirm step.

## Requirements

- The confirm step to show the cancellation policy and schedule a reminder.

## Acceptance Criteria

- [ ] The confirm step shows the booking summary and the cancellation policy.
- [ ] Confirming schedules the reminder (PRD-07, e.g. 24h prior).
- [ ] The confirmation shows 'Reminder scheduled' (and 'Intake + consent sent' when the send was set).
- [ ] The created Appointment is identical to online/walk-in.

## UI designs / screenshots

- Prototype: 'New booking' wizard (booking-wizard.png) step 5 confirm — summary, 'Intake + consent SMS sent', 'Reminder scheduled for 24h prior'.
- The cancellation policy is shown on the summary.
- Confirming schedules the reminder via PRD-07.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends BOOKING-WIZARD)** — no new entities; the confirm step reads CancellationPolicy and schedules a ReminderSchedule
  - _Reminder scheduled via PRD-07; policy from PRD-02/REMINDERS-POLICY; the Appointment is identical to online/walk-in._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Confirm step: policy display + reminder scheduling**
  Behaviour: a summary that shows the cancellation policy and, on confirm, schedules the reminder. Requirements: show the cancellation policy on the summary; schedule the reminder (PRD-07, e.g. 24h prior) and trigger the intake/consent send if the checkbox was set; show 'Intake + consent sent · Reminder scheduled'; the created Appointment is identical to online/walk-in.
