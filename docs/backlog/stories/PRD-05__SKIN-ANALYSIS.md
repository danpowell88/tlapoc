# Skin analysis & assessment (with AI scan, advisory)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/SKIN-ANALYSIS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a dermal therapist / injector, I want to record a structured skin assessment (and optionally an AI-assisted scan) and share results with the client, so that skin treatment is planned and tracked, and clients see their progress.
A structured skin assessment: concerns scored by zone and tracked over time, driving a recommended treatment plan and giving the client visible progress (manual record in v1; AI-assisted scan advisory and Phase 2+). The front door to non-injectable care under PRD-05 charting on the clinic-first spine; it depends on the guided note (NOTE-TEMPLATE) and feeds plans (TREATMENT-PLANS) and outcomes (OUTCOMES). Skin images are Personal Health Information (PHI), so image-use consent and Australian storage apply. The prototype's Clinical → Skin analysis screen captures a structured skin assessment with zone scoring, an AI scan (simulateScan) and a push-to-client summary (pushSkinToClient). Per the no-AI-in-v1 stance, AI scoring is advisory/Phase 2; the manual assessment record can be v1.

## How it works

As a dermal therapist / injector, I want to record a structured skin assessment (and optionally an AI-assisted scan) and share results with the client, so that skin treatment is planned and tracked, and clients see their progress.
Skin assessment is the front door to non-injectable care: an objective record of a client's skin concerns, scored and tracked over time, that drives the recommended plan and gives the client something tangible to see progress against. The manual structured assessment is v1; AI scoring is advisory and Phase 2+ per the no-AI-in-v1 stance.
A SkinAssessment records a set of zones/concerns (the prototype scores eight: wrinkles, UV/sun spots, pores, texture, redness, firmness, plus skin age vs actual) each as a percentile-vs-cohort score, captured against the client with a date. Scores trend across assessments so progress is visible. Concerns below a threshold drive the recommended plan - tappable chips that jump to the matching treatment (feeding TREATMENT-PLANS).
An optional AI-assisted scan can populate scores, but it is advisory + human-confirmed and gated to Phase 2 (ADR-0020) - the prototype's 'Run new scan' (simulateScan) is a scripted demo of that pattern. In v1 the clinician records the assessment manually; the source field marks each assessment manual vs ai_advisory so the model is ready when AI lands.
The assessment summary can be pushed to the client app (pushSkinToClient), respecting consent - skin images are PHI, so image-use consent + AU storage (C14) apply exactly as for clinical photos. Assessments feed treatment planning (TREATMENT-PLANS) and outcomes (OUTCOMES).

## Requirements

- To record a structured skin assessment (and optionally an AI-assisted scan) and share results with the client.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] A structured skin assessment (concerns, zones, scores + skin age vs actual) can be recorded against the client and trends across assessments.
- [ ] AI auto-scoring is advisory and human-confirmed, and gated to Phase 2 (no AI in v1); the source is recorded as manual vs ai_advisory.
- [ ] An assessment summary can be pushed to the client app, respecting image-use consent + AU storage (C14).
- [ ] Concerns below threshold drive recommended-plan chips that feed TREATMENT-PLANS; assessments feed OUTCOMES.

## UI designs / screenshots

_Prototype screen: prototype.html — Clinical → Skin analysis (scan + push-to-client); client-app.html._

- Client card with the scanned face + concern dots overlay, 'Skin age 37 vs 34 actual' and an overall-trend sparkline.
- Concern scores: eight rows (wrinkles, UV/sun spots, pores, texture, redness, firmness...) as percentile-vs-cohort bars with the change since last scan.
- 'Recommended plan - focus areas (score < 60)' chips that jump to the matching treatment (feed TREATMENT-PLANS).
- 'Run new scan' (advisory, Phase 2) + 'Send to client' actions; banners noting 'Concept - AI is Phase 3' and 'Skin images are PHI - image-use consent + AU storage apply (C14)'.
- New vs the prototype (build these): the persisted manual assessment record, the trend over real assessments, and the consent-respecting push to the client app.

![clinical-skin — prototype screen](../screens/clinical-skin.png)

## Suggested data model

- **SkinAssessment** — id, tenant_id, client_id, assessed_at, assessed_by, skin_age, actual_age, source (manual|ai_advisory), pushed_to_client_at, image_consent_id (if image-backed)
  - _Manual record is v1; AI advisory Phase 2 (ADR-0020). Image-backed assessments respect C14._
- **SkinZoneScore** — id, assessment_id (FK), concern (wrinkles|uv|pores|texture|redness|firmness|...), score (percentile vs cohort), recommended_service_id
  - _Trends across assessments; below-threshold concerns drive recommended-plan chips (TREATMENT-PLANS)._

## Technical notes (high level)

- Architecture decisions: [ADR-0020](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0025](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Skin assessment record + scoring UI (manual v1; AI advisory Phase 2)**
  EF Core: SkinAssessment + SkinZoneScore (per-concern percentile-vs-cohort score, recommended service), tenant_id + Row-Level Security (RLS, the per-tenant database isolation), indexed by client for trend. API to record/retrieve assessments and trend them across visits; below-threshold concerns surface recommended-plan chips that feed TREATMENT-PLANS; a consent-respecting push-to-client summary (C14 image-use + AU storage for image-backed assessments). UI: the concern-score bars, skin-age vs actual, trend sparkline and recommended-plan chips per the prototype. Keep AI auto-scoring advisory + human-confirmed and gated to Phase 2 (ADR-0020) - v1 records manually; mark source manual vs ai_advisory.
