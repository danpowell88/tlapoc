# Membership: benefits & credits auto-apply at checkout (non-S4)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-BENEFITS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a front desk, I want a member's benefits and credits to apply automatically at the till, so that members get their perks without manual entry and never on an S4 item.
Plainly: when a member checks out, their plan's perks — member pricing, 10% off non-S4, a periodic complimentary add-on — apply themselves as deduction lines, and never touch a prescription injectable. Where it fits: a follow-up to the basic membership enrolment (PRD-06/MEMBERSHIP) that connects a member's plan benefits to the till; it surfaces through the checkout deduction lines (PRD-06/POS-DEDUCTIONS) and reads the per-plan benefit set from PRD-06/MEMBERSHIP-PLANS. Benefits NEVER apply to an S4 (Schedule 4 prescription-only medicine) line (C9), re-checked server-side. Money figures owner-gated (.fin).

## How it works

A member's benefits and credits apply automatically at the till — member pricing, 10% off non-S4, periodic complimentary add-on — appearing as deduction lines on the sale (surfaced via PRD-06/POS-DEDUCTIONS). Benefits NEVER apply to an S4 (Schedule 4 prescription-only medicine) line (C9) — re-checked server-side against the live line schedule.
The per-plan benefit set is defined by the plan (PRD-06/MEMBERSHIP-PLANS). This extends the basic membership enrolment (PRD-06/MEMBERSHIP). Money figures owner-gated (.fin).

## Requirements

- A member's benefits and credits to apply automatically at the till.

## Acceptance Criteria

- [ ] A member's benefits and credits apply automatically at the till — member pricing, 10% off non-S4, periodic complimentary add-on — as deduction lines on the sale.
- [ ] Benefits NEVER apply to an S4 (Schedule 4 prescription-only medicine) line (C9), re-checked server-side against the live line schedule.
- [ ] The per-plan benefit set is defined by the plan (PRD-06/MEMBERSHIP-PLANS).
- [ ] Money figures owner-gated (.fin).

## UI designs / screenshots

- Prototype: Checkout — member benefit/credit deduction lines (non-S4); the per-plan benefit set comes from PRD-06/MEMBERSHIP-PLANS.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(reads PRD-06/MEMBERSHIP-PLANS, writes via PRD-06/POS-DEDUCTIONS)** — benefit set per plan → deduction lines at checkout
  - _No new entity; non-S4 only (C9), re-checked server-side._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Auto-apply plan benefits/credits at checkout (non-S4, C9)**
  Behaviour: a member's plan benefits (member pricing, 10% off non-S4, periodic complimentary add-on) auto-apply as deduction lines at the till. Requirements: NEVER on an S4 (Schedule 4 prescription-only medicine) line (C9), re-checked server-side; benefit set from PRD-06/MEMBERSHIP-PLANS; surfaced via PRD-06/POS-DEDUCTIONS; owner-only (.fin).
