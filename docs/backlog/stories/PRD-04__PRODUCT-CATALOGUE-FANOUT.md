# Product catalogue: schedule-change classification fan-out + audit

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRODUCT-CATALOGUE-FANOUT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a owner, I want an S4-flag change to re-classify a product across rewards and public naming at once, and be audited, so that a compliance-load-bearing classification change is consistent everywhere and explainable to a regulator.
Plainly: when someone flips a product's S4 (Schedule 4 prescription-only medicine) flag, that one change must instantly re-classify the product everywhere — what the rewards engine may discount and how the public booking page names and prices it — and the change must be logged. Where it fits: a follow-up to PRD-04/PRODUCT-CATALOGUE that adds the cross-module propagation and audit on top of the toggle the basic already provides. The schedule column is the single source the rewards engine (PRD-06) and the public booking page (PRD-07) read.

## How it works

This follow-up makes the S4 toggle load-bearing across the platform. The schedule(S4|non-S4) column the basic maintains is the single source of truth; the rewards engine (PRD-06) and the public booking page (PRD-07) read it directly rather than holding their own copy that could drift.
Toggling a product to S4 immediately excludes it from rewards (rewards may never apply to an S4 prescription-only medicine — C9) and switches the public booking page to the generic-naming / withheld-price policy for that product; toggling back reverses both.
Every catalogue mutation that matters — a product add, a remove, and every schedule toggle — writes an AuditEvent to the append-only stream so a regulator can see exactly when and by whom a compliance-load-bearing classification changed.

## Requirements

- An S4-flag change to re-classify a product across rewards and public naming at once, and be audited.

## Acceptance Criteria

- [ ] Setting the S4 flag re-classifies the product everywhere at once: the rewards engine (PRD-06) immediately excludes it (rewards may never apply to an S4 prescription-only medicine, C9).
- [ ] The public booking page (PRD-07) applies the generic-naming / withheld-price policy to a newly-S4 product.
- [ ] The schedule(S4|non-S4) column is the single source those modules read — no second copy that could drift.
- [ ] Every product add/remove and every schedule toggle writes an AuditEvent to the append-only stream.

## UI designs / screenshots

- Prototype screen: Stock & medicines — Products catalogue (stock.png, 'Products' button).
- Toggling the S4 pill on a product row immediately re-renders the rewards-eligibility and public-naming behaviour for that product.
- An audit entry is written for each add/remove/toggle (surfaced in the governance audit view).

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **AuditEvent** — id, tenant_id, actor_id, at, entity('product'), entity_id, action(add|remove|schedule_toggle), detail
  - _Extends the basic's model — no new product fields; the append-only audit of classification changes (ADR-0010)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Schedule-change fan-out to rewards + public naming**
  Behaviour: setting the S4 flag re-classifies the product everywhere at once — the rewards engine (PRD-06) excludes it (C9) and the public booking page (PRD-07) applies generic-naming / withheld-price. Requirements: the schedule(S4|non-S4) column is the single source those modules read; no denormalised second copy.
- [ ] **Catalogue-change audit trail**
  Behaviour: every product add/remove and every schedule toggle writes an AuditEvent to the append-only stream (ADR-0010). Requirements: a compliance-load-bearing classification change must be explainable to a regulator — who changed what and when.
