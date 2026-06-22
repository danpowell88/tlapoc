# Outcomes & revision tracking

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/OUTCOMES`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/PHOTOS`

## Background

As a injector / owner, I want to track treatment outcomes and any revisions/touch-ups, so that we can measure quality and feed it to reporting.
Outcomes and revision tracking: capturing how treatments turned out (a result rating, the before/after linkage) and recording any revision/touch-up against the original treatment, so quality can be measured per treatment type and practitioner. The quality-measurement capability under PRD-05 charting on the clinic-first spine; it depends on standardised photos (PHOTOS) for evidence and consent rules, and its aggregates feed reporting (PRD-08); complications tie back to adverse-event records (ADVERSE-EVENT). The prototype's Photography & outcomes view tracks before/after outcomes and a revision/touch-up signal that feeds reporting (REQ-CLIN-13).

## How it works

As an injector / owner, I want to track treatment outcomes and any revisions/touch-ups, so that we can measure quality and feed it to reporting.
Quality is only manageable if it is measured. Outcome tracking captures how treatments turned out - a result rating, the before/after linkage - and records revision/touch-up events against the original treatment, so the clinic can see touch-up rates, satisfaction and complication rates per treatment type and per practitioner, and feed those signals to reporting.
An Outcome is captured against a finalised ChartEntry: a result rating, optional satisfaction signal, and links to the before/after photos that evidence it (respecting image-use consent - any photo-based outcome obeys the PHOTOS / C14 rules). A revision/touch-up is recorded as an Outcome that points back (revision_of) at the original treatment, so a touch-up is never counted as a fresh success.
These signals aggregate into the Photography & outcomes view - touch-up rate, % satisfied, n and complications per treatment type (the prototype's outcomeStats: Anti-wrinkle 8% touch-up / 96% satisfied, Filler 14% / 91%, Skin, Laser/IPL) - and feed PRD-08 reporting (quality by treatment + practitioner). Complications surfaced here tie back to the AdverseEvent records (ADVERSE-EVENT).
Outcomes read from and write to the same clinical spine; they feed treatment-plan reviews (TREATMENT-PLANS) and the True cost/quality reporting.

## Requirements

- To track treatment outcomes and any revisions/touch-ups.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Outcomes are captured against treatments (result rating, optional satisfaction, before/after linkage).
- [ ] Revision/touch-up events are recorded and linked to the original treatment (revision_of) so they are not counted as fresh successes.
- [ ] Outcome/revision signals aggregate per treatment type + practitioner and feed reporting (PRD-08); complications tie back to AdverseEvent.
- [ ] Any photo-based outcome respects image-use consent (PHOTOS / C14).

## UI designs / screenshots

_Prototype screen: prototype.html — Clinical → Photography & outcomes._

- 'Outcomes & revisions - per treatment type' table: Treatment - Touch-up rate - Satisfied - n - Complications (Anti-wrinkle 8% / 96% / 96 / 0; Filler 14% / 91% / 34 / 1; Skin 5% / 94% / 120 / 0; Laser/IPL 5% / 94% / 60 / 0).
- Sits alongside the standardised-photography card (shared with PHOTOS) so outcomes link to the before/after evidence.
- New vs the prototype (build these): per-treatment Outcome capture, the revision_of linkage, the consent-respecting photo linkage and the aggregation that feeds PRD-08 reporting.

![clinical-imaging — prototype screen](../screens/clinical-imaging.png)

## Suggested data model

- **Outcome** — id, tenant_id, chart_entry_id (FK), client_id, rating, satisfaction (nullable), before_photo_id, after_photo_id, revision_of (nullable FK), recorded_at, recorded_by
  - _Revision links to the original treatment; photo links respect image-use consent (C14); aggregates feed reporting (PRD-08)._
- **Derived / reporting** — per treatment type + practitioner: touch-up rate = revisions/treatments, % satisfied, n, complications (from AdverseEvent)
  - _Read-model for the Outcomes & revisions table + PRD-08 quality reporting._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Outcome + revision capture, aggregation & UI**
  EF Core: Outcome linked to a finalised ChartEntry (rating, optional satisfaction, before/after photo links, revision_of pointing at the original treatment), tenant_id + Row-Level Security (RLS, the per-tenant database isolation), indexed by treatment type + practitioner. API to capture outcomes/revisions and a read-model aggregating touch-up rate, % satisfied, n and complications (from AdverseEvent) per treatment type/practitioner, feeding PRD-08 reporting. UI: per-treatment outcome capture + the 'Outcomes & revisions - per treatment type' table; any photo-based outcome respects image-use consent (PHOTOS / C14). Keep money/quality figures owner-gated per the financial-gating rules.
