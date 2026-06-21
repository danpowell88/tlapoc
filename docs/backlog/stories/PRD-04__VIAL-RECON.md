# Vial / unit reconciliation

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/VIAL-RECON`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a owner, I want vial/unit reconciliation across draws and wastage, so that stock, billing and the medicine register always agree.
Units drawn vs vial size + wastage must reconcile so stock, billing and the register agree (C8).

## Requirements

- Vial/unit reconciliation across draws and wastage.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
- [ ] Discrepancies are surfaced.
- [ ] Reconciliation data feeds reporting (PRD-08).
- [ ] Partial-vial handling is supported.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C8); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
