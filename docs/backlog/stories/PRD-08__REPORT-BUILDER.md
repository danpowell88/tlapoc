# Custom report builder / external BI (placeholder)

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/REPORT-BUILDER`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web

## Background

As a owner, I want to build custom reports and benchmark against other clinics, so that I can answer bespoke questions.
A custom report builder, external BI warehouse and cross-clinic benchmarking are Phase 2+. Placeholder.

## How it works

Placeholder (Phase 2+). A custom report builder (user-defined queries/columns over the reporting read-models), an external BI warehouse export, and cross-clinic benchmarking are out of scope for v1, which ships fixed dashboards + register exports. Captured now so the read-model layer (READ-MODELS) stays export-friendly and query-stable — the projections are the substrate a builder would sit on, so no architectural rework is needed when this is pulled into a sprint.
No build in v1; design-only when scheduled.

## Requirements

- To build custom reports and benchmark against other clinics.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2+; v1 ships fixed dashboards + register exports.
- [ ] Captured so the read-model layer stays export-friendly (a builder sits on the existing projections).
- [ ] No build in v1; scope/design when pulled into a sprint.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports (reports.png) — v1 ships the fixed tabs; a custom builder is not represented (concept only).
- Future: a query/column picker over the read-models + a benchmarking view; design-only for now.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(future) CustomReport** — user-defined query/columns over the reporting read-models
  - _Phase 2+; sits on the existing projections (no OLTP access)._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1. When scheduled, confirm it still fits scope (fixed dashboards + exports remain the v1 contract), then design the builder as a query/column picker over the reporting read-models (never OLTP) plus the benchmarking data-sharing/anonymisation question. Verify the read-model layer is still export-friendly before committing.
