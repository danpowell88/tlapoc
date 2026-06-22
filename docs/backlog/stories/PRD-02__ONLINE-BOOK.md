# Online self-booking (scope-aware)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/ONLINE-BOOK`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`, `PRD-01/CREDENTIALS`

## Background

As a client, I want to book a consult/treatment online by choosing service, practitioner and time, so that I can book without calling the clinic.
Clients self-book service → practitioner → slot online; injectable services only offer cleared RN/NP and the public page uses generic names (C4/C9).

## How it works

Client-facing self-booking on the public page: service -> practitioner -> slot -> account -> intake/consent. It reuses the same scope-aware availability as the desk, so an injectable only offers cleared RN/NP and requires the consult step downstream.
Public service names are generic and S4 prices withheld by configuration (C9). Under-18 bookings are flagged so cooling-off can be enforced later (PRD-03).

## Requirements

- To book a consult/treatment online by choosing service, practitioner and time.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Booking wizard: service → practitioner → time → client → confirm.
- [ ] Injectable services offer only cleared RN/NP (scope-aware, per C4); others never appear bookable for it.
- [ ] Public service names are generic and S4 prices withheld by configuration (C9, see PRD-07).
- [ ] Under-18 bookings are flagged for downstream cooling-off (feeds PRD-03).

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: public booking page (public-booking.png) and the booking widget (booking-widget.png) — generic service list, practitioner choice, slot grid, account create, then intake/consent.
- No S4 brand names or prices shown; injectables present consult+treatment as a gated flow.

![public-booking — prototype screen](../screens/public-booking.png)

## Suggested data model

- **Appointment** — (as CALENDAR) source=online
  - _Same entity; created via the public flow._
- **PublicBookingConfig** — tenant_id, generic_names(bool), withhold_s4_prices(bool)
  - _Drives naming/pricing per C9 (shared with PRD-07 BOOKING-PAGE)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Appointment — (as CALENDAR) source=online (Same entity; created via the public flow.)
  - PublicBookingConfig — tenant_id, generic_names(bool), withhold_s4_prices(bool) (Drives naming/pricing per C9 (shared with PRD-07 BOOKING-PAGE).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Booking wizard: service → practitioner → time → client → confirm.
  - Rule: Injectable services offer only cleared RN/NP (scope-aware, per C4); others never appear bookable for it.
  - Rule: Public service names are generic and S4 prices withheld by configuration (C9, see PRD-07).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/CALENDAR, PRD-01/CREDENTIALS.
- [ ] **Enforce compliance gate + audit events**
  Enforce C4, C6, C9 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Injectable services offer only cleared RN/NP (scope-aware, per C4); others never appear bookable for it.
- [ ] **Web UI**
  Build on the Angular web app: the public-booking per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: public booking page (public-booking.png) and the booking widget (booking-widget.png) — generic service list, practitioner choice, slot grid, account create, then intake/consent.
  - No S4 brand names or prices shown; injectables present consult+treatment as a gated flow.
