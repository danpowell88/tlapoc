# Injection-mapping canvas (per-point lot)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `SPRINT-0/SPIKE-CANVAS`, `PRD-04/RECALL-LOOKUP`

## Background

As a injector, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.
On a facial diagram and/or patient photo, tap-to-add and drag injection points, each capturing product, units, depth, technique and batch-lot/expiry; charted units deduct from the selected lot on finalise (REQ-CLIN-2, C8).

## How it works

The injection map is the clinical hero screen and the evidentiary heart of the S4 medicine register: it records exactly what was injected, where on the face, how much, and from which vial — the data that later proves the consult→prescription→administration chain and powers the lot→client recall.
It sits inside the guided charting flow as step 3 and only opens once the consult + consent gate is satisfied (PRD-03/PRD-04). Step 1 surfaces the pre-treatment review (consult/consent/screening + last visit); step 2 forces the injector to choose the exact product and the in-date, in-custody, ARTG-checked lot they are drawing from before any point is placed; step 3 is the map itself.
Each point is tap-to-add on a facial diagram (or the patient photo) and drag-to-fine-tune. A point carries units, plus depth and technique in the real build. A running Total units sums the points. On Finalise, the charted units are decremented from the selected lot, the note is locked (immutable — later edits are appended amendments per ADR-0010), and every point becomes part of the medicine register with its lot→client link for recall and vial reconciliation (PRD-04).
It is modality-aware: anti-wrinkle (toxin) shows the map + lot step, while a non-S4 skin treatment shows a note variant (areas, device/modality, settings, consumables) with no prescription or lot. Built web-first; the provider app (PRD-09, later) re-surfaces the same canvas room-side and offline. 'Auto-detect' landmark suggestions are advisory + human-confirmed and deferred to Phase 2 (no AI in v1).

## Requirements

- To drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Charting opens with product & batch (lot) selection, restricted to in-date/ARTG/in-custody stock.
- [ ] Each point records product, units, depth, technique and batch-lot/expiry.
- [ ] On finalise, charted units deduct from the selected lot and link to the medicine register + recall (PRD-04).
- [ ] Built on the SPIKE-CANVAS approach; performs smoothly with many points.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Screen header: 'Charting — {client}' with live gate chips (Consult ✓ · Consent ✓ · screening clear); a 'Read-only view' chip replaces edit controls for oversight roles (e.g. owner).
- Treatment-type toggle pills: 'Anti-wrinkle (toxin)' / 'Skin treatment' — switches between the injection map and the non-S4 skin note.
- Step 1 — Pre-treatment review card: safety flags, last treatment, and the linked consult/Rx (read-only summary).
- Step 2 — Product & batch card (toxin only): Product dropdown + Batch/lot dropdown listing only in-date / in-custody / ARTG-checked lots, a lot-info line (exp, on-hand), and the helper 'Units charted below deduct from this lot on finalise.'
- Step 3 — Injection map (toxin only): LEFT = face image/diagram with a crosshair cursor; tap to add a numbered pin, drag to reposition; 'Auto-detect' (advisory, Phase 2) and 'Clear' buttons. RIGHT = selected-point editor (label, units, product, lot, exp), the point list, a 'Total units' running sum, and the active 'Product · lot' label; helper 'Tap the face to add · drag a point to fine-tune.'
- Skin note variant (non-S4): 'Areas treated' multi-select chips (Full face / Cheeks / Under-eye / Neck / Décolletage), Device/modality select (needling / Hydrafacial / Laser-IPL / peel), Settings/depth input, Consumables (non-S4) input; note that no Rx or lot is required.
- Right rail: Before/after compare with a draggable slider ('stored securely, never on device'); 'Finalise & checkout' button (locks note, deducts units) — hidden in read-only.
- New vs the prototype (build these too): per-point depth and technique/needle fields, optional per-point product/lot for multi-product sessions, and an amendment trail for post-finalise edits.
- Prototype reference: prototype.html → Clinical → Charting (section #chart), step 3 'Injection map' (faceClick / renderInj / finaliseChart).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry** — id, tenant_id, client_id, appointment_id, consult_id, treatment_type (toxin|skin|filler|…), status (draft|final), author_id (RN/NP), finalised_at, locked
  - _One per treatment. Immutable once final; post-finalise changes create a linked Amendment (ADR-0010)._
- **InjectionPoint** — id, chart_entry_id (FK), product_id (FK Product), lot_id (FK StockItem), units (decimal), depth, technique, coord_x, coord_y (percent of image/diagram), region/label, sequence
  - _Prototype `pts[]{id,name,u,x,y}` maps to {label=name, units=u, coord_x=x, coord_y=y}; the real build adds product_id, lot_id, depth, technique._
- **SkinNote (non-S4 variant)** — id, chart_entry_id, areas[] (enum), device_modality, settings_text, consumables_text
  - _No prescription or lot; non-S4._
- **Amendment** — id, chart_entry_id, author_id, created_at, reason, payload
  - _Append-only edits after finalise; original preserved._
- **Links / derived** — InjectionPoint.lot_id → StockItem/StockLedger (PRD-04): finalise writes an administration movement per lot, decrements on-hand, and powers lot→client recall + vial reconciliation. ChartEntry.consult_id → Consult/Prescription gate (PRD-04). Photos link to ChartEntry (PRD-05/PHOTOS). total_units = Σ InjectionPoint.units (shown live; reconciled on finalise).

## Technical notes (high level)

- Stack: Flutter provider app

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: ChartEntry + InjectionPoint** — ChartEntry (treatment_type, status, consult/consent links) + InjectionPoint (product, lot, units, depth, technique, coord_x/y). tenant_id + RLS; index by client and by lot for recall.
- [ ] **Charting API: open draft, add/move/delete points** — Gate-checked draft open; CRUD points; live total. Validate the lot is in-date/in-custody/ARTG and product matches.
- [ ] **Finalise endpoint (transactional, immutable)** — Validate gate, lock the note, deduct Σunits from the lot (StockLedger administration movement), write the lot→client register link, reject if units > on-hand. Idempotent + audited (ADR-0010).
- [ ] **Injection-map canvas (web)** — Facial diagram/photo with tap-to-add + drag pins (SPIKE-CANVAS approach); selected-point editor (units/depth/technique), point list, live total, product·lot label; crosshair + read-only mode.
- [ ] **Product & batch (lot) selector** — Step-2 dropdowns restricted to in-date/in-custody/ARTG lots; lot-info line; wire the selected lot into point deductions.
- [ ] **Skin-note (non-S4) variant** — Areas multi-select, device/modality, settings, consumables; no lot/Rx; the treatment-type toggle switches map vs note.
