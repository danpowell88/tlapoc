# Reminders: confirm / decline handling

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS-CONFIRM-DECLINE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/REMINDERS`

## Background

As a client, I want to confirm or decline my appointment straight from the reminder, so that the clinic knows I'm coming and a declined slot can be reused.
Plainly: the confirm/decline links carried by a reminder that let a client respond without calling, updating the appointment and freeing a declined slot. Where it fits: a follow-up to the reminders basic scheduling & dispatch (PRD-02/REMINDERS) that adds client response handling on top of the sent reminder. A confirm updates the visit lifecycle status; a decline frees the slot and emits the event the waitlist (PRD-02/WAITLIST) backfills from. It sits in Reception (PRD-02).

## How it works

The basic story schedules and dispatches reminders; this follow-up adds the client's response. Each reminder carries confirm/decline links the client can action without calling the clinic.
A confirm link updates Appointment.status (→ reminded/confirmed) and shows a 'Confirmed' chip on the Schedule/Today board; a decline frees the slot and emits the slot-freed event the waitlist (PRD-02/WAITLIST) listens to for backfill.
The links resolve to authenticated-by-token public endpoints (no login needed) and are idempotent so a repeated click never double-applies.

## Requirements

- To confirm or decline my appointment straight from the reminder.

## Acceptance Criteria

- [ ] The reminder carries confirm/decline links the client can action without calling.
- [ ] A confirm updates Appointment.status (→ reminded/confirmed) and shows a 'Confirmed' chip on the Schedule/Today board.
- [ ] A decline frees the slot and emits the slot-freed event the waitlist listens to.
- [ ] Links resolve to authenticated-by-token public endpoints and are idempotent.

## UI designs / screenshots

- Client app / SMS / email: a reminder with confirm/decline actions (self-service, no call needed).
- Desk: a 'Confirmed' chip on the appointment in the Schedule/Today board (schedule.png).
- A decline frees the slot and feeds the waitlist backfill.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends REMINDERS)** — ReminderSchedule.status → confirmed|declined; a confirm/decline updates Appointment.status
  - _A decline emits the slot-freed event WAITLIST consumes; token-authenticated public endpoints._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Confirm / decline links + status update + slot-freed event**
  Behaviour: the reminder carries confirm/decline links the client can action without calling. Requirements: a confirm link updates Appointment.status (→ reminded/confirmed) and shows a 'Confirmed' chip on the Schedule/Today board; a decline frees the slot and emits the slot-freed event WAITLIST listens to; links resolve to authenticated-by-token public endpoints; idempotent.
