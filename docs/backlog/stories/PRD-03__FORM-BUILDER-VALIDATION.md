# Intake-form builder: server-side answer validation

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/FORM-BUILDER-VALIDATION`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/FORM-BUILDER`

## Background

As a owner / manager, I want submitted intake answers validated against the form's schema, so that a malformed or incomplete response can never count as a valid intake.
Plainly: validating every submitted set of intake answers against the form's field schema, server-side. Where it fits: a follow-up to the intake-form builder basic versioned templates (PRD-03/FORM-BUILDER) that adds answer validation on top of the versioned schema. It is what lets the treatment gate (PRD-03/GATING) trust that a required, current response is genuinely complete. It sits in Intake & Consent (PRD-03).

## How it works

The basic story models the versioned form schema; this follow-up enforces it on submission. Every submitted set of answers is validated against the form's field schema.
Validation is enforced server-side so a malformed or out-of-schema submission is rejected (it can't slip through the client), and required fields must be present for the response to count toward the GATING evaluation.
The response is stamped with the exact form_version it was validated against, keeping it bound to the correct version even as the form evolves.

## Requirements

- Submitted intake answers validated against the form's schema.

## Acceptance Criteria

- [ ] Every submitted set of answers is validated against the form's field schema.
- [ ] Validation is enforced server-side — a malformed/out-of-schema submission is rejected.
- [ ] Required fields must be present for the response to count toward the GATING evaluation.
- [ ] The response is stamped with the exact form_version validated against.

## UI designs / screenshots

- No new primary screen — validation runs server-side on the intake submission (client-app.png / checkin.png).
- A malformed/incomplete submission is rejected with a clear reason.
- The response is stamped with the form_version validated against.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeResponse (extends FORM-BUILDER)** — validated against IntakeForm.fields(json schema); form_version stamped
  - _Server-side validation; required fields must be present to count toward GATING._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Server-side answer validation against the active schema**
  Behaviour: validate every submitted set of answers against the form's field schema. Requirements: enforced server-side (a malformed/out-of-schema submission is rejected); required fields must be present for the response to count toward the GATING evaluation; the response is stamped with the exact form_version validated against.
