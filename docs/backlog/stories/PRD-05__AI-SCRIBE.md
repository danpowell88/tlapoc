# AI note dictation / auto-detect injection points (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/AI-SCRIBE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

As a injector, I want optional AI assistance for notes and injection-point suggestions, so that charting is faster (with human confirmation).
AI scribe and advisory auto-detection of injection points are explicitly out for v1 (no AI; everything manual + human-confirmed). Placeholder (REQ-CLIN-6, ADR-0020).

## How it works

As an injector, I want optional AI assistance for notes and injection-point suggestions, so that charting is faster (with human confirmation).
Placeholder / Phase 2. There is explicitly no AI in v1 - every note and every injection point is entered and confirmed by a human. This card exists to keep the data model and stance ready, not to build anything.
If ever built, AI assistance is advisory + human-confirmed only: ambient/dictated note drafting that the clinician edits and accepts, and advisory auto-detection of injection points that proposes candidates from facial landmarks (ADR-0020). It would never set product/units, never auto-finalise, never auto-administer - the clinician must review, adjust and confirm every suggestion.
Preference would be on-device/edge landmarking for privacy + latency; any server-side processing must stay within AU residency (ADR-0016) and respect image-use consent (ADR-0009). The prototype's 'Auto-detect' button is a scripted demo of the advisory pattern, not a real model.
v1 = manual tap-to-add + drag and the templated note only. Captured here so the schema can carry advisory suggestions attached to a draft without rework later.

## Requirements

- Optional AI assistance for notes and injection-point suggestions.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder - explicitly no AI in v1; everything is manual and human-controlled.
- [ ] Any future feature is advisory + human-confirmed only: it proposes, the clinician reviews/adjusts/confirms; it never sets units, never auto-finalises, never auto-administers.
- [ ] Captured to keep the data model ready (advisory suggestions attach to a draft ChartEntry).

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Charting 'Auto-detect' button animates placing the preset points to demonstrate the advisory, human-confirmed pattern - labelled Phase 2.
- Deferred - no v1 build; v1 ships manual tap-to-add + drag and the templated note only.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **(future) AIAssist** — advisory suggestions (note draft / candidate points) attached to a draft ChartEntry; confidence; human confirms before anything is committed
  - _No AI in v1; on-device/edge preferred, AU residency + image-use consent if server-side (ADR-0020/0016/0009)._

## Technical notes (high level)

- Architecture decisions: [ADR-0020](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Scope & design AI assistance when pulled into a sprint**
  Deferred placeholder - explicitly no AI in v1. If ever pulled in: design advisory note dictation + advisory injection-point auto-detect that is human-confirmed only (proposes candidates from facial landmarks; never sets units/finalises/administers, ADR-0020), prefer on-device/edge landmarking, and ensure AU residency (ADR-0016) + image-use consent (ADR-0009) for any server-side processing. Confirm the regulatory/clinical stance before any build.
