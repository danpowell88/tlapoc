# Other-modality charting: filler / energy / weight-loss (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MODALITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

As a injector, I want modality-aware charting for filler, energy devices and weight-loss, so that the platform covers the full treatment menu.
Phase 2 adds dermal filler (multi-area, per-area lot, VO/blindness consent gate), energy-device charting (per-pass settings, laser-licence gated), weight-loss titration and ghost-overlay photo alignment (REQ-CLIN-10..13). Placeholder.

## How it works

Placeholder/extension (Phase 2): modality-aware charting beyond toxin — dermal filler (multi-area, per-area lot, mandatory VO/blindness consent gate), energy-device charting (per-pass settings/fluence, laser-licence gated), weight-loss titration, and ghost-overlay photo alignment. The modality model already anticipates these (ADR-0025).
v1 ships toxin + a non-S4 skin note; each modality's specific gates are captured for later build.

## Requirements

- Modality-aware charting for filler, energy devices and weight-loss.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — v1 ships toxin + non-S4 skin notes; the modality model already anticipates these.
- [ ] Each modality's specific gates (e.g. filler VO consent, laser licence) are captured for later build.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: Clinical -> Body contouring (clinical-body.png) and the skin note demonstrate the modality model; filler/energy/weight-loss are concept-level for v1.

![clinical-body — prototype screen](../screens/clinical-body.png)

## Suggested data model

- **ChartEntry.treatment_type** — + modality-specific payloads (filler areas, device passes, titration)
  - _Filler adds VO/blindness consent gate; energy requires laser licence._

## Technical notes (high level)

- Architecture decisions: [ADR-0025](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
