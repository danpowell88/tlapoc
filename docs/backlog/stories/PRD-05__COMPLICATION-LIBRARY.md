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

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C12, C20); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
