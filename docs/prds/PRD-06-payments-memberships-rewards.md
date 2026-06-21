# PRD-06 — Payments, Memberships & Non-S4 Rewards

> **▸ Prototype alignment (rev 2, 2026-06-19).** Adds **REQ-PAY-6 checkout assist** (subtle membership/restock upsell + **client rapport** panel + **post-checkout rebooking** on the treatment interval), **REQ-MEMB-8** loyalty/referrals/gift-cards + **dunning retry** (full campaigns/referrals stay Phase 2), and **REQ-MEMB-9 pricing & what-if planning** for the owner (ADR-0022). Square AU card-on-file **recurring autopay** remains a de-risk spike (🔬 F3). See [requirements §12](../02-requirements.md#12-prototype-alignment--feasibility-register).
>
> **▸ Prototype alignment (rev 4, 2026-06-20).** Adds the **Finance** money-read-models (ADR-0027): **per-line GST coding** (services + retail both taxable — fixes the naive total÷11), **refunds/credit-notes & disputes** (restock non-S4 only; dispute → Job), **BNPL/tips** tenders, **retail SKUs + supplier POs**, a **BAS/GST summary**, and a **commission/pay-run** with an **engagement-type risk banner** — explicitly **attribution & export, not a payroll/tax engine** (REQ-PAY-7..10, REQ-RPT-6, REQ-MED-14/15). Referral/affiliate credit is **non-S4 only** (REQ-MEMB-10). Online checkout/deposits & BNPL stay Phase 2 (ADR-0036, F14 cooling-off invariant).
>
> **▸ Scope cut (rev 4.1, 2026-06-20).** Finances move to **Xero & integrations**: the app keeps only **pricing / what-if** (ADR-0022) and **high-level reporting** (PRD-08). In-app **commission pay-run, supplier POs/AP, refund/dispute management and BAS/GST tooling are dropped** (ADR-0027 revised) — the Finance screen is now a light pricing + reporting hub that defers the ledger to Xero, while invoices/payments still sync from checkout.

> **Phase:** 1 · **Status:** Draft<br>
> **Requirements:** REQ-PAY-1…5, REQ-MEMB-1…7 · **Compliance:** C9, C23 (reward comms), C18 (records)<br>
> **ADRs:** 0007 (payments abstraction), 0014 (catalog S4 classification)<br>
> **Depends on:** PRD-01, PRD-02; integrates with PRD-10 (Xero)

## 1. Summary
Commerce for the clinic: **in-person POS** (Square card-present + recorded cash + gift cards),
**automatic recurring membership autopay** via stored card-on-file, packages/series, and a
**rewards engine that only ever applies to non-S4 items** — driving repeat visits without eroding
margin or breaching advertising law.

## 2. Goals & non-goals
**Goals:** in-person checkout (card via Square, cash, gift card); package/series sale + redemption;
client balances/credit + AR; daily closeout; membership plans with **automatic** recurring autopay
(card-on-file); visit-based + membership **rewards on non-S4 only**, margin-aware.

**Non-goals (v1):** customer-facing online checkout for one-off purchases; BNPL; commission/payroll;
advanced loyalty campaigns/referrals (Phase 2).

## 3. Users
Front desk (POS), client (joins membership, earns/redeems rewards), owner (plans, reward rules, reconciliation).

## 4. User stories
- As **front desk**, I take payment **in person** by Square card or **record cash**, sell/redeem **gift cards**, and redeem package/series visits.
- As a **client**, I join a membership; my card is stored and **auto-charged on schedule** (I can add it online/in-app — not only at the desk).
- As a **client**, I earn **visit-based rewards** and member perks I can redeem on **non-S4** items (skincare/retail, non-S4 add-ons, or account/gift credit) — never on the toxin itself.
- As an **owner**, I set **margin-aware reward rules** (caps, eligible non-S4 items) and see **reward-cost vs retention**.
- As an **owner**, payments/invoices reconcile to **Xero** and a **daily closeout** balances card + cash.

## 5. Key flow
```mermaid
flowchart TD
  A[Checkout] --> B[Line items<br/>service/retail/package]
  B --> C{Item schedule}
  C -- S4 --> C1[No reward/discount<br/>applied (C9)]
  C -- non-S4 --> C2[Rewards eligible]
  B --> D[Tender: Square card / cash / gift card]
  D --> E[Receipt + balances]
  E --> F[Post to Xero<br/>+ daily closeout]
  subgraph Membership
    M1[Join plan] --> M2[Tokenise card-on-file]
    M2 --> M3[Automatic recurring charge<br/>+ dunning on failure]
  end
```

## 6. Functional scope
**Payments**
- REQ-PAY-1 (ADR-0007): `IPaymentProvider` (authorize/capture, refund, void, **tokenize**, **recurring**, gift-card); **Square adapter** first; **cash** as internal tender.
- REQ-PAY-2: **in-person POS only in v1** (Square card-present + cash); receipts; partial/split; tips; surcharge config. *(Online one-off checkout deferred; no booking deposits.)*
- REQ-PAY-3: package/series sale + redemption ("visits remaining"); client balance/credit; AR ageing.
- REQ-PAY-4: daily closeout/reconciliation (card + cash).
- REQ-PAY-5: **gift cards** — sell/redeem/track balances.

**Memberships & rewards**
- REQ-MEMB-1: plans/tiers; **automatic recurring** billing; card-on-file (added online/in-app or at desk); failed-payment dunning/recovery.
- REQ-MEMB-2/3: auto-apply benefits/credits at checkout; expirations; lifecycle (join/pause/cancel/win-back) → MRR/churn reporting.
- REQ-MEMB-4/5: **visit-based rewards** (milestones / every-Nth-visit) + membership/frequency perks (discounted/complimentary **non-S4** items, add-ons, gift/account credit).
- REQ-MEMB-6: **margin-aware reward rules** (value caps, eligible items, reward-cost vs retention reporting); reward **communications** respect advertising rules — no public S4 price promotion, delivered to consented logged-in clients (C9/C23).
- REQ-MEMB-7 (C9, ADR-0014): **rewards on non-S4 only** — catalog `schedule` flag; engine **blocks** earn/redeem/discount on S4 items.

## 7. Data & entities
`Invoice`/`InvoiceLine`, `Payment` (card|cash|giftcard, token ref), `GiftCard`, `Package`/`Series`,
`AccountBalance`/`Credit`, `MembershipPlan`/`Membership` (card-on-file token, schedule), `RewardRule` (non-S4 eligibility, caps),
`RewardLedger` (earned/redeemed), `Closeout`. Catalog `Service`/`Product` carry `schedule` (S4|non-S4).

## 8. Acceptance criteria
- **AC1 (REQ-PAY-2):** A sale can be completed in person by Square card or by **recording cash**; both appear in the daily closeout.
- **AC2 (REQ-MEMB-1):** A membership auto-charges on schedule from a stored token (card added online/in-app **or** in person); a failed charge triggers dunning.
- **AC3 (C9/REQ-MEMB-7):** The rewards engine **refuses** to earn, redeem or discount against any item flagged **S4**; only non-S4 items are eligible. Attempting to configure an S4 reward is blocked.
- **AC4 (margin):** A reward rule enforces its value cap and surfaces reward-cost vs retention in reporting.
- **AC5 (PCI):** No PAN is stored — only provider tokens (ADR-0007).
- **AC6 (gift cards):** A gift card can be sold, its balance tracked, and redeemed at checkout.
- **AC7 (Xero):** A completed sale posts to Xero with correct account/GST mapping (PRD-10).

## 9. Dependencies & sequencing
After PRD-01/02; catalog `schedule` flag (shared with PRD-02). Xero posting via PRD-10. Reward comms via PRD-07. **Spike:** Square AU card-on-file recurring.

## 10. Out of scope
Online one-off checkout, BNPL, commission/payroll, referrals/advanced loyalty (Phase 2).

## 11. Open questions
- Exact membership tiers/prices/benefits + reward-rule values (§10.3).
- Square Gift Cards vs internal gift-card ledger.
