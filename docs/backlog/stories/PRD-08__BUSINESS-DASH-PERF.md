# Business dashboards: PERFORMANCE band tiles

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-PERF`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a PERFORMANCE band of conversion, retention, rebooking and no-show, so that I can track operational performance against target.
Plainly: the PERFORMANCE band of the business dashboard — Conversion, Retention, Rebooking and No-show — each tile showing value, target and variance, with a green state when the target is met. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that adds the operational-performance band over the core's projection and tiles. These are operational metrics visible to managers without the owner-only financial (.fin) capability — no money figures.

## How it works

The PERFORMANCE band renders the operational-performance metrics: Conversion, Retention, Rebooking and No-show, each tile showing value, target and variance, with a green state when the target is met. No-show is read against a ceiling rather than a floor (lower is better), so its green state is the inverse of the others.
These are operational metrics computed over the appointment/lifecycle projections (PRD-08/BUSINESS-DASH BusinessMetrics) and are visible to managers without the owner-only financial (.fin) capability — there are no money figures in this band. Each tile drills into its underlying client/appointment list (e.g. from a low rebooking rate to the clients who didn't rebook).

## Requirements

- A PERFORMANCE band of conversion, retention, rebooking and no-show.

## Acceptance Criteria

- [ ] The PERFORMANCE band renders Conversion, Retention, Rebooking and No-show, each with value / target / variance.
- [ ] A green state shows when the target is met (no-show uses a ceiling, not a floor).
- [ ] These are operational metrics visible to managers without .fin (no money figures).
- [ ] Each tile drills into its underlying client/appointment list.

## UI designs / screenshots

- Prototype: Reports — the PERFORMANCE band: Conversion, Retention, Rebooking, No-show; each tile shows value / target / variance with a green state when met.
- Operational metrics visible to managers (no .fin gating); no-show uses a ceiling; tiles drill into the client/appointment list.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics (PERFORMANCE slice, extends PRD-08/BUSINESS-DASH)** — conversion, retention, rebooking, no_show_rate
  - _Extends the BusinessMetrics projection; operational metrics (no money); no-show compared against a ceiling._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **PERFORMANCE band tiles (conversion, retention, rebooking, no-show)**
  Behaviour: the PERFORMANCE band renders Conversion, Retention, Rebooking and No-show, each with value / target / variance and a green state when the target is met (no-show uses a ceiling, not a floor). Requirements: these are operational metrics visible to managers without .fin; computed over the appointment/lifecycle projections; each drills into its underlying client/appointment list.
