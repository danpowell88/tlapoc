# Closeout: back-office tablet surface

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT-BACKROOM`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CLOSEOUT`

## Background

As a owner, I want to run the daily closeout from the back-office tablet, so that I can balance the till away from the front desk.
Plainly: make the same daily closeout available on the back-room tablet so the owner can balance and lock the day without standing at the front desk. Where it fits: a follow-up to the basic daily closeout (PRD-06/CLOSEOUT), which renders at the checkout/desk; this surfaces the same closeout on the back-office tablet (backroom device sim), sharing one component/state. Figures are owner-gated (.fin).

## How it works

The basic closeout (PRD-06/CLOSEOUT) renders at the checkout/desk; this follow-up surfaces the same closeout on the back-office tablet (backroom) so the owner can run it away from the front desk — card vs cash totals, counted-cash entry, note + lock, close.
The back-office tablet shares the same component/state as the desk view (no divergent copy). Owner-only capability gate is enforced. Loading/empty/error states are handled.

## Requirements

- To run the daily closeout from the back-office tablet.

## Acceptance Criteria

- [ ] The closeout renders on the back-office tablet (backroom) with card/cash totals, counted-cash entry, note + lock and close.
- [ ] The back-office tablet shares the same component/state as the desk view (no divergent copy).
- [ ] Owner-only capability gate is enforced on the tablet surface (.fin).
- [ ] Loading/empty/error states are handled.

## UI designs / screenshots

- Prototype: back-office tablet (backroom) closeout surface, mirroring the desk closeout (card vs cash, counted-cash, note + lock).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(reuses PRD-06/CLOSEOUT)** — same Closeout entity, rendered on the backroom surface
  - _No new entity; shared component/state with the desk view._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Back-office tablet closeout surface (shared component/state)**
  Behaviour: render the closeout on the back-office tablet (backroom) sharing the same component/state as the desk view. Requirements: owner-only capability gate; loading/empty/error states; no divergent copy of the closeout logic.
