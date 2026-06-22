# Services & treatment menu — basic catalogue & S4 flag

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a owner / manager, I want to manage the menu of services with durations, eligible roles and the S4 flag, so that booking, rewards and the public page all behave correctly per service.
The service catalogue is the treatment menu that defines every bookable service, and the single switch that makes booking behave correctly per service. It sits in Reception (PRD-02) and depends on the medicines/products catalogue in Injectables (PRD-04/PRODUCT-CATALOGUE) for the stock a service consumes. It is foundational to the booking surfaces: the S4/non-S4 schedule flag set here is what drives scope-aware booking (the booking wizard and online self-booking only offer cleared injectors), rewards eligibility (PRD-06), and the generic public-page naming (PRD-07) — so this catalogue is read everywhere a service is offered, priced or charted. As owner / manager, I want to manage the menu of services with durations, eligible roles and the S4 flag, so that booking, rewards and the public page all behave correctly per service.  The prototype's clinical Treatment menu + admin services list defines bookable services with durations, eligible roles, and the S4/non-S4 flag that drives scope-aware booking, rewards eligibility and public-page naming.

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
  Behaviour: model Service (id/name/public_name/category/duration/buffer/price/schedule/reg_class/unit/eligible_roles[]/requires[]/product_id?). Requirements: the schedule flag (ADR-0014/0021) is the single source of truth; persist with tenant RLS (row-level security); derive rewards_eligible = (schedule != S4 (Schedule 4 prescription-only medicine)).
- [ ] **Minimal services-list admin (create/view)**
  Behaviour: a basic services list to create and view services with their duration/buffer, eligible roles, price and schedule flag. Requirements: only the core list + create/view; cross-platform wiring of the schedule flag, the audit + S4-control validation, the treatment-menu card UI, and the Active/Archived/All filter are follow-ups.
