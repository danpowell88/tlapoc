# Checkout assist & post-visit rebooking

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-ASSIST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval, so that I help clients and keep them on cadence.
What this is, plainly: gentle, rules-safe prompts at the till — a quiet membership or restock nudge, a one-line rapport cue, and an offer to rebook the next visit at the right interval. Where it sits: it layers onto the POS checkout and ties out to the calendar (PRD-02) and recall (PRD-07); it sits in the Payments layer after the clinical core. Subtle membership/restock upsell + client rapport panel + post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

## How it works

A 'Worth mentioning' panel shows subtle, derived suggestions: membership offer if not a member ('Not a member — offer Glow Club · $89/mo'), a likely retail restock ('Likely low on retinol serum — bought 10 wks ago, lasts ~8') with an 'Add restock' action, and a 'Toxin due ~now' rebook cue. A 'Pairs well with today's treatment' cross-sell row matches non-S4 aftercare/retail to what was treated, each showing its margin ('+$21 margin'). None of these ever discount or promote an S4 item.
After payment, the post-checkout rebooking view offers the next visit on the treatment interval (toxin ~12 weeks): pick a slot or 'Text her the options'; a non-S4 restock reminder can be toggled on. Booking a slot creates the appointment (PRD-02); the recall nudge ties to PRD-07. Suggestions are derived (rewards eligibility + stock ageing + treatment interval), not a stored entity.

## Requirements

- Checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval.

## Acceptance Criteria

- [ ] Checkout shows a subtle 'Worth mentioning' upsell (membership/restock) and a client-rapport panel derived from history.
- [ ] A non-S4 'Pairs well with today's treatment' cross-sell row matches aftercare/retail to the cart, showing margin.
- [ ] Post-checkout rebooking is offered on the treatment interval (slot pick or text options); booking creates the appointment (PRD-02).
- [ ] No upsell or cross-sell discounts or promotes an S4 item.

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout 'Worth mentioning' panel (Glow Club offer / retinol restock with 'Add restock' / 'Toxin due ~now'); 'Pairs well with today's treatment' cards with margin + 'Add'; post-payment rebook view (slot grid, 'Text her the options', restock reminder toggle).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived) CheckoutSuggestion** — from RewardRule eligibility + stock ageing + treatment interval + membership status
  - _Non-S4 upsell/cross-sell only; rebook -> Appointment (PRD-02), recall -> PRD-07._

## Technical notes (high level)

- Architecture decisions: [ADR-0022](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **'Worth mentioning' upsell panel (membership / restock / rebook cue)**
  Behaviour: a subtle 'Worth mentioning' panel surfaces derived prompts at the till — a membership offer if the client isn't a member ('Not a member — offer Glow Club · $89/mo') with an 'Add to sale' action, a likely retail restock ('Likely low on retinol serum — bought 10 wks ago, lasts ~8') with an 'Add restock' action, and a 'Toxin due ~now' rebook cue. Requirements: suggestions are derived (membership status + stock ageing + treatment interval), computed server-side; the copy is a quiet staff nudge ('suggest, don't push'); none of these ever discount or promote an S4 (Schedule 4 prescription-only medicine) item.
- [ ] **Client-rapport panel (derived from history)**
  Behaviour: a one-line rapport panel derived from the client record — preferences ('Natural finish · a chamomile tea on arrival'), recent treatments, and a connection cue ('Birthday in 12 days · referred by Hannah L.') — to help the desk personalise. Requirements: read-only, derived from the Client 360; no money figures; respects RBAC (no clinical detail beyond what reception may see).
- [ ] **'Pairs well with today's treatment' non-S4 cross-sell**
  Behaviour: a cross-sell row matches non-S4 aftercare/retail to what was treated (toxin → arnica/recovery serum; filler → lip balm; skin → SPF/HA serum; etc.), each card showing price, margin (e.g. '+$21 margin') and an 'Add' action that appends the line to the cart. Requirements: matched from cart signals server-side; S4 (Schedule 4 prescription-only medicine) items are suppressed entirely; margin figures are owner-relevant but shown to the desk as a selling aid (no daily-takings exposure); empty state when the cart already covers aftercare.
- [ ] **Post-payment rebooking on the treatment interval**
  Behaviour: after payment, a rebook view offers the next visit on the treatment interval (toxin ~12 weeks) — a slot grid to pick a time or 'Text her the options', plus a non-S4 restock-reminder toggle. Booking a slot creates the appointment (PRD-02); the text/recall nudge ties to PRD-07. Requirements: slots come from the calendar availability engine (scope-aware); 'Text her the options' sends via INotifier (PRD-07) honouring consent; confirming sets confirmation + reminders. No S4 discount/promotion anywhere.
