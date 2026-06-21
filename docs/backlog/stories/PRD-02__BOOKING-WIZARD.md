# Staff booking wizard (service → practitioner → time → client → confirm)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/BOOKING-WIZARD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`, `PRD-02/SERVICE-CATALOGUE`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a front desk, I want a guided booking wizard to create an appointment in a few steps, so that I can book clients quickly at the desk or over the phone.

The prototype's front-desk 'New booking' wizard (service select, slot pick, client attach, confirm) is the staff counterpart to client self-booking, and the entry point most bookings flow through.

## Requirements

- A guided booking wizard to create an appointment in a few steps.
- Traces to requirement(s): REQ-BOOK-2.
- Must satisfy compliance obligation(s): C4.

## Acceptance Criteria

- [ ] Wizard steps: service → practitioner → time slot → client → confirm.
- [ ] Scope-aware: injectable services offer only cleared RN/NP (C4); slots reflect roster ∩ availability.
- [ ] An existing client can be attached or a new one created inline; under-18 is flagged.
- [ ] Confirmation shows the cancellation policy and schedules reminders (PRD-07).

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-02/CALENDAR, PRD-02/SERVICE-CATALOGUE.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/BOOKING-WIZARD.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C4.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4); blocked path explains why.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
