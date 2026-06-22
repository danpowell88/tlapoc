# Compliance: lot → clients recall lookup

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH-RECALL`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`, `PRD-04/RECALL-LOOKUP`

## Background

As a compliance officer, I want to look up every client treated from a given medicine lot, so that a lot safety notice can be turned into a recall instantly.
Plainly: type in a medicine lot number and instantly get every client treated from that lot, with treatment date and contactability — the lookup that turns a product safety notice into a recall list. Where it fits: a follow-up to the compliance dashboards core (PRD-08/COMPLIANCE-DASH) that reuses the Injectables recall lookup (PRD-04/RECALL-LOOKUP) over the administration-register projection. It is the input both to the recall campaign (gov-recalls / DAEN) and the S4 register export; the result set is itself audit-logged as a sensitive read. No money figures.

## How it works

The lot → clients recall lookup takes a lot (batch) number and returns every client treated from that lot, with treatment date and contactability. It is the input both to the recall campaign (gov-recalls / DAEN) and the S4 register export (PRD-08/COMPLIANCE-DASH-S4REGISTER) — a lot safety notice becomes an actionable recall list rather than a manual hunt.
It reuses the Injectables recall lookup (PRD-04/RECALL-LOOKUP) over the administration-register projection, so it must be instant at clinic volumes (an indexed projection, never an OLTP scan). Because it returns who-was-treated-with-what, the result set is itself audit-logged as a sensitive read (ADR-0010). No money figures appear.

## Requirements

- To look up every client treated from a given medicine lot.

## Acceptance Criteria

- [ ] Given a lot number, the lookup returns every client treated from that lot with treatment date and contactability.
- [ ] It reuses PRD-04 RECALL-LOOKUP over the administration-register projection.
- [ ] It is instant at clinic volumes (indexed projection, not an OLTP scan).
- [ ] The result set is itself audit-logged as a sensitive read; no money figures.

## UI designs / screenshots

- Prototype: Governance → Overview register exports — the lot-recall lookup (enter a lot, return affected clients).
- Reuses PRD-04 RECALL-LOOKUP; instant at clinic volumes; the result set is audit-logged as a sensitive read; no money figures.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) LotRecallLookup** — lot_ref → [{client_id, treatment_date, contactability}]
  - _Reuses PRD-04/RECALL-LOOKUP over the administration-register projection (indexed, not OLTP); the lookup itself is audited as a sensitive read._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Lot → clients recall lookup**
  Behaviour: given a lot number, return every client treated from that lot with treatment date and contactability — the input both to the recall campaign (gov-recalls / DAEN) and the register export. Requirements: reuse PRD-04 RECALL-LOOKUP over the administration-register projection; must be instant at clinic volumes (indexed projection, not an OLTP scan); the result set is itself audit-logged as a sensitive read.
