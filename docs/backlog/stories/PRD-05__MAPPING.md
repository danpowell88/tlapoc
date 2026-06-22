# Injection-mapping canvas: add/edit points + save draft (MVP)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-CANVAS`, `PRD-04/RECALL-LOOKUP`

## Background

As a injector, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.
The injection-mapping canvas: on a facial diagram or photo the injector taps to drop and drags each injection point, recording product, dose in units, depth, technique and the batch-lot drawn from. It is the clinical hero screen of PRD-05, sitting right after the S4 (Schedule 4 'Prescription Only Medicine') consult/prescribing moat (PRD-04) on the clinic-first spine, opening after the pre-treatment review (NOTE-TEMPLATE) and feeding immutable finalisation (IMMUTABILITY), which deducts charted units from stock on finalise. On a facial diagram and/or patient photo, tap-to-add and drag injection points, each capturing product, units, depth, technique and batch-lot/expiry; charted units deduct from the selected lot on finalise (REQ-CLIN-2, C8).

## How it works

As an injector, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.
The injection map is the clinical hero screen and the evidentiary heart of the S4 medicine register: it records exactly what was injected, where on the face, how much, and from which vial — the data that later proves the consult→prescription→administration chain and powers the lot→client recall and vial reconciliation.
It sits inside the guided charting flow as step 3 and only opens once the consult + consent gate is satisfied (PRD-03/PRD-04). Step 1 surfaces the pre-treatment review (NOTE-TEMPLATE); step 2 forces the injector to choose the exact product and the in-date, in-custody, Australian Register of Therapeutic Goods (ARTG)-checked lot they are drawing from before any point is placed; step 3 is the map itself.
Each point is tap-to-add on a facial diagram (or the patient photo) and drag-to-fine-tune; coordinates are stored as a percentage of the image so they survive different render sizes and the room-side provider app. A point carries units, plus depth and technique in the real build (the prototype captures name + units only). A running Total units sums the points live, and the active 'Product · lot' label is shown so the injector always knows which vial they are charting against.
On Finalise, the charted Σunits are decremented from the selected lot inside one transaction (a StockLedger administration movement, PRD-04), the note is locked (immutable — later edits become appended amendments per ADR-0010, built in IMMUTABILITY), and every point becomes part of the medicine register with its lot→client link for recall and vial reconciliation. Finalise is rejected if the units exceed on-hand, and is idempotent so a retried request never double-deducts.
It is modality-aware: anti-wrinkle (toxin) shows the map + lot step, while a non-S4 skin treatment shows a note variant (areas, device/modality, settings, consumables) with no prescription or lot. Built web-first; the provider app (PRD-09, later) re-surfaces the same canvas room-side and offline (OFFLINE). 'Auto-detect' landmark suggestions are advisory + human-confirmed and deferred to Phase 2 (no AI in v1, ADR-0020) — v1 is manual tap-to-add + drag only.

## Requirements

- To drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Charting opens with product & batch (lot) selection, restricted to in-date / ARTG / in-custody stock; no point can be placed until a valid lot is selected.
- [ ] Each point records product, units, depth, technique and batch-lot/expiry; coordinates are stored relative to the image so they reproduce at any size.
- [ ] On finalise, charted units deduct from the selected lot in one transaction and write the lot→client register link (PRD-04); finalise is rejected if Σunits > on-hand and is idempotent.
- [ ] Built on the SPIKE-CANVAS approach; the canvas adds/drags points smoothly with many points and works room-side on the provider app.
- [ ] 'Auto-detect' is advisory + human-confirmed and deferred to Phase 2 (no AI in v1); v1 is manual tap-to-add + drag.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Screen header: 'Charting — {client}' with live gate chips (Consult ✓ · Consent ✓ · screening clear); a 'Read-only view' chip replaces edit controls for oversight roles (e.g. owner).
- Treatment-type toggle pills: 'Anti-wrinkle (toxin)' / 'Skin treatment' — switches between the injection map and the non-S4 skin note.
- Step 2 — Product & batch card (toxin only): Product dropdown + Batch/lot dropdown listing only in-date / in-custody / ARTG-checked lots, a lot-info line (on hand · location · in-date/expiring · S4), and the helper 'Units charted below deduct from this lot on finalise.'
- Step 3 — Injection map (toxin only): LEFT = face image/diagram in a crosshair-cursor wrapper; tap to add a numbered pin, drag to reposition; 'Auto-detect' (advisory, Phase 2) and 'Clear' buttons. RIGHT = selected-point editor (label, units, lot/exp shown), the point list, a 'Total units' running sum, and the active 'Product · lot' label; helper 'Tap the face to add · drag a point to fine-tune.'
- Right rail: Before/after compare with a draggable slider ('stored securely, never on device'); 'Finalise & checkout' button (locks the note, deducts units) — hidden in read-only.
- New vs the prototype (build these too): per-point depth and technique/needle fields, optional per-point product/lot for multi-product sessions, and the amendment trail for post-finalise edits.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry** — id, tenant_id, client_id, appointment_id, consult_id, treatment_type (toxin|skin|filler|...), status (draft|final), author_id (RN/NP), finalised_at, locked
  - _One per treatment. Immutable once final; post-finalise changes create a linked Amendment (ADR-0010)._
