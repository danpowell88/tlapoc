# Body contouring: consumable cost roll-up into true cost & margin

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/BODY-CONTOURING-COST`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/BODY-CONTOURING`

## Background

As a owner, I want the per-cycle applicator (consumable) cost captured and rolled into true cost & margin, so that body-contouring profitability is measured accurately.
Plainly: this captures the real cost driver of a body-contouring treatment — the single-use applicator per cycle — and feeds it into profit reporting, so body-contouring margin is real rather than a guess. Where it fits: a follow-up to PRD-05/BODY-CONTOURING that adds the cost layer on top of the body-map chart. The chart already tallies applicators and cycles; this story attaches the per-cycle consumable cost and rolls it into True cost & margin reporting (PRD-08). All dollar/margin figures are owner-only (.fin).

## How it works

This follow-up adds the cost layer on top of the body-map chart. Each applicator placed on the map (the basic's bodyAdd over bodyZones) is mapped to its applicator type and a per-cycle consumable cost/time (APPL); the chart tallies the applicator (consumable) cost across cycles and areas.
That cost flows into True cost & margin reporting (PRD-08) so body-contouring profit is real, not a guess. Every dollar/margin figure is owner-only and stripped for non-owner roles (the .fin capability).
It extends the basic's BodyChart with the consumable_cost field — no new entity.

## Requirements

- The per-cycle applicator (consumable) cost captured and rolled into true cost & margin.

## Acceptance Criteria

- [ ] Each applicator maps to its applicator type and a per-cycle consumable cost/time.
- [ ] The chart tallies the applicator (consumable) cost across cycles and areas.
- [ ] The consumable cost flows into True cost & margin reporting (PRD-08).
- [ ] Every dollar/margin figure is owner-only and stripped for non-owner roles (the .fin capability).

## UI designs / screenshots

- Per-area table adds Cost per area; summary tiles 'Applicator (consumable) cost - price - margin'.
- Cost/margin tiles render only when the .fin capability is present.
- Cost rolls up into True cost & margin (PRD-08).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **BodyChart (extended)** — + consumable_cost (per-cycle applicator cost tallied across areas)
  - _Extends the basic's BodyChart: the consumable cost feeds True cost & margin (PRD-08); owner-only (.fin)._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Per-cycle consumable cost + true-cost/margin roll-up**
  Behaviour: each applicator maps to its type and a per-cycle consumable cost/time (APPL); the chart tallies the applicator cost across cycles/areas and rolls it into True cost & margin (PRD-08). Requirements: every dollar/margin figure is owner-only and stripped for non-owner roles (.fin).
