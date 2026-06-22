# Payment provider abstraction + Square adapter

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PAYMENT-PROVIDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration
>
> **Depends on:** `SPRINT-0/SPIKE-SQUARE`

## Background

As a developer, I want a payment-provider abstraction with a Square adapter and cash tender, so that payments are swappable and PCI-safe.
What this is, plainly: the single payment 'plug' the rest of the platform talks to, with Square wired in behind it as the first provider. Where it sits: Payments is commerce layered on top of an already-booked and charted visit, so it comes after the clinical core in the clinic-first build; this story is the very first brick of that commerce layer — every later payments feature (the till, memberships, gift cards) calls this one port and nothing else. An IPaymentProvider port (authorize/capture, refund, void, tokenize, recurring, gift-card) with a Square adapter first and cash as an internal tender; no PAN (primary account number) stored, only tokens (ADR-0007).

## How it works

IPaymentProvider exposes a small, deliberate surface: authorize/capture (card-present at the Square terminal), refund, void, tokenize (store a card-on-file as a provider token), recurringCharge (charge a stored token off-session for membership autopay) and gift-card issue/redeem. Cash is modelled as an internal tender with no processor round-trip — it is recorded, not authorised — so card and cash reconcile in one ledger.
Strictly tokens, never PAN: the platform stores only the provider's token reference plus the display crumbs (brand, last4, exp). No PAN (primary account number), CVV or magnetic data ever lands in our database, which keeps PCI-DSS (the card-security standard) scope to SAQ-A-style minimums (ADR-0007).
Built on the SPIKE-SQUARE findings (the card-on-file recurring de-risk). The adapter is a thin translation layer: it maps our domain calls to Square's Payments/Cards/Refunds APIs and maps Square's responses and webhook events back onto our ProviderTxn states, so swapping processors later means writing one new adapter, not touching checkout.

## Requirements

- A payment-provider abstraction with a Square adapter and cash tender.

## Acceptance Criteria

- [ ] IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurringCharge and gift-card issue/redeem.
- [ ] A SquareAdapter implements the port (card-present + card-on-file); cash is recorded as an internal tender with no processor call.
- [ ] No PAN (primary account number), CVV or track data is ever persisted — only a provider token plus brand/last4/exp.
- [ ] Provider responses and webhooks map onto ProviderTxn states; the port is swappable without touching checkout.
- [ ] Built on the SPIKE-SQUARE recurring/card-on-file findings.

## UI designs / screenshots

- No dedicated screen — this is the backend port + Square adapter. It surfaces through the Checkout tenders (Square card / Record cash / Gift card) and through membership card-on-file capture; see those stories for UI.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **PaymentMethodToken** — id, tenant_id, client_id, provider(square), token_ref, brand, last4, exp
  - _Token only — never a PAN (primary account number) (ADR-0007). Used by membership autopay._
- **ProviderTxn** — id, payment_id, provider_ref, type(auth|capture|refund|void), amount, status, raw_event_ref
  - _Adapter-mapped processor transactions; reconciled against webhook callbacks._

## Technical notes (high level)

- Architecture decisions: [ADR-0007](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Define IPaymentProvider port + ProviderTxn state model**
  Define the IPaymentProvider port and the ProviderTxn lifecycle, decoupled from any processor.
  - Port methods: authorize, capture (or combined authorize+capture for card-present), refund, void, tokenize (card-on-file -> token), recurringCharge (off-session charge of a stored token), giftIssue, giftRedeem.
  - ProviderTxn states: created -> pending -> succeeded | failed | voided | refunded; carry provider_ref + amount + raw_event_ref.
  - Cash is an internal tender: recorded straight to succeeded with no port call (reconciled in the same ledger).
  - Tokens-only invariant lives here: the port signature accepts/returns token refs, brand/last4/exp — never PAN (primary account number)/CVV/track data.
- [ ] **SquareAdapter: card-present, card-on-file tokenise, recurring charge**
  Implement the Square adapter behind the port, built on SPIKE-SQUARE.
  - Map domain calls to Square Payments/Cards/Refunds APIs; card-present via terminal, card-on-file via Cards API.
  - recurringCharge does an off-session charge of a stored card token (the autopay (automatic recurring billing) path the membership story consumes).
  - Idempotency keys on every charge; map Square error/decline codes to a normalised result the dunning (the retry-and-chase on a failed recurring charge) logic can branch on.
  - OAuth/app credentials stored encrypted in config; tenant -> Square location mapping.
- [ ] **Webhook intake + ProviderTxn reconciliation; tokens-only enforcement**
  Close the loop between async processor events and our ledger.
  - Subscribe to Square webhooks (payment updated, refund updated, dispute created); verify signatures; update the matching ProviderTxn idempotently.
  - A dispute event raises a Job (PRD-07 Follow-ups) and is surfaced to the owner-only finance view.
  - Enforce the tokens-only invariant at the persistence boundary: reject/strip any PAN (primary account number)/CVV; assert only token_ref + brand/last4/exp are stored (PCI-DSS card-security standard, ADR-0007).
