# Skin analysis: consent-respecting push to client app

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/SKIN-ANALYSIS-PUSH`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/SKIN-ANALYSIS`

## Background

As a dermal therapist / injector, I want to push an assessment summary to the client app, respecting image-use consent and AU storage, so that clients can see their skin progress without breaching privacy rules.
Plainly: this lets the clinic share a client's skin-assessment summary to their app so they can see their own progress — but only when image-use consent allows and with the images kept in Australia. Where it fits: a follow-up to PRD-05/SKIN-ANALYSIS that adds the client-facing share on top of the recorded assessment. Skin images are Personal Health Information (PHI), so the same image-use consent + Australian storage rules as clinical photos apply (C14).

## How it works

This follow-up adds the client-facing share on top of the recorded assessment. The assessment summary can be pushed to the client app (pushSkinToClient), respecting consent — skin images are PHI, so image-use consent + Australian storage (C14) apply exactly as for clinical photos.
The push is gated on current image-use consent: missing or withdrawn consent blocks the share with a reason, and a withdrawal stops downstream use. Any image-backed summary is stored in Australia and served via short-lived signed URLs.
The push reads the SkinAssessment the basic records.

## Requirements

- To push an assessment summary to the client app, respecting image-use consent and AU storage.

## Acceptance Criteria

- [ ] An assessment summary can be pushed to the client app.
- [ ] The push is blocked unless current image-use consent is present; a withdrawn consent stops downstream use.
- [ ] Any image-backed summary is stored in Australia and served via short-lived signed URLs (C14).
- [ ] The push reads the recorded assessment (PRD-05/SKIN-ANALYSIS).

## UI designs / screenshots

- 'Send to client' action on the skin-analysis screen (pushSkinToClient).
- A banner notes 'Skin images are PHI - image-use consent + AU storage apply (C14)'.
- The action is blocked with a reason when image-use consent is missing/withdrawn.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **SkinAssessment (extended)** — + pushed_to_client_at, image_consent_id (if image-backed)
  - _Extends the basic's SkinAssessment: the consent-gated push to the client app; image-backed assessments respect C14._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Consent-respecting push-to-client summary**
  Behaviour: push an assessment summary to the client app (pushSkinToClient). Requirements: gate on current image-use consent (block when missing/withdrawn; a withdrawal stops downstream use); any image-backed summary is stored in Australia and served via short-lived signed URLs (C14). Reads the recorded SkinAssessment (PRD-05/SKIN-ANALYSIS).
