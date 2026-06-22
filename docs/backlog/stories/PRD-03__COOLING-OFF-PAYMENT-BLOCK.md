# Cooling-off: payment-block coordination & deposit suppression (F14)

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/COOLING-OFF-PAYMENT-BLOCK`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/COOLING-OFF`

## Background

As a system, I want the under-18 payment block coordinated with checkout and deposits suppressed during cooling-off, so that no money beyond the consult is taken from a minor during the wait.
Plainly: holding back money during an under-18 cooling-off — checkout blocks all non-consult charges, and any booking deposit/hold is suppressed. Where it fits: a follow-up to the cooling-off basic under-18 7-day enforcement (PRD-03/COOLING-OFF) that adds the payment coordination on top of the timer. It coordinates with Payments (PRD-06), where the block is actually enforced at checkout, and with the deferred deposit placeholder (PRD-02/DEPOSITS) via the F14 invariant. It sits in Intake & Consent (PRD-03).

## How it works

The basic story creates the cooling-off timer and the payment_blocked flag; this follow-up coordinates the money side. The cooling-off/payment-blocked state is exposed so checkout holds money back during the window.
PRD-06 checkout blocks all non-consult charges until eligible_at passes, and the (Phase-2) DEPOSITS hold is suppressed during the window (the F14 invariant — no deposit/hold may be placed during an under-18 cooling-off).
The consult (the assessment appointment where suitability is established and an S4 prescription can be written) line is the one exception that may be charged, so the initial consult is never blocked.

## Requirements

- The under-18 payment block coordinated with checkout and deposits suppressed during cooling-off.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] PRD-06 checkout blocks all non-consult charges until eligible_at.
- [ ] The (Phase-2) DEPOSITS hold is suppressed during the window (F14 invariant).
- [ ] The consult line is the one exception that may be charged.
- [ ] The cooling-off/payment-blocked state is exposed for checkout to read.

## UI designs / screenshots

- Patient header shows a checkout-blocked indicator (except the consult) during the under-18 cooling-off.
- PRD-06 checkout blocks non-consult charges until eligible_at; the consult line is the exception.
- Any (Phase-2) deposit/hold is suppressed during the window (F14).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **CoolingOffTimer (extends COOLING-OFF)** — payment_blocked(bool) read by PRD-06 checkout; suppresses BookingHold (F14)
  - _Checkout blocks non-consult charges until eligible_at; deposit/hold suppressed during the window (F14)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Payment-block coordination (PRD-06) + deposit suppression (F14)**
  Behaviour: expose the cooling-off/payment-blocked state so money is held back during the window. Requirements: PRD-06 checkout blocks all non-consult charges until eligible_at; the (Phase-2) DEPOSITS hold is suppressed during the window (F14 invariant); the consult (the assessment appointment where suitability is established and an S4 prescription can be written) line is the one exception that may be charged.
