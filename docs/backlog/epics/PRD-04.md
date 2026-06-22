# PRD-04 — Consult, prescribing & S4 medicines governance (the moat)

> **Stage / Milestone:** M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05)  ·  **Phase:** 1  ·  **Stories:** 12

The defensible core. Every S4 administration is provably tied to a synchronous consult, an individual prescription, valid consent, and a batch/lot drawn from lawfully-supplied, ARTG-approved stock held under correct custody. QLD S4 + TGA rules implemented as enforced invariants, producing an audit-ready medicine register and a lot→clients recall lookup. Highest-risk module — build right after PRD-01, with a legal review of the requirements first.

**Source PRD:** `docs/prds/PRD-04-consult-prescribing-s4.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CONSULT` | [Synchronous consult record](../stories/PRD-04__CONSULT.md) | Story | P0 | 5 | 3 |
| `PRESCRIPTION` | [Individual prescription (no batch / no async)](../stories/PRD-04__PRESCRIPTION.md) | Story | P0 | 5 | 3 |
| `PRODUCT-CATALOGUE` | [Medicines & product catalogue (S4 classification)](../stories/PRD-04__PRODUCT-CATALOGUE.md) | Story | P0 | 5 | 3 |
| `ADMIN-GATE` | [Administration gating & immutable record](../stories/PRD-04__ADMIN-GATE.md) | Story | P0 | 5 | 3 |
| `STOCK-RECEIVE` | [Stock receipt, ARTG & lawful-supply provenance](../stories/PRD-04__STOCK-RECEIVE.md) | Story | P0 | 5 | 3 |
| `CUSTODY-STORAGE` | [Custody & secure storage](../stories/PRD-04__CUSTODY-STORAGE.md) | Story | P0 | 5 | 3 |
| `COLD-CHAIN` | [Temperature logging & excursion alerts](../stories/PRD-04__COLD-CHAIN.md) | Story | P1 | 3 | 4 |
| `VIAL-RECON` | [Vial / unit reconciliation](../stories/PRD-04__VIAL-RECON.md) | Story | P1 | 3 | 3 |
| `RECALL-LOOKUP` | [Lot → clients recall lookup & medicine register](../stories/PRD-04__RECALL-LOOKUP.md) | Story | P0 | 5 | 3 |
| `WASTAGE-DESTRUCTION` | [Wastage, disposal & destruction records](../stories/PRD-04__WASTAGE-DESTRUCTION.md) | Story | P1 | 3 | 3 |
| `STOCKTAKE` | [Stocktake, discrepancy & loss/theft reporting](../stories/PRD-04__STOCKTAKE.md) | Story | P1 | 3 | 3 |
| `MODE-B` | [Mode B pharmacy-dispensing model (placeholder)](../stories/PRD-04__MODE-B.md) | Story | P2 | 1 | 1 |

_Totals: 12 stories · 35 tasks._
