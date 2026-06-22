# Rewards: loyalty tiers (Silver / Gold / Platinum) + top balances

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REWARDS-TIERS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/REWARDS-ENGINE`

## Background

As a owner, I want clients banded into loyalty tiers and a view of the top point balances, so that loyalty is recognised by tier and the desk can see the clinic's best clients.
Plainly: group clients into tiers (Silver / Gold / Platinum) based on their points, and show a 'top balances' list. Where it fits: a follow-up to the rewards engine core (PRD-06/REWARDS-ENGINE), which runs points earn/redeem into the RewardLedger; this derives tiers and a top-balances view from that ledger. Tier thresholds are owner-configurable; tier is derived (not stored on the client). Top-balance visibility is a staff read with no money figures (so not .fin-gated), but client PII (personally identifiable information) access is audited.

## How it works

Clients are banded into loyalty tiers (Silver · Gold · Platinum) by their balance/activity, derived from the per-client RewardLedger (PRD-06/REWARDS-ENGINE). Tier thresholds are owner-configurable; tier is derived, not stored on the client.
The Loyalty surface shows a 'Top balances' list (e.g. 'Amelia Ross 1,240 pts'). Top-balance visibility is a staff read — no money figures, so not .fin-gated — but client PII (personally identifiable information) access is audited. This extends the rewards engine core (PRD-06/REWARDS-ENGINE).

## Requirements

- Clients banded into loyalty tiers and a view of the top point balances.

## Acceptance Criteria

- [ ] Clients are banded into loyalty tiers (Silver · Gold · Platinum) derived from their balance/activity.
- [ ] Tier thresholds are owner-configurable; tier is derived from the RewardLedger, not stored separately.
- [ ] A 'Top balances' list shows the highest point balances (e.g. 'Amelia Ross 1,240 pts').
- [ ] Top-balance visibility is a staff read (no money figures); client PII (personally identifiable information) access is audited.

## UI designs / screenshots

- Prototype: Memberships → Loyalty — Tiers 'Silver · Gold · Platinum' and a Top balances list (e.g. 'Amelia Ross 1,240 pts').

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived over PRD-06/REWARDS-ENGINE RewardLedger)** — tier = f(balance, owner-configured thresholds); top-balances = ranked ledger balances
  - _No new entity; tier derived, not stored; PII access audited._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Tier derivation (configurable thresholds) + top-balances query**
  Behaviour: derive a client's tier (Silver/Gold/Platinum) from their RewardLedger balance against owner-configurable thresholds; expose a top-balances ranked query. Requirements: tier derived, not stored; thresholds owner-configurable; client PII (personally identifiable information) access audited; no money figures so not .fin-gated.
