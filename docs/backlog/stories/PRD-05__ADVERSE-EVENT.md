# Adverse-event capture → DAEN pathway

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/ADVERSE-EVENT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/IMMUTABILITY`

## Background

As a injector, I want to log an adverse event linked to the treatment, product and lot, so that it feeds the TGA report and the right follow-ups happen.
Adverse-event capture: when a treatment causes an unwanted medical occurrence, the clinician logs it against the treatment, product and batch-lot, classifies seriousness, and the system routes it to the correct Database of Adverse Event Notifications (DAEN), the Therapeutic Goods Administration's (TGA) reporting system. The safety-reporting source record within PRD-05 charting on the clinic-first spine after the S4 (Schedule 4 'Prescription Only Medicine') moat (PRD-04); it depends on immutable finalisation (IMMUTABILITY), can be raised from COMPLICATION-LIBRARY, and routes to the Governance hub (PRD-08/DAEN). Log an adverse event/complication linked to the treatment, product and lot, classify seriousness and target the correct DAEN database (REQ-CLIN-5, C12). Includes the vascular occlusion (VO)/anaphylaxis complication-response flow.

## How it works

As an injector, I want to log an adverse event linked to the treatment, product and lot, so that it feeds the TGA report and the right follow-ups happen.
When something goes wrong — a vascular occlusion, an anaphylactic reaction, an unexpected reaction to a toxin — the clinician needs to act immediately and capture, in the moment, exactly what a TGA report will later need. This story is the adverse event (AE) capture itself: linked to the treatment, product and lot, classified by seriousness, and routed to the correct DAEN database.
An adverse event is logged against the ChartEntry (so it inherits the client, treatment, product and lot context automatically) and captures the fields a TGA DAEN report needs: description, onset, seriousness classification, the product + batch-lot involved, and the outcome/treatment given. The DAEN target is derived from the modality (C12): a toxin or filler-as-medicine routes to DAEN-medicines; a device-class filler/PDO/RF routes to DAEN-medical devices. The system flags the cases where reporting is mandatory rather than voluntary.
Capture can be reached two ways: directly from the finalise close-out ('any adverse event?'), or as the outcome of a complication-response flow (COMPLICATION-LIBRARY) — e.g. a vascular-occlusion or anaphylaxis protocol completes and logs the hyaluronidase/adrenaline given, then raises the AE pre-filled. Either way, logging an AE raises follow-up Jobs (review, mandatory-report check, client follow-up) so nothing is dropped.
Because the AE links to the lot, it ties straight into the lot→client recall lookup (PRD-04) — if a batch is implicated, the affected clients are already known. The AE is part of the immutable clinical record (amendments only, ADR-0010).
This story captures and routes the AE and raises the jobs; the full prefilled DAEN submission/export lives in the Governance hub (PRD-08/DAEN) — the AE record is the data source for it.

## Requirements

- To log an adverse event linked to the treatment, product and lot.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An adverse event captures the data a TGA DAEN report needs (description, onset, seriousness, product, lot, treatment given) and links to the treatment, product and lot.
- [ ] Seriousness is classified and the correct DAEN database is targeted (medicine vs device), derived from the treatment modality; mandatory-reporting cases are flagged.
- [ ] An AE can be raised directly (finalise close-out) or from a completed complication-response flow, and either way raises follow-up Jobs.
- [ ] The AE links to the lot→client recall lookup (PRD-04) and is part of the immutable clinical record.
- [ ] Full submission/prefill lives in the Governance hub (PRD-08/DAEN); this story is the source record + routing.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Complication protocol cards ('Start response') launch a timestamped checklist that logs the drug used and, on completion, opens a routed adverse-event case (completeComplication) — seriousness pre-set (e.g. Serious), route derived (device for VO/filler, medicine for anaphylaxis).
- An adverse-event capture form linked to the treatment/product/lot (description, onset, seriousness, outcome) reachable from the finalise close-out as well.
- On creation it raises follow-up Jobs (complication follow-up / review) and routes to Governance → Adverse events & DAEN (gov-ae) with seriousness + DAEN target set.
- New vs the prototype (build these): the structured AE capture fields, the modality-derived DAEN routing + mandatory-report flag, and the lot→client recall linkage.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **AdverseEvent** — id, tenant_id, client_id, chart_entry_id (FK), product_id, lot_id, onset_at, seriousness (mild|moderate|serious), daen_target (medicine|device), mandatory_report (bool), description, treatment_given, status (open|reported|closed), created_at
  - _Links to treatment/product/lot; feeds DAEN prefill (PRD-08) and the lot→client recall (PRD-04); raises Jobs. Immutable (amendments only)._
- **Job (referenced, ADR-0023)** — type=ae, linked client/chart, assignee, due, status
  - _AE creation projects follow-up jobs (review / mandatory-report check / client follow-up)._
- **ComplicationResponse (referenced)** — outcome, kit_used[], drug given
  - _A completed response (COMPLICATION-LIBRARY) can raise a pre-filled AdverseEvent._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: AdverseEvent**
  EF Core: AdverseEvent linked to ChartEntry (so it inherits client/treatment/product/lot), with onset, seriousness, daen_target, mandatory_report flag, description, treatment_given, status. tenant_id + Row-Level Security (RLS, the per-tenant database isolation); index by lot_id (recall) and by status (governance worklist). Append-only/immutable like the rest of the clinical record.
- [ ] **AE capture + modality-derived DAEN routing API**
  Command to log an AE from a ChartEntry or a completed complication response. Derive daen_target from the treatment modality (toxin/filler-as-medicine → DAEN-medicines; device-class filler/PDO/RF → DAEN-devices, ADR-0025/C12) and set the mandatory_report flag for the defined cases. Link the lot for the lot→client recall lookup (PRD-04). Emit events that raise follow-up Jobs and feed the PRD-08 DAEN prefill. Enforce C12 as a server-side invariant; audit (ADR-0010).
- [ ] **AE capture UI + complication hand-off**
  Build the structured AE capture form (description, onset, seriousness, product/lot prefilled from the chart, treatment given) reachable from the finalise close-out and from a completed complication-response flow. Show the derived DAEN target + mandatory-report flag. On save, confirm the raised jobs and the route to Governance. Capability-gated to clinical roles; clear states.
- [ ] **Raise follow-up jobs + route to Governance**
  On AE creation, project the right Jobs (complication follow-up/review, mandatory-report check, client follow-up) into the shared queue (ADR-0023) and surface the AE in Governance → Adverse events & DAEN with seriousness + DAEN target set. Keep the full prefilled DAEN submission in PRD-08/DAEN — this task just routes the record and the work.
