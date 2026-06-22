# Cooling-off: optional adult cooling-off config (not a gate)

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF-ADULT-CONFIG`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/COOLING-OFF`

## Background

As a owner / manager, I want an optional, advisory adult cool-off / second-consult setting, so that the clinic can adopt one as policy without it blocking treatment.
Plainly: an optional clinic-policy setting for an adult cool-off / second consultation — advisory only, never a compliance gate, because there is NO mandated adult cooling-off. Where it fits: a follow-up to the cooling-off basic under-18 7-day enforcement (PRD-03/COOLING-OFF) that adds the optional adult policy alongside the mandatory minor rule. It produces an advisory adult timer that never blocks treatment or payment. It sits in Intake & Consent (PRD-03).

## How it works

The basic story enforces the mandatory under-18 cooling-off; this follow-up adds the optional adult policy distinct from it. An adult cool-off / second-consult is a configurable clinic-policy setting, default off per legal read.
Crucially there is NO mandated adult cooling-off (a 2025 regulatory correction), so this is a policy convenience, not a compliance gate.
When enabled it produces an optional adult CoolingOffTimer (basis=adult_policy) that is advisory only and NEVER blocks treatment or payment — unlike the under-18 timer, which is a hard invariant.

## Requirements

- An optional, advisory adult cool-off / second-consult setting.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An optional adult cool-off / second-consult is a configurable clinic-policy setting, default off per legal read.
- [ ] There is NO mandated adult cooling-off.
- [ ] When on, it produces an optional adult CoolingOffTimer (basis=adult_policy) that is advisory only.
- [ ] The adult cool-off never blocks treatment/payment.

## UI designs / screenshots

- Adult cool-off is a configurable clinic-policy setting (default off per legal read).
- When on, it produces an advisory adult CoolingOffTimer (basis=adult_policy) that never blocks treatment/payment.
- Clearly distinguished from the mandatory under-18 rule.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **CoolingOffTimer (extends COOLING-OFF)** — basis(adult_policy); advisory only
  - _Optional/config; default off; NEVER blocks treatment/payment (no mandated adult cooling-off)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Adult cooling-off config (optional, not a gate)**
  Behaviour: an optional adult cool-off / second-consult is a clinic-policy setting, not a compliance gate. Requirements: configurable, default off per legal read (there is NO mandated adult cooling-off); when on it produces an optional adult CoolingOffTimer (basis=adult_policy) that is advisory only and never blocks treatment/payment.
