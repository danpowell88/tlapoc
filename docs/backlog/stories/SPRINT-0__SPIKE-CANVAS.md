# Spike — Flutter injection-mapping canvas

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-CANVAS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

As a mobile engineer, I want a spike of the Flutter canvas: tap-to-add and drag injection points over a facial diagram and a photo, each holding metadata, so that PRD-05 charting builds on a proven, performant canvas.
The injection-mapping canvas is the hero clinical screen and the highest app risk: tap-to-add and drag injection points over a facial diagram and a photo, each point holding metadata, performing smoothly with many points (the Injection map tab in treatment-room.png). The spike proves the Flutter approach before PRD-05 charting builds on it (ADR-0006).  Output feeds PRD-05/MAPPING: a proven, performant canvas pattern and a persistable coordinate model that survives image scaling/rotation.

## How it works

A Flutter prototype supports tap-to-add, drag-to-move and per-point metadata over both a facial diagram and a real image. The hard parts to prove are interaction performance with many points on a mid-range device, and a coordinate model that is anchored to the image (normalised coordinates) so points stay correct when the image is scaled, rotated or displayed at different sizes — and can be persisted and re-rendered identically later.
Go/no-go bar: smooth tap-to-add/drag with per-point metadata over diagram and image, acceptable performance with many points on a mid-range device, and a coordinate model that survives scaling/rotation and round-trips through persistence. If the naive approach stutters, the spike identifies the rendering technique that works (custom painter, layering) and notes it.
It's a spike — prove the canvas and the coordinate model, document the approach, then discard the prototype. PRD-05/MAPPING implements the real screen on the proven pattern.

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

- [ ] **Define the spike scope, questions and go/no-go criteria**
  Frame the canvas risk and the bar PRD-05 needs cleared.
  - Questions: can Flutter do smooth tap-to-add + drag points with per-point metadata over a diagram AND a photo; does it stay performant with many points on a mid-range device; can the coordinate model survive image scale/rotation and persist?
  - Go/no-go bar: all of the above hold, with a coordinate model that round-trips through persistence and re-renders identically.
  - Time-box and the hand-off (PRD-05 MAPPING).
- [ ] **Build the throwaway canvas prototype**
  Prove interaction + performance + the coordinate model.
  - Tap-to-add, drag-to-move and per-point metadata over both a facial diagram and a real image.
  - Stress with many points on a mid-range device; if naive rendering stutters, find the technique that doesn't (custom painter/layering).
  - Use normalised, image-anchored coordinates; verify they survive scaling/rotation and persist/re-render. Disposable code.
- [ ] **Document the proven canvas approach and coordinate model**
  Capture what PRD-05/MAPPING should build on.
  - The rendering/interaction approach that performed, and the persistable, scale/rotation-safe coordinate model.
  - The go/no-go and any device-performance caveats.
  - ADR only if a notable technical decision emerged.
