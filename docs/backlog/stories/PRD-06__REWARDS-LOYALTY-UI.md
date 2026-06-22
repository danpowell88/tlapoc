# Rewards: Loyalty screen UI

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REWARDS-LOYALTY-UI`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/REWARDS-ENGINE`

## Background

As a owner / front desk, I want a Loyalty screen showing the points program, tiers and top balances, so that staff can see and explain the loyalty programme at a glance.
Plainly: the screen that lays out the points programme (earn/redeem rules), the tiers and the top balances, with the rule note that points never touch S4. Where it fits: a follow-up to the rewards engine core (PRD-06/REWARDS-ENGINE) and the tiers follow-up (PRD-06/REWARDS-TIERS); it presents what those produce. It also makes the S4 (Schedule 4 prescription-only medicine) block visible — S4 catalogue items render disabled reward/discount controls with a tooltip — and the earn/redeem is also visible on the Client 360 and client-app Rewards.

## How it works

The Loyalty screen shows the Points program (Earn '1 pt / $1 on non-S4', Redeem '200 pts = $20 off non-S4'), Tiers (Silver · Gold · Platinum), the rule note 'Points never earn or redeem on S4 medicines — enforced at checkout', and Top balances. It presents what PRD-06/REWARDS-ENGINE and PRD-06/REWARDS-TIERS produce.
S4 (Schedule 4 prescription-only medicine) catalogue items render disabled reward/discount controls with a tooltip — the visible face of the engine's invariant. Earn/redeem is also visible on the Client 360 and the client-app Rewards. Loading/empty/error states handled.

## Requirements

- A Loyalty screen showing the points program, tiers and top balances.

## Acceptance Criteria

- [ ] The Loyalty screen shows the Points program (Earn '1 pt / $1 on non-S4', Redeem '200 pts = $20 off non-S4'), Tiers (Silver · Gold · Platinum) and Top balances.
- [ ] The rule note 'Points never earn or redeem on S4 medicines — enforced at checkout' is shown.
- [ ] S4 (Schedule 4 prescription-only medicine) catalogue items render disabled reward/discount controls with a tooltip.
- [ ] Earn/redeem is also visible on the Client 360 and client-app Rewards; loading/empty/error states handled.

## UI designs / screenshots

- Prototype: Memberships → Loyalty — Points program (Earn '1 pt / $1 on non-S4', Redeem '200 pts = $20 off non-S4'), Tiers 'Silver · Gold · Platinum', the rule note 'Points never earn or redeem on S4 medicines — enforced at checkout', and Top balances; S4 catalogue items show disabled reward/discount controls with a tooltip; earn/redeem also on Client 360 + client-app Rewards.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(read-only over PRD-06/REWARDS-ENGINE + REWARDS-TIERS)** — renders points program, tiers and top balances
  - _No new entity; presentation only._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Loyalty screen UI (points program + tiers + top balances + S4 note)**
  Behaviour: render the Points program (earn/redeem rules), Tiers (Silver/Gold/Platinum), Top balances and the 'Points never earn or redeem on S4 medicines — enforced at checkout' note. Requirements: S4 (Schedule 4 prescription-only medicine) catalogue items render disabled reward/discount controls with a tooltip; earn/redeem also visible on Client 360 + client-app Rewards; loading/empty/error states.
