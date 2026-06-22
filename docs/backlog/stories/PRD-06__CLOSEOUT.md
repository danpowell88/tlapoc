# Daily closeout & reconciliation

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want a daily closeout that balances card and cash, so that the till reconciles every day.
End-of-day closeout balances card + cash (REQ-PAY-4).

## How it works

An end-of-day closeout balances card + cash for the day and surfaces variances. Figures are owner-gated and reconcile to the Xero posting (PRD-10).
The daily till-reconciliation routine.

## Requirements

- A daily closeout that balances card and cash.

## Acceptance Criteria

- [ ] Closeout summarises card + cash tenders for the day.
- [ ] Variances are surfaced.
- [ ] Closeout figures are owner-gated.
- [ ] Closeout reconciles to the Xero posting (PRD-10).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout -> daily closeout (checkout.png) — card vs cash totals for the day, variance highlight; owner-only figures.
- Also surfaced on the back-office tablet (backroom.png).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Closeout** — id, tenant_id, location_id, date, card_total, cash_total, variance, closed_by
  - _Reconciles to Xero (PRD-10)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Closeout — id, tenant_id, location_id, date, card_total, cash_total, variance, closed_by (Reconciles to Xero (PRD-10).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Closeout summarises card + cash tenders for the day.
  - Rule: Variances are surfaced.
  - Rule: Closeout figures are owner-gated.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-06/POS.
- [ ] **Web UI**
  Build on the Angular web app: the checkout per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Checkout -> daily closeout (checkout.png) — card vs cash totals for the day, variance highlight; owner-only figures.
  - Also surfaced on the back-office tablet (backroom.png).
