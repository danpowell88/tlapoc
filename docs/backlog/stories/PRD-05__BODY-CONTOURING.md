# Body contouring charting (e.g. CoolSculpting)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/BODY-CONTOURING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/MODALITY`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a therapist, I want to chart body-contouring treatments on a body map with per-area applicator/cycle settings, so that non-facial treatments are recorded with the same rigour.

The prototype's Clinical → Body contouring screen charts body treatments on a body map (bodyAdd/bodyDel/bodyCyc) with applicator/cycle settings — a distinct modality beyond the face.

## Requirements

- To chart body-contouring treatments on a body map with per-area applicator/cycle settings.
- Traces to requirement(s): REQ-CLIN-10, REQ-CLIN-12.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] A body map supports adding/removing/cycling treatment areas with per-area settings (applicator, cycles, parameters).
- [ ] Sessions feed multi-session plans and outcomes.
- [ ] Device-gated where a licence/patch-test applies (per modality rules).
- [ ] Part of the modality-aware charting model (extends PRD-05/MODALITY).

## UI designs / screenshots

prototype.html — Clinical → Body contouring (body map).

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0025 (see docs/adr/decision-log.md).
Depends on: PRD-05/MODALITY.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/BODY-CONTOURING.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
