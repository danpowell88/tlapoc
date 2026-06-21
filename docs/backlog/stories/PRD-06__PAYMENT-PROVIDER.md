# Payment provider abstraction + Square adapter

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PAYMENT-PROVIDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration
>
> **Depends on:** `SPRINT-0/SPIKE-SQUARE`

## Background

As a developer, I want a payment-provider abstraction with a Square adapter and cash tender, so that payments are swappable and PCI-safe.
An IPaymentProvider port (authorize/capture, refund, void, tokenize, recurring, gift-card) with a Square adapter first and cash as an internal tender; no PAN stored, only tokens (ADR-0007).

## Requirements

- A payment-provider abstraction with a Square adapter and cash tender.

## Acceptance Criteria

- [ ] IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurring and gift-card.
- [ ] Square adapter implemented; cash is an internal tender.
- [ ] No PAN is ever stored — only provider tokens.
- [ ] Built on SPIKE-SQUARE findings.

## Technical notes (high level)

- Stack: .NET API (domain/services); Ports-and-adapters integration
- Architecture decisions: [ADR-0007](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
