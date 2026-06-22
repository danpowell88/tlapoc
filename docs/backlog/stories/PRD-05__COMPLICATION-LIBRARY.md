# Complication protocol library & response kits

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/COMPLICATION-LIBRARY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

As a clinician, I want a library of complication protocols with guided response steps and kit links, so that in an emergency I follow the correct, documented steps.
The prototype's Clinical → Complication protocols (openComplication/completeComplication) provides step-by-step VO/anaphylaxis protocols and links the emergency kit — the reference side of the adverse-event response.

## How it works

As a clinician, I want a library of complication protocols with guided response steps and kit links, so that in an emergency I follow the correct, documented steps.
When a complication happens - a vascular occlusion mid-filler, an anaphylactic reaction - there is no time to look things up. The complication library is the reference + response side of safety: clinic-curated, editable protocols (VO, anaphylaxis, ...) with ordered steps and the emergency-kit items they draw on, launched as a timestamped checklist that logs what was done and opens a routed adverse-event case.
Each ComplicationProtocol is an editable template: a name, a sub-line, ordered response steps, and the required kit items (e.g. VO -> high-dose hyaluronidase; anaphylaxis -> adrenaline 1:1000). 'Edit steps' lets the clinic tailor protocols to its own policy. The protocols read against the emergency-kit register (PRD-11/EMERGENCY-KIT) so the items they need are known to be on hand with in-date expiry.
'Start response' launches the protocol as a live, timestamped checklist (openComplication): the clinician ticks steps as they go and records the drug/kit used. On 'Complete & open AE case' (completeComplication) the response records its timing + outcome and raises a pre-filled, routed AdverseEvent (ADVERSE-EVENT) - seriousness pre-set, DAEN route derived from the modality (device for VO/filler, medicine for anaphylaxis) - plus a complication follow-up Job.
This is the reference + response library; the AE record + DAEN routing live in ADVERSE-EVENT, and the kit register lives in PRD-11. Completion is part of the immutable clinical record.

## Requirements

- A library of complication protocols with guided response steps and kit links.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Protocols (e.g. vascular occlusion, anaphylaxis) present guided ordered steps and the required kit items, and are editable to match clinic policy.
- [ ] 'Start response' launches a timestamped checklist that records the drug/kit used; completion is recorded with timing + outcome.
- [ ] Completing a protocol can raise a pre-filled, routed adverse event (ADVERSE-EVENT) and a complication follow-up Job.
- [ ] Protocols link to the emergency-kit register (PRD-11/EMERGENCY-KIT) so the required items are on hand and in date.

## UI designs / screenshots

_Prototype screen: prototype.html — Clinical → Complication protocols._

- Protocol cards: Vascular occlusion ('Filler emergency - time-critical ... any visual symptom = ocular emergency, transfer immediately') and Anaphylaxis ('Adrenaline first, then escalate'), each with a numbered step list, 'Edit steps' and 'Start response'.
- Response modal: the steps as a timestamped checklist with checkboxes, a 'Close' and a 'Complete & open AE case' action (completeComplication).
- Emergency kit register table: Item - For - Qty - Expiry (Hyaluronidase 1500IU / Adrenaline 1:1000 / Hydrocortisone) with add/remove - links protocols to the kit (PRD-11).
- New vs the prototype (build these): persisted protocols + responses, the timing/outcome capture, the pre-filled AE hand-off and the kit-register linkage with expiry checks.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **ComplicationProtocol** — id, tenant_id, name, sub, icon, steps[], required_kit[] (kit item refs), route (medicine|device), drug, active
  - _Editable reference library; reads against the emergency-kit register (PRD-11)._
- **ComplicationResponse** — id, protocol_id (FK), client_id, chart_entry_id, started_at, completed_at, steps_done[], kit_used[], outcome
  - _Timestamped response; can raise a pre-filled AdverseEvent + a follow-up Job. Immutable once completed._
- **EmergencyKitItem (PRD-11, referenced)** — item, for, qty, expiry
  - _Protocols link required kit; expiry/availability surfaced so the kit is ready._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: ComplicationProtocol + ComplicationResponse**
  EF Core: ComplicationProtocol (name, ordered steps, required_kit refs, route, drug, editable) + ComplicationResponse (protocol_id, client/chart links, started_at/completed_at, steps_done, kit_used, outcome). tenant_id + RLS; a response is immutable once completed. Reference the emergency-kit register (PRD-11).
- [ ] **Protocol library + response API**
  CRUD for clinic-editable protocols; a start-response command that creates a timestamped ComplicationResponse and a complete command that records timing/outcome + kit used, raises a pre-filled routed AdverseEvent (ADVERSE-EVENT) and a complication follow-up Job. Surface required-kit availability/expiry from the kit register. Audit completions (ADR-0010); publish OpenAPI.
- [ ] **Protocol cards + timestamped response checklist UI**
  Build the protocol cards (steps, 'Edit steps', 'Start response'), the editable-steps composer, and the response modal as a timestamped checklist (tick steps, record drug/kit used, 'Complete & open AE case'). Wire completion to the AE hand-off + job creation. Capability-gated to clinical roles; clear states.
- [ ] **Emergency-kit register linkage + expiry surfacing**
  Wire protocols to the emergency-kit register (PRD-11/EMERGENCY-KIT): show each protocol's required items with qty + expiry, flag missing/expired kit so the clinic restocks, and let a response record which kit items were consumed. Read from the kit register; don't relocate it.
