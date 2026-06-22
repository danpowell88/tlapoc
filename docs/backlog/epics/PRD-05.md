# PRD-05 — Clinical charting: injection mapping & before/after

> **Stage / Milestone:** M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05)  ·  **Phase:** 1  ·  **Stories:** 31

The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway — usable room-side on the provider app, even offline.

**Source PRD:** `docs/prds/PRD-05-clinical-charting.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `NOTE-TEMPLATE` | [Guided toxin note: pre-treatment review & gate (MVP)](../stories/PRD-05__NOTE-TEMPLATE.md) | Story | P0 | 5 | 4 |
| `NOTE-TEMPLATE-TYPE-TOGGLE` | [Charting: treatment-type toggle (toxin / non-S4 skin)](../stories/PRD-05__NOTE-TEMPLATE-TYPE-TOGGLE.md) | Story | P2 | 2 | 1 |
| `NOTE-TEMPLATE-ENGINE` | [Charting: configurable, versioned note-template engine + snippet admin](../stories/PRD-05__NOTE-TEMPLATE-ENGINE.md) | Story | P2 | 2 | 2 |
| `MAPPING` | [Injection-mapping canvas: add/edit points + save draft (MVP)](../stories/PRD-05__MAPPING.md) | Story | P0 | 5 | 3 |
| `MAPPING-FINALISE` | [Injection map: finalise → transactional stock deduction + register link](../stories/PRD-05__MAPPING-FINALISE.md) | Story | P2 | 2 | 1 |
| `MAPPING-POINT-DEPTH` | [Injection map: per-point depth, technique & multi-product lot](../stories/PRD-05__MAPPING-POINT-DEPTH.md) | Story | P2 | 2 | 1 |
| `MAPPING-SKIN-NOTE` | [Charting: non-S4 skin-note variant fields](../stories/PRD-05__MAPPING-SKIN-NOTE.md) | Story | P2 | 2 | 1 |
| `PRODUCT-LOT-PICKER` | [Charting product & batch (lot) selector (MVP)](../stories/PRD-05__PRODUCT-LOT-PICKER.md) | Story | P0 | 5 | 3 |
| `PRODUCT-LOT-PICKER-GATE` | [Charting lot picker: lot-required-before-points gate](../stories/PRD-05__PRODUCT-LOT-PICKER-GATE.md) | Story | P2 | 2 | 1 |
| `PHOTOS` | [Clinical photo capture: signed-URL storage & consent gate (MVP)](../stories/PRD-05__PHOTOS.md) | Story | P1 | 3 | 3 |
| `PHOTOS-COMPARE` | [Clinical photos: before/after compare, per-pose gallery & annotation](../stories/PRD-05__PHOTOS-COMPARE.md) | Story | P2 | 2 | 1 |
| `PHOTOS-OFFLINE-CACHE` | [Clinical photos: on-device transient cache & post-sync purge](../stories/PRD-05__PHOTOS-OFFLINE-CACHE.md) | Story | P2 | 2 | 1 |
| `IMMUTABILITY` | [Immutable finalisation & audited amendments](../stories/PRD-05__IMMUTABILITY.md) | Story | P0 | 5 | 3 |
| `OFFLINE` | [Offline queue & sync for room-side charting](../stories/PRD-05__OFFLINE.md) | Story | P1 | 3 | 4 |
| `ADVERSE-EVENT` | [Adverse-event capture & DAEN routing (MVP)](../stories/PRD-05__ADVERSE-EVENT.md) | Story | P1 | 3 | 3 |
| `ADVERSE-EVENT-JOBS` | [Adverse event: follow-up jobs & route to Governance](../stories/PRD-05__ADVERSE-EVENT-JOBS.md) | Story | P2 | 2 | 1 |
| `TREATMENT-PLANS` | [Treatment plans & protocol templates (MVP)](../stories/PRD-05__TREATMENT-PLANS.md) | Story | P2 | 2 | 2 |
| `TREATMENT-PLANS-RECALL` | [Treatment plans: project upcoming sessions as recall jobs](../stories/PRD-05__TREATMENT-PLANS-RECALL.md) | Story | P2 | 2 | 1 |
| `TREATMENT-PLANS-VIEWS` | [Treatment plans: protocol builder, Client 360 progress & in-room list](../stories/PRD-05__TREATMENT-PLANS-VIEWS.md) | Story | P2 | 2 | 1 |
| `MODALITY` | [Other-modality charting: filler / energy / weight-loss (placeholder)](../stories/PRD-05__MODALITY.md) | Story | P2 | 1 | 1 |
| `AI-SCRIBE` | [AI note dictation / auto-detect injection points (placeholder)](../stories/PRD-05__AI-SCRIBE.md) | Story | P2 | 1 | 1 |
| `SKIN-ANALYSIS` | [Skin analysis: structured assessment & zone scoring (MVP)](../stories/PRD-05__SKIN-ANALYSIS.md) | Story | P2 | 1 | 1 |
| `SKIN-ANALYSIS-RECOMMEND` | [Skin analysis: recommended-plan chips feeding treatment plans](../stories/PRD-05__SKIN-ANALYSIS-RECOMMEND.md) | Story | P2 | 2 | 1 |
| `SKIN-ANALYSIS-PUSH` | [Skin analysis: consent-respecting push to client app](../stories/PRD-05__SKIN-ANALYSIS-PUSH.md) | Story | P2 | 2 | 1 |
| `BODY-CONTOURING` | [Body contouring charting: body map & applicator/cycle capture (MVP)](../stories/PRD-05__BODY-CONTOURING.md) | Story | P2 | 1 | 1 |
| `BODY-CONTOURING-COST` | [Body contouring: consumable cost roll-up into true cost & margin](../stories/PRD-05__BODY-CONTOURING-COST.md) | Story | P2 | 2 | 1 |
| `BODY-CONTOURING-PROGRESS` | [Body contouring: standardised body photos & measurements over the course](../stories/PRD-05__BODY-CONTOURING-PROGRESS.md) | Story | P2 | 2 | 1 |
| `COMPLICATION-LIBRARY` | [Complication protocol library & timestamped response (MVP)](../stories/PRD-05__COMPLICATION-LIBRARY.md) | Story | P1 | 3 | 3 |
| `COMPLICATION-KIT-LINK` | [Complication protocols: emergency-kit register linkage & expiry surfacing](../stories/PRD-05__COMPLICATION-KIT-LINK.md) | Story | P2 | 2 | 1 |
| `OUTCOMES` | [Outcomes & revision capture (MVP)](../stories/PRD-05__OUTCOMES.md) | Story | P2 | 1 | 1 |
| `OUTCOMES-REPORTING` | [Outcomes: per-treatment/practitioner aggregation & reporting feed](../stories/PRD-05__OUTCOMES-REPORTING.md) | Story | P2 | 2 | 1 |

_Totals: 31 stories · 51 tasks._
