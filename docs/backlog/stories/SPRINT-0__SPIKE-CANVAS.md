# Spike — Flutter injection-mapping canvas

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-CANVAS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

As a mobile engineer, I want a spike of the Flutter canvas: tap-to-add and drag injection points over a facial diagram and a photo, each holding metadata, so that PRD-05 charting builds on a proven, performant canvas.
The injection-mapping canvas is the hero clinical screen and the highest app risk (tap-to-add + drag points on a facial diagram/photo, per-point metadata). Prove the approach before PRD-05.

## How it works

Spike of the Flutter injection-mapping canvas: tap-to-add + drag points over a facial diagram and a photo, each holding metadata, performing smoothly with many points, with a coordinate model that survives image scaling/rotation. De-risks the hero clinical screen (PRD-05/MAPPING).

## Requirements

- A spike of the Flutter canvas: tap-to-add and drag injection points over a facial diagram and a photo, each holding metadata.

## Acceptance Criteria

- [ ] Prototype supports tap-to-add, drag-to-move and per-point metadata over both a diagram and an image.
- [ ] Performs smoothly on a mid-range device with many points.
- [ ] Coordinate model survives image scaling/rotation and is persistable.
- [ ] Approach documented; feeds PRD-05 mapping stories.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)
- Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
