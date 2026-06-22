# In-person POS checkout (card + cash)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a front desk, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.
Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split, tips and surcharge config (REQ-PAY-2). Financial figures are owner-gated.

## How it works

Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split payments, tips and surcharge config. Both card and cash appear in the daily closeout. Online one-off checkout is deferred; financial figures respect the owner-only capability.
The everyday till for the clinic.

## Requirements

- To take payment in person by Square card or recorded cash with receipts and split/partial support.

## Acceptance Criteria

- [ ] A sale completes by Square card or recorded cash; both appear in the daily closeout.
- [ ] Receipts, partial/split payments, tips and surcharge config supported.
- [ ] Money figures respect the owner-only financial capability (reception sees no money totals beyond the sale).
- [ ] Online one-off checkout is not exposed (deferred).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout (checkout.png) — line items (service/retail/package), tender selection (Square card / cash / gift card), receipt, partial/split, tips; S4 items show no reward/discount controls (C9).
- Reception sees the sale but not owner-only money totals.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Invoice** — id, tenant_id, client_id, lines[]{type, ref, qty, price, gst}, total, status
  - _Lines carry the service/product schedule flag._
- **Payment** — id, invoice_id, tender(card|cash|giftcard), amount, token_ref?, tip, surcharge, at
  - _Appears in Closeout; posts to Xero (PRD-10)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Invoice — id, tenant_id, client_id, lines[]{type, ref, qty, price, gst}, total, status (Lines carry the service/product schedule flag.)
  - Payment — id, invoice_id, tender(card|cash|giftcard), amount, token_ref?, tip, surcharge, at (Appears in Closeout; posts to Xero (PRD-10).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A sale completes by Square card or recorded cash; both appear in the daily closeout.
  - Rule: Receipts, partial/split payments, tips and surcharge config supported.
  - Rule: Money figures respect the owner-only financial capability (reception sees no money totals beyond the sale).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-06/PAYMENT-PROVIDER.
- [ ] **Web UI**
  Build on the Angular web app: the checkout per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Checkout (checkout.png) — line items (service/retail/package), tender selection (Square card / cash / gift card), receipt, partial/split, tips; S4 items show no reward/discount controls (C9).
  - Reception sees the sale but not owner-only money totals.
