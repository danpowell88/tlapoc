# Checkout assist & post-visit rebooking

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-ASSIST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a front desk, I want checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval, so that I help clients and keep them on cadence.

Subtle membership/restock upsell + client rapport panel + post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

## Requirements

- Checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval.
- Traces to requirement(s): REQ-PAY-6.

## Acceptance Criteria

- [ ] Checkout shows a subtle membership/restock upsell and a client rapport panel.
- [ ] Post-checkout rebooking is offered on the treatment interval.
- [ ] Upsell suggestions never include S4 discounting.
- [ ] Rebooking integrates with the calendar (PRD-02) and recall (PRD-07).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0022 (see docs/adr/decision-log.md).
Depends on: PRD-06/POS.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/CHECKOUT-ASSIST.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
