# Client app: rewards, perks & referrals

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-REWARDS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CARE`, `PRD-06/MEMBERSHIP`

## Background

As a client, I want to see my points, perks and gift cards and refer a friend, so that I get the value of being a member.
Plainly: the Rewards tab of the client app — the membership card, points balance, member perks, a refer-a-friend, and gift-card redeem. Where it fits: a follow-up to the My care health hub (PRD-09/CLIENT-CARE) that adds the rewards surface; it reads the rewards/membership module (PRD-06), the client's own figures only. Rewards are never applied to S4 (Schedule 4 prescription-only medicine) — you can't discount or incentivise a prescription medicine.

## How it works

The Rewards tab shows the membership card, points balance / ledger, member perks, milestones, a give-$25/get-$25 referral with tracking, and gift-card redeem. It reads PRD-06 reward/membership data, the client's OWN figures only — never clinic revenue or another client's balances.
Rewards are never applied to S4 (Schedule 4 prescription-only medicine) medicines — you can't discount or incentivise a prescription medicine — so the engine excludes S4 lines. Redemptions post back to PRD-06, which remains the source of truth for the ledger.

## Requirements

- To see my points, perks and gift cards and refer a friend.

## Acceptance Criteria

- [ ] The Rewards tab shows the membership card, points balance / ledger, member perks, milestones, a give-$25/get-$25 referral with tracking, and gift-card redeem.
- [ ] It reads PRD-06 reward/membership data — the client's OWN figures only, never clinic revenue.
- [ ] Rewards are never applied to S4 medicines (you can't discount or incentivise a prescription medicine).
- [ ] Redemptions post back to PRD-06.

## UI designs / screenshots

- Prototype: client-app — Rewards (membership card, redeem points, perks, milestones, give-$25/get-$25 referral, gift-card redeem).
- Client's own figures only; rewards never applied to S4.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Membership/RewardLedger** — PRD-06 — membership, points/perks, referral, gift cards
  - _Extends CLIENT-CARE; client sees own figures only; rewards never applied to S4._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Rewards tab over PRD-06 (points, perks, gift cards, referrals)**
  Behaviour: the Rewards tab shows the membership card, points balance / ledger, member perks, milestones, a give-$25/get-$25 referral with tracking, and gift-card redeem. Requirements: reads PRD-06 reward/membership data, the client's OWN figures only; rewards are never applied to S4 medicines (you can't discount or incentivise a prescription medicine); redemptions post back to PRD-06.
