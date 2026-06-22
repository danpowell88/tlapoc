# Complication protocol library & response kits

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/COMPLICATION-LIBRARY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

As a clinician, I want a library of complication protocols with guided response steps and kit links, so that in an emergency I follow the correct, documented steps.
The prototype's Clinical → Complication protocols (openComplication/completeComplication) provides step-by-step VO/anaphylaxis protocols and links the emergency kit — the reference side of the adverse-event response.

## How it works

A library of complication protocols (e.g. vascular occlusion, anaphylaxis) with guided response steps and required kit items — the reference side of the adverse-event response. Launching a protocol logs the response, can raise an adverse event, and records completion timing/outcome.
Links to the emergency-kit register (PRD-11) so the right kit is on hand.

## Requirements

- A library of complication protocols with guided response steps and kit links.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Protocols (e.g. vascular occlusion, anaphylaxis) present guided steps and required kit items.
- [ ] Launching a protocol logs the response and can raise an adverse event (PRD-05/ADVERSE-EVENT).
- [ ] Completion is recorded with timing and outcome.
- [ ] Links to the emergency-kit register (PRD-11/EMERGENCY-KIT).

## UI designs / screenshots

_Prototype screen: prototype.html — Clinical → Complication protocols._

- Prototype: Clinical -> Complication protocols (clinical-safety.png) — protocol cards with step-by-step guidance and kit links; openComplication/completeComplication actions.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **ComplicationProtocol** — id, tenant_id, name, steps[], required_kit[]
  - _Reference library._
- **ComplicationResponse** — id, protocol_id, client_id, chart_entry_id, started_at, completed_at, outcome, kit_used[]
  - _Can raise an AdverseEvent + jobs._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ComplicationProtocol — id, tenant_id, name, steps[], required_kit[] (Reference library.)
  - ComplicationResponse — id, protocol_id, client_id, chart_entry_id, started_at, completed_at, outcome, kit_used[] (Can raise an AdverseEvent + jobs.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Protocols (e.g. vascular occlusion, anaphylaxis) present guided steps and required kit items.
  - Rule: Launching a protocol logs the response and can raise an adverse event (PRD-05/ADVERSE-EVENT).
  - Rule: Completion is recorded with timing and outcome.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-05/ADVERSE-EVENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C12, C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the clinical-safety per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Clinical -> Complication protocols (clinical-safety.png) — protocol cards with step-by-step guidance and kit links; openComplication/completeComplication actions.
