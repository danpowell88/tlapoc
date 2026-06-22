# Daily closeout — card + cash rollup, count & lock (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want a daily closeout that totals card and cash and locks the day, so that the till reconciles every day.
What this is, plainly: the end-of-day till balance — total the card and cash takings, enter the counted cash, note it and lock it. This is the minimal end-to-end core; Square-batch variance detection, the Xero reconciliation and the back-office tablet surface are each added as their own follow-ups. Where it sits: it reads the day's POS payments and is the bridge to Xero accounting (PRD-10); it follows the till in the Payments layer, on top of the booked/charted visit. End-of-day closeout (reconciliation of takings against recorded payments) balances card + cash (REQ-PAY-4).

## How it works

A Closeout summarises the day's tenders per location: card_total (reconciled to Square's batch), cash_total (counted vs recorded), and the resulting variance, with the operator who closed it. Variances are highlighted so they can be noted and explained rather than buried. The closeout reconciles to the Xero posting (PRD-10): the day's invoices/payments that posted to Xero should foot to the closeout totals.
Because it exposes daily takings, the whole closeout is behind the owner-only financial capability; Reception never sees it. The closeout also appears on the back-office tablet so the owner can run it away from the front desk.

## Requirements

- A daily closeout that totals card and cash and locks the day.

## Acceptance Criteria

- [ ] Closeout summarises card and cash tenders for the day per location (one Closeout row per location per trading day).
- [ ] The operator enters the counted cash and the closeout records a simple counted-vs-recorded difference.
- [ ] The operator can note and lock the closeout; a locked closeout is immutable and stamps closed_by/closed_at.
- [ ] Closeout figures are owner-gated (not visible to Reception).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout -> daily closeout — card total vs cash total for the day, variance highlight, a notes/lock step ('Note locked & saved'), close-out action; owner-only figures.
- Also surfaced on the back-office tablet (backroom).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Closeout** — id, tenant_id, location_id, date, card_total, cash_total, counted_cash, variance, note, closed_by, closed_at
  - _Reconciles to Xero (PRD-10); owner-gated._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Card + cash day-rollup per location + counted-cash entry**
  Behaviour: at end of day the closeout summarises the day's tenders per location — card_total (from card Payments) and cash_total (what the system recorded) — and the operator enters the counted cash, giving a simple counted-vs-recorded difference. One Closeout row per location per trading day. Requirements: totals aggregate from the day's Payment rows (PRD-06/POS); tenant-scoped with RLS (row-level security); the whole surface is owner-only (.fin) — Reception never sees daily takings. (Square-batch variance flagging is a follow-up.)
- [ ] **Note, lock + immutability**
  Behaviour: the operator records a note and locks the closeout ('Note locked & saved'); a locked closeout is immutable and stamps closed_by/closed_at. Requirements: once locked the day cannot be silently re-opened/edited (audit any correction); owner-only. (Reconcile-to-Xero is a follow-up.)
- [ ] **Closeout web UI (front desk)**
  Behaviour: render the closeout at the checkout/desk — card vs cash totals, counted-cash entry, the counted-vs-recorded difference, note + lock, close action. Requirements: owner-only capability gate; loading/empty/error states. (The back-office tablet surface is a follow-up.)
