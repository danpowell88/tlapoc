# Cooling-off & under-18 payment block

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/CLIENT-CORE`, `PRD-03/CONSENT`

## Background

As a system, I want to enforce a 7-day cooling-off and payment block for under-18s and record a second consultation, so that minors are protected per the rules.
Cooling-off and the under-18 payment block is the minor-protection rule inside Intake & Consent (PRD-03): for patients under 18 it enforces a mandatory 7-day wait between consent and procedure and blocks payment until it elapses. It builds on the core client record (PRD-01/CLIENT-CORE) for the age flag and on consent (PRD-03/CONSENT), whose timestamp starts the clock. In the flow it coordinates outward with Payments (PRD-06), where the payment block is actually enforced at checkout, and with the deferred booking-deposit placeholder (PRD-02/DEPOSITS), whose holds must be suppressed during the cooling-off window. For adults there is no mandated cooling-off — only an optional clinic-policy setting. As the system, I want to enforce a 7-day cooling-off and payment block for under-18s and record a second consultation, so that minors are protected per the rules.  Under-18s require ≥7 days between consent and procedure plus a payment block (except the consult) and a recorded second consultation; an optional adult cooling-off is configurable (C6).

## How it works

For under-18s the system enforces a mandatory ≥7-day cooling-off between consent and procedure and blocks payment (except the initial consult) until it elapses, and records a second-consultation offer (C6, AHPRA 2 Sept 2025). A CoolingOffTimer is created from the under-18 flag (set at booking) + the consent timestamp: eligible_at = consent_at + 7 days; payment_blocked stays true until eligible_at passes.
The patient header shows an 'under-18 cooling-off' chip with the elapse date; checkout is blocked (except the consult) until then. The payment block coordinates with PRD-06 (the block is enforced where money is taken) and the booking deposit/hold is suppressed during cooling-off (F14 invariant, DEPOSITS placeholder).
For ADULTS there is NO mandatory cooling-off (a 2025 regulatory correction); an optional adult cool-off / second-consult is a configurable clinic-policy setting (default per legal read), not a compliance gate. The second-consultation offer is recorded on the client timeline for all patients where applicable.

## Requirements

- To enforce a 7-day cooling-off and payment block for under-18s and record a second consultation.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
- [ ] A second-consultation offer is recorded.
- [ ] Optional adult cooling-off is configurable (default per legal read).
- [ ] Payment block coordinates with PRD-06.

## UI designs / screenshots

- Patient header shows an 'under-18 cooling-off' chip with the elapse date; checkout is blocked (except consult) until then (mirrors Forms & consent 'Under-18 consent (+ guardian) · 7-day cool-off' status).
- A recorded second-consultation offer appears on the client timeline; the intake/consent done screen notes 'If under 18, a mandatory 7-day cooling-off applies before any treatment' (client-app.png / forms-consent.png).
- Adult cool-off is a configurable clinic-policy setting (default off per legal read).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **CoolingOffTimer** — id, tenant_id, client_id, appointment_id, consent_at, eligible_at, payment_blocked(bool), second_consult_offered_at, basis(under18_mandatory|adult_policy)
  - _Under-18: mandatory 7d (eligible_at=consent_at+7d). Adult: optional/config. Suppresses deposits during the window (F14)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **CoolingOffTimer: under-18 7-day enforcement**
  On consent for an under-18 (under_18 flag from booking + ConsentSignature.signed_at), create a CoolingOffTimer with eligible_at = consent_at + 7 days and payment_blocked = true. Server-side, the procedure cannot be charted/finalised and checkout (except the consult (the assessment appointment where suitability is established and an S4 prescription can be written) line) cannot complete until eligible_at passes. Enforce as a domain invariant (ADR-0008), not UI. Audited.
- [ ] **Payment-block coordination (PRD-06) + deposit suppression (F14)**
  Expose the cooling-off/payment-blocked state so PRD-06 checkout blocks all non-consult charges until eligible_at, and so the (Phase-2) DEPOSITS hold is suppressed during the window (F14 invariant). Record the second_consultation offer (second_consult_offered_at) on the client timeline. Clears automatically when eligible_at passes.
- [ ] **Adult cooling-off config + header chip UI**
  Configurable adult cool-off / second-consult clinic-policy setting (default off per legal read) producing an optional adult CoolingOffTimer (basis=adult_policy) — NOT a compliance gate. UI: 'under-18 cooling-off (the mandatory wait before a cosmetic procedure can proceed)' chip with elapse date on the patient/charting header; checkout-blocked indicator (except consult (the assessment appointment where suitability is established and an S4 prescription can be written)); second-consult offer on the timeline; the client done-screen note.
