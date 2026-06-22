# In-person POS checkout — basic cart + single tender (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a front desk, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.
What this is, plainly: the everyday till at the front desk — add what the client is buying, take the money once, hand over a receipt. This is the minimal end-to-end core; GST per line, split/partial tenders, gift/package redemption, member rewards and the Square-terminal modal are each added as their own follow-ups. Where it sits: it builds directly on the PAYMENT-PROVIDER port and is the first thing a client actually pays through; like all of Payments it sits on top of the booked/charted visit, so it arrives after the clinical core. Front desk takes payment in person via Square card-present or recorded cash, with a basic receipt (REQ-PAY-2). Financial figures are owner-gated.

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
- [ ] **S4-inert reward/discount controls (C9 enforcement at the line)**
  Behaviour: an S4 (Schedule 4 prescription-only medicine) line (e.g. the Anti-wrinkle treatment) shows an 'S4 · no rewards' tag and exposes NO reward, discount or points control; the control is disabled with a tooltip explaining why. Requirements: the rewards engine (PRD-06/REWARDS-ENGINE) refuses to earn/redeem/discount against any S4 line — re-checked server-side at checkout against the live line schedule, never trusting a client/UI value (C9). This invariant is the visible face of the no-S4-incentive rule and must be present from the basic slice and never regress.
- [ ] **Single-tender payment panel: Square card OR record cash + basic receipt**
  Behaviour: a 'Take payment (in person)' panel takes the whole sale on ONE tender — Square card OR recorded cash — and issues a basic receipt; the sale completes and appears in the day's Closeout. Requirements: card goes through IPaymentProvider authorize+capture (PRD-06/PAYMENT-PROVIDER); cash is recorded as an internal tender with no processor call; every tender becomes a Payment row. Split/partial, tips, surcharge, gift-card tender and the Square-terminal progress modal are deliberately OUT of this basic slice (each is its own follow-up). The panel notes 'Membership autopay runs automatically on the card on file.'
- [ ] **Checkout API: single-tender sale, take payment, receipt, Closeout**
  Behaviour: server-authoritative checkout for the core slice — create/append invoice line, take payment on one tender (card via IPaymentProvider authorize+capture; or cash recorded), issue a receipt, write the sale to the day's Closeout. Requirements: owner-only gate on takings/margin read-models (Reception completes a sale and sees its total only); never trust the client for schedule/eligibility — re-check server-side; the S4-no-incentive invariant holds (no reward/discount control reaches an S4 line). Per-line GST, split/partial tenders, deductions, gift/package redemption and the Xero post are added by their follow-ups. Online one-off checkout stays unexposed (deferred).
