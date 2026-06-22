# Checkout assist & post-visit rebooking

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-ASSIST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval, so that I help clients and keep them on cadence.
Subtle membership/restock upsell + client rapport panel + post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

## How it works

At checkout, a subtle membership/restock upsell + a client-rapport panel, and a post-checkout rebooking prompt on the treatment interval. Upsell suggestions never include S4 discounting.
Helps the desk add value and keep clients on cadence; integrates with the calendar (PRD-02) and recall (PRD-07).

## Requirements

- Checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval.

## Acceptance Criteria

- [ ] Checkout shows a subtle membership/restock upsell and a client rapport panel.
- [ ] Post-checkout rebooking is offered on the treatment interval.
- [ ] Upsell suggestions never include S4 discounting.
- [ ] Rebooking integrates with the calendar (PRD-02) and recall (PRD-07).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout (checkout.png) — a subtle upsell card (e.g. 'Slow-moving retail: bundle SPF with facials'), a client-rapport panel, and a rebook prompt at the interval after payment.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived) CheckoutSuggestion** — from RewardRule + stock aging + treatment interval
  - _Non-S4 upsell only; rebook -> Appointment (PRD-02)._

## Technical notes (high level)

- Architecture decisions: [ADR-0022](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Web UI**
  Build on the Angular web app: the checkout per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Checkout (checkout.png) — a subtle upsell card (e.g. 'Slow-moving retail: bundle SPF with facials'), a client-rapport panel, and a rebook prompt at the interval after payment.
