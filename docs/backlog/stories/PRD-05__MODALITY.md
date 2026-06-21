# Other-modality charting: filler / energy / weight-loss (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MODALITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want modality-aware charting for filler, energy devices and weight-loss, so that the platform covers the full treatment menu.

Phase 2 adds dermal filler (multi-area, per-area lot, VO/blindness consent gate), energy-device charting (per-pass settings, laser-licence gated), weight-loss titration and ghost-overlay photo alignment (REQ-CLIN-10..13). Placeholder.

## Requirements

- Modality-aware charting for filler, energy devices and weight-loss.
- Traces to requirement(s): REQ-CLIN-10, REQ-CLIN-11, REQ-CLIN-12, REQ-CLIN-13.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — v1 ships toxin + non-S4 skin notes; the modality model already anticipates these.
- [ ] Each modality's specific gates (e.g. filler VO consent, laser licence) are captured for later build.

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0025 (see docs/adr/decision-log.md).

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/MODALITY.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
