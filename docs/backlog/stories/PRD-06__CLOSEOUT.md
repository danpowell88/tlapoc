# Daily closeout & reconciliation

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want a daily closeout that balances card and cash, so that the till reconciles every day.
End-of-day closeout balances card + cash (REQ-PAY-4).

## Requirements

- A daily closeout that balances card and cash.

## Acceptance Criteria

- [ ] Closeout summarises card + cash tenders for the day.
- [ ] Variances are surfaced.
- [ ] Closeout figures are owner-gated.
- [ ] Closeout reconciles to the Xero posting (PRD-10).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
