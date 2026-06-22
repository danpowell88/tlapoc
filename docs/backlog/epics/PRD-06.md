# PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards

> **Stage / Milestone:** M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10)  ·  **Phase:** 1  ·  **Stories:** 10

Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law. Financials stay owner-only; the ledger defers to Xero.

**Source PRD:** `docs/prds/PRD-06-payments-memberships-rewards.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `PAYMENT-PROVIDER` | [Payment provider abstraction + Square adapter](../stories/PRD-06__PAYMENT-PROVIDER.md) | Story | P0 | 5 | 3 |
| `POS` | [In-person POS checkout (card + cash)](../stories/PRD-06__POS.md) | Story | P0 | 5 | 3 |
| `PACKAGES-GIFT` | [Packages/series, gift cards & client balances](../stories/PRD-06__PACKAGES-GIFT.md) | Story | P1 | 3 | 3 |
| `CLOSEOUT` | [Daily closeout & reconciliation](../stories/PRD-06__CLOSEOUT.md) | Story | P1 | 3 | 3 |
| `MEMBERSHIP` | [Memberships with automatic autopay & dunning](../stories/PRD-06__MEMBERSHIP.md) | Story | P0 | 5 | 2 |
| `REWARDS-ENGINE` | [Rewards engine — non-S4 only](../stories/PRD-06__REWARDS-ENGINE.md) | Story | P0 | 5 | 3 |
| `MARGIN-RULES` | [Margin-aware reward rules](../stories/PRD-06__MARGIN-RULES.md) | Story | P1 | 3 | 3 |
| `CHECKOUT-ASSIST` | [Checkout assist & post-visit rebooking](../stories/PRD-06__CHECKOUT-ASSIST.md) | Story | P2 | 2 | 1 |
| `PRICING-WHATIF` | [Pricing & what-if planning (owner)](../stories/PRD-06__PRICING-WHATIF.md) | Story | P2 | 2 | 3 |
| `REFERRALS` | [Referrals & affiliate credit (non-S4) (placeholder)](../stories/PRD-06__REFERRALS.md) | Story | P2 | 1 | 1 |

_Totals: 10 stories · 25 tasks._
