# Checkout: per-line GST (goods and services tax)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS-GST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk / owner, I want GST computed per line on every sale with a clear tax-inclusive totals strip, so that tax is correct per item and maps cleanly to the accounts.
Plainly: work out the 10% GST (goods and services tax) on each line of the sale, not as a lump on the total, so the figures are right and accounting-ready. Where it fits: a follow-up to the basic in-person POS checkout (PRD-06/POS) that adds per-line tax to a sale that, in the basic slice, just totals line prices. Both services and retail are taxable in this clinic; computing GST per line means a future GST-free line is handled correctly and the eventual Xero (the clinic's cloud accounting system) post (PRD-10) gets per-line tax mapping. Money figures stay owner-aware but the sale total is sale-level (Reception may see it); takings/margin read-models stay behind the owner-only .fin capability.

## How it works

GST (goods and services tax) is computed PER LINE — both services and retail are taxable in this clinic — and the totals strip shows Subtotal, 'GST incl.' and Total. Do NOT take a flat total/11 shortcut: each Invoice line carries its own tax_code and gst amount so a future GST-free line is handled correctly, and so the eventual Xero (the clinic's cloud accounting system) post (PRD-10) gets per-line tax mapping.
GST is shown tax-inclusive per Australian convention. This extends the basic checkout's line list (PRD-06/POS): the same lines now carry tax, and the totals strip replaces the basic running total. The sale total is sale-level (Reception may see it); owner-only takings/margin read-models stay behind .fin.

## Requirements

- GST computed per line on every sale with a clear tax-inclusive totals strip.

## Acceptance Criteria

- [ ] GST (goods and services tax) is computed per line — both services and retail taxable — not as a flat total/11 shortcut.
- [ ] Each line carries its own tax_code and GST amount; a GST-free line (rare) computes to zero correctly.
- [ ] The totals strip shows Subtotal, 'GST incl.' and Total, tax-inclusive per AU convention.
- [ ] Per-line tax is available for the eventual Xero post (PRD-10).

## UI designs / screenshots

- Prototype: Checkout totals strip — Subtotal / 'GST incl.' / Total beneath the line list; each line's price is tax-inclusive.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Invoice (extends PRD-06/POS)** — + lines[].tax_code, lines[].gst; totals: subtotal, gst_incl, total
  - _Per-line tax_code + gst added to the basic Invoice; no new entity._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Per-line GST computation + tax_code on each Invoice line**
  Behaviour: each Invoice line carries a tax_code and a computed gst amount; GST is summed across lines rather than derived from the total. Requirements: both services and retail taxable; a GST-free tax_code computes to zero; no flat total/11 shortcut; tenant-scoped.
- [ ] **Totals strip (Subtotal / GST incl. / Total) in checkout**
  Behaviour: the checkout shows Subtotal, 'GST incl.' and Total, tax-inclusive per AU convention, recomputing live as lines change. Requirements: reads the per-line gst; sale total is sale-level (Reception may see it); owner-only .fin gate on any takings/margin figures.
