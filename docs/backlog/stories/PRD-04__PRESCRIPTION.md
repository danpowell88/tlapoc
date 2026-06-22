# Individual prescription (no batch / no async)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRESCRIPTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CONSULT`, `PRD-01/CREDENTIALS`

## Background

As a prescriber, I want to write an individual prescription for this patient tied to their consult, so that prescribing is lawful and patient-specific.
An individual prescription per client per consult — never batch/standing-order, never async (text/email/online-only) (C2). Supports the designated RN prescriber identity.

## How it works

An individual prescription per client per consult is the second link in the moat (C2). QLD's Medicines and Poisons (Medicines) Regulation 2021 and AHPRA forbid standing-order / batch scripts and async-only prescribing for S4 cosmetic injectables: a standing order cannot authorise an RN to administer toxin. The script is the legal authority an administering RN acts against.
Three prescriber identities are valid (rev 5 re-review): an NP/on-site prescriber, a remote telehealth prescriber, and — new from QLD Sept 2025 — a designated RN prescriber, who may prescribe S2–S4 in partnership with an authorised prescriber. The last is gated on a verified AHPRA endorsement AND a recorded partnered prescriber (GAP-1).
After a synchronous Consult (PRD-04/CONSULT), the prescriber writes one Prescription for one client tied to that one consult: product, dose/units, quantity, off-label flag. The (client, consult, single-Rx) shape is enforced — there is no data path to attach one script to many clients or to create a standing-order/batch script.
The prescriber identity is resolved through the PRD-01 credential gate: NP and remote prescriber carry the prescribe-S4 capability directly; the designated-RN-prescriber preset only unlocks it when both a verified endorsement and a partnered_prescriber_id are present, else it behaves as a plain administer-only RN.
Off-label use is flagged on the script; the linked consent (PRD-03) must cover off-label use before an administration against this script can proceed (C5, AC8). The prescriber assumes TGA-equivalent responsibility for off-label safety/efficacy and informed consent.
The Prescription has a lifecycle status (active -> consumed | expired). 'Consumed' is set when an administration draws against it; the administration gate (PRD-04/ADMIN-GATE) only accepts a valid, unexpired, UNCONSUMED script for the same client.

## Requirements

- To write an individual prescription for this patient tied to their consult.
- Compliance: [C2](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] One prescription per client per consult; applying one script to multiple clients is rejected.
- [ ] Standing-order/batch scripts and async-only prescribing are impossible to create.
- [ ] Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
- [ ] Off-label is flagged on the script and requires consent covering off-label use.

## UI designs / screenshots

- Prototype screen: Charting — 'Write prescription' (charting.png).
- 'Write prescription' on the 'Consult & prescription' card opens the script: product, dose/units, quantity, off-label flag — tied to the just-recorded consult and this single client.
- When the user is an administering RN the card shows the script they administer against: prescriber (Dr Lena Park NP), date, '30u authorised', 'individual (this client)' — never a batch.
- Attempting a batch/standing-order, or applying one script to multiple clients, is rejected with an explanatory reason.
- Designated-RN-prescriber: the 'Write prescription' action only appears when the endorsement + partnered prescriber are present; otherwise the RN sees the administer-on-script view only.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Prescription** — id, tenant_id, client_id, consult_id, prescriber_id, partnered_prescriber_id?, product_id, dose_units, quantity, off_label(bool), status(active|consumed|expired), created_at, expires_at
  - _One per client per consult (C2). consult_id FK is mandatory. partnered_prescriber_id required when the prescriber is a designated RN prescriber (GAP-1). off_label gates against ImageConsent/Consent off-label coverage (C5)._
- **Prescriber (StaffProfile capability)** — staff_id, capability(prescribe-S4), ahpra_endorsement?, partnered_prescriber_id?
  - _prescribe-S4 unlocked for NP/remote directly; for a designated RN prescriber only with a verified endorsement + partnered prescriber (PRD-01 credential gate)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Prescription entity, lifecycle status & off-label flag (model & migration)**
  Add Prescription: id, tenant_id, client_id, consult_id(FK, NOT NULL), prescriber_id, partnered_prescriber_id (nullable), product_id, dose_units, quantity, off_label(bool), status(active|consumed|expired), created_at, expires_at; RLS by tenant_id. There is intentionally NO 'client_ids' / batch column — the schema makes a batch script unrepresentable. Unique-ish shape: one active Rx per (client_id, consult_id, product_id). Index (client_id, status, expires_at) for the admin-gate lookup of a valid unconsumed script.
- [ ] **Prescribing API + 3 prescriber identities**
  Endpoints: POST /clients/{id}/consults/{cid}/prescriptions (create individual script), GET /clients/{id}/prescriptions?status=active. Resolve prescriber via the PRD-01 capability gate: NP / remote carry prescribe-S4; a designated RN prescriber only passes when ahpra_endorsement is verified AND partnered_prescriber_id is set, else 403 behaving as a plain RN (GAP-1). Reject any payload that would target more than one client or omit consult_id. off_label=true requires the linked Consent to cover off-label use (C5) — return an explainable reason if not.
- [ ] **C2 individual-only invariant + status transitions + audit**
  Enforce in domain + DB (ADR-0008): no standing-order / batch / async-only path can create a script; applying one script to multiple clients is rejected. Status transitions: active -> consumed (set by an administration draw, PRD-04/ADMIN-GATE) | active -> expired (by expires_at). A consumed/expired script is not selectable for administration. Audit every script create + status change to the append-only stream.
