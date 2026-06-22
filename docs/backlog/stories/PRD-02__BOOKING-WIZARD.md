# Staff booking wizard (service → practitioner → time → client → confirm)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/BOOKING-WIZARD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`, `PRD-02/SERVICE-CATALOGUE`

## Background

As a front desk, I want a guided booking wizard to create an appointment in a few steps, so that I can book clients quickly at the desk or over the phone.
Built on the calendar (PRD-02/CALENDAR) availability engine and the service catalogue (PRD-02/SERVICE-CATALOGUE), the staff booking wizard is the desk and phone counterpart to online self-booking and the path most bookings in Reception (PRD-02) flow through, applying the same scope rules at the desk as online. In the flow it is front-of-house entry to a visit: a guided service → practitioner → time → client → confirm that creates the booking and kicks off the Intake/Consent send (PRD-03) which must be complete before treatment can start. As front desk, I want a guided booking wizard to create an appointment in a few steps, so that I can book clients quickly at the desk or over the phone.  The prototype's front-desk 'New booking' wizard (service select, slot pick, client attach, confirm) is the staff counterpart to client self-booking, and the entry point most bookings flow through.

## How it works

The staff booking wizard is the desk/phone counterpart to online self-booking and the path most bookings flow through: service → practitioner → time slot → client → confirm. It uses the same scope-aware availability engine as everything else, so the practitioner step for an injectable offers only cleared RN/NP (and a 'Next available' shortcut to the soonest eligible injector), and the slot grid reflects roster ∩ availability with taken slots struck through.
At the client step the desk attaches an existing (returning) client or creates one inline (new) — returning gets a quick medical re-screen, new gets full intake + medical history + BDD screen + consent; under-18 is flagged. A checkbox sends the intake + consent links now with the note 'treatment can't start until complete' (ties to PRD-03 GATING).
Confirm shows the booking summary, the cancellation policy, and schedules the reminder (e.g. 24h prior, via PRD-07). The created Appointment is source=desk — identical entity/flow to online and walk-in.

## Requirements

- A guided booking wizard to create an appointment in a few steps.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Wizard steps: service → practitioner → time slot → client → confirm.
- [ ] Scope-aware: injectable services offer only cleared RN/NP (C4); slots reflect roster ∩ availability.
- [ ] An existing client can be attached or a new one created inline; under-18 is flagged.
- [ ] Confirmation shows the cancellation policy and schedules reminders (PRD-07).

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: 'New booking' wizard (booking-wizard.png) — stepper (1 Service · 2 Practitioner · 3 Time · 4 Client · 5 Confirm). Step 1 service cards show duration/price/schedule (e.g. 'Anti-wrinkle · 45 min · from $11/unit · S4'); header note 'Public service names stay generic · injectables offer RN/NP only'.
- Step 2: 'RN/NP only — injectable' with 'rostered today · availability respects shifts & existing bookings'; step 3 slot grid with taken slots struck through; step 4 attach Returning/New client + reason + 'Send intake + consent links now (treatment can't start until complete)'.
- Step 5 confirm: summary, 'Intake + consent SMS sent', 'Reminder scheduled for 24h prior'.

![booking-wizard — prototype screen](../screens/booking-wizard.png)

## Suggested data model

- **Appointment** — (as CALENDAR) source=desk
  - _Created via the wizard; same entity/flow as online + walk-in._
- **Client (ref)** — new|returning, dob/under_18, reason
  - _Attach existing or create inline; under-18 flagged; drives intake type + cooling-off._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Step 1 — service selection (generic names, schedule shown)**
  Behaviour: service cards showing duration / price / schedule (e.g. 'Anti-wrinkle · 45 min · from $11/unit · S4') with a header note that public names stay generic and injectables offer RN/NP only. Requirements: only bookable services appear; the schedule flag on each card drives the downstream scope filtering; selecting a service advances the stepper.
- [ ] **Step 2 — practitioner selection (scope-filtered + Next available)**
  Behaviour: practitioner cards for the chosen service, with a 'Next available' shortcut. Requirements: for an S4 (Schedule 4 prescription-only medicine) service only cleared RN/NP are offered (the canInject gate, C4); the eligible list comes from the SAME server-side availability engine as CALENDAR/online — no client-side scope logic; 'Next available' resolves to the soonest eligible injector.
- [ ] **Step 3 — time-slot grid (roster ∩ availability)**
  Behaviour: a slot grid for the chosen service + practitioner with taken slots struck through. Requirements: slots = roster ∩ canInject ∩ free room/chair/device for the whole block incl. buffers, from the shared engine; over-capacity/taken slots are disabled; the server returns only genuinely bookable slots.
- [ ] **Step 4 — client step (attach existing / create inline + under-18)**
  Behaviour: search/attach a returning client or create a new one inline capturing DOB, plus a reason/notes field and a 'Send intake + consent links now (treatment can't start until complete)' checkbox. Requirements: the Returning/New toggle changes the intake hint (returning = quick re-screen; new = full intake + history + BDD + consent); derive and stamp under_18 from DOB; the checkbox wires to the PRD-03 intake + consent send.
- [ ] **Step 5 — confirm (policy + create source=desk + reminder)**
  Behaviour: a summary that shows the cancellation policy and commits the booking. Requirements: on confirm, call the create endpoint (source=desk) with full server-side scope/conflict checks, schedule the reminder (PRD-07, e.g. 24h prior), and trigger the intake/consent send if the checkbox was set; show 'Intake + consent sent · Reminder scheduled'; the created Appointment is identical to online/walk-in.
