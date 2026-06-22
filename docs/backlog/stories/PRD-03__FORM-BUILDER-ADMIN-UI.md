# Intake-form builder: form-builder admin UI

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/FORM-BUILDER-ADMIN-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/FORM-BUILDER`

## Background

As a owner / manager, I want an editor to add, reorder and require intake fields without code, so that I can adjust the medical-history and screening questions myself.
Plainly: the Forms & consent editor that lets an admin add/reorder fields, mark them required, and tag contraindication items, publishing a new version on edit. Where it fits: a follow-up to the intake-form builder basic versioned templates (PRD-03/FORM-BUILDER) that adds the authoring UI on top of the versioned schema. It is the consent-form counterpart of the intake builder, capability-gated to admin. It sits in Intake & Consent (PRD-03).

## How it works

The basic story models the versioned form schema; this follow-up adds the editor that lets an admin author it without code. A Forms & consent editor adds/reorders fields (checkbox/radio/text), marks them required, and tags contraindication items, reached via '+ New template'.
Editing a current form warns the admin that it will publish a new version (consistent with the basic's versioning discipline), and superseded versions remain viewable for responses bound to them.
The admin UI is capability-gated so only authorised staff change the intake questions.

## Requirements

- An editor to add, reorder and require intake fields without code.

## Acceptance Criteria

- [ ] A Forms & consent editor adds/reorders fields (checkbox/radio/text), marks required, and tags contraindication items, reached via '+ New template'.
- [ ] Editing a current form warns it will publish a new version.
- [ ] Superseded versions remain viewable for responses bound to them.
- [ ] The admin UI is capability-gated.

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — '+ New template' opens the form editor; the Templates table lists e.g. 'Medical history & screening · Intake · v4.0 · Current'.
- Form editor: add/reorder fields (checkbox/radio/text), mark required, tag contraindication items.
- Editing a current form warns it will publish a new version; superseded versions remain viewable.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeForm (extends FORM-BUILDER)** — authored via the editor; editing publishes a new version
  - _Capability-gated admin; superseded versions remain viewable for bound responses._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Form-builder admin UI (add/reorder/require fields)**
  Behaviour: a Forms & consent editor to add/reorder fields (checkbox/radio/text), mark required, and tag contraindication items, reached via '+ New template'. Requirements: editing a current form warns it will publish a new version; superseded versions remain viewable for responses bound to them; capability-gated admin.
