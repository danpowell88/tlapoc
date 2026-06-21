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

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
