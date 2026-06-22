# Payment provider abstraction + Square adapter

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PAYMENT-PROVIDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration
>
> **Depends on:** `SPRINT-0/SPIKE-SQUARE`

## Background

As a developer, I want a payment-provider abstraction with a Square adapter and cash tender, so that payments are swappable and PCI-safe.
An IPaymentProvider port (authorize/capture, refund, void, tokenize, recurring, gift-card) with a Square adapter first and cash as an internal tender; no PAN stored, only tokens (ADR-0007).

## How it works

A payment-provider abstraction (IPaymentProvider) exposes authorize/capture, refund, void, tokenize, recurring and gift-card, with a Square adapter first and cash as an internal tender. No PAN is ever stored — only provider tokens (ADR-0007, PCI-safe).
Built on the SPIKE-SQUARE findings; keeps the platform provider-swappable.

## Requirements

- A payment-provider abstraction with a Square adapter and cash tender.

## Acceptance Criteria

- [ ] IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurring and gift-card.
- [ ] Square adapter implemented; cash is an internal tender.
- [ ] No PAN is ever stored — only provider tokens.
- [ ] Built on SPIKE-SQUARE findings.

## UI designs / screenshots

- No dedicated screen — surfaces through Checkout (checkout.png) and membership card-on-file capture; this story is the backend port + Square adapter.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **PaymentMethodToken** — id, tenant_id, client_id, provider(square), token_ref, brand, last4, exp
  - _Token only; no PAN (ADR-0007)._
- **ProviderTxn** — id, payment_id, provider_ref, type(auth|capture|refund|void), amount, status
  - _Adapter-mapped provider transactions._

## Technical notes (high level)

- Architecture decisions: [ADR-0007](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - PaymentMethodToken — id, tenant_id, client_id, provider(square), token_ref, brand, last4, exp (Token only; no PAN (ADR-0007).)
  - ProviderTxn — id, payment_id, provider_ref, type(auth|capture|refund|void), amount, status (Adapter-mapped provider transactions.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurring and gift-card.
  - Rule: Square adapter implemented; cash is an internal tender.
  - Rule: No PAN is ever stored — only provider tokens.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: SPRINT-0/SPIKE-SQUARE.
- [ ] **Integration adapter, sync & config**
  Implement the provider behind its swappable port:
  - Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.
  - Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.
  - Handle partial failures + replays; surface errors to the user.
  - Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).
