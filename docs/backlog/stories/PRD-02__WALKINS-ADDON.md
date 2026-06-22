# Walk-ins: same-day add-on to an in-progress visit

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS-ADDON`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WALKINS`

## Background

As a front desk, I want to append an extra service to a visit that's already underway, so that we can treat opportunistically without starting a new booking.
Plainly: adding an extra service to a client whose visit is already in progress. Where it fits: a follow-up to the walk-ins basic gate-respecting booking (PRD-02/WALKINS) that adds same-day add-ons on top of the walk-in flow. It re-uses the calendar (PRD-02/CALENDAR) availability engine and respects the same scope and compliance gates — an S4 (Schedule 4 prescription-only medicine) add-on still needs a consult and consent. It sits in Reception (PRD-02).

## How it works

The basic walk-in flow books a new appointment; this follow-up lets the desk append an additional service to a visit already in progress without re-keying the client.
The add-on must land on a free resource for its whole block including buffers (using the same availability engine), and inherits the in-progress visit's client.
It respects the same scope and compliance gates as any booking: an S4 add-on still carries the consult gate (charting blocked until a consult is linked) and still requires consent — an add-on never bypasses the rules.

## Requirements

- To append an extra service to a visit that's already underway.

## Acceptance Criteria

- [ ] An extra service can be appended to a visit already underway.
- [ ] The add-on must land on a free resource for its whole block incl. buffers.
- [ ] It inherits the visit's client and respects the same scope/gate rules.
- [ ] An S4 add-on still needs consult + consent.

## UI designs / screenshots

- Prototype: Schedule (schedule.png) — append a service to an in-progress visit from the appointment/visit context.
- The add-on picks a free resource for its whole block incl. buffers and inherits the visit's client.
- An S4 add-on shows it still needs consult + consent before charting.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment (extends WALKINS)** — an additional Appointment line on the same visit/client; source=walkin
  - _Lands on a free Resource for the whole block incl. buffers; S4 add-on still requires consult_id + consent._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Same-day add-on to an in-progress visit**
  Behaviour: append an additional service to a visit already underway. Requirements: the add-on must land on a free resource for its whole block incl. buffers; it inherits the visit's client and respects the same scope/gate rules; an S4 add-on still needs consult + consent.
