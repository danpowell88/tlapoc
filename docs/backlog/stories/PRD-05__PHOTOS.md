# Standardised before/after photos + compare

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a injector, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.
Capture standardised before/after photos room-side (framing/ghosting guide), compare side-by-side across visits; media stored centrally via signed URLs, never on personal devices, gated by image-use consent (REQ-CLIN-3, C14/ADR-0009).

## How it works

Standardised before/after photos captured room-side with a framing/ghosting guide, compared side-by-side across visits. Media is stored centrally via short-lived signed URLs, never persisted on the device beyond a transient sync cache, and capture requires current image-use consent (PRD-03/C14/ADR-0009).
The drag-to-compare slider lets the clinician show progress; annotations supported.

## Requirements

- To capture standardised before/after photos and compare them against prior visits.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Camera/upload with standardised framing/ghosting guide; side-by-side compare across visits.
- [ ] Capture requires current image-use consent (PRD-03).
- [ ] Photos stored centrally via signed URLs; never persisted on device beyond a transient sync cache.
- [ ] Annotation supported.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: Charting 'Before / after' compare with a drag slider ('12 weeks apart · stored securely, never on device') — see charting.png; and Clinical -> Photography & outcomes (clinical-imaging.png) for the gallery/compare.
- Camera/upload with a framing/ghost overlay; capture blocked without image-use consent.

![clinical-imaging — prototype screen](../screens/clinical-imaging.png)

## Suggested data model

- **Photo** — id, tenant_id, client_id, chart_entry_id, blob_ref(signed-url), framing_meta(json), taken_at, image_consent_id
  - _Central storage; never on device (C14/ADR-0009)._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Photo — id, tenant_id, client_id, chart_entry_id, blob_ref(signed-url), framing_meta(json), taken_at, image_consent_id (Central storage; never on device (C14/ADR-0009).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Camera/upload with standardised framing/ghosting guide; side-by-side compare across visits.
  - Rule: Capture requires current image-use consent (PRD-03).
  - Rule: Photos stored centrally via signed URLs; never persisted on device beyond a transient sync cache.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-03/IMAGE-CONSENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C14 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Capture requires current image-use consent (PRD-03).
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the clinical-imaging per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Charting 'Before / after' compare with a drag slider ('12 weeks apart · stored securely, never on device') — see charting.png; and Clinical -> Photography & outcomes (clinical-imaging.png) for the gallery/compare.
  - Camera/upload with a framing/ghost overlay; capture blocked without image-use consent.
