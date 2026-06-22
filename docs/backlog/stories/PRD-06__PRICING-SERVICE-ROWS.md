# Pricing & what-if: editable service-pricing rows

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-SERVICE-ROWS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PRICING-WHATIF`

## Background

As a owner, I want editable service-pricing rows that feed the projection, so that I can model service price changes alongside membership ones.
Plainly: rows for the clinic's services (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) with their volume and projected monthly revenue, editable as what-if inputs. Where it fits: a follow-up to the pricing core (PRD-06/PRICING-WHATIF), which handles membership plan prices; this adds the service-pricing side to the same Projected-impact panel. Editing is a what-if input only; volumes read from PRD-08 read-models. Owner-only (.fin).

## How it works

Editable service-pricing rows (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) with per-service volume and projected monthly revenue feed the same Projected-impact panel as the pricing core (PRD-06/PRICING-WHATIF).
'per-treatment price · assumes volume holds' is stated; editing is a what-if input only; volumes read from PRD-08 read-models. Owner-only (.fin).

## Requirements

- Editable service-pricing rows that feed the projection.

## Acceptance Criteria

- [ ] Editable service-pricing rows (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) show per-service volume and projected monthly revenue.
- [ ] Editing a service price is a what-if input only; it feeds the same Projected-impact panel.
- [ ] 'per-treatment price · assumes volume holds' is stated; volumes read from PRD-08 read-models.
- [ ] Owner-only (.fin).

## UI designs / screenshots

- Prototype: Pricing & what-if — editable Service pricing rows (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) with volume + projected revenue.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(extends PRD-06/PRICING-WHATIF projection)** — + service price/volume inputs → service rev/mo projection
  - _No new entity; volumes from PRD-08 read-models; owner-only (.fin)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Editable service-pricing rows + projection**
  Behaviour: editable service-pricing rows (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) with per-service volume and projected monthly revenue feed the Projected-impact panel. Requirements: 'per-treatment price · assumes volume holds' stated; what-if input only; volumes from PRD-08 read-models; owner-only (.fin).
