# Cost catalogue: consumable → Stock auto-decrement

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COST-CATALOGUE-STOCK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COST-CATALOGUE`

## Background

As a owner, I want a procedure's consumable definitions to decrement Stock automatically when the treatment is finalised, so that consumable usage is counted by the system, not by hand.
Plainly: linking each procedure's consumable definitions to Stock so that finalising the treatment automatically decrements those items (needles, tips, peels) — no one counting tips by hand. Where it fits: a follow-up to the per-procedure cost catalogue core (PRD-08/COST-CATALOGUE), which owns the consumable cost components; this story turns those definitions into automatic stock movements. The decrement happens on chart finalisation (PRD-05), consistent with the existing S4 lot deduction.

## How it works

A clinic under-counts true cost — and runs out of supplies unexpectedly — when consumable usage is tracked by hand. This follow-up links each procedure's consumable definitions (from the cost catalogue, PRD-08/COST-CATALOGUE) to Stock: defining that a treatment uses N needles / tips / peels means finalising that treatment decrements those items automatically.
Quantity-per-procedure is modelled against the relevant stock items (ConsumableUsage). The decrement fires on chart finalisation (PRD-05), in the same step and consistent with the existing S4 lot deduction, so consumables and S4 stock are kept honest the same way — no hand-counting.

## Requirements

- A procedure's consumable definitions to decrement Stock automatically when the treatment is finalised.

## Acceptance Criteria

- [ ] A procedure's consumable definitions feed Stock so finalising that treatment decrements those items automatically.
- [ ] Quantity-per-procedure is modelled against stock items.
- [ ] The decrement happens on chart finalisation (PRD-05), consistent with the S4 lot deduction.
- [ ] No hand-counting of consumables.

## UI designs / screenshots

- No new screen — the catalogue's consumable definitions drive an automatic Stock decrement on chart finalisation; the catalogue note explains 'consumables feed Stock so usage decrements automatically'.
- Decrement is consistent with the S4 lot deduction on finalisation (PRD-05).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **ConsumableUsage** — service_id, stock_item_id, qty_per_procedure
  - _Links a procedure's consumables (PRD-08/COST-CATALOGUE) to Stock so finalising a treatment decrements them automatically (PRD-05)._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Consumable → Stock usage link (auto-decrement)**
  Behaviour: a procedure's consumable definitions feed Stock so finalising that treatment decrements the consumable items automatically. Requirements: model qty-per-procedure against stock items; the decrement happens on chart finalisation (PRD-05) consistent with the S4 lot deduction; no hand-counting.
