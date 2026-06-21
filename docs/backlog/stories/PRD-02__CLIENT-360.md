# Client 360° profile

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-360`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/CLIENT-CORE`

## Background

As a staff member, I want a single 360° client profile pulling together history, medical flags, consents, photos, memberships, balances and comms, so that I have the full picture in one place.
Any staff member can open a client's full profile: history, contacts, medical flags, consents, photos, memberships, balances, comms and complaints.

## Requirements

- A single 360° client profile pulling together history, medical flags, consents, photos, memberships, balances and comms.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Profile aggregates overview, medical/contraindications, consents, photos, visits, memberships, balance, comms, complaints.
- [ ] Consent/age chips render on the header (consent ✓ / image-use ✓ / under-18 cooling-off).
- [ ] Access is RBAC-scoped (reception sees limited clinical info) and audited.
- [ ] Surfaces data owned by PRD-03/04/05/06/11 via the API.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
