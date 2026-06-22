# Guided toxin treatment note & pre-treatment review

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/Rx surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

## How it works

As an injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
Charting at The Lounge is not a blank text box — it is a guided, treatment-type-aware flow that puts the safety- and compliance-critical context in front of the clinician before they touch a single field. The note itself is templated (structured fields + free text + reusable phrases) so a routine anti-wrinkle treatment can be charted in under a minute without losing the medico-legal detail an AHPRA inspection expects.
Step 1 is a Pre-treatment review card the injector reads before anything is editable: safety flags (allergies, contraindications, BDD-screen result), the linked consult/prescription status, and a one-line Last treatment summary (e.g. '24u · 12 Mar · forehead + glabella · Bella RN') with a 'Copy last map' shortcut. These are read-only chips pulled from PRD-03 (intake/consent/screening) and PRD-04 (consult/Rx) — the injector confirms them, the system does not let them be edited here.
A treatment-type toggle (Anti-wrinkle (toxin) / Skin treatment) selects which template renders. The toxin template is a configurable NoteTemplate: structured fields (indication, areas, technique notes, aftercare) plus a free-text area and a library of reusable phrases/snippets the clinic curates. Selecting 'Skin treatment' swaps in a non-S4 skin-note variant (areas / device / settings / consumables) with no prescription or lot — built in PRD-05/MAPPING's skin-note story.
Charting cannot open at all unless the consult + consent gate (PRD-03/PRD-04) is satisfied — the safe path is the only path. The gate state is shown as header chips ('Consult ✓ · Consent ✓ · screening clear'); when it is not satisfied the entry point is blocked with a reason rather than opening a half-usable note.
The same NoteTemplate model is what later modalities (filler, energy, weight-loss) extend, so the template engine is built generically now even though v1 only ships the toxin template and the non-S4 skin variant.

## Requirements

- A guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template.

## Acceptance Criteria

- [ ] Step 1 'Pre-treatment review' surfaces safety flags, the last-treatment summary and the linked consult/Rx as read-only context the injector confirms before the note becomes editable.
- [ ] The toxin template is configurable per tenant: structured fields, free text and reusable phrases/snippets, all versioned.
- [ ] A treatment-type toggle switches between the toxin template and the non-S4 skin-note variant; the rendered fields change accordingly.
- [ ] Charting cannot open unless the consult + consent gate (PRD-03/04) is satisfied; a blocked entry point states why and who can resolve it.
- [ ] 'Copy last map' / copy-last-note pre-fills from the client's previous matching treatment for editing (never auto-finalised).

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Header: 'Charting — {client}' with a green gate chip ('Consult ✓ · Consent ✓ · screening clear') and a 'Read-only view' chip for oversight roles.
- Treatment-type toggle pills: 'Anti-wrinkle (toxin)' (default) / 'Skin treatment' (renderChartReview + applyChartType swap the template).
- Step 1 'Pre-treatment review' card: safety chips (Allergies: none · Contraindications: none · BDD screen: clear · Consent ✓ · Consult ✓), a 'Last treatment' row ('24u · 12 Mar · forehead + glabella · Bella RN') with a 'Copy last map' button, and a 'Consult & prescription' panel that surfaces the synchronous-consult + individual-Rx chain inline (prescriber writes / administrator verifies).
- The toxin note template lives in the same flow; a finalise close-out (aftercare · recall · 2-day wellbeing call · adverse event) captures the wrap-up before checkout (closeoutGo).
- New vs the prototype (build these): the template builder/admin (fields + snippets), template versioning, and the non-S4 skin-note variant toggle wired to its own fields.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry** — id, tenant_id, client_id, appointment_id, consult_id, treatment_type (toxin|skin|...), status (draft|final), author_id, finalised_at, locked
  - _Shared spine with MAPPING; one per treatment. Immutable once final (ADR-0010)._
- **NoteTemplate** — id, tenant_id, treatment_type, version, fields (json schema of structured fields), snippets[] (reusable phrases), active
  - _Configurable per tenant + versioned; the toxin template and the non-S4 skin variant are two instances of the same model._
- **NoteValue** — id, chart_entry_id, template_version, structured (json keyed to template fields), free_text
  - _Captured note content bound to the template version used, so a finalised note always renders against the schema it was written with._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: ChartEntry + NoteTemplate**
  EF Core entities + migrations (every table tenant_id + RLS). ChartEntry carries treatment_type, status, consult_id/appointment_id links and the locked flag (immutability lands in IMMUTABILITY). NoteTemplate is versioned and tenant-scoped, holding a JSON field-schema + a snippet library; NoteValue binds captured content to the template version so a finalised note always renders against the schema it was authored with. Index ChartEntry by client and appointment.
- [ ] **Charting API: gated draft open + guided note capture**
  Open-draft command is gate-checked server-side (reject unless PRD-03 consent + PRD-04 consult/Rx are satisfied — never trust the UI) and returns the pre-treatment review payload (safety flags, last-treatment summary, consult/Rx status) read-only. CRUD for note structured fields/free text against the active template version; a 'copy last' query that pre-fills from the client's previous matching ChartEntry. Emit domain events for the visit lifecycle (ADR-0024) and publish the OpenAPI contract.
- [ ] **Provider/web UI: pre-treatment review + template + type toggle**
  Build the Charting screen per the spec: header gate chips, the read-only Step-1 pre-treatment review card, the toxin note template (structured fields + free text + snippet picker) and the treatment-type toggle that swaps to the non-S4 skin-note variant. Wire to the API with loading/empty/error states; show the blocked-action banner when the gate is unmet; capability-gate to clinical roles and render the read-only oversight view for non-editors. Include the clinic-side template/snippet admin.
