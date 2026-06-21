# Payment provider abstraction + Square adapter

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PAYMENT-PROVIDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration
>
> **Depends on:** `SPRINT-0/SPIKE-SQUARE`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a developer, I want a payment-provider abstraction with a Square adapter and cash tender, so that payments are swappable and PCI-safe.

An IPaymentProvider port (authorize/capture, refund, void, tokenize, recurring, gift-card) with a Square adapter first and cash as an internal tender; no PAN stored, only tokens (ADR-0007).

## Requirements

- A payment-provider abstraction with a Square adapter and cash tender.
- Traces to requirement(s): REQ-PAY-1.

## Acceptance Criteria

- [ ] IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurring and gift-card.
- [ ] Square adapter implemented; cash is an internal tender.
- [ ] No PAN is ever stored — only provider tokens.
- [ ] Built on SPIKE-SQUARE findings.

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: .NET API (domain/services); Ports-and-adapters integration.
Architecture decisions: ADR-0007 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/SPIKE-SQUARE.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/PAYMENT-PROVIDER.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
