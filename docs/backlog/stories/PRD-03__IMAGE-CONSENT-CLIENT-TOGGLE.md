# Image-use consent: client self-manage toggle

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT-CLIENT-TOGGLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a client, I want to grant or withdraw image-use consent myself, separately from treatment consent, so that I control how my photos are used at any time.
Plainly: the client-facing controls for image-use consent — a scoped toggle in the intake 'Photos (optional)' step and in the client-app Privacy & consents screen, withdrawable any time. Where it fits: a follow-up to the image-use consent basic entity & grant/withdraw (PRD-03/IMAGE-CONSENT) that adds the client self-manage UI on top of the consent record. It is clearly framed as separate from treatment consent. It sits in Intake & Consent (PRD-03), in the client app.

## How it works

The basic story provides grant/withdraw endpoints; this follow-up gives the client the controls. A scoped image-use toggle appears in the intake 'Photos (optional)' step and in the client-app Privacy & consents screen, where it can be withdrawn at any time.
Withdrawing prompts a confirmation and shows a 'Consent withdrawn' toast, and the toggle is clearly framed as separate from treatment consent (declining photos never affects treatment).
State persists immediately so a change takes effect at once, working hand-in-hand with the downstream enforcement (PRD-03/IMAGE-CONSENT-ENFORCEMENT).

## Requirements

- To grant or withdraw image-use consent myself, separately from treatment consent.

## Acceptance Criteria

- [ ] A scoped image-use toggle in the intake 'Photos (optional)' step and in the client-app Privacy & consents screen.
- [ ] It can be withdrawn any time; withdrawing prompts a confirmation and shows a 'Consent withdrawn' toast.
- [ ] The toggle is clearly framed as separate from treatment consent.
- [ ] State persists immediately.

## UI designs / screenshots

- Client app: a separate image-use consent toggle with scope + a withdraw control (client-app.png) — intake step 'Photos (optional)… separate from treatment consent. Withdraw any time'; Privacy & consents screen lists consents with toggles ('Consent withdrawn' toast on withdraw).
- Withdrawing prompts a confirmation; the toggle is framed as separate from treatment consent.
- State persists immediately.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ImageConsent (extends IMAGE-CONSENT)** — client grant/withdraw via intake + Privacy & consents
  - _Client self-manages; framed as separate from treatment consent; state persists immediately._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Client self-manage toggle (intake + Privacy & consents)**
  Behaviour: the client controls image-use consent — a scoped toggle in the intake 'Photos (optional)' step and in the client-app Privacy & consents screen, where it can be withdrawn any time. Requirements: withdrawing prompts a confirmation and shows a 'Consent withdrawn' toast; the toggle is clearly framed as separate from treatment consent; state persists immediately.
