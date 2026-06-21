# Daily closeout & reconciliation

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want a daily closeout that balances card and cash, so that the till reconciles every day.
End-of-day closeout balances card + cash (REQ-PAY-4).

## How it works

An end-of-day closeout balances card + cash for the day and surfaces variances. Figures are owner-gated and reconcile to the Xero posting (PRD-10).
The daily till-reconciliation routine.

## Requirements

- A daily closeout that balances card and cash.

## Acceptance Criteria

- [ ] Closeout summarises card + cash tenders for the day.
- [ ] Variances are surfaced.
- [ ] Closeout figures are owner-gated.
- [ ] Closeout reconciles to the Xero posting (PRD-10).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout -> daily closeout (checkout.png) — card vs cash totals for the day, variance highlight; owner-only figures.
- Also surfaced on the back-office tablet (backroom.png).

## Suggested data model

- **Closeout** — id, tenant_id, location_id, date, card_total, cash_total, variance, closed_by
  - _Reconciles to Xero (PRD-10)._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
