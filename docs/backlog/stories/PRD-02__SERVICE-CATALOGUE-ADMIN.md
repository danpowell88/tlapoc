# Service catalogue: capability-gated admin & audit

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE-ADMIN`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/SERVICE-CATALOGUE`

## Background

As a owner / manager, I want catalogue changes gated to prescriber/owner, audited, and S4 reward controls disabled, so that only authorised staff change the menu and a prescription medicine can never be discounted.
Plainly: the governance around editing the catalogue — capability-gating to prescriber/owner, auditing every change, archiving instead of deleting, and refusing to enable reward/discount controls on S4 services. Where it fits: a follow-up to the services & treatment menu basic catalogue (PRD-02/SERVICE-CATALOGUE) that adds the admin governance on top of create/view. The S4-no-rewards rule (C9) is enforced here. It sits in Reception (PRD-02).

## How it works

The basic catalogue allows create/view; this follow-up adds the governance. Add/edit/archive of a service is gated to prescriber (a practitioner authorised to write a prescription) / owner capability, so the menu can't be changed by an unauthorised role.
Every change writes an AuditEvent so catalogue history is demonstrable, and S4 (Schedule 4 prescription-only medicine) services cannot have reward/discount controls enabled — validated server-side (C9/REQ-MEMB-7: you can't discount or incentivise a prescription medicine).
Services are archived rather than hard-deleted, so past bookings keep their service history intact.

## Requirements

- Catalogue changes gated to prescriber/owner, audited, and S4 reward controls disabled.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Add/edit/archive is gated to prescriber/owner capability.
- [ ] Every change writes an AuditEvent.
- [ ] S4 services cannot have reward/discount controls enabled (validated server-side, C9).
- [ ] Archive (never hard-delete) so past bookings keep their service history.

## UI designs / screenshots

- Prototype: Clinical → Treatment menu (clinical-menu.png) — Edit/Archive per card, capability-gated admin; changes audited.
- The S4 tag disables reward/discount controls; archive (never delete) retires a service.
- Capability-gated to prescriber/owner.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **AuditEvent (ref)** — actor, service_id, change, at
  - _Catalogue changes audited; admin capability-gated (prescriber/owner); S4 reward controls disabled server-side (C9)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Capability-gated catalogue admin + audit + S4-no-rewards validation**
  Behaviour: add/edit/archive a service from the admin surface. Requirements: gated to prescriber (a practitioner authorised to write a prescription)/owner capability; every change writes an AuditEvent; S4 (Schedule 4 prescription-only medicine) services cannot have reward/discount controls enabled (validated server-side); archive (never hard-delete) so past bookings keep their service history.
