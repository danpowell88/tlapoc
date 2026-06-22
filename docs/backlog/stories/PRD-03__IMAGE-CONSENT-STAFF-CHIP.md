# Image-use consent: staff header chip

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT-STAFF-CHIP`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a staff member, I want the image-use consent state shown as a chip on the client/charting header, so that I know whether photos may be used before I open a gallery.
Plainly: showing the granted/withdrawn image-use consent state to staff as a chip on the Client 360 and charting header. Where it fits: a follow-up to the image-use consent basic entity & grant/withdraw (PRD-03/IMAGE-CONSENT) that adds the staff-facing chip on top of the consent record. It ties to the before/after gallery (PRD-02/PHOTOS-GALLERY), which hides when consent is withdrawn. It sits in Intake & Consent (PRD-03).

## How it works

The basic story records the consent state; this follow-up surfaces it to staff. An 'Image use ✓ / withdrawn' chip renders on the Client 360 and charting header.
Photo galleries note 'image-use consent on file' and hide when consent is withdrawn (ties to PRD-02/PHOTOS-GALLERY), so staff never see images the client hasn't consented to.
The chip reflects the current ImageConsent state, giving staff an at-a-glance read before opening any photo feature.

## Requirements

- The image-use consent state shown as a chip on the client/charting header.

## Acceptance Criteria

- [ ] An 'Image use ✓ / withdrawn' chip renders on the Client 360 + charting header.
- [ ] Photo galleries note 'image-use consent on file' and hide when withdrawn.
- [ ] The chip reflects the current ImageConsent state.

## UI designs / screenshots

- Staff: the image-use chip on the Client 360 / charting header ('Image use ✓') (charting.png).
- Photo galleries note 'image-use consent on file' and hide when withdrawn.
- The chip reflects the current ImageConsent state.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads IMAGE-CONSENT)** — no new entities; renders ImageConsent.status as a header chip
  - _Presentation of the consent state; ties to PRD-02/PHOTOS-GALLERY (hidden when withdrawn)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Staff image-use header chip**
  Behaviour: show the granted/withdrawn state to staff. Requirements: render an 'Image use ✓ / withdrawn' chip on the Client 360 + charting header; photo galleries note 'image-use consent on file' and hide when withdrawn (ties to PRD-02/PHOTOS-GALLERY).
