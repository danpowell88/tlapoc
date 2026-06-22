# Service catalogue: schedule flag wired to scope, rewards & public naming

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE-WIRING`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/SERVICE-CATALOGUE`

## Background

As a owner / manager, I want the S4 schedule flag to actually drive scope, rewards and public naming across the platform, so that classifying a service once makes booking, rewards and the public page all behave correctly.
Plainly: making the S4/non-S4 schedule flag the master switch it's meant to be — driving scope-aware booking, rewards eligibility, public-page naming and the charting requirements. Where it fits: a follow-up to the services & treatment menu basic catalogue (PRD-02/SERVICE-CATALOGUE), which defines the flag; this wires it across the platform. It is read by the availability engine (PRD-02/CALENDAR), the rewards engine (PRD-06), the public booking config (PRD-02/ONLINE-BOOK) and charting (PRD-05). It sits in Reception (PRD-02).

## How it works

The basic catalogue defines each Service and its schedule flag; this follow-up makes that single classification (ADR-0014/0021) actually drive behaviour everywhere a service is offered, priced or charted.
The availability engine restricts S4 (Schedule 4 prescription-only medicine) services to canInject roles (C4 — only cleared injectors); the rewards engine (PRD-06) is constrained to non-S4 by the flag (C9/REQ-MEMB-7 — no earn/redeem/discount on a prescription medicine); the public booking config (PRD-02/ONLINE-BOOK, shared with PRD-07) uses the generic name and withholds price for S4.
Each service's requires(consult/rx/s4_lot/standard_consent) declaration is read by charting (PRD-05) and the gates, and product_id links to the medicines/products catalogue (PRD-04/PRODUCT-CATALOGUE) so stock decrements on administration.

## Requirements

- The S4 schedule flag to actually drive scope, rewards and public naming across the platform.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The availability engine restricts S4 to canInject roles (C4).
- [ ] The rewards engine (PRD-06) is constrained to non-S4 by this flag (C9/REQ-MEMB-7).
- [ ] The public booking config (ONLINE-BOOK) uses the generic name + withholds price for S4 (PRD-07).
- [ ] The requires(consult/rx/s4_lot/standard_consent) declaration is read by charting (PRD-05) and the gates; product_id links to PRODUCT-CATALOGUE for stock decrement.

## UI designs / screenshots

- No new primary screen — the flag's effects show wherever a service is offered (booking, rewards, public page, charting).
- S4 services are offered only to canInject roles in booking and never earn/redeem rewards.
- The public page uses the generic name and withholds price for S4 (Compounded GLP-1 blocked banner illustrates catalogue-driven enforcement).

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Service (extends SERVICE-CATALOGUE)** — schedule(S4|non-S4), requires(consult|rx|s4_lot|standard_consent), product_id?, rewards_eligible(derived)
  - _The schedule flag (ADR-0014/0021) is read by the availability engine, rewards engine, public booking config and charting; product_id links to PRD-04/PRODUCT-CATALOGUE._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Wire schedule flag to scope, rewards, public naming and charting**
  Behaviour: make the schedule flag actually drive behaviour across the platform. Requirements: the availability engine restricts S4 (Schedule 4 prescription-only medicine) to canInject roles (C4); the rewards engine (PRD-06) is constrained to non-S4 by this flag (C9/REQ-MEMB-7); the public booking config (ONLINE-BOOK) uses the generic name + withholds price for S4; the requires(consult/rx/s4_lot/standard_consent) declaration is read by charting (PRD-05) and the gates; product_id links to PRODUCT-CATALOGUE for stock decrement.
