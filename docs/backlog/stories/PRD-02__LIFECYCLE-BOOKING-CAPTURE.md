# Visit lifecycle: booking capture (new/returning, reason, roster)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE-BOOKING-CAPTURE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a front desk, I want the booking to capture whether the client is new or returning, the reason, and the rostered practitioner, so that the right intake is sent and recall and reporting have what they need.
Plainly: capturing the few booking fields that drive what happens downstream — new-versus-returning (which intake is sent), the reason for the visit, and which rostered practitioner. Where it fits: a follow-up to the visit lifecycle basic state-machine (PRD-02/LIFECYCLE) that adds the booking-time capture fields. New-vs-returning selects the intake variant in Intake & Consent (PRD-03); reason and practitioner feed recall and reporting. It sits in Reception (PRD-02).

## How it works

The basic state-machine tracks status; this follow-up captures the booking-time fields those downstream flows depend on. At booking, the Appointment records new_or_returning, a reason/notes field, and the rostered practitioner.
New-vs-returning selects the intake variant downstream (a new client gets the full intake; a returning client gets a quick re-screen — PRD-03/INTAKE), and the reason and practitioner feed recall and reporting.
The capture respects the roster so a booking can't be taken against a practitioner who isn't working at that time.

## Requirements

- The booking to capture whether the client is new or returning, the reason, and the rostered practitioner.

## Acceptance Criteria

- [ ] New-vs-returning, reason/notes and the rostered practitioner are captured on the Appointment.
- [ ] New-vs-returning selects the intake type downstream (full intake vs quick re-screen).
- [ ] Reason and practitioner feed recall and reporting.
- [ ] A booking can't be taken against an unrostered practitioner.

## UI designs / screenshots

- Prototype: the booking flow captures Returning/New, a reason/notes field, and the practitioner (booking-wizard.png / dashboard.png).
- New-vs-returning visibly changes the intake hint (full vs quick re-screen).
- The practitioner field only offers rostered practitioners.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment (booking fields, extends LIFECYCLE)** — new_or_returning, reason, practitioner_id
  - _Captured at booking; drives intake type (full vs re-screen), recall and reporting._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Capture new-vs-returning, reason, rostered practitioner**
  Behaviour: at booking, capture new_or_returning, reason/notes and the rostered practitioner on the Appointment. Requirements: new-vs-returning selects the intake type downstream (full intake vs quick re-screen); reason and practitioner feed recall and reporting; respects the roster so a booking can't be taken against an unrostered practitioner.
