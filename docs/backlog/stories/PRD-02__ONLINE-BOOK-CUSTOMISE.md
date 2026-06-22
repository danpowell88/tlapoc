# Online self-booking: owner customise & embed panel

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/ONLINE-BOOK-CUSTOMISE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a owner, I want to customise and embed the public booking widget and see its compliance posture at a glance, so that the booking page matches our brand and I can confirm it's compliant by configuration.
Plainly: the owner-facing view that brands, configures and embeds the public booking widget, with a 'Compliant by configuration' summary. Where it fits: a follow-up to online self-booking basic (PRD-02/ONLINE-BOOK) that adds the owner customise/embed surface. It writes the per-tenant PublicBookingConfig (including the embed token) — the same policy the generic-names follow-up (PRD-02/ONLINE-BOOK-GENERIC-NAMES) and the PRD-07 public booking page share. It is capability-gated to the owner and sits in Reception (PRD-02).

## How it works

The basic online flow is the client-facing wizard; this follow-up adds the OWNER-facing view that brands and embeds it. The owner sets the brand colour, clinic name and which services appear, and obtains an embed token for the embeddable widget.
Alongside customisation sits a 'Compliant by configuration' summary that states the public surface's posture: generic names, withheld prices, S4 always price-free and 'consultation required', and 'no deposit / card on file in v1'. It reassures the owner that compliance is achieved by configuration, not manual policing.
The panel writes the per-tenant PublicBookingConfig (including embed_token) — the same policy object the generic-names follow-up and the PRD-07 public booking page read — so naming/pricing/embedding are configured in one place. The view is capability-gated to the owner.

## Requirements

- To customise and embed the public booking widget and see its compliance posture at a glance.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The owner can customise the widget (brand colour, clinic name, service selection) and obtain an embed token.
- [ ] A 'Compliant by configuration' summary shows generic names, withheld prices, S4 always price-free + 'consultation required', and 'no deposit / card on file in v1'.
- [ ] The panel writes PublicBookingConfig (incl. embed_token), shared policy with PRD-07 BOOKING-PAGE.
- [ ] The customise panel is capability-gated to owner.

## UI designs / screenshots

- Prototype: the embeddable/customise view (public-booking.png) — brand colour, clinic name, service selection, and the embeddable widget controls.
- The 'Compliant by configuration' panel: generic names, withheld prices, S4 always price-free + 'consultation required', and 'no deposit / card on file in v1'.
- Capability-gated to owner; produces the embed token for the widget.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **PublicBookingConfig (extends ONLINE-BOOK-GENERIC-NAMES)** — tenant_id, brand_colour, clinic_name, service_selection[], embed_token (+ generic_names / withhold_s4_prices / display_name_overrides)
  - _The owner customise panel writes this config (incl. embed_token); shared policy with PRD-07 BOOKING-PAGE._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Owner customise/embed panel ('Compliant by configuration')**
  Behaviour: the owner-facing embed/customise view (brand colour, clinic name, service selection) plus the 'Compliant by configuration' summary — generic names, withheld prices, S4 (Schedule 4 prescription-only medicine) always price-free + 'consultation required', 'no deposit / card on file in v1'. Requirements: writes PublicBookingConfig (incl. embed_token for the embeddable widget); shared policy with PRD-07 BOOKING-PAGE; capability-gated to owner.
