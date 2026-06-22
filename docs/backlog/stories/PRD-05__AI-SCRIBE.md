# AI note dictation / auto-detect injection points (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/AI-SCRIBE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

As a injector, I want optional AI assistance for notes and injection-point suggestions, so that charting is faster (with human confirmation).
AI scribe and advisory auto-detection of injection points are explicitly out for v1 (no AI; everything manual + human-confirmed). Placeholder (REQ-CLIN-6, ADR-0020).

## How it works

Placeholder (Phase 2): optional AI assistance for note dictation and advisory auto-detection of injection points. Explicitly no AI in v1 — everything manual and human-controlled; any future feature is advisory + human-confirmed only (ADR-0020).
Captured to keep the data model ready.

## Requirements

- Optional AI assistance for notes and injection-point suggestions.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — explicitly no AI in v1; any future feature is advisory + human-confirmed only.
- [ ] Captured to keep the data model ready.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **(future) AIAssist** — advisory suggestions attached to a draft ChartEntry; human confirms
  - _No AI in v1._

## Technical notes (high level)

- Architecture decisions: [ADR-0020](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1; confirm it still fits scope/regulatory stance, then break down.
