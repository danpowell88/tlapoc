# Reminders & self-service reschedule/cancel

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a client, I want appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself, so that I don't need to call and the clinic's diary stays accurate.
Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling.

## How it works

Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling. Outside policy, the configured rule applies (no auto-charge in v1).
The reminder channel is provided by PRD-07; this story is the booking-side scheduling + self-service actions.

## Requirements

- Appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself.

## Acceptance Criteria

- [ ] Reminders fire per template (SMS/app/email); confirm/decline updates status.
- [ ] Self-reschedule/cancel within policy; outside policy the configured rule applies (no auto-charge in v1).
- [ ] Cancellation/no-show policy is configurable.
- [ ] Reminder channel is provided by PRD-07.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Client app / email-SMS: reminder with confirm/decline + reschedule/cancel links; the desk sees confirm/decline status on the appointment (schedule.png).
- Cancellation/no-show policy is configurable in settings.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **ReminderSchedule** — id, appointment_id, channel, send_at, status(sent|confirmed|declined)
  - _Updates Appointment.status on confirm/decline._
- **CancellationPolicy** — tenant_id, window_hours, no_show_rule
  - _No deposit/auto-charge in v1._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ReminderSchedule — id, appointment_id, channel, send_at, status(sent|confirmed|declined) (Updates Appointment.status on confirm/decline.)
  - CancellationPolicy — tenant_id, window_hours, no_show_rule (No deposit/auto-charge in v1.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Reminders fire per template (SMS/app/email); confirm/decline updates status.
  - Rule: Self-reschedule/cancel within policy; outside policy the configured rule applies (no auto-charge in v1).
  - Rule: Cancellation/no-show policy is configurable.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/LIFECYCLE.
- [ ] **Web UI**
  Build on the Angular web app: the schedule per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Client app / email-SMS: reminder with confirm/decline + reschedule/cancel links; the desk sees confirm/decline status on the appointment (schedule.png).
  - Cancellation/no-show policy is configurable in settings.
