# Services & treatment-menu admin (durations, eligible roles, S4 flag)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a owner / manager, I want to manage the menu of services with durations, eligible roles and the S4 flag, so that booking, rewards and the public page all behave correctly per service.
The prototype's clinical Treatment menu + admin services list defines bookable services with durations, eligible roles, and the S4/non-S4 flag that drives scope-aware booking, rewards eligibility and public-page naming.

## How it works

The services / treatment menu defines every bookable service with duration/buffer, eligible roles, price and the S4/non-S4 flag. That single flag drives scope-aware booking (C4), rewards eligibility (C9) and public-page naming (PRD-07).
Linked to the medicines/products catalogue (PRD-04) where a service consumes a product.

## Requirements

- To manage the menu of services with durations, eligible roles and the S4 flag.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Services carry duration/buffer, eligible roles, price and the S4/non-S4 flag.
- [ ] The S4 flag drives scope-aware booking (C4), rewards eligibility (C9) and public naming (PRD-07).
- [ ] Capability-gated admin; changes are audited.
- [ ] Linked to the medicines/products catalogue (PRD-04) where a service consumes a product.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Clinical -> Treatment menu (clinical-menu.png) and admin Services & products — each service row shows duration, eligible roles, price, S4 flag; capability-gated admin; changes audited.
- The S4 tag visibly marks services and disables reward/discount controls on them.

![clinical-menu — prototype screen](../screens/clinical-menu.png)

## Suggested data model

- **Service** — id, tenant_id, name, public_name, duration, buffer, price, schedule(S4|non-S4), eligible_roles[], product_id?
  - _schedule flag is the master classification (ADR-0014)._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C9); blocked path explains why.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
