# Client store-credit & AR (accounts receivable) ageing

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-CREDIT-AR`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PACKAGES-GIFT`

## Background

As a owner / manager, I want to track each client's store credit and what they owe by age, so that pre-paid credit and receivables are always reconciled and visible.
Plainly: keep a per-client running store-credit balance and an ageing view of anything a client owes, so nothing is lost and overdue amounts are visible. Where it fits: a follow-up to the basic pre-paid value story (PRD-06/PACKAGES-GIFT) that adds the money-balance layer behind packages and gift cards. Store credit is usable as a checkout deduction (PRD-06/POS-DEDUCTIONS draws it down). All money figures here are owner-only (.fin) — Reception sees memberships/packages but not credit or AR (accounts receivable) dollar figures. Feeds the Client 360 billing tab.

## How it works

An AccountBalance per client holds store-credit (usable as a checkout deduction) and AR (accounts receivable) ageing buckets (what the client owes, grouped by age) for owner/manager visibility. Store credit applied at checkout decrements the balance (the deduction line lives in PRD-06/POS-DEDUCTIONS); AR ageing is surfaced to owner/manager only.
All money figures here are owner-gated (.fin) — Reception sees memberships/packages but not credit/AR dollar figures. This extends the basic pre-paid-value story (PRD-06/PACKAGES-GIFT) and feeds the Client 360 billing tab.

## Requirements

- To track each client's store credit and what they owe by age.

## Acceptance Criteria

- [ ] A per-client AccountBalance holds store-credit and AR (accounts receivable) ageing buckets (what the client owes, by age).
- [ ] Store credit applied at checkout decrements the balance (consumed by PRD-06/POS-DEDUCTIONS).
- [ ] AR ageing is surfaced to owner/manager only and feeds the Client 360 billing tab.
- [ ] All credit/AR money figures are owner-gated (.fin); Reception does not see them.

## UI designs / screenshots

- Prototype: Client 360 billing tab — store-credit balance + AR (accounts receivable) ageing buckets (owner/manager only); credit applies as a deduction at checkout (PRD-06/POS-DEDUCTIONS).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **AccountBalance** — client_id, credit, ar_ageing
  - _New entity; client store credit + AR (accounts receivable) ageing; owner/manager visibility (.fin)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **AccountBalance model: store-credit + AR ageing**
  Behaviour: a per-client AccountBalance holds store-credit and AR (accounts receivable) ageing buckets. Requirements: store credit applied at checkout decrements it (consumed by PRD-06/POS-DEDUCTIONS); AR ageing computed by age; tenant-scoped with RLS (row-level security); all figures owner-only (.fin).
- [ ] **Client-360 billing tab (credit + AR ageing, owner-gated)**
  Behaviour: the Client 360 billing tab shows the store-credit balance and AR ageing buckets to owner/manager only. Requirements: owner-only .fin gate; loading/empty/error states; figures read the AccountBalance, not a separate copy.
