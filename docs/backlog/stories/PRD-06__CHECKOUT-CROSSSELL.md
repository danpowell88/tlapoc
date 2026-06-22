# Checkout: 'Pairs well with today's treatment' non-S4 cross-sell

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-CROSSSELL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CHECKOUT-ASSIST`

## Background

As a front desk, I want a cross-sell row matching non-S4 aftercare/retail to what was treated, so that I can suggest relevant add-ons that suit the visit.
Plainly: a row of suggested non-S4 aftercare/retail that pairs with the treatment just done — toxin pairs with a recovery serum, skin with SPF — each with an 'Add' to drop it into the cart. Where it fits: a follow-up to the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST) that adds matched cross-sell. Matches are computed server-side from cart signals; S4 (Schedule 4 prescription-only medicine) items are suppressed entirely; margin is shown to the desk as a selling aid (no daily-takings exposure).

## How it works

A cross-sell row matches non-S4 aftercare/retail to what was treated (toxin → arnica/recovery serum; filler → lip balm; skin → SPF/HA serum; etc.), each card showing price, margin (e.g. '+$21 margin') and an 'Add' action that appends the line to the cart.
Matched from cart signals server-side; S4 (Schedule 4 prescription-only medicine) items are suppressed entirely; margin figures are owner-relevant but shown to the desk as a selling aid (no daily-takings exposure); an empty state shows when the cart already covers aftercare. This extends the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST).

## Requirements

- A cross-sell row matching non-S4 aftercare/retail to what was treated.

## Acceptance Criteria

- [ ] A 'Pairs well with today's treatment' row matches non-S4 aftercare/retail to what was treated (toxin → arnica/recovery serum; filler → lip balm; skin → SPF/HA serum).
- [ ] Each card shows price, margin (e.g. '+$21 margin') and an 'Add' action that appends the line to the cart.
- [ ] Matches are computed server-side from cart signals; S4 (Schedule 4 prescription-only medicine) items are suppressed entirely.
- [ ] An empty state shows when the cart already covers aftercare; margin figures are a selling aid, not daily-takings exposure.

## UI designs / screenshots

- Prototype: Checkout 'Pairs well with today's treatment' cards with margin + 'Add'.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived CheckoutSuggestion, extends PRD-06/CHECKOUT-ASSIST)** — matched from cart signals → non-S4 aftercare/retail with margin
  - _Non-S4 cross-sell only; S4 suppressed; derived, not stored._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **'Pairs well with today's treatment' non-S4 cross-sell**
  Behaviour: a cross-sell row matches non-S4 aftercare/retail to what was treated, each card showing price, margin and an 'Add'. Requirements: matched from cart signals server-side; S4 (Schedule 4 prescription-only medicine) items suppressed entirely; margin shown as a selling aid (no daily-takings exposure); empty state when the cart already covers aftercare.
