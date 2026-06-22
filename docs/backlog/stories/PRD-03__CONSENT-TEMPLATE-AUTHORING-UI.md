# Consent templates: authoring UI & audit

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT-TEMPLATE-AUTHORING-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/CONSENT-TEMPLATE-ADMIN`

## Background

As a owner / manager, I want an editor to author and version consent templates, with every change audited, so that I can maintain the consent wording while keeping a clear change trail.
Plainly: the Forms & consent template editor — the mandated sections as named required blocks, a '+ New template' affordance, a publish action, and an audit of every change. Where it fits: a follow-up to the consent templates basic versioned templates (PRD-03/CONSENT-TEMPLATE-ADMIN) that adds the authoring UI on top of the versioned template. It surfaces the mandated-content publish gate (PRD-03/CONSENT-TEMPLATE-MANDATED-GATE) and is capability-gated. It sits in Intake & Consent (PRD-03).

## How it works

The basic story models versioned consent templates; this follow-up adds the editor that authors them. The Forms & consent template editor presents the mandated-content sections as named required blocks, a '+ New template' affordance, and a publish action (disabled until complete, surfacing the mandated-content gate).
Editing a current template warns it will publish a new version (consistent with the basic's versioning), and superseded versions remain viewable for signatures bound to them.
The editor is capability-gated so only authorised staff change consent wording, and every authoring change is audited.

## Requirements

- An editor to author and version consent templates, with every change audited.
- Compliance: [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The Forms & consent template editor presents the mandated sections as named required blocks, with a '+ New template' affordance and a publish action.
- [ ] Editing a current template warns it will publish a new version.
- [ ] Superseded versions remain viewable for signatures bound to them.
- [ ] The editor is capability-gated and every change is audited.

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — Templates table with version + status (e.g. 'Anti-wrinkle consent v3.2 · Current'); '+ New template' opens the editor.
- Template editor with the mandated-content sections as named, required blocks; a publish action disabled until all mandated sections are filled.
- Editing a current template warns it will publish a new version; superseded versions remain viewable; every change audited.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ConsentTemplate (extends CONSENT-TEMPLATE-ADMIN)** — authored via the editor; editing publishes a new version
  - _Capability-gated; every authoring change audited; superseded versions remain viewable for bound signatures._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Template authoring UI + audit**
  Behaviour: the Forms & consent template editor — the mandated sections as named required blocks, a '+ New template' affordance, and a publish action disabled until complete. Requirements: editing a current template warns it will publish a new version; superseded versions remain viewable for signatures bound to them; capability-gated; every change audited.
