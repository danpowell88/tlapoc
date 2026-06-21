# Online self-booking (scope-aware)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/ONLINE-BOOK`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`, `PRD-01/CREDENTIALS`

## Background

As a client, I want to book a consult/treatment online by choosing service, practitioner and time, so that I can book without calling the clinic.
Clients self-book service → practitioner → slot online; injectable services only offer cleared RN/NP and the public page uses generic names (C4/C9).

## Requirements

- To book a consult/treatment online by choosing service, practitioner and time.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Booking wizard: service → practitioner → time → client → confirm.
- [ ] Injectable services offer only cleared RN/NP (scope-aware, per C4); others never appear bookable for it.
- [ ] Public service names are generic and S4 prices withheld by configuration (C9, see PRD-07).
- [ ] Under-18 bookings are flagged for downstream cooling-off (feeds PRD-03).

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C6, C9); blocked path explains why.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
