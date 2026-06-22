# Online self-booking: generic names & withheld S4 prices (C9)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/ONLINE-BOOK-GENERIC-NAMES`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a client, I want the public booking page to show generic service names and not advertise prescription-medicine prices, so that the clinic stays within the advertising rules for prescription-only cosmetic medicines.
Plainly: the configuration that makes the public booking page use generic service names and withhold prices for prescription-only (S4) medicines, tagging them 'consultation required'. Where it fits: a follow-up to online self-booking basic (PRD-02/ONLINE-BOOK) that adds the advertising-compliance layer on top of the public flow. It satisfies compliance criterion C9 (TGA/AHPRA advertising of prescription medicines) via a per-tenant PublicBookingConfig — a configuration policy, not an automated linter — and shares that policy with the public booking page in Comms (PRD-07). It sits in Reception (PRD-02).

## How it works

The basic online flow books a service; this follow-up constrains how services are PRESENTED publicly to meet the advertising rules for prescription-only medicines (C9). Services show clinic-customised generic display names (no S4 brands or 'anti-wrinkle injection' wording), and S4 services are tagged 'Consultation required' and shown price-free.
Crucially the sanitisation happens server-side: the public endpoint returns ALREADY-SANITISED data so the browser never receives an S4 brand name or price. This is a configuration policy (a per-tenant PublicBookingConfig with generic_names, display_name_overrides and withhold_s4_prices), not an automated advertising linter.
The same PublicBookingConfig policy is shared with the public booking page in Comms (PRD-07 BOOKING-PAGE), so the clinic configures naming/pricing compliance once and it applies wherever a service is offered publicly.

## Requirements

- The public booking page to show generic service names and not advertise prescription-medicine prices.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Public service names are generic and S4 prices are withheld by configuration (C9).
- [ ] S4 services are tagged 'Consultation required' and shown price-free ('Pricing is confirmed privately with your practitioner').
- [ ] The server returns already-sanitised data so the browser never receives an S4 brand or price.
- [ ] Naming/pricing is driven by a per-tenant PublicBookingConfig, shared with PRD-07 BOOKING-PAGE.

## UI designs / screenshots

- Prototype: public booking widget (booking-widget.png) — 'What can we help with?' service list with generic display names; S4 services tagged 'Consultation required' and shown price-free, 'Pricing is confirmed privately with your practitioner'.
- S4 cards never show a brand name or price; non-S4 services may show price per config.
- The public-booking.png 'Compliant by configuration' panel reflects: generic names, withheld prices, S4 always price-free + 'consultation required'.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **PublicBookingConfig** — tenant_id, generic_names(bool), withhold_s4_prices(bool), display_name_overrides(map), embed_token
  - _Drives naming/pricing per C9 (shared with PRD-07 BOOKING-PAGE); a config setting, not a linter._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Server-side public sanitisation (generic names, withheld S4 prices)**
  Behaviour: the public service list returns generic-named cards; S4 (Schedule 4 prescription-only medicine) services carry a 'Consultation required' tag, no price, and 'Pricing is confirmed privately with your practitioner' copy. Requirements: read PublicBookingConfig (generic_names, display_name_overrides, withhold_s4_prices); the server returns ALREADY-SANITISED data so the browser never receives an S4 brand or price (C9, a configuration policy not an advertising linter); only bookable services appear.
