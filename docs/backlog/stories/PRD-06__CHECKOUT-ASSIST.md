# Checkout assist & post-visit rebooking

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-ASSIST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval, so that I help clients and keep them on cadence.
Subtle membership/restock upsell + client rapport panel + post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

## Requirements

- Checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval.

## Acceptance Criteria

- [ ] Checkout shows a subtle membership/restock upsell and a client rapport panel.
- [ ] Post-checkout rebooking is offered on the treatment interval.
- [ ] Upsell suggestions never include S4 discounting.
- [ ] Rebooking integrates with the calendar (PRD-02) and recall (PRD-07).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0022](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
