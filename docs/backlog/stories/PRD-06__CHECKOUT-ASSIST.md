# Post-visit rebooking on the treatment interval (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-ASSIST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want checkout to prompt rebooking the next visit at the right interval, so that I keep clients on cadence before they leave.
What this is, plainly: after payment, offer the next visit at the right interval — pick a slot or text the options — so the client leaves with their next appointment booked. This is the minimal end-to-end core; the subtle 'Worth mentioning' upsell panel, the client-rapport panel and the 'Pairs well with today's treatment' cross-sell are each added as their own follow-ups. Where it sits: it layers onto the POS checkout and ties out to the calendar (PRD-02) and recall (PRD-07); it sits in the Payments layer after the clinical core. Post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

## How it works

A 'Worth mentioning' panel shows subtle, derived suggestions: membership offer if not a member ('Not a member — offer Glow Club · $89/mo'), a likely retail restock ('Likely low on retinol serum — bought 10 wks ago, lasts ~8') with an 'Add restock' action, and a 'Toxin due ~now' rebook cue. A 'Pairs well with today's treatment' cross-sell row matches non-S4 aftercare/retail to what was treated, each showing its margin ('+$21 margin'). None of these ever discount or promote an S4 item.
After payment, the post-checkout rebooking view offers the next visit on the treatment interval (toxin ~12 weeks): pick a slot or 'Text her the options'; a non-S4 restock reminder can be toggled on. Booking a slot creates the appointment (PRD-02); the recall nudge ties to PRD-07. Suggestions are derived (rewards eligibility + stock ageing + treatment interval), not a stored entity.

## Requirements

- Checkout to prompt rebooking the next visit at the right interval.

## Acceptance Criteria

- [ ] After payment, a rebook view offers the next visit on the treatment interval (toxin ~12 weeks): pick a slot or 'Text her the options'.
- [ ] Booking a slot creates the appointment (PRD-02); the text/recall nudge ties to PRD-07.
- [ ] A non-S4 restock-reminder can be toggled on; no rebooking prompt discounts or promotes an S4 item.
- [ ] Slots come from the calendar availability engine (scope-aware).

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

- [ ] **Post-payment rebooking on the treatment interval**
  Behaviour: after payment, a rebook view offers the next visit on the treatment interval (toxin ~12 weeks) — a slot grid to pick a time or 'Text her the options', plus a non-S4 restock-reminder toggle. Booking a slot creates the appointment (PRD-02); the text/recall nudge ties to PRD-07. Requirements: slots come from the calendar availability engine (scope-aware); 'Text her the options' sends via INotifier (PRD-07) honouring consent; confirming sets confirmation + reminders. No S4 (Schedule 4 prescription-only medicine) discount/promotion anywhere.
