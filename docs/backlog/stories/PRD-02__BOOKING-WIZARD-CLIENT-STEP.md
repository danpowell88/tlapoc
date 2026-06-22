# Staff booking wizard: new-client creation, under-18 & intake/consent send

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/BOOKING-WIZARD-CLIENT-STEP`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/BOOKING-WIZARD`

## Background

As a front desk, I want to create a new client inline at the booking step and send their intake & consent, so that a first-time client is set up and gated correctly without leaving the wizard.
Plainly: enriching the wizard's client step so the desk can create a new client inline (capturing date of birth), flag under-18, choose the right intake variant, and send the intake + consent links. Where it fits: a follow-up to the staff booking wizard basic scope-aware flow (PRD-02/BOOKING-WIZARD), which only attaches existing clients. New-vs-returning selects the intake variant in Intake & Consent (PRD-03), the under-18 flag feeds cooling-off, and the send kicks off PRD-03 GATING. It sits in Reception (PRD-02).

## How it works

The basic wizard attaches an existing client; this follow-up enriches the client step. The desk can attach a returning client or create a new one inline, capturing date of birth and a reason/notes field.
The Returning/New toggle changes the intake hint (returning gets a quick medical re-screen; new gets full intake + medical history + BDD screen + consent), and under_18 is derived and stamped from the DOB so cooling-off can be enforced downstream.
A 'Send intake + consent links now (treatment can't start until complete)' checkbox wires to the PRD-03 intake + consent send, tying the booking to the GATING flow that must be complete before treatment.

## Requirements

- To create a new client inline at the booking step and send their intake & consent.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An existing client can be attached or a new one created inline capturing DOB.
- [ ] Under-18 is derived and stamped from the DOB.
- [ ] The Returning/New toggle changes the intake hint (returning = quick re-screen; new = full intake + history + BDD + consent).
- [ ] A 'Send intake + consent links now (treatment can't start until complete)' checkbox wires to the PRD-03 intake + consent send.

## UI designs / screenshots

- Prototype: 'New booking' wizard (booking-wizard.png) step 4 — attach Returning/New client + reason + 'Send intake + consent links now (treatment can't start until complete)'.
- New creates the client inline capturing DOB; the Returning/New toggle changes the intake hint.
- Under-18 derived from DOB; the checkbox triggers the PRD-03 send.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Client (ref, extends BOOKING-WIZARD)** — new|returning, dob/under_18, reason
  - _Attach existing or create inline; under-18 flagged; drives intake type + cooling-off; the checkbox triggers the PRD-03 intake + consent send._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Client step: attach existing / create inline + under-18 + intake/consent send**
  Behaviour: search/attach a returning client or create a new one inline capturing DOB, plus a reason/notes field and a 'Send intake + consent links now (treatment can't start until complete)' checkbox. Requirements: the Returning/New toggle changes the intake hint (returning = quick re-screen; new = full intake + history + BDD + consent); derive and stamp under_18 from DOB; the checkbox wires to the PRD-03 intake + consent send.
