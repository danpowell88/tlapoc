# Guided toxin treatment note & pre-treatment review

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/Rx surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

## How it works

Charting is a guided, treatment-type-aware flow. Step 1 (pre-treatment review) surfaces safety flags, the last treatment, and the linked consult/Rx — read-only context the injector checks before starting. The toxin note is a configurable template (structured fields + free text + reusable phrases/snippets); a non-S4 skin variant swaps the map for a skin note.
Charting cannot open unless the consult+consent gate (PRD-03/04) is satisfied — the safe path is the only path.

## Requirements

- A guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template.

## Acceptance Criteria

- [ ] Pre-treatment review surfaces safety flags, last treatment and the linked consult/Rx (verified before opening).
- [ ] Configurable toxin template with structured fields, free text and reusable phrases/snippets.
- [ ] A non-S4 skin note variant exists (treatment-type-aware).
- [ ] Charting cannot open unless the consult+consent gate is satisfied (PRD-03/04).

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: Charting (charting.png) — header gate chips; Step 1 'Pre-treatment review' card (Allergies/Contraindications/BDD/Consent/Consult chips + 'Last treatment: 24u 12 Mar forehead+glabella Bella RN' + Consult & prescription).
- Treatment-type toggle: Anti-wrinkle (toxin) / Skin treatment.
- A finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event before checkout.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry** — id, tenant_id, client_id, appointment_id, consult_id, treatment_type, status(draft|final), author_id, finalised_at
  - _Shared with MAPPING; one per treatment._
- **NoteTemplate** — id, tenant_id, treatment_type, fields(json), snippets[]
  - _Configurable toxin template; non-S4 skin variant._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ChartEntry — id, tenant_id, client_id, appointment_id, consult_id, treatment_type, status(draft|final), author_id, finalised_at (Shared with MAPPING; one per treatment.)
  - NoteTemplate — id, tenant_id, treatment_type, fields(json), snippets[] (Configurable toxin template; non-S4 skin variant.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Pre-treatment review surfaces safety flags, last treatment and the linked consult/Rx (verified before opening).
  - Rule: Configurable toxin template with structured fields, free text and reusable phrases/snippets.
  - Rule: A non-S4 skin note variant exists (treatment-type-aware).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/ADMIN-GATE.
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the charting per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Charting (charting.png) — header gate chips; Step 1 'Pre-treatment review' card (Allergies/Contraindications/BDD/Consent/Consult chips + 'Last treatment: 24u 12 Mar forehead+glabella Bella RN' + Consult & prescription).
  - Treatment-type toggle: Anti-wrinkle (toxin) / Skin treatment.
  - A finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event before checkout.
