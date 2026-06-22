# In-person POS checkout (card + cash)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a front desk, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.
What this is, plainly: the everyday till at the front desk — add what the client is buying, take the money, print a receipt. Where it sits: it builds directly on the PAYMENT-PROVIDER port and is the first thing a client actually pays through; like all of Payments it sits on top of the booked/charted visit, so it arrives after the clinical core. Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split, tips and surcharge config (REQ-PAY-2). Financial figures are owner-gated.

## How it works

A sale is an Invoice of lines (service / retail / package / membership), each carrying its catalog schedule flag, GST (goods and services tax) computed per line (services and retail are both taxable — no flat total/11), and a running total. Payment is taken via the IPaymentProvider port: Square card-present, or cash recorded as an internal tender, or a gift card drawn down. Partial and split tenders are supported (e.g. $200 on card + remainder on a gift card), as are tips and a configurable card surcharge.
S4 (Schedule 4 prescription-only medicines such as cosmetic injectables) lines are visibly inert for incentives: the Anti-wrinkle line shows an 'S4 · no rewards' tag and carries no reward, discount or points control — the engine refuses them (C9). Non-S4 lines can attract the member reward (10% off non-S4) and store credit, which appear as their own deduction lines.
On completion the sale posts to the daily Closeout and syncs to Xero (PRD-10). The screen states this plainly: 'Membership autopay runs automatically on the card on file. Invoice posts to Xero on completion.' Reception sees the sale total but not owner-only money read-models (daily takings, margins).

## Requirements

- To take payment in person by Square card or recorded cash with receipts and split/partial support.

## Acceptance Criteria

- [ ] A sale completes in person by Square card or by recording cash; both appear in the daily Closeout.
- [ ] Receipts, partial/split tenders, tips and a configurable card surcharge are supported.
- [ ] GST (goods and services tax) is computed per line (services and retail both taxable); the invoice posts to Xero on completion (PRD-10).
- [ ] S4 (Schedule 4 prescription-only medicines) lines carry no reward/discount/points control; non-S4 member reward and store credit show as deduction lines.
- [ ] Money figures respect the owner-only financial capability — Reception sees the sale but not daily-takings/margin read-models.
- [ ] Online one-off checkout is not exposed (deferred).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout — client header (name, VIP/Glow Club badge, prefs, recent treatments, birthday/connection); line list with per-line schedule tag (S4 · no rewards / non-S4 / membership); 'Member reward — 10% off non-S4' and 'Store credit applied' deduction lines; Subtotal / GST incl. / Total.
- 'Take payment (in person)' panel: Square card, Record cash, Gift card; note 'Membership autopay runs automatically on the card on file. Invoice posts to Xero on completion.'
- Square-terminal modal (Processing -> Approved) then the post-checkout rebook view (CHECKOUT-ASSIST).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Invoice** — id, tenant_id, client_id, lines[]{type(service|retail|package|membership), ref, qty, price, schedule(S4|nonS4), tax_code, gst}, subtotal, deductions[]{reward|credit}, total, status
  - _Per-line schedule + GST; deductions only on non-S4 lines._
- **Payment** — id, invoice_id, tender(card|cash|giftcard), amount, token_ref?, tip, surcharge, provider_txn_id?, at
  - _Split/partial = multiple Payments per Invoice; appears in Closeout; posts to Xero (PRD-10)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Cart / invoice line list (add, remove, per-line schedule tag)**
  Behaviour: the sale is an Invoice of lines a client is buying — service, retail, package or membership. The desk adds lines (from the booked visit, the treatment menu or retail) and can remove any line; each line shows its name, sub-detail and price, and a schedule tag derived from the catalogue: 'S4 · no rewards' (rose), 'non-S4' (green) or 'membership' (brand). Requirements: the schedule flag on every line comes from the catalogue (PRD-02/SERVICE-CATALOGUE), never hand-set; line type drives downstream tax + reward eligibility; an empty cart renders an empty state. This is the spine the GST, deductions, tenders and suggestions all read.
- [ ] **Per-line GST (goods and services tax) computation**
  Behaviour: GST is computed PER LINE — both services and retail are taxable in this clinic — and the totals strip shows Subtotal, 'GST incl.' and Total. Requirements: do NOT take a flat total/11 shortcut; each line carries its own tax_code and GST so a future GST-free line (rare) is handled correctly, and so the Xero (the clinic's cloud accounting system) post (PRD-10) gets per-line tax mapping. GST is shown tax-inclusive per AU convention.
- [ ] **S4-inert reward/discount controls (C9 enforcement at the line)**
  Behaviour: an S4 (Schedule 4 prescription-only medicine) line (e.g. the Anti-wrinkle treatment) shows an 'S4 · no rewards' tag and exposes NO reward, discount or points control; the control is disabled with a tooltip explaining why. Requirements: the rewards engine (PRD-06/REWARDS-ENGINE) refuses to earn/redeem/discount against any S4 line — re-checked server-side at checkout against the live line schedule, never trusting a client/UI value (C9). This invariant is the visible face of the no-S4-incentive rule and must never regress.
- [ ] **Member reward + store-credit deduction lines (non-S4 only)**
  Behaviour: when the client is a member, a 'Member reward — 10% off non-S4' line and an 'Store credit applied' line appear as their own negative deduction rows beneath the cart, reducing the total. Requirements: the reward is computed only on the non-S4 subtotal (S4 lines excluded); store credit draws from the client AccountBalance (PACKAGES-GIFT); deductions recompute live as lines change. Non-members see neither. All money figures shown here are sale-level (Reception may see them); owner-only read-models (takings/margin) stay behind .fin.
- [ ] **Tender panel: Square card, record cash, gift card (split / partial)**
  Behaviour: a 'Take payment (in person)' panel offers Square card, Record cash and Gift card; a sale can be paid by one tender or split/partial across several (e.g. $200 on card + remainder on a gift card). Tips and a configurable card surcharge are supported. Requirements: card goes through IPaymentProvider authorize+capture (PRD-06/PAYMENT-PROVIDER); cash is recorded as an internal tender with no processor call; gift card draws down a balance (PACKAGES-GIFT). Every tender becomes a Payment row and lands in the day's Closeout (PRD-06/CLOSEOUT). The panel notes 'Membership autopay runs automatically on the card on file. Invoice posts to Xero on completion.'
- [ ] **Square-terminal payment modal (Processing -> Approved) + receipt**
  Behaviour: taking a card payment opens a terminal modal that shows 'Processing on Square terminal…' then 'Payment approved', after which the sale completes and a receipt can be issued. Requirements: the modal reflects the real ProviderTxn state from the adapter (not a fixed timer in production); a decline surfaces a clear retry/alternate-tender path; on completion the invoice posts to Xero (PRD-10) and the post-checkout rebook view (PRD-06/CHECKOUT-ASSIST) is offered. Receipts are available for card, cash and gift-card sales.
- [ ] **Checkout API: sale, tenders, split/partial, receipt, Closeout + Xero post**
  Behaviour: server-authoritative checkout — create/append invoice line, apply member reward/credit (non-S4 only; reject if a line is S4), take payment (card via IPaymentProvider authorize+capture; cash recorded; gift-card redeem), split/partial across tenders, void/refund, issue receipt. Requirements: on completion write to the day's Closeout and enqueue the Xero post (PRD-10) with per-line account/GST mapping; owner-only gate on takings/margin read-models (Reception completes a sale and sees its total only); never trust the client for schedule/eligibility — re-check server-side. Online one-off checkout stays unexposed (deferred).
