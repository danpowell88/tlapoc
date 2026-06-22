# Reminders & self-service reschedule/cancel

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a client, I want appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself, so that I don't need to call and the clinic's diary stays accurate.
Reminders and self-service reschedule/cancel keep the diary accurate without a phone call. The story sits in Reception (PRD-02) on top of the visit lifecycle (PRD-02/LIFECYCLE) — a confirm/decline or cancel moves the lifecycle status and frees the slot — and just before the waitlist (PRD-02/WAITLIST), which backfills the freed slot. It owns the booking-side scheduling, the self-service actions and the cancellation policy; the actual message delivery (SMS/app/email) is provided later by Comms (PRD-07), so this story schedules and reacts but does not itself send.  Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling.

## How it works

Clients get appointment reminders they can confirm or decline, and can self-reschedule or cancel within policy without calling — keeping the diary accurate. Confirm/decline updates the Appointment status (→ reminded/confirmed); a decline or cancel frees the slot (feeds WAITLIST backfill).
Self-reschedule/cancel is allowed inside the configurable cancellation window; outside the window the configured rule applies (a message/flag) — there is NO deposit and NO auto-charge in v1 (REQ-BOOK-3). The cancellation/no-show policy (window hours, no-show rule) is a per-tenant setting.
This story owns the booking-side scheduling + self-service actions and policy; the actual SMS/app/email delivery channel is provided by PRD-07 (INotifier). Reminders are scheduled relative to the appointment (e.g. 24h prior) per template.

## Requirements

- Appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself.

## Acceptance Criteria

- [ ] Reminders fire per template (SMS/app/email); confirm/decline updates status.
- [ ] Self-reschedule/cancel within policy; outside policy the configured rule applies (no auto-charge in v1).
- [ ] Cancellation/no-show policy is configurable.
- [ ] Reminder channel is provided by PRD-07.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Client app / SMS / email: reminder with confirm/decline + reschedule/cancel links (self-service within policy).
- Desk: confirm/decline status shows on the appointment in the Schedule (schedule.png) — e.g. 'Confirmed' chip on the Today board.
- Settings: cancellation/no-show policy (window hours, rule) is configurable; v1 states 'no auto-charge'.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **ReminderSchedule** — id, tenant_id, appointment_id, channel(sms|app|email), template_id, send_at, status(scheduled|sent|confirmed|declined)
  - _Scheduled relative to the appointment; delivery via PRD-07 INotifier; confirm/decline updates Appointment.status._
- **CancellationPolicy** — tenant_id, window_hours, no_show_rule, allow_self_reschedule(bool)
  - _No deposit/auto-charge in v1; governs the self-service reschedule/cancel boundary._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Reminder scheduling + dispatch**
  Behaviour: create ReminderSchedule rows when an appointment is booked or moved, with send_at relative to start per template; a scheduled job dispatches due reminders. Requirements: delivery goes through the PRD-07 INotifier (SMS/app/email) — this story schedules and reacts but does not itself send; reschedule/cancel reschedules or cancels the pending reminder; idempotent (a due reminder is dispatched once).
- [ ] **Confirm / decline handling from the reminder**
  Behaviour: the reminder carries confirm/decline links the client can action without calling. Requirements: a confirm link updates Appointment.status (→ reminded/confirmed) and shows a 'Confirmed' chip on the Schedule/Today board; a decline frees the slot and emits the slot-freed event WAITLIST listens to; links resolve to authenticated-by-token public endpoints; idempotent.
- [ ] **Self-service reschedule / cancel within policy**
  Behaviour: the client can self-reschedule or cancel within the cancellation window. Requirements: enforce CancellationPolicy.window_hours server-side — inside the window reuse the availability engine to move, or cancel and free the slot (emits the slot-freed event for WAITLIST); outside the window apply the configured rule (block/flag/message) with NO charge or deposit in v1; all actions audited.
- [ ] **Cancellation / no-show policy settings UI**
  Behaviour: a per-tenant settings screen for window_hours, no_show_rule and allow_self_reschedule. Requirements: validate and persist; surface the plain-language 'no auto-charge in v1' note; the policy is shown to the client at confirm time (ties to BOOKING-WIZARD's confirmation step) and is the source of truth the self-service endpoints enforce.
