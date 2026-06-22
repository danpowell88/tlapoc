# Image-use consent: downstream media-use enforcement on withdraw

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT-ENFORCEMENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a client, I want withdrawing image-use consent to immediately stop any further use of my photos, so that I stay in control of my images at all times.
Plainly: making every media operation check current image-use consent first, so withdrawing it immediately stops further use. Where it fits: a follow-up to the image-use consent basic entity & grant/withdraw (PRD-03/IMAGE-CONSENT) that adds the downstream enforcement on top of the consent record. Photos/charting (PRD-05) and app media features (PRD-09) check it before serving or capturing — satisfying compliance criterion C14. It sits in Intake & Consent (PRD-03).

## How it works

The basic story records grant/withdraw; this follow-up makes the withdrawal actually bite. Every media operation checks current image-use consent before proceeding, so a withdrawal immediately stops further use.
Photos/charting media operations (PRD-05) and app media features (PRD-09) — serve signed URL, capture, share — check ImageConsent.status server-side first. On the withdraw event no new signed URLs (temporary, expiring links) are issued (ADR-0009: media never on personal devices, always via consent-gated signed URLs).
All media access is audited (C14), so consent enforcement is demonstrable. This is the rule that makes the separate, withdrawable consent meaningful in practice.

## Requirements

- Withdrawing image-use consent to immediately stop any further use of my photos.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Media operations check current image-use consent before proceeding.
- [ ] PRD-05/09 media ops (serve signed URL, capture, share) check ImageConsent.status server-side first.
- [ ] On the withdraw event no new signed URLs are issued (ADR-0009).
- [ ] Media access is audited.

## UI designs / screenshots

- No new primary screen — enforcement runs server-side ahead of any media op (ties to PRD-02/PHOTOS-GALLERY).
- On withdraw, no new signed URLs are issued; galleries hide/empty.
- Media access audited (C14).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ImageConsent (extends IMAGE-CONSENT)** — status checked by PRD-05/09 media ops before serving/capturing/sharing
  - _withdrawn_at IMMEDIATELY blocks media use; no new signed URLs on withdraw (ADR-0009); audited (C14)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Downstream media-use enforcement on withdraw**
  Behaviour: media operations check current image-use consent before proceeding so a withdrawal immediately stops further use. Requirements: PRD-05/09 media ops (serve signed URL, capture, share) check current ImageConsent.status server-side first; on the withdraw event no new signed URLs are issued (ADR-0009: media never on personal devices, always via consent-gated signed URLs (a temporary, expiring link)); audited.
