# Spike — Flutter injection-mapping canvas

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-CANVAS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a mobile engineer, I want a spike of the Flutter canvas: tap-to-add and drag injection points over a facial diagram and a photo, each holding metadata, so that PRD-05 charting builds on a proven, performant canvas.

The injection-mapping canvas is the hero clinical screen and the highest app risk (tap-to-add + drag points on a facial diagram/photo, per-point metadata). Prove the approach before PRD-05.

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

Stack: Flutter provider app.
Architecture decisions: ADR-0006 (see docs/adr/decision-log.md).
Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SPIKE-CANVAS.
Phase: 0 · Priority: P1 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
