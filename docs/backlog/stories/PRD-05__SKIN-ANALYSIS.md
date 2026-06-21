# Skin analysis & assessment (with AI scan, advisory)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/SKIN-ANALYSIS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a dermal therapist / injector, I want to record a structured skin assessment (and optionally an AI-assisted scan) and share results with the client, so that skin treatment is planned and tracked, and clients see their progress.

The prototype's Clinical → Skin analysis screen captures a structured skin assessment with zone scoring, an AI scan (simulateScan) and a push-to-client summary (pushSkinToClient). Per the no-AI-in-v1 stance, AI scoring is advisory/Phase 2; the manual assessment record can be v1.

## Requirements

- To record a structured skin assessment (and optionally an AI-assisted scan) and share results with the client.
- Traces to requirement(s): REQ-CLIN-1, REQ-CLIN-7.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] A structured skin assessment (concerns, zones, scores) can be recorded against the client.
- [ ] AI auto-scoring is advisory and human-confirmed, and is gated to Phase 2 (no AI in v1).
- [ ] An assessment summary can be pushed to the client app (consent-respecting).
- [ ] Assessments feed treatment planning (PRD-05/TREATMENT-PLANS) and outcomes.

## UI designs / screenshots

prototype.html — Clinical → Skin analysis (scan + push-to-client); client-app.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0020, ADR-0025 (see docs/adr/decision-log.md).
Depends on: PRD-05/NOTE-TEMPLATE.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/SKIN-ANALYSIS.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
