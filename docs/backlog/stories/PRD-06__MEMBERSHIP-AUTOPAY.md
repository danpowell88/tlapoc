# Membership: autopay scheduler (off-session recurring charge)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-AUTOPAY`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a owner, I want due memberships to be charged automatically on schedule from the card on file, so that recurring revenue collects itself without manual chasing.
Plainly: a scheduled job charges each member's stored card on the right day and rolls the date forward, so nobody has to take the payment by hand. Where it fits: a follow-up to the basic membership enrolment (PRD-06/MEMBERSHIP), which stores the card-on-file and sets next_charge_at; this adds the recurring charging itself. It charges off-session via IPaymentProvider.recurringCharge (PRD-06/PAYMENT-PROVIDER), built on the Square card-on-file recurring spike (SPRINT-0/SPIKE-SQUARE). Each charge feeds the Closeout/Xero like any payment. All money figures are owner-gated (.fin).

## How it works

A scheduled job picks up memberships where next_charge_at <= now and charges the stored card off-session via IPaymentProvider.recurringCharge (PRD-06/PAYMENT-PROVIDER), then advances next_charge_at to the next period. Charging is idempotent per period — a retry never double-bills the same period.
Each charge writes a ProviderTxn and feeds the Closeout/Xero like any payment. Autopay is built on the Square card-on-file recurring spike (SPRINT-0/SPIKE-SQUARE). This extends the basic enrolment (PRD-06/MEMBERSHIP); failed-charge handling is the dunning follow-up. All money figures owner-gated (.fin).

## Requirements

- Due memberships to be charged automatically on schedule from the card on file.

## Acceptance Criteria

- [ ] A scheduled job picks up memberships where next_charge_at <= now and charges the stored card off-session via IPaymentProvider.recurringCharge.
- [ ] After a successful charge, next_charge_at advances to the next period.
- [ ] Charging is idempotent per period — a retry never double-bills the same period.
- [ ] Each charge writes a ProviderTxn and feeds the Closeout/Xero like any payment; money figures owner-gated (.fin).

## UI designs / screenshots

- No dedicated screen — surfaces as charges on the members list (PRD-06/MEMBERSHIP-MEMBERS) and in the daily Closeout; client app shows 'Glow Club renews 1 Jul · autopay is on'.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Membership (extends PRD-06/MEMBERSHIP)** — uses schedule + next_charge_at; each charge writes a ProviderTxn (PRD-06/PAYMENT-PROVIDER)
  - _No new entity; the scheduler reads/advances next_charge_at._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Scheduled off-session recurring charge + advance next_charge_at**
  Behaviour: a scheduled job charges memberships due (next_charge_at <= now) off-session via IPaymentProvider.recurringCharge and advances next_charge_at. Requirements: idempotent per period (no double-bill on retry); each charge writes a ProviderTxn and feeds Closeout/Xero; built on SPRINT-0/SPIKE-SQUARE; owner-only (.fin).
