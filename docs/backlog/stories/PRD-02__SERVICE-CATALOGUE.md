# Services & treatment-menu admin (durations, eligible roles, S4 flag)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a owner / manager, I want to manage the menu of services with durations, eligible roles and the S4 flag, so that booking, rewards and the public page all behave correctly per service.
The prototype's clinical Treatment menu + admin services list defines bookable services with durations, eligible roles, and the S4/non-S4 flag that drives scope-aware booking, rewards eligibility and public-page naming.

## How it works

The services / treatment menu defines every bookable service with duration + buffer, eligible roles, price and the S4 / non-S4 schedule flag. That single classification (ADR-0014) is the master switch that drives scope-aware booking (C4 — only canInject roles for S4), rewards eligibility (C9/REQ-MEMB-7 — no earn/redeem/discount on S4), and public-page naming/pricing (PRD-07 — generic name + withheld price for S4).
Each service also declares what charting & compliance it drives: an S4 service requires a synchronous consult + individual script + batch-lot selection at charting and 'standard consent'; a non-S4 skin service requires neither lot nor Rx. Where a service consumes a product it links to the medicines/products catalogue (PRD-04 PRODUCT-CATALOGUE) so stock can decrement on administration.
Catalogue admin is capability-gated (prescriber/owner) and every change is audited; the S4 tag visibly marks services and disables reward/discount controls on them.

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

- Prototype: Clinical → Treatment menu (clinical-menu.png) — each treatment card shows category, schedule (S4/non-S4) + regulatory class, unit, performed-by roles (NP/RN/Dermal), price, duration, linked stock, AE route, and 'Charting & compliance this drives' (synchronous consult · individual S4 script · batch-lot select · standard consent · rewards-eligible vs S4 'not rewards-eligible').
- Active/Archived/All filter; '+ Add treatment'; Edit/Archive/Delete per card; the S4 tag marks services and disables reward/discount controls; capability-gated admin; changes audited.
- (Compounded GLP-1 blocked banner illustrates catalogue-driven enforcement.)

![clinical-menu — prototype screen](../screens/clinical-menu.png)

## Suggested data model

- **Service** — id, tenant_id, name, public_name, category, duration, buffer, price, schedule(S4|non-S4), reg_class(medicine|device|none), eligible_roles[], requires(consult|rx|s4_lot|standard_consent), product_id?, rewards_eligible(derived from schedule), unit
  - _schedule flag is the master classification (ADR-0014/0021) driving scope, rewards and public naming._
- **AuditEvent (ref)** — actor, service_id, change, at
  - _Catalogue changes audited; admin capability-gated (prescriber/owner)._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Service entity + schedule(S4|non-S4) classification**
  Model Service with id/name/public_name/category/duration/buffer/price/schedule/reg_class/unit/eligible_roles[]/requires[]/product_id?. The schedule flag (ADR-0014/0021) is the single source of truth. Persist with tenant RLS. Derive rewards_eligible = (schedule != S4).
- [ ] **Schedule flag wired to scope, rewards and public naming**
  Make the schedule flag actually drive behaviour: the availability engine restricts S4 to canInject roles (C4); the rewards engine (PRD-06) is constrained to non-S4 by this flag (C9/REQ-MEMB-7); the public booking config (ONLINE-BOOK) uses generic name + withholds price for S4. Service also declares requires(consult/rx/s4_lot/standard_consent) that charting (PRD-05) and the gates read. Link product_id to PRODUCT-CATALOGUE for stock decrement.
- [ ] **Capability-gated catalogue admin + audit**
  Admin endpoints to add/edit/archive a service, gated to prescriber/owner capability; every change writes an AuditEvent. Validate that S4 services cannot have reward/discount controls enabled. Archive (not hard-delete) to preserve history on past bookings.
- [ ] **Treatment menu admin UI**
  Angular Treatment-menu screen: cards per service showing category, schedule + reg class, unit, performed-by roles, price, duration, linked stock, AE route and 'Charting & compliance this drives'. Active/Archived/All filter, '+ Add treatment', Edit/Archive. Visibly tag S4 and disable reward/discount controls on S4 cards. Capability-gate the admin actions.
