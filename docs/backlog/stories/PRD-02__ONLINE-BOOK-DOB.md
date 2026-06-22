# Online self-booking: DOB capture & under-18 flag

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/ONLINE-BOOK-DOB`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a system, I want to capture the client's date of birth at online account creation and flag under-18 bookings, so that the downstream cooling-off and payment block can be enforced for minors.
Plainly: capturing date of birth when a client creates an account during online booking, and stamping an under-18 flag on the resulting appointment. Where it fits: a follow-up to online self-booking basic (PRD-02/ONLINE-BOOK) that adds the details/account step's age capture. The under-18 flag is what lets Intake & Consent (PRD-03/COOLING-OFF and PRD-03/GATING) enforce the mandatory 7-day cooling-off and payment block for minors. It sits in Reception (PRD-02).

## How it works

The basic online flow confirms and creates a booking; this follow-up adds the details/account step's age capture. On account creation the client's date of birth is captured (or matched to an existing account), with the 'Your details are kept private & used only to manage your booking' assurance.
Under-18 is DERIVED from the DOB and stamped on the resulting Appointment so that Intake & Consent (PRD-03) can later enforce the 7-day cooling-off (the mandatory wait before a cosmetic procedure can proceed) and the payment block for minors. A domain event (a fact emitted when something happens in the system) is emitted so the downstream gates react.
Guardian and additional contact capture is deferred to PRD-03 (GUARDIAN-CONSENT); this story only captures DOB and sets the flag the gates read.

## Requirements

- To capture the client's date of birth at online account creation and flag under-18 bookings.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The details/account step captures date of birth and creates or matches an account.
- [ ] Under-18 is derived from DOB and stamped on the resulting Appointment.
- [ ] A domain event is emitted so downstream gates (PRD-03) react to the under-18 flag.
- [ ] The 'kept private' assurance is shown; guardian/contact capture is deferred to PRD-03.

## UI designs / screenshots

- Prototype: public booking widget (booking-widget.png) — the 'your details / account' step with DOB capture and 'Your details are kept private & used only to manage your booking'.
- DOB field on the details step; the resulting Appointment carries the derived under-18 flag.
- No guardian capture here — the under-18 path's guardian co-sign is handled in PRD-03.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Client (ref)** — dob, under_18(derived)
  - _DOB captured at account create; under-18 flag stamped on the Appointment and feeds PRD-03 cooling-off (C6)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **DOB capture + under-18 flag on the Appointment**
  Behaviour: the details/account step captures date of birth, creates or matches an account, and shows the 'kept private' assurance. Requirements: derive under_18 from DOB and stamp it on the resulting Appointment so PRD-03 COOLING-OFF/GATING can enforce the 7-day cooling-off (the mandatory wait before a cosmetic procedure can proceed) + payment block; emit a domain event (a fact emitted when something happens in the system) so downstream gates react; guardian/contact capture is deferred to PRD-03.
