# Medicines & product catalogue — core typed catalogue + S4 classification (MVP)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRODUCT-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend

## Background

As a owner, I want a product catalogue where each product has a type, unit, S4 flag and regulatory metadata, so that the right rules apply to each product across the platform.
Plainly: this is the list of everything the clinic stocks and sells — each toxin, filler, skin product and retail item — tagged with what it is and how it is regulated. The single most important tag is whether a product is an S4 (Schedule 4 prescription-only medicine). Where it fits: it underpins the whole moat. The S4 flag set here is read everywhere — it decides which lots flow through the prescribe→administer chain (PRD-04), what the rewards engine may never discount (PRD-06) and how a product is named on the public booking page (PRD-07). Stock receipt (PRD-04/STOCK-RECEIVE) and lots hang off these products.  A typed, multi-unit catalogue (toxin/filler/skin/retail) with the S4 flag — the single classification driving rewards eligibility and public-page naming — plus regClass/ARTG/compounded for GLP-1 handling (ADR-0014/0021).

## How it works

The catalogue is the single source of truth for product classification. Per ADR-0021/0014 each product is typed (toxin/filler/skin/retail) with its own unit (toxin 'units' vs filler 'syringes/mL'), a par level, expiry tracking and an S4 flag. The S4 flag is the master classification that drives rewards eligibility (PRD-06, non-S4 only — C9) and public-booking-page naming (PRD-07) everywhere.
Rev-4 extends the catalogue to filler-as-medicine and weight-loss GLP-1 programs: products carry regClass / ARTG / compounded metadata so the platform can block prohibited compounded GLP-1 (banned 1 Oct 2024) and route adverse events to the correct DAEN dataset (medicine vs device).
A capability-gated catalogue admin (prescriber/owner) adds/removes products and sets the S4 flag, type, unit and par. On-hand / usage / wastage / expiry aggregate per product + unit, never across units — a single 'units on hand' across a toxin and a filler is meaningless (ADR-0021).
Lots (StockItem) belong to a product; the product's unit governs all lot quantities. Toggling the S4 flag re-classifies the product everywhere at once: the rewards engine immediately excludes it, and the public booking page applies the generic-naming/withheld-price policy.
regClass + compounded enable two rules: block receiving/holding prohibited compounded GLP-1, and tag the product so a downstream adverse event is routed to DAEN-medicines (toxin) vs DAEN-medical-devices (device-class filler) in PRD-08.
Retail (non-S4) SKUs live in the same catalogue alongside medicines so the same classification and stock machinery serves both.

## Requirements

- A product catalogue where each product has a type, unit, S4 flag and regulatory metadata.

## Acceptance Criteria

- [ ] Typed products each with their own unit (units vs syringes), par, expiry tracking.
- [ ] Capability-gated product admin sets the S4 flag (drives PRD-06 rewards + PRD-07 naming).
- [ ] Products carry regClass/artg/compounded; prohibited compounded GLP-1 is blocked.
- [ ] Retail (non-S4) SKUs supported alongside medicines.

## UI designs / screenshots

- Prototype screen: Stock & medicines — Products catalogue (stock.png, 'Products' button).
- 'Products' opens the catalogue modal: rows of typed products with name, type, unit, par, an S4 toggle pill ('S4 ✓' / 'non-S4'), per-product on-hand, and a Remove action.
- Toggling S4 re-renders the stock view and the lot-detail S4 badge live — one classification point.
- Product cards on the main screen show on-hand, used/wasted (90d), a usage sparkline and a 'below par' state per product (e.g. 'reorder 2').
- Add-product form: name, type, unit, par, S4 checkbox — capability-gated to prescriber/owner.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **Product** — id, tenant_id, name, type(toxin|filler|skin|retail), unit(units|syringes|each), schedule(S4|non-S4), reg_class, artg_no, sponsor, compounded(bool), par_level, color
  - _schedule flag is the master classification (ADR-0014/0021): drives rewards (non-S4 only, C9) + public naming. Prototype mapping: the products[] catalogue + toggleS4()/addProduct()._
- **ProductAggregate (read model)** — product_id, unit, on_hand, used_90d, wasted_90d, below_par(bool)
  - _Computed per product+unit, never across units (ADR-0021). Mapping: prodAgg() in the prototype._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0021](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0025](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Product entity + S4 classification (model & migration)**
  Behaviour: add the Product table — id, tenant_id, name, type(toxin|filler|skin|retail), unit(units|syringes|each), schedule(S4|non-S4), reg_class, artg_no, sponsor, compounded(bool), par_level, color — RLS-scoped by tenant. Requirements: the schedule(S4|non-S4) flag is the master classification the whole platform reads (rewards eligibility, public naming); unit is fixed at creation and governs every lot quantity under the product so on-hand is only ever aggregated per product+unit, never across a toxin's units and a filler's syringes (ADR-0021).
- [ ] **Products catalogue table + add-product form (typed rows + S4 toggle pill)**
  Behaviour: the 'Products' modal lists every product as a row — name, type, unit, par level, an S4 toggle pill ('S4 ✓' / 'non-S4'), per-product on-hand in that product's unit, and a Remove action; an add-product form captures name, type, unit, par and an S4 checkbox (prototype renderCatalog/toggleS4/removeProduct/addProduct). Requirements: toggling the S4 pill re-renders the stock view and the lot-detail S4 badge live, in one place; the toggle, add and Remove are capability-gated to prescriber/owner and non-owner stock roles see the table read-only; on create, a compounded GLP-1 (Glucagon-Like Peptide-1) product is refused (prohibited compounded GLP-1, banned 1 Oct 2024).
