# Business dashboards: custom range & per-practitioner filter

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-FILTERS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a custom date range and a per-practitioner filter on the business dashboards, so that I can scope every metric to any window or to a single clinician.
Plainly: extends the business dashboard's date control with a custom (any-dates) range and a per-practitioner switch, so the owner can slice every tile to an arbitrary window or to one clinician. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that adds the richer scoping on top of the 7d/30d/90d presets that ship in the basic. It re-queries the same reporting read-models (PRD-08/READ-MODELS) the core does, and the selection persists per user as the single source of truth every band reads from. Money figures stay owner-only (.fin).

## How it works

The business dashboard core (PRD-08/BUSINESS-DASH) ships the 7d/30d/90d date presets. This follow-up adds the two richer scoping controls the prototype shows: a custom date range (arbitrary start/end) and a per-practitioner switch, so the owner can ask 'how did April look' or 'how is this one injector doing' rather than only the fixed windows.
Changing the range or the practitioner re-queries the reporting read-models (PRD-08/READ-MODELS) — never OLTP — and re-computes every tile against the matching comparison window. The selection persists per user and is the single source of truth all the metric bands and the Insights strip read from, so the whole screen stays consistent. Money figures remain owner-only (.fin) under any slice.

## Requirements

- A custom date range and a per-practitioner filter on the business dashboards.

## Acceptance Criteria

- [ ] A custom date range (any start/end) is available alongside the 7d/30d/90d presets from the core.
- [ ] A per-practitioner switch re-scopes every tile on the screen to one clinician.
- [ ] Changing the range or practitioner re-queries the read-models (not OLTP) and re-computes every tile against the matching comparison window.
- [ ] The selection persists per user and is the single source of truth all bands and callouts read from; money figures stay owner-only (.fin).

## UI designs / screenshots

- Prototype: Reports header — the custom-range control beside the 7d/30d/90d presets and the per-practitioner switch; the sub-header echoes the active window ('last 30 days · figures synthetic').
- Changing the range/practitioner re-scopes every tile; the selection persists per user; money figures stay .fin-gated (owner-only).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics (extends PRD-08/BUSINESS-DASH)** — adds custom date-range + per-practitioner slicing as query parameters over the existing projection
  - _No new entity — extends the BusinessMetrics query with custom-range + practitioner parameters; money fields stay owner-gated._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Custom range + per-practitioner query over the business read-models**
  Behaviour: extend the BusinessMetrics query (PRD-08/BUSINESS-DASH) with a custom date range (any start/end) and a per-practitioner slice as query parameters over the read schema, never OLTP. Requirements: re-compute every tile against the matching comparison window; money fields stay owner-financial (stripped for non-owner roles).
- [ ] **Custom-range + per-practitioner controls (persisted, single source of truth)**
  Behaviour: a custom-range control beside the presets and a per-practitioner switch that re-scope every tile and the Insights strip; the sub-header echoes the active window. Requirements: the selection persists per user and is the single source of truth all bands read from; changing it re-queries the read-models; money figures stay .fin-gated (owner-only).
