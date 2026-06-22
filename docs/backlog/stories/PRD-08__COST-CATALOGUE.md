# Per-procedure cost catalogue (core: cost model + editor)

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COST-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/TRUE-COST`

## Background

As a owner, I want to maintain the product, consumable and per-use device cost of each procedure in one place, so that every margin report and pricing model stays honest from a single source of truth.
Plainly: the place the owner sets, once, what each treatment actually costs to deliver — the S4/product cost, the single-use consumables (needles, tips, peels) and the per-use device cost (laser/RF tips, CoolSculpting applicators) — so the true-cost/margin reporting and the pricing planner all read the same numbers. Where it fits: a sibling of the true-cost/margin reporting (PRD-08/TRUE-COST) in the Reporting layer (step 6 of the clinic-first build); it is the INPUT surface (maintained via Settings → Cost catalogue) that feeds the margin projection and the pricing & what-if planner (PRD-06), and its consumable definitions also feed Stock so usage decrements automatically. Where TRUE-COST reports margin, this story owns the editable cost components behind it. Every figure here is money and owner-only (.fin).

## How it works

A clinic under-counts true cost when consumables and device-per-use are left out — CoolSculpting applicators and laser tips especially. This story is the per-procedure cost catalogue that fixes that: for each treatment the owner maintains the product/S4 cost, the single-use consumables cost (needles, tips, peels) and the per-use device cost (laser/RF tips, applicators), which derive a cost-per-procedure.
It is the INPUT behind the true-cost/margin report (TRUE-COST): maintain each component once and every margin report and pricing model stays honest, because they all read this catalogue rather than re-keying figures. The product/S4 unit cost still reconciles against the per-product/per-unit stock model + vial reconciliation (PRD-04 VIAL-RECON); this catalogue owns the consumable and device-per-use components.
Consumable definitions also feed Stock: defining a procedure's consumables here means finalising that treatment decrements those items automatically, rather than someone counting tips by hand. The catalogue is maintained via Settings → Cost catalogue in the live build.
Every figure here is money and is gated behind the owner financial capability (.fin) — non-owner roles never see cost inputs. Changes are audited so any margin number can be traced back to the cost inputs and the version in force when it was computed.

## Requirements

- To maintain the product, consumable and per-use device cost of each procedure in one place.

## Acceptance Criteria

- [ ] Each procedure has editable cost components: product/S4, consumables, and per-use device cost, deriving a cost-per-procedure.
- [ ] The catalogue is the single source the true-cost/margin report (TRUE-COST) and the pricing & what-if planner (PRD-06) read — change a cost once and every report stays consistent.
- [ ] Consumable definitions feed Stock so usage decrements automatically rather than being counted by hand.
- [ ] The entire surface is owner-only (.fin); non-owner roles never see cost figures.
- [ ] Cost changes are audited so a margin figure can be traced to the inputs that produced it.

## UI designs / screenshots

- Prototype: Reports → Revenue tab (reports.png) — the 'Cost inputs · per-procedure' table (repCostInputs): Treatment, Product/S4, Consumables, Device/use, Cost/procedure, with the note that demo figures are editable via Settings → Cost catalogue and that consumables feed Stock so usage decrements automatically.
- Editable per-procedure rows for the three cost components; the derived Cost/procedure updates live and flows into the True-cost & margin table above it.
- Owner-only (.fin) throughout; a change writes an audit entry.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **ProcedureCost** — id, tenant_id, service_id, product_cost, consumables_cost, device_per_use_cost, cost_per_procedure(derived), updated_at, updated_by
  - _Single source for COGS components; product_cost reconciles with VIAL-RECON (PRD-04); owner-gated (.fin); changes audited._
- **ConsumableUsage (ref)** — service_id, stock_item_id, qty_per_procedure
  - _Links a procedure's consumables to Stock so finalising a treatment decrements them automatically._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **ProcedureCost model + cost-per-procedure derivation**
  Behaviour: model ProcedureCost per service with editable product/S4, consumables and per-use device cost, deriving cost_per_procedure. Requirements: tenant-scoped (+ RLS); product cost reconciles against the per-product/per-unit stock model + VIAL-RECON (PRD-04); all fields owner-financial (.fin); changes are append-only audited so a margin figure traces to its inputs.
- [ ] **Cost catalogue editor UI (owner-only)**
  Behaviour: the Settings → Cost catalogue editor — per-procedure rows for the three cost components with a live-updating Cost/procedure, surfaced read-through on the Reports Revenue tab. Requirements: gate the entire surface behind .fin (owner-only); non-owner roles never see cost figures; edits validate and persist and write an audit entry; the note explains consumables feed Stock.
