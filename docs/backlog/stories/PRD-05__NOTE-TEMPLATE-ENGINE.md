# Charting: configurable, versioned note-template engine + snippet admin

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE-ENGINE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a clinic admin, I want to build and version note templates with structured fields and reusable snippets, so that notes stay consistent and a finalised note always renders against the version it was written with.
Plainly: this lets the clinic design and version its own treatment-note templates — choosing the structured fields and curating reusable phrases — instead of a single fixed note. Where it fits: a follow-up to PRD-05/NOTE-TEMPLATE that generalises the basic's fixed toxin note into a configurable, versioned engine. The same generic engine is what later modalities (filler, energy, weight-loss) extend, and it ensures a finalised note always renders against the exact template version it was authored with.

## How it works

This follow-up generalises the basic's fixed toxin note into a configurable engine. The toxin note becomes a per-tenant NoteTemplate — structured fields (indication, areas, technique notes, aftercare), a free-text area and a curated library of reusable phrases/snippets — with a clinic-side builder/admin and template versioning.
NoteValue binds captured content to the template version used so a finalised note always renders against the schema it was authored with — a later template edit never silently re-renders an old note.
The same generic engine is what later modalities (filler, energy, weight-loss) extend, even though v1 ships only the toxin template + the non-S4 skin variant. tenant_id + Row-Level Security (RLS, the per-tenant database isolation) throughout.

## Requirements

- To build and version note templates with structured fields and reusable snippets.

## Acceptance Criteria

- [ ] The toxin note is a per-tenant NoteTemplate: structured fields (indication, areas, technique notes, aftercare), a free-text area and a curated library of reusable phrases/snippets.
- [ ] A clinic-side builder/admin lets the clinic edit fields and snippets; templates are versioned.
- [ ] NoteValue binds captured content to the template version used, so a finalised note always renders against the schema it was authored with.
- [ ] The same generic engine is what later modalities (filler, energy, weight-loss) extend.

## UI designs / screenshots

- A clinic-side template builder/admin: add/edit/reorder structured fields and curate the reusable-phrase/snippet library, with template versioning.
- The charting note renders against the active template version; a finalised note renders against the version it was authored with.
- Capability-gated to a clinic-admin role.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **NoteTemplate** — id, tenant_id, treatment_type, version, fields (json schema of structured fields), snippets[] (reusable phrases), active
  - _New entity (extends the basic's fixed note). Configurable per tenant + versioned; the toxin template and the non-S4 skin variant are two instances of the same model._
- **NoteValue (extended)** — + template_version (the version the content was authored against)
  - _Binds captured content to the template version so a finalised note always renders against its authoring schema._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Versioned NoteTemplate model + version-bound NoteValue**
  Behaviour: the toxin note becomes a per-tenant NoteTemplate (structured fields + free text + curated snippets) with template versioning; NoteValue binds captured content to the template version used. Requirements: a finalised note always renders against the schema it was authored with; the same generic engine is what later modalities extend; tenant_id + Row-Level Security (RLS, the per-tenant database isolation).
- [ ] **Template builder/admin + snippet library (UI)**
  Behaviour: a clinic-side builder/admin to add/edit/reorder structured fields and curate the reusable-phrase/snippet library, with versioning. Requirements: capability-gated to a clinic-admin role; editing a template creates a new version rather than mutating in place.