- **InjectionPoint** — id, chart_entry_id (FK), product_id (FK Product), lot_id (FK StockItem), units (decimal), depth, technique, coord_x, coord_y (percent of image/diagram), region/label, sequence
  - _Prototype pts[]{id,name,u,x,y} maps to {label=name, units=u, coord_x=x, coord_y=y}; the real build adds product_id, lot_id, depth, technique._
- **SkinNote (non-S4 variant)** — id, chart_entry_id, areas[] (enum), device_modality, settings_text, consumables_text
  - _No prescription or lot; non-S4._
- **Amendment** — id, chart_entry_id, author_id, created_at, reason, payload
  - _Append-only edits after finalise; original preserved (built in IMMUTABILITY)._
- **Links / derived** — InjectionPoint.lot_id → StockItem/StockLedger (PRD-04): finalise writes an administration movement per lot, decrements on-hand, and powers lot→client recall + vial reconciliation. ChartEntry.consult_id → Consult/Prescription gate (PRD-04). Photos link to ChartEntry (PHOTOS). total_units = Σ InjectionPoint.units (shown live; reconciled on finalise).

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Injection-map canvas: tap-to-add + drag pins (image-relative)**
  Behaviour: the LEFT pane is a facial diagram/photo in a crosshair-cursor wrapper; tapping adds a numbered pin and dragging repositions it (prototype faceClick/startDrag/renderInj). Requirements: build on the SPIKE-CANVAS approach; coordinates are stored as a percentage of the image (coord_x/coord_y 0–100) so they reproduce at any render size and room-side on the provider app; drag clamps pins to 2–98% so they stay on-image; the canvas must stay smooth with many points. A 'Clear' button removes all pins; honour a read-only mode (oversight roles see pins/detail, no edit controls).
- [ ] **Per-point editor + point list + live total**
  Behaviour: the RIGHT pane is the selected-point editor — label, units (depth and technique/needle in the real build), with the active 'Lot · exp' shown — plus the point list and a running 'Total units' that sums all points live (prototype editor/ptlist/totalu/updPt). Requirements: selecting a pin opens its editor; the live Σunits is recomputed by the server on every write rather than trusting a client total; the real build adds per-point depth + technique and optional per-point product/lot for multi-product sessions (the prototype captures name + units only). Read-only roles see point detail without editors.
- [ ] **Charting API: open draft, add/move/delete points, draft sync**
  Behaviour: gate-checked draft open (reject unless consult+consent satisfied), then CRUD for points. Requirements: validate on every write that the selected lot is in-date, in-custody and ARTG (Australian Register of Therapeutic Goods)-checked and that the product matches the lot; coordinates accepted as 0–100 percentages; the server recomputes the live Σunits. Emit draft-changed domain events for offline sync (OFFLINE) + read models; publish the OpenAPI contract. tenant_id + Row-Level Security (RLS, the per-tenant database isolation); index InjectionPoint by lot_id for the lot→client recall lookup (C8). Finalisation + transactional stock deduction is a follow-up (PRD-05/MAPPING-FINALISE); this basic ends at a saved draft.
