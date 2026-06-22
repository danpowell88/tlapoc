# Checkout: member-reward & store-credit deduction lines (non-S4)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS-DEDUCTIONS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want member rewards and store credit to appear as deduction lines on the sale, so that members get their benefit automatically without ever touching an S4 item.
Plainly: when a member checks out, show their reward (10% off non-S4) and any store credit as their own negative lines under the cart, reducing the total. Where it fits: a follow-up to the basic in-person POS checkout (PRD-06/POS) that adds the deduction lines a member sees; the basic slice has no deductions. The reward is computed only on the non-S4 subtotal — it must NEVER reduce an S4 (Schedule 4 prescription-only medicine) line (C9) — and store credit draws from the client AccountBalance (PRD-06/PACKAGES-GIFT). All figures here are sale-level (Reception may see them); owner-only takings/margin read-models stay behind .fin.

## How it works

When the client is a member, a 'Member reward — 10% off non-S4' line and a 'Store credit applied' line appear as their own negative deduction rows beneath the cart, reducing the total. The reward is computed only on the non-S4 subtotal (S4 lines excluded, C9 — re-checked server-side against the live line schedule, never trusting a UI value); store credit draws from the client AccountBalance (PRD-06/PACKAGES-GIFT). Deductions recompute live as lines change; non-members see neither.
This extends the basic checkout (PRD-06/POS) and reads the rewards/benefit rules from PRD-06/REWARDS-ENGINE and PRD-06/MEMBERSHIP. All money figures shown here are sale-level (Reception may see them); owner-only read-models (takings/margin) stay behind .fin.

## Requirements

- Member rewards and store credit to appear as deduction lines on the sale.

## Acceptance Criteria

- [ ] For a member, a 'Member reward — 10% off non-S4' line and a 'Store credit applied' line appear as negative deduction rows beneath the cart.
- [ ] The reward is computed only on the non-S4 subtotal; S4 (Schedule 4 prescription-only medicine) lines are excluded (C9), re-checked server-side.
- [ ] Store credit draws from the client AccountBalance (PRD-06/PACKAGES-GIFT); deductions recompute live as lines change.
- [ ] Non-members see neither line; money figures shown are sale-level (owner-only takings/margin stay behind .fin).

## UI designs / screenshots

- Prototype: Checkout — 'Member reward — 10% off non-S4' and 'Store credit applied' negative deduction rows beneath the line list, above the totals strip.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Invoice (extends PRD-06/POS)** — + deductions[]{kind(reward|credit), amount}
  - _Deductions only on non-S4 subtotal (C9); store credit reads AccountBalance (PRD-06/PACKAGES-GIFT)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Member-reward deduction line (non-S4 subtotal only, C9)**
  Behaviour: a member's reward (default 10% off non-S4) appears as a negative deduction line computed only on the non-S4 subtotal. Requirements: S4 (Schedule 4 prescription-only medicine) lines are excluded server-side against the live schedule (C9); recomputes as lines change; non-members see no line; rule comes from PRD-06/REWARDS-ENGINE / MEMBERSHIP.
- [ ] **Store-credit deduction line (draws AccountBalance)**
  Behaviour: available store credit appears as a 'Store credit applied' negative line and decrements the client AccountBalance on completion. Requirements: credit reads/writes AccountBalance (PRD-06/PACKAGES-GIFT); deductions recompute live; figures sale-level, owner-only takings/margin behind .fin.
