# PRD-03 — Intake, consent & compliance gating

> **Stage / Milestone:** M2 · Booking, CRM, intake & consent (PRD-02, PRD-03)  ·  **Phase:** 1  ·  **Stories:** 9

Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s. Treatment is blocked until required intake/consent is complete and current.

**Source PRD:** `docs/prds/PRD-03-intake-consent-gating.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `INTAKE` | [Pre-visit intake forms](../stories/PRD-03__INTAKE.md) | Story | P0 | 5 | 4 |
| `FORM-BUILDER` | [Configurable intake-form builder (versioned templates)](../stories/PRD-03__FORM-BUILDER.md) | Story | P1 | 3 | 3 |
| `BDD` | [BDD / psychological screening instrument](../stories/PRD-03__BDD.md) | Story | P0 | 5 | 4 |
| `CONSENT` | [Versioned e-signed consent with mandated content](../stories/PRD-03__CONSENT.md) | Story | P0 | 5 | 3 |
| `CONSENT-TEMPLATE-ADMIN` | [Consent template authoring & versioning (mandated-content)](../stories/PRD-03__CONSENT-TEMPLATE-ADMIN.md) | Story | P1 | 3 | 3 |
| `IMAGE-CONSENT` | [Separate, withdrawable image-use consent](../stories/PRD-03__IMAGE-CONSENT.md) | Story | P1 | 3 | 4 |
| `COOLING-OFF` | [Cooling-off & under-18 payment block](../stories/PRD-03__COOLING-OFF.md) | Story | P1 | 3 | 4 |
| `GUARDIAN-CONSENT` | [Under-18 guardian consent & recorded second consultation](../stories/PRD-03__GUARDIAN-CONSENT.md) | Story | P1 | 3 | 3 |
| `GATING` | [Server-enforced treatment gating](../stories/PRD-03__GATING.md) | Story | P0 | 5 | 2 |

_Totals: 9 stories · 30 tasks._
