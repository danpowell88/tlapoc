# Medicines & product catalogue (S4 classification)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRODUCT-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend

## Background

As a owner, I want a product catalogue where each product has a type, unit, S4 flag and regulatory metadata, so that the right rules apply to each product across the platform.
A typed, multi-unit catalogue (toxin/filler/skin/retail) with the S4 flag — the single classification driving rewards eligibility and public-page naming — plus regClass/ARTG/compounded for GLP-1 handling (ADR-0014/0021).

## Requirements

- A product catalogue where each product has a type, unit, S4 flag and regulatory metadata.

## Acceptance Criteria

- [ ] Typed products each with their own unit (units vs syringes), par, expiry tracking.
- [ ] Capability-gated product admin sets the S4 flag (drives PRD-06 rewards + PRD-07 naming).
- [ ] Products carry regClass/artg/compounded; prohibited compounded GLP-1 is blocked.
- [ ] Retail (non-S4) SKUs supported alongside medicines.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0021](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0025](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (see Other); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
