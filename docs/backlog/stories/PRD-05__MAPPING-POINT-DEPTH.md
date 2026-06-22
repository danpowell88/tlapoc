# Injection map: per-point depth, technique & multi-product lot

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING-POINT-DEPTH`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want each injection point to record depth and technique, and to pick a per-point product/lot for multi-product sessions, so that the chart captures the full clinical detail and traces each point to the right vial.
Plainly: deepens each injection point so it records not just how many units but the depth and technique used, and lets a session that uses more than one product assign a different vial per point. Where it fits: a follow-up to PRD-05/MAPPING that enriches the per-point editor beyond the basic's label + units. It adds the medico-legal detail (depth, technique/needle) an inspection expects and supports multi-product sessions, extending the InjectionPoint the basic already stores.

## How it works

This follow-up enriches the per-point editor beyond the basic's label + units (the prototype captures name + units only). Each point gains depth and technique/needle fields — the medico-legal detail an Australian Health Practitioner Regulation Agency (AHPRA) inspection expects.
It also adds optional per-point product/lot for multi-product sessions: a point defaults to the chart's selected lot (PRD-05/PRODUCT-LOT-PICKER) but can be reassigned, so a session that uses more than one product traces each point to the right vial.
Depth, technique and per-point lot persist on the InjectionPoint and survive draft sync; read-only roles see the detail without editors.

## Requirements

- Each injection point to record depth and technique, and to pick a per-point product/lot for multi-product sessions.

## Acceptance Criteria

- [ ] The per-point editor adds depth and technique/needle fields alongside label and units.
- [ ] A point can carry its own product/lot for multi-product sessions, defaulting to the chart's selected lot.
- [ ] Depth, technique and per-point lot persist on the InjectionPoint and survive draft sync.
- [ ] Read-only roles see the per-point depth/technique detail without editors.

## UI designs / screenshots

- Per-point editor adds depth and technique/needle inputs beside label + units.
- An optional per-point product/lot selector (defaults to the chart's selected lot) for multi-product sessions.
- Read-only roles see per-point depth/technique/lot detail without edit controls.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **InjectionPoint (extended)** — + depth, technique, product_id?, lot_id? (per-point, defaulting to the chart's selected lot)
  - _Extends the basic's InjectionPoint (which stores label/units/coords) with depth, technique and optional per-point product/lot for multi-product sessions._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Per-point depth/technique + multi-product lot**
  Behaviour: the per-point editor adds depth and technique/needle fields and an optional per-point product/lot (defaulting to the chart's selected lot) for multi-product sessions. Requirements: persist depth, technique and per-point lot on InjectionPoint and survive draft sync; read-only roles see the detail without editors.
