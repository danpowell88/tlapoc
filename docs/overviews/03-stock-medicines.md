# Stock & medicines — overview

> The S4 medicines ledger and product catalogue: secure custody, batch-lot traceability, cold-chain,
> wastage and reconciliation — the evidence trail behind every treatment. Primary owners:
> **Nurse Practitioner** (custody + catalogue), **Lead Nurse** (day-to-day stock).

## What's in this area

| Function | What it does | When it's used | Primary role(s) |
|---|---|---|---|
| Product catalogue | Typed products (toxin/filler/skin/device) with unit, par, **S4 flag**, ARTG, modality class | Setup + maintenance | NP, Owner |
| Lots / batches | Per-product batches with expiry, on-hand, location, temperature | Receiving + dispensing | NP, Lead |
| Receive stock | Book in a delivery against a product + lot | On delivery | NP (custody) |
| Cold-chain | Per-lot temperature; twice-daily fridge log; excursion → quarantine | Daily | Lead, Reception |
| Wastage & reconciliation | Vial reconciliation, wastage log, stocktake | Per session / periodic | Lead, NP |
| Recall lookup | Lot → exact client list (instant) | On a recall | NP, Owner |
| Expiry / par alerts | FEFO use-first prompts; below-par signals | Continuous | Lead |

## Workflows

### 1 · Receive → custody → dispense → reconcile  — *NP / Lead*

```mermaid
flowchart TD
  A[Delivery arrives] --> B[NP receives against product + lot<br/>verify ARTG + lawful supply]
  B --> C[Lot enters secure custody<br/>fridge for cold-chain items]
  C --> D[Charting selects this lot<br/>in-date, FEFO]
  D --> E[Finalise deducts units from the lot]
  E --> F[Vial reconciliation + wastage logged]
  F --> G[Periodic stocktake reconciles on-hand]
```

### 2 · Cold-chain breach pathway  — *Reception logs, Lead acts*

```mermaid
flowchart TD
  A[Twice-daily fridge reading] --> B{Within 2-8 C?}
  B -->|Yes| C[Logged - all good]
  B -->|No| D[Affected lots flagged Do not use]
  D --> E[Quarantine - do not discard]
  E --> F[Breach job to Lead Nurse]
  F --> G[Notify state health dept]
  G --> H{Advice}
  H -->|Use| C
  H -->|Destroy| I[Destruction record + register update]
```

### 3 · Recall from a lot  — *NP / Owner*

```mermaid
flowchart LR
  A[Sponsor field-safety notice<br/>names a lot] --> B[Lot to exact client list]
  B --> C[Authorise recall - NP/Owner]
  C --> D[Run safety campaign - Governance]
  D --> E[Track acknowledgements]
```

## Roles at a glance

| Role | Responsibilities in this area |
|---|---|
| **Nurse Practitioner** | S4 custody, receive stock, manage the catalogue + S4 flag, recall authorisation |
| **Lead Nurse** | Day-to-day stock, cold-chain integrity, wastage, par/expiry, stocktake |
| **Reception** | Logs fridge temps as part of open/close |
| **Owner** | Read-only oversight; sees stock-on-hand and expiry on the dashboard |

## Related

- Requirements: `REQ-MED-4/7/11/12/13/14/15`, compliance `C8/C11/C13/C15..C17`
- ADRs: **ADR-0021** (multi-product/unit catalogue), **ADR-0014** (S4 flag drives rewards/ads), **ADR-0008** (compliance by construction)
- PRDs: [PRD-04](../prds/PRD-04-consult-prescribing-s4.md)
