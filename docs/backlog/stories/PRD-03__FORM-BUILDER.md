# Configurable intake-form builder (versioned templates)

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/FORM-BUILDER`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a owner / manager, I want to define and version the pre-visit intake forms without code, so that we can adjust the medical-history and screening questions as guidance changes while keeping every past answer tied to the form it was answered against.
Plainly: the admin tool that lets the clinic define what questions appear on the pre-visit intake form — and version those forms so a change never rewrites answers already given. Where it fits: a sibling of pre-visit intake (PRD-03/INTAKE) inside Intake & Consent (PRD-03), which sits between booking (PRD-02) and treatment. INTAKE collects and acts on a client's answers; this story owns the configurable, versioned TEMPLATE those answers are captured against. It is the structural backbone the intake wizard renders and the GATING evaluation relies on (a response is only valid against a known form version), and it mirrors the versioning discipline used for consent (PRD-03/CONSENT).

## How it works

Intake forms are admin-configurable so the clinic can change the medical-history and screening questions as clinical guidance evolves, without a code change. An IntakeForm carries a versioned JSON field schema (field types, labels, options, required flags, contraindication items) and a required flag.
Versioning is the core discipline: editing a form publishes a NEW version and supersedes the old; a submitted IntakeResponse references the form_version it was answered against, so a later edit never rewrites or invalidates an answer already given (mirrors CONSENT's versioning). The GATING evaluation can therefore reason about whether a response is current.
Submitted answers are validated server-side against the active schema; templates are tenant-scoped (RLS). The v1 medical-history & screening template (history checkboxes, contraindication items, the embedded BDD/wellbeing block from PRD-03/BDD) is seeded.

## Requirements

- To define and version the pre-visit intake forms without code.

## Acceptance Criteria

- [ ] Admins can define intake fields (a JSON field schema) without code, including required flags and contraindication items.
- [ ] Editing a form creates a NEW version; previously submitted responses stay bound to the version they were answered against.
- [ ] Submitted answers are validated server-side against the form's schema.
- [ ] Templates are tenant-scoped and the v1 medical-history & screening template is seeded.

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — the Templates table lists 'Medical history & screening · Intake · v4.0 · Current'; a '+ New template' affordance creates/edits a versioned form.
- Form editor: add/reorder fields (checkbox/radio/text), mark required, tag contraindication items; medical-history step uses checkboxes incl. 'None of the above'.
- Editing a current form warns it will publish a new version; superseded versions remain viewable for responses bound to them.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeForm** — id, tenant_id, name, version, fields(json schema), required(bool), status(current|superseded)
  - _Configurable; versioned; editing publishes a new version; old versions immutable so bound responses stay valid._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Versioned IntakeForm + JSON field schema**
  Behaviour: model IntakeForm (name, version, fields as a JSON schema, required flag) so admins define fields without code. Requirements: tenant-scoped (RLS (row-level security)); editing publishes a NEW version and supersedes the old; old versions are immutable so a bound IntakeResponse stays valid; seed the v1 medical-history & screening template (history checkboxes, contraindication items, the embedded BDD/wellbeing block).
- [ ] **Server-side answer validation against the active schema**
  Behaviour: validate every submitted set of answers against the form's field schema. Requirements: enforced server-side (a malformed/out-of-schema submission is rejected); required fields must be present for the response to count toward the GATING evaluation; the response is stamped with the exact form_version validated against.
- [ ] **Form-builder admin UI (add/reorder/require fields)**
  Behaviour: a Forms & consent editor to add/reorder fields (checkbox/radio/text), mark required, and tag contraindication items, reached via '+ New template'. Requirements: editing a current form warns it will publish a new version; superseded versions remain viewable for responses bound to them; capability-gated admin.
