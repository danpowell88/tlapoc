# Consent templates — basic versioned per-treatment templates

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT-TEMPLATE-ADMIN`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/CONSENT`

## Background

As a owner / manager, I want to author and version per-treatment consent templates with all mandated content, so that every consent a client signs is legally complete and changes never rewrite consents already given.
Plainly: the staff tool for writing and versioning the consent templates clients sign — and the check that each template actually contains everything AHPRA requires before it can be published. Where it fits: a sibling of versioned e-signed consent (PRD-03/CONSENT) inside Intake & Consent (PRD-03). CONSENT owns the client-facing reader and the binding signature; this story owns the authoring side — the per-treatment-type templates, their version history, and the mandated-content validation gate that must pass before a version goes live. It is the consent counterpart to the intake form builder (PRD-03/FORM-BUILDER) and the source of the versions a ConsentSignature binds to.

## How it works

Consent templates are authored per treatment type (anti-wrinkle, dermal filler, under-18 + guardian, image-use) and versioned. Editing a current template publishes a NEW version and supersedes the old; the old version is never mutated, so a ConsentSignature that referenced it stays valid and readable exactly as signed.
Each publishable version must satisfy a mandated_fields[] checklist — nature of the procedure, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language (no minimising/overstating), and complaint mechanisms including the explicit right to complain to AHPRA despite any NDA (C5). The publish action is blocked until every mandated section is present.
Templates and all versions are retained per the retention policy (C18, PRD-01/RETENTION); every authoring change is audited and capability-gated. This is the authoring backbone the client reader (CONSENT) renders and a signature binds to.

## Requirements

- To author and version per-treatment consent templates with all mandated content.

## Acceptance Criteria

- [ ] Templates are per-treatment-type and versioned; editing creates a NEW version and supersedes the old, never mutating it.
- [ ] A version cannot be published unless it covers every mandated-content section (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA).
- [ ] Previously signed consents stay bound to the version they were signed against.
- [ ] Templates and versions are retained per the retention policy (C18) and admin changes are audited.

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — Templates table with version + status (e.g. 'Anti-wrinkle consent v3.2 · Current'; 'Dermal filler consent v2.1 · Current'; 'Under-18 consent (+ guardian) v1.0 · 7-day cool-off'); '+ New template'.
- Template editor with the mandated-content sections as named, required blocks; a publish action disabled until all mandated sections are filled.
- Editing a current template warns it will publish a new version; superseded versions remain viewable for signatures bound to them.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ConsentTemplate** — id, tenant_id, treatment_type, version, content(sections), mandated_fields[], status(current|superseded)
  - _New version on change; old versions immutable + retained (C18); the mandated_fields[] checklist gates publish; bound by ConsentSignature.template_version._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Versioned ConsentTemplate per treatment-type**
  Behaviour: model ConsentTemplate per treatment_type with immutable, versioned content(sections). Requirements: editing creates a NEW version and supersedes the old; old versions are never mutated so bound signatures stay valid; retained per C18 (PRD-01/RETENTION); seed anti-wrinkle, dermal filler, under-18 (+ guardian) and image-use templates; tenant-scoped. The mandated-content publish gate and the authoring UI are follow-ups.
