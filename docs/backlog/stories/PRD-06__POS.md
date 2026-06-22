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

- [ ] **Invoice/Payment model + per-line GST & schedule flag (migrations)**
  Model Invoice, InvoiceLine and Payment (every table tenant_id + RLS (row-level security)).
  - InvoiceLine carries type, ref, qty, price, the catalog schedule flag (S4 (Schedule 4 prescription-only medicine) — Schedule 4 prescription-only medicine — vs non-S4) and a tax_code; GST (goods and services tax) computed PER LINE (services + retail both taxable) — not a flat total/11.
  - Payment supports split/partial (many Payments per Invoice), tip and surcharge, with tender(card|cash|giftcard) and an optional provider_txn_id/token_ref.
  - Deduction lines (member reward, store credit) attach only to non-S4 lines.
- [ ] **Checkout API: sale, tenders, split/partial, receipt, Closeout+Xero post**
  Server-authoritative checkout commands/queries.
  - Endpoints: create/append invoice line, apply member reward/credit (non-S4 only — reject if a line is S4 (Schedule 4 prescription-only medicine) — Schedule 4 prescription-only medicine), take payment (card via IPaymentProvider authorize+capture; cash recorded; gift-card redeem), split/partial across tenders, void/refund.
  - On completion: write to the day's Closeout (the daily reconciliation of takings) and enqueue the Xero (the clinic's cloud accounting system) post (PRD-10) with per-line account/GST (goods and services tax) mapping.
  - Owner-only gate on takings/margin read-models; Reception can complete a sale and see its total only. Never trust the client for schedule/eligibility — re-check server-side.
- [ ] **Checkout web UI: lines, tenders, S4-inert controls, terminal modal**
  Angular checkout per the screenshot.
  - Line list with per-line schedule tag; S4 (Schedule 4 prescription-only medicine) lines render reward/discount/points controls disabled with a tooltip (engine refuses them).
  - Tender panel (Square (the card-payment provider) card / Record cash / Gift card), split/partial entry, tip + surcharge; Subtotal / GST (goods and services tax) incl. / Total with member-reward + store-credit deduction lines.
  - Square-terminal modal: Processing -> Approved; loading/empty/error states; capability-gate owner-only money figures.
