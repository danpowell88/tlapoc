# Checkout: 'Worth mentioning' upsell panel (membership / restock / rebook cue)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-UPSELL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CHECKOUT-ASSIST`

## Background

As a front desk, I want a subtle prompt panel at the till for membership, restock and rebook cues, so that I can nudge relevant non-S4 offers without being pushy.
Plainly: a quiet 'Worth mentioning' panel at the till that surfaces a membership offer, a likely retail restock and a rebook cue — derived from what the system already knows. Where it fits: a follow-up to the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST) that adds the suggestion panel beside it. Suggestions are derived (membership status + stock ageing + treatment interval), computed server-side; the copy is a quiet staff nudge ('suggest, don't push'); none of these ever discount or promote an S4 (Schedule 4 prescription-only medicine) item.

## How it works

A 'Worth mentioning' panel shows subtle, derived suggestions: a membership offer if not a member ('Not a member — offer Glow Club · $89/mo') with 'Add to sale', a likely retail restock ('Likely low on retinol serum — bought 10 wks ago, lasts ~8') with 'Add restock', and a 'Toxin due ~now' rebook cue.
Suggestions are derived (membership status + stock ageing + treatment interval), not a stored entity, computed server-side; the copy is a quiet staff nudge ('suggest, don't push'); none ever discount or promote an S4 (Schedule 4 prescription-only medicine) item. This extends the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST).

## Requirements

- A subtle prompt panel at the till for membership, restock and rebook cues.

## Acceptance Criteria

- [ ] A subtle 'Worth mentioning' panel shows a membership offer if the client isn't a member ('Not a member — offer Glow Club · $89/mo') with an 'Add to sale' action.
- [ ] It shows a likely retail restock ('Likely low on retinol serum — bought 10 wks ago, lasts ~8') with an 'Add restock' action, and a 'Toxin due ~now' rebook cue.
- [ ] Suggestions are derived (membership status + stock ageing + treatment interval), computed server-side.
- [ ] None of these ever discount or promote an S4 (Schedule 4 prescription-only medicine) item.

## UI designs / screenshots

- Prototype: Checkout 'Worth mentioning' panel — Glow Club offer / retinol restock with 'Add restock' / 'Toxin due ~now'.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived CheckoutSuggestion, extends PRD-06/CHECKOUT-ASSIST)** — from membership status + stock ageing + treatment interval
  - _Non-S4 upsell only; derived, not stored._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **'Worth mentioning' upsell panel (membership / restock / rebook cue)**
  Behaviour: a subtle 'Worth mentioning' panel surfaces derived prompts at the till — a membership offer if not a member ('Not a member — offer Glow Club · $89/mo') with 'Add to sale', a likely retail restock ('Likely low on retinol serum') with 'Add restock', and a 'Toxin due ~now' rebook cue. Requirements: suggestions derived (membership status + stock ageing + treatment interval), computed server-side; quiet staff-nudge copy; none ever discount/promote an S4 (Schedule 4 prescription-only medicine) item.
