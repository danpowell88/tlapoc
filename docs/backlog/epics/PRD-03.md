# PRD-03 — Intake, consent & compliance gating

> **Stage / Milestone:** M2 · Booking, CRM, intake & consent (PRD-02, PRD-03)  ·  **Phase:** 1  ·  **Stories:** 29

Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s. Treatment is blocked until required intake/consent is complete and current.

**Source PRD:** `docs/prds/PRD-03-intake-consent-gating.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `INTAKE` | [Pre-visit intake — basic capture & chart-link](../stories/PRD-03__INTAKE.md) | Story | P0 | 5 | 2 |
| `INTAKE-RESCREEN` | [Pre-visit intake: re-screen vs full form (new/returning)](../stories/PRD-03__INTAKE-RESCREEN.md) | Story | P2 | 2 | 1 |
| `INTAKE-MEDICAL-HISTORY` | [Pre-visit intake: medical-history step & quick safety check](../stories/PRD-03__INTAKE-MEDICAL-HISTORY.md) | Story | P2 | 2 | 1 |
| `INTAKE-STAFF-STATUS` | [Pre-visit intake: staff status + send/chase](../stories/PRD-03__INTAKE-STAFF-STATUS.md) | Story | P2 | 2 | 1 |
| `FORM-BUILDER` | [Intake-form builder — basic versioned templates](../stories/PRD-03__FORM-BUILDER.md) | Story | P1 | 3 | 1 |
| `FORM-BUILDER-VALIDATION` | [Intake-form builder: server-side answer validation](../stories/PRD-03__FORM-BUILDER-VALIDATION.md) | Story | P2 | 2 | 1 |
| `FORM-BUILDER-ADMIN-UI` | [Intake-form builder: form-builder admin UI](../stories/PRD-03__FORM-BUILDER-ADMIN-UI.md) | Story | P2 | 2 | 1 |
| `BDD` | [BDD / psychological screening — basic instrument & scoring](../stories/PRD-03__BDD.md) | Story | P0 | 5 | 1 |
| `BDD-REVIEW-GATE` | [BDD screening: positive-flag surfacing & RN/NP review requirement](../stories/PRD-03__BDD-REVIEW-GATE.md) | Story | P2 | 2 | 1 |
| `BDD-WELLBEING-UI` | [BDD screening: wellbeing questions in the intake wizard](../stories/PRD-03__BDD-WELLBEING-UI.md) | Story | P2 | 2 | 1 |
| `BDD-STAFF-CHIP` | [BDD screening: prescriber/staff screening chip UI](../stories/PRD-03__BDD-STAFF-CHIP.md) | Story | P2 | 2 | 1 |
| `CONSENT` | [Versioned e-signed consent — basic signature capture](../stories/PRD-03__CONSENT.md) | Story | P0 | 5 | 1 |
| `CONSENT-READER-UI` | [Consent: plain-language reader & type-to-sign](../stories/PRD-03__CONSENT-READER-UI.md) | Story | P2 | 2 | 1 |
| `CONSENT-STATUS-CHIP` | [Consent: status chip & blocked-action banner](../stories/PRD-03__CONSENT-STATUS-CHIP.md) | Story | P2 | 2 | 1 |
| `CONSENT-TEMPLATE-ADMIN` | [Consent templates — basic versioned per-treatment templates](../stories/PRD-03__CONSENT-TEMPLATE-ADMIN.md) | Story | P1 | 3 | 1 |
| `CONSENT-TEMPLATE-MANDATED-GATE` | [Consent templates: mandated-content validation gate on publish](../stories/PRD-03__CONSENT-TEMPLATE-MANDATED-GATE.md) | Story | P2 | 2 | 1 |
| `CONSENT-TEMPLATE-AUTHORING-UI` | [Consent templates: authoring UI & audit](../stories/PRD-03__CONSENT-TEMPLATE-AUTHORING-UI.md) | Story | P2 | 2 | 1 |
| `IMAGE-CONSENT` | [Image-use consent — basic entity & grant/withdraw](../stories/PRD-03__IMAGE-CONSENT.md) | Story | P1 | 3 | 1 |
| `IMAGE-CONSENT-ENFORCEMENT` | [Image-use consent: downstream media-use enforcement on withdraw](../stories/PRD-03__IMAGE-CONSENT-ENFORCEMENT.md) | Story | P2 | 2 | 1 |
| `IMAGE-CONSENT-CLIENT-TOGGLE` | [Image-use consent: client self-manage toggle](../stories/PRD-03__IMAGE-CONSENT-CLIENT-TOGGLE.md) | Story | P2 | 2 | 1 |
| `IMAGE-CONSENT-STAFF-CHIP` | [Image-use consent: staff header chip](../stories/PRD-03__IMAGE-CONSENT-STAFF-CHIP.md) | Story | P2 | 2 | 1 |
| `COOLING-OFF` | [Cooling-off — basic under-18 7-day enforcement](../stories/PRD-03__COOLING-OFF.md) | Story | P1 | 3 | 1 |
| `COOLING-OFF-PAYMENT-BLOCK` | [Cooling-off: payment-block coordination & deposit suppression (F14)](../stories/PRD-03__COOLING-OFF-PAYMENT-BLOCK.md) | Story | P2 | 2 | 1 |
| `COOLING-OFF-ADULT-CONFIG` | [Cooling-off: optional adult cooling-off config (not a gate)](../stories/PRD-03__COOLING-OFF-ADULT-CONFIG.md) | Story | P2 | 2 | 1 |
| `COOLING-OFF-CHIP-UI` | [Cooling-off: header chip & done-screen note](../stories/PRD-03__COOLING-OFF-CHIP-UI.md) | Story | P2 | 2 | 1 |
| `GUARDIAN-CONSENT` | [Under-18 guardian consent — basic guardian co-signature](../stories/PRD-03__GUARDIAN-CONSENT.md) | Story | P1 | 3 | 1 |
| `GUARDIAN-CONSENT-SECOND-CONSULT` | [Under-18 guardian consent: recorded second consultation](../stories/PRD-03__GUARDIAN-CONSENT-SECOND-CONSULT.md) | Story | P2 | 2 | 1 |
| `GUARDIAN-CONSENT-COSIGN-UI` | [Under-18 guardian consent: co-sign step in the consent flow](../stories/PRD-03__GUARDIAN-CONSENT-COSIGN-UI.md) | Story | P2 | 2 | 1 |
| `GATING` | [Server-enforced treatment gating](../stories/PRD-03__GATING.md) | Story | P0 | 5 | 2 |

_Totals: 29 stories · 31 tasks._
