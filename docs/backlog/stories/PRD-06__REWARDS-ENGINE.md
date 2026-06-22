# Rewards engine — non-S4 only

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REWARDS-ENGINE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a client, I want to earn and redeem rewards on non-S4 items only, so that I'm rewarded without breaching S4 advertising rules.
What this is, plainly: the loyalty rules — points and perks earned and spent — built so they can never touch a prescription injectable. Where it sits: it depends on the PRD-04 product catalogue's schedule flag and underpins later loyalty work; it lives in the Payments/commerce layer after the clinical core. Visit-based + membership rewards that the engine blocks from ever applying to S4 (Schedule 4 prescription-only medicine) items; configuring an S4 reward is blocked (REQ-MEMB-4/5/7, C9/ADR-0014).

## How it works

Two reward bases: visit-based (milestones / every-Nth-visit) and membership/frequency perks. Earning and redemption produce a RewardLedger entry per client (earned / redeemed / balance). The catalog schedule flag (PRD-04, ADR-0014) is the single source of truth for eligibility: a RewardRule's eligible_items are constrained to non-S4, and at checkout the engine recomputes eligibility server-side against the live line's schedule — an S4 line is inert (its reward/points control is disabled with a tooltip).
The S4 block is a server-side invariant, not a UI nicety: attempting to configure a reward whose eligible items include an S4 service is rejected with a clear reason; attempting to earn/redeem/discount against an S4 line at checkout is refused. The loyalty screen states it plainly — 'Points never earn or redeem on S4 medicines — enforced at checkout.'
Defaults match the prototype: earn 1 pt / $1 on non-S4; redeem 200 pts = $20 off non-S4; tiers Silver / Gold / Platinum; top point balances are visible to staff.

## Requirements

- To earn and redeem rewards on non-S4 items only.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Visit-based rewards (milestones / every-Nth-visit) and membership perks apply to non-S4 items, add-ons or account/gift credit.
- [ ] The engine refuses to earn, redeem or discount against any S4-flagged item (server-side invariant, re-checked at checkout).
- [ ] Attempting to configure a reward whose eligible items include an S4 item is blocked with a clear reason.
- [ ] The catalog schedule flag (PRD-04/ADR-0014) drives eligibility; earn/redeem land in the RewardLedger.

## UI designs / screenshots

- Prototype: Memberships -> Loyalty — Points program (Earn '1 pt / $1 on non-S4', Redeem '200 pts = $20 off non-S4'), Tiers 'Silver · Gold · Platinum', the rule note 'Points never earn or redeem on S4 medicines — enforced at checkout', and Top balances.
- S4 catalog items show disabled reward/discount controls with a tooltip; earn/redeem also visible on Client 360 + client-app Rewards.

![memb-loyalty — prototype screen](../screens/memb-loyalty.png)

## Suggested data model

- **RewardRule** — id, tenant_id, basis(milestone|nth_visit|membership), eligible_items(non-S4 only), value_cap, reward_kind(discount|addon|credit)
  - _S4 eligibility blocked at config time (C9/ADR-0014)._
- **RewardLedger** — id, client_id, earned, redeemed, balance, ref(invoice|visit)
  - _Non-S4 redemptions only; feeds Client 360 + client-app Rewards._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Points program: earn + redeem (non-S4) into the RewardLedger**
  Behaviour: clients earn points on completed non-S4 spend (default 1 pt / $1) and visit milestones, and redeem them against non-S4 lines (default 200 pts = $20 off non-S4); earn/redeem land in a per-client RewardLedger (earned / redeemed / balance) with a ref to the originating invoice/visit. Requirements: redemption only ever discounts a non-S4 line; the ledger surfaces on the Client 360 and the client-app Rewards; defaults match the prototype but are configurable.
- [ ] **Tiers (Silver / Gold / Platinum) + top balances**
  Behaviour: clients are banded into loyalty tiers (Silver · Gold · Platinum) by their balance/activity, and the Loyalty screen shows a 'Top balances' list (e.g. 'Amelia Ross 1,240 pts'). Requirements: tier thresholds are owner-configurable; tier is derived from the ledger; top-balance visibility is a staff read (no money figures, so not .fin-gated, but client PII access is audited).
- [ ] **S4 reward block at config time (C9 invariant)**
  Behaviour: a RewardRule's eligible_items reference catalogue items; attempting to add an S4 (Schedule 4 prescription-only medicine) item to a rule's eligible set is rejected with a clear blocked-action reason (what's blocked / which item / why). Requirements: enforce as a DB/domain constraint AND at the API — not a UI nicety; the schedule flag (PRD-04/ADR-0014) is the source of truth; the loyalty screen states 'Points never earn or redeem on S4 medicines — enforced at checkout'; audit the block (ADR-0010).
- [ ] **S4 reward block at checkout (live schedule re-check) + audit**
  Behaviour: at checkout the engine recomputes eligibility against the LIVE line schedule and refuses to earn, redeem or discount against any S4 line — the S4 line's reward/points control is inert/disabled with a tooltip. Requirements: never trust a cached/UI eligibility value; the refusal is server-side and returns a clear reason for the disabled control; audit both blocked attempts and successful non-S4 redemptions. This is the same invariant POS surfaces as 'S4 · no rewards'.
- [ ] **Loyalty screen UI (points program + tiers + top balances)**
  Behaviour: the Loyalty screen shows the Points program (Earn '1 pt / $1 on non-S4', Redeem '200 pts = $20 off non-S4'), Tiers (Silver · Gold · Platinum), the rule note 'Points never earn or redeem on S4 medicines — enforced at checkout', and Top balances. Requirements: earn/redeem also visible on Client 360 + client-app Rewards; S4 catalogue items render disabled reward/discount controls with a tooltip; loading/empty/error states.
