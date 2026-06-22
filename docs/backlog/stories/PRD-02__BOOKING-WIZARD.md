# Staff booking wizard (service → practitioner → time → client → confirm)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/BOOKING-WIZARD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`, `PRD-02/SERVICE-CATALOGUE`

## Background

As a front desk, I want a guided booking wizard to create an appointment in a few steps, so that I can book clients quickly at the desk or over the phone.
The prototype's front-desk 'New booking' wizard (service select, slot pick, client attach, confirm) is the staff counterpart to client self-booking, and the entry point most bookings flow through.

## How it works

The staff booking wizard is the desk/phone counterpart to online self-booking and the path most bookings flow through: service -> practitioner -> time slot -> client -> confirm, with the cancellation policy shown and reminders scheduled.
Scope-aware: injectable services only offer cleared RN/NP; under-18 is flagged for cooling-off.

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

- Prototype: 'New booking' wizard (booking-wizard.png) — stepper (service, practitioner, slot, client, confirm); attach existing client or create inline; slot grid reflects roster + availability.
- Confirmation shows policy + schedules reminders.

![booking-wizard — prototype screen](../screens/booking-wizard.png)

## Suggested data model

- **Appointment** — (as CALENDAR) source=desk
  - _Created via the wizard; same entity/flow._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Appointment — (as CALENDAR) source=desk (Created via the wizard; same entity/flow.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Wizard steps: service → practitioner → time slot → client → confirm.
  - Rule: Scope-aware: injectable services offer only cleared RN/NP (C4); slots reflect roster ∩ availability.
  - Rule: An existing client can be attached or a new one created inline; under-18 is flagged.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/CALENDAR, PRD-02/SERVICE-CATALOGUE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C4 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Scope-aware: injectable services offer only cleared RN/NP (C4); slots reflect roster ∩ availability.
- [ ] **Web UI**
  Build on the Angular web app: the booking-wizard per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: 'New booking' wizard (booking-wizard.png) — stepper (service, practitioner, slot, client, confirm); attach existing client or create inline; slot grid reflects roster + availability.
  - Confirmation shows policy + schedules reminders.
