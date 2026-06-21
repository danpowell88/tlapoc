# Stock receipt, ARTG & lawful-supply provenance

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-RECEIVE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

Consult, prescribing & S4 medicines governance (the moat) — The defensible core.

As a prescriber/owner, I want to receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source, so that we only hold lawfully-supplied, approved medicine.

S4 stock is received from a TGA-approved wholesaler with ARTG status, brand, sponsor and lawful supply source recorded; non-ARTG/unverified source is warned/blocked (C11). S4 POs require a prescriber signer.

## Requirements

- To receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source.
- Traces to requirement(s): REQ-MED-6, REQ-MED-2.
- Must satisfy compliance obligation(s): C11.

## Acceptance Criteria

- [ ] Receiving records ARTG status, brand, sponsor and supply source per lot.
- [ ] Receiving non-ARTG or unverified-source stock is warned/blocked per config.
- [ ] S4 purchase orders require a prescriber signer + TGA-approved wholesaler.
- [ ] ARTG validation supports manual entry (lookup against an ARTG dataset is an open option).

## UI designs / screenshots

prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-04/PRODUCT-CATALOGUE.

## Other

Epic: PRD-04 — Consult, prescribing & S4 medicines governance (the moat).
Source PRD: docs/prds/PRD-04-consult-prescribing-s4.md.
Backlog key: PRD-04/STOCK-RECEIVE.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C11.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C11); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
