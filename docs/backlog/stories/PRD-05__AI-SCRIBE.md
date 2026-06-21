# AI note dictation / auto-detect injection points (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/AI-SCRIBE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want optional AI assistance for notes and injection-point suggestions, so that charting is faster (with human confirmation).

AI scribe and advisory auto-detection of injection points are explicitly out for v1 (no AI; everything manual + human-confirmed). Placeholder (REQ-CLIN-6, ADR-0020).

## Requirements

- Optional AI assistance for notes and injection-point suggestions.
- Traces to requirement(s): REQ-CLIN-6.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — explicitly no AI in v1; any future feature is advisory + human-confirmed only.
- [ ] Captured to keep the data model ready.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0020 (see docs/adr/decision-log.md).

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/AI-SCRIBE.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
