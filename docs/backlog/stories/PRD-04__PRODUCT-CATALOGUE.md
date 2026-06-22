# Medicines & product catalogue (S4 classification)

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

- [ ] **Products catalogue table (typed rows + S4 toggle pill)**
  Behaviour: the 'Products' modal lists every product as a row — name, type(toxin|filler|skin|retail), unit, par level, an S4 toggle pill ('S4 ✓' / 'non-S4'), per-product on-hand in that product's unit, and a Remove action (prototype renderCatalog/toggleS4/removeProduct). Requirements: the schedule(S4|non-S4) flag is the master classification — toggling it re-renders the stock view and the lot-detail S4 badge live, in one place; on-hand shown per product is its own-unit aggregate only (never summed across a toxin's units and a filler's syringes, ADR-0021). The toggle and Remove are capability-gated to prescriber/owner; non-owner stock roles see the table read-only.
- [ ] **Add-product form (type, unit, par, S4)**
  Behaviour: an add-product form captures name, type, unit (units vs syringes vs each), par level and an S4 checkbox, appending a new typed product to the catalogue (prototype addProduct). Requirements: unit is chosen at creation and governs every lot quantity under the product; reg_class/ARTG/sponsor/compounded metadata are captured here too so adverse-event DAEN routing (medicine vs device) and the GLP-1 block can key off them; on create, a compounded GLP-1 (Glucagon-Like Peptide-1) product is refused (prohibited compounded GLP-1, banned 1 Oct 2024). Capability-gated to prescriber/owner.
- [ ] **Per-product cards: on-hand, usage, below-par & sparkline**
  Behaviour: the main stock screen renders a card per product showing on-hand, used/wasted over 90 days, a usage sparkline and an S4 badge, with a 'below par' state when on-hand drops under the par level (prototype prodCards/prodAgg/spark). Requirements: each figure is computed per product+unit from the ProductAggregate read model over the StockLedger (ADR-0013) — never a cross-unit roll-up; below-par drives the reorder count on the KPI strip. Cost/margin fields, if shown, stay owner-only behind the .fin capability.
- [ ] **Schedule-change classification fan-out + audit**
  Behaviour: setting the S4 flag re-classifies the product everywhere at once — the rewards engine (PRD-06) immediately excludes it (rewards may never apply to an S4 prescription-only medicine, C9) and the public booking page (PRD-07) applies the generic-naming / withheld-price policy. Requirements: the schedule(S4|non-S4) column is the single source those modules read; every product add/remove and every schedule toggle writes an AuditEvent to the append-only stream so a compliance-load-bearing classification change is explainable to a regulator.
