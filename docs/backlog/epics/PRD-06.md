# PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards

> **Stage / Milestone:** M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10)  ·  **Phase:** 1  ·  **Stories:** 37

Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law. Financials stay owner-only; the ledger defers to Xero.

**Source PRD:** `docs/prds/PRD-06-payments-memberships-rewards.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `PAYMENT-PROVIDER` | [Payment provider abstraction + Square adapter](../stories/PRD-06__PAYMENT-PROVIDER.md) | Story | P0 | 5 | 3 |
| `POS` | [In-person POS checkout — basic cart + single tender (core)](../stories/PRD-06__POS.md) | Story | P0 | 5 | 4 |
| `POS-GST` | [Checkout: per-line GST (goods and services tax)](../stories/PRD-06__POS-GST.md) | Story | P2 | 2 | 2 |
| `POS-SPLIT-TENDER` | [Checkout: split / partial tenders, tips & card surcharge](../stories/PRD-06__POS-SPLIT-TENDER.md) | Story | P2 | 2 | 2 |
| `POS-DEDUCTIONS` | [Checkout: member-reward & store-credit deduction lines (non-S4)](../stories/PRD-06__POS-DEDUCTIONS.md) | Story | P2 | 2 | 2 |
| `POS-TERMINAL-MODAL` | [Checkout: Square-terminal modal (Processing → Approved) + decline path](../stories/PRD-06__POS-TERMINAL-MODAL.md) | Story | P2 | 2 | 2 |
| `POS-XERO-POST` | [Checkout: post completed sale to Xero (per-line tax mapping)](../stories/PRD-06__POS-XERO-POST.md) | Story | P2 | 2 | 2 |
| `PACKAGES-GIFT` | [Packages/series: sell & redeem (visits remaining) — basic pre-paid value (core)](../stories/PRD-06__PACKAGES-GIFT.md) | Story | P1 | 3 | 2 |
| `PACKAGES-GIFTCARD` | [Gift cards: issue, balance-track & partial redeem](../stories/PRD-06__PACKAGES-GIFTCARD.md) | Story | P2 | 2 | 2 |
| `PACKAGES-CREDIT-AR` | [Client store-credit & AR (accounts receivable) ageing](../stories/PRD-06__PACKAGES-CREDIT-AR.md) | Story | P2 | 2 | 2 |
| `CLOSEOUT` | [Daily closeout — card + cash rollup, count & lock (core)](../stories/PRD-06__CLOSEOUT.md) | Story | P1 | 3 | 3 |
| `CLOSEOUT-VARIANCE` | [Closeout: Square-batch variance detection & annotation](../stories/PRD-06__CLOSEOUT-VARIANCE.md) | Story | P2 | 2 | 2 |
| `CLOSEOUT-XERO-RECONCILE` | [Closeout: reconcile to the Xero posting](../stories/PRD-06__CLOSEOUT-XERO-RECONCILE.md) | Story | P2 | 2 | 1 |
| `CLOSEOUT-BACKROOM` | [Closeout: back-office tablet surface](../stories/PRD-06__CLOSEOUT-BACKROOM.md) | Story | P2 | 2 | 1 |
| `MEMBERSHIP` | [Membership join + card-on-file — basic enrolment (core)](../stories/PRD-06__MEMBERSHIP.md) | Story | P0 | 5 | 2 |
| `MEMBERSHIP-AUTOPAY` | [Membership: autopay scheduler (off-session recurring charge)](../stories/PRD-06__MEMBERSHIP-AUTOPAY.md) | Story | P2 | 2 | 1 |
| `MEMBERSHIP-DUNNING` | [Membership: failed-payment dunning (retry-and-chase) + manual Retry](../stories/PRD-06__MEMBERSHIP-DUNNING.md) | Story | P2 | 2 | 2 |
| `MEMBERSHIP-LIFECYCLE` | [Membership: lifecycle (pause / cancel / win-back) → MRR/churn](../stories/PRD-06__MEMBERSHIP-LIFECYCLE.md) | Story | P2 | 2 | 1 |
| `MEMBERSHIP-BENEFITS` | [Membership: benefits & credits auto-apply at checkout (non-S4)](../stories/PRD-06__MEMBERSHIP-BENEFITS.md) | Story | P2 | 2 | 1 |
| `MEMBERSHIP-MEMBERS` | [Membership: members & billing list + overview KPIs](../stories/PRD-06__MEMBERSHIP-MEMBERS.md) | Story | P2 | 2 | 2 |
| `MEMBERSHIP-PLANS` | [Membership plans & tiers — define plans + non-S4 benefit constraint (core)](../stories/PRD-06__MEMBERSHIP-PLANS.md) | Story | P1 | 3 | 2 |
| `MEMBERSHIP-PLANS-ADMIN` | [Membership plans: capability-gated admin, audit & member-term preservation](../stories/PRD-06__MEMBERSHIP-PLANS-ADMIN.md) | Story | P2 | 2 | 1 |
| `MEMBERSHIP-PLANS-UI` | [Membership plans: Plans & packages tab UI (tier cards + per-tier MRR)](../stories/PRD-06__MEMBERSHIP-PLANS-UI.md) | Story | P2 | 2 | 1 |
| `REWARDS-ENGINE` | [Rewards engine — non-S4 points earn/redeem + S4 block (core)](../stories/PRD-06__REWARDS-ENGINE.md) | Story | P0 | 5 | 3 |
| `REWARDS-TIERS` | [Rewards: loyalty tiers (Silver / Gold / Platinum) + top balances](../stories/PRD-06__REWARDS-TIERS.md) | Story | P2 | 2 | 1 |
| `REWARDS-LOYALTY-UI` | [Rewards: Loyalty screen UI](../stories/PRD-06__REWARDS-LOYALTY-UI.md) | Story | P2 | 2 | 1 |
| `MARGIN-RULES` | [Margin-aware reward rules](../stories/PRD-06__MARGIN-RULES.md) | Story | P1 | 3 | 3 |
| `CHECKOUT-ASSIST` | [Post-visit rebooking on the treatment interval (core)](../stories/PRD-06__CHECKOUT-ASSIST.md) | Story | P2 | 2 | 1 |
| `CHECKOUT-UPSELL` | [Checkout: 'Worth mentioning' upsell panel (membership / restock / rebook cue)](../stories/PRD-06__CHECKOUT-UPSELL.md) | Story | P2 | 2 | 1 |
| `CHECKOUT-RAPPORT` | [Checkout: client-rapport panel (derived from history)](../stories/PRD-06__CHECKOUT-RAPPORT.md) | Story | P2 | 2 | 1 |
| `CHECKOUT-CROSSSELL` | [Checkout: 'Pairs well with today's treatment' non-S4 cross-sell](../stories/PRD-06__CHECKOUT-CROSSSELL.md) | Story | P2 | 2 | 1 |
| `PRICING-WHATIF` | [Pricing & what-if — editable plan prices + projected impact (core)](../stories/PRD-06__PRICING-WHATIF.md) | Story | P2 | 2 | 2 |
| `PRICING-CHURN-SLIDER` | [Pricing & what-if: churn-sensitivity slider](../stories/PRD-06__PRICING-CHURN-SLIDER.md) | Story | P2 | 2 | 1 |
| `PRICING-SERVICE-ROWS` | [Pricing & what-if: editable service-pricing rows](../stories/PRD-06__PRICING-SERVICE-ROWS.md) | Story | P2 | 2 | 1 |
| `PRICING-SAVE-APPLY` | [Pricing & what-if: save scenario + apply-via-admin handoff](../stories/PRD-06__PRICING-SAVE-APPLY.md) | Story | P2 | 2 | 1 |
| `PRICING-FINANCE-HUB` | [Pricing & what-if: Finance hub framing (defers to Xero)](../stories/PRD-06__PRICING-FINANCE-HUB.md) | Story | P2 | 2 | 1 |
| `REFERRALS` | [Referrals & affiliate credit (non-S4) (placeholder)](../stories/PRD-06__REFERRALS.md) | Story | P2 | 1 | 1 |

_Totals: 37 stories · 62 tasks._
