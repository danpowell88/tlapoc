# PRD-04 — Consult, prescribing & S4 medicines governance (the moat)

> **Stage / Milestone:** M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05)  ·  **Phase:** 1  ·  **Stories:** 23

The defensible core. Every S4 administration is provably tied to a synchronous consult, an individual prescription, valid consent, and a batch/lot drawn from lawfully-supplied, ARTG-approved stock held under correct custody. QLD S4 + TGA rules implemented as enforced invariants, producing an audit-ready medicine register and a lot→clients recall lookup. Highest-risk module — build right after PRD-01, with a legal review of the requirements first.

**Source PRD:** `docs/prds/PRD-04-consult-prescribing-s4.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CONSULT` | [Synchronous consult record](../stories/PRD-04__CONSULT.md) | Story | P0 | 5 | 3 |
| `PRESCRIPTION` | [Individual prescription (no batch / no async)](../stories/PRD-04__PRESCRIPTION.md) | Story | P0 | 5 | 3 |
| `PRODUCT-CATALOGUE` | [Medicines & product catalogue — core typed catalogue + S4 classification (MVP)](../stories/PRD-04__PRODUCT-CATALOGUE.md) | Story | P0 | 5 | 2 |
| `PRODUCT-CATALOGUE-CARDS` | [Product catalogue: per-product on-hand cards, usage history & below-par](../stories/PRD-04__PRODUCT-CATALOGUE-CARDS.md) | Story | P2 | 2 | 2 |
| `PRODUCT-CATALOGUE-FANOUT` | [Product catalogue: schedule-change classification fan-out + audit](../stories/PRD-04__PRODUCT-CATALOGUE-FANOUT.md) | Story | P2 | 2 | 2 |
| `ADMIN-GATE` | [Administration gating & immutable record](../stories/PRD-04__ADMIN-GATE.md) | Story | P0 | 5 | 3 |
| `STOCK-RECEIVE` | [Stock receipt: ARTG & lawful-supply provenance per lot (MVP)](../stories/PRD-04__STOCK-RECEIVE.md) | Story | P0 | 5 | 2 |
| `STOCK-RECEIVE-PO-SIGNER` | [S4 purchase orders: prescriber-signer & approved-wholesaler gate](../stories/PRD-04__STOCK-RECEIVE-PO-SIGNER.md) | Story | P2 | 2 | 2 |
| `STOCK-OVERVIEW` | [Stock at-a-glance: KPI tiles (MVP)](../stories/PRD-04__STOCK-OVERVIEW.md) | Story | P1 | 3 | 2 |
| `STOCK-OVERVIEW-USAGE` | [Stock overview: usage-history chart](../stories/PRD-04__STOCK-OVERVIEW-USAGE.md) | Story | P2 | 2 | 1 |
| `STOCK-OVERVIEW-NUDGES` | [Stock overview: reduce-waste & lift-margin nudges (FEFO, non-S4)](../stories/PRD-04__STOCK-OVERVIEW-NUDGES.md) | Story | P2 | 2 | 2 |
| `CUSTODY-STORAGE` | [Custody & secure storage: exclusive-custody binding (MVP)](../stories/PRD-04__CUSTODY-STORAGE.md) | Story | P0 | 5 | 2 |
| `CUSTODY-CABINET-MONITOR` | [Custody & storage: access-logged cabinet monitor (CM-01)](../stories/PRD-04__CUSTODY-CABINET-MONITOR.md) | Story | P2 | 2 | 2 |
| `COLD-CHAIN` | [Temperature logging & excursion alerts (manual + ESP32) (MVP)](../stories/PRD-04__COLD-CHAIN.md) | Story | P1 | 3 | 3 |
| `COLD-CHAIN-COMMERCIAL-LOGGERS` | [Cold chain: commercial-logger adapters (Testo / Dickson / LogTag)](../stories/PRD-04__COLD-CHAIN-COMMERCIAL-LOGGERS.md) | Story | P2 | 2 | 1 |
| `VIAL-RECON` | [Vial / unit reconciliation](../stories/PRD-04__VIAL-RECON.md) | Story | P1 | 3 | 3 |
| `RECALL-LOOKUP` | [Lot → clients recall lookup & medicine register (MVP)](../stories/PRD-04__RECALL-LOOKUP.md) | Story | P0 | 5 | 2 |
| `RECALL-EXECUTION` | [Recall execution & acknowledgement tracking](../stories/PRD-04__RECALL-EXECUTION.md) | Story | P2 | 2 | 2 |
| `WASTAGE-DESTRUCTION` | [Wastage recording (partial-vial) (MVP)](../stories/PRD-04__WASTAGE-DESTRUCTION.md) | Story | P1 | 3 | 2 |
| `DESTRUCTION-RECORDS` | [Witnessed destruction & disposal records (licensed/RUM + certificate)](../stories/PRD-04__DESTRUCTION-RECORDS.md) | Story | P2 | 2 | 2 |
| `STOCKTAKE` | [Stocktake & discrepancy surfacing (MVP)](../stories/PRD-04__STOCKTAKE.md) | Story | P1 | 3 | 2 |
| `STOCK-LOSS-THEFT` | [Loss / theft reporting from a stock discrepancy](../stories/PRD-04__STOCK-LOSS-THEFT.md) | Story | P2 | 2 | 2 |
| `MODE-B` | [Mode B pharmacy-dispensing model (placeholder)](../stories/PRD-04__MODE-B.md) | Story | P2 | 1 | 1 |

_Totals: 23 stories · 48 tasks._
