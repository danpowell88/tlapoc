# Reminders & self-service reschedule/cancel

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a client, I want appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself, so that I don't need to call and the clinic's diary stays accurate.
Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling.

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

- [ ] **Reminder scheduling + confirm/decline handling**
  Create ReminderSchedule rows when an appointment is booked/moved (send_at relative to start, per template). A scheduled job dispatches due reminders via the PRD-07 INotifier (SMS/app/email). Public confirm/decline links resolve to endpoints that update Appointment.status (confirmed) or mark declined and free the slot (emit an event WAITLIST listens to). Idempotent; reschedule/cancel reschedules the reminder.
- [ ] **Self-service reschedule/cancel within policy**
  Client-facing reschedule/cancel that enforces CancellationPolicy.window_hours server-side: inside the window → reuse the availability engine to move, or cancel and free the slot; outside the window → apply the configured rule (block/flag/message) with NO charge or deposit (v1). All actions audited; cancel emits the slot-freed event for WAITLIST.
- [ ] **Cancellation/no-show policy settings UI**
  Per-tenant settings: window_hours, no_show_rule, allow_self_reschedule. Validate and persist; surface a plain-language 'no auto-charge in v1' note. The policy is shown to the client at confirm time (ties to BOOKING-WIZARD confirmation step) and enforced by the self-service endpoints.
