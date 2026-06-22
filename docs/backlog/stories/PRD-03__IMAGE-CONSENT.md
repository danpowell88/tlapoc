# Separate, withdrawable image-use consent

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/CONSENT`

## Background

As a client, I want to give separate consent for photo use and withdraw it whenever I want, so that I control how my images are used.
Image-use consent is the separate, withdrawable photo permission inside Intake & Consent (PRD-03) — distinct from treatment consent because a client can agree to treatment but decline photos. It sits just after consent (PRD-03/CONSENT) in the flow. Crucially it is NOT part of the treatment gate: declining photos never blocks treatment. Instead it governs downstream media — the photos/charting in PRD-05 and media features in the apps (PRD-09) must check it before serving or capturing — so withdrawing it immediately stops further use.  Photo use requires its own scoped consent, withdrawable at any time, which immediately stops downstream use (C14).

## How it works

Photo use needs its OWN scoped consent, separate from treatment consent (a client can consent to treatment but decline photos), and withdrawable at any time. Withdrawing it sets withdrawn_at and IMMEDIATELY blocks downstream media use — PRD-05 (photos/charting) and PRD-09 media features check ImageConsent before serving or capturing, and the withdrawal is audited (C14).
Scope records what the photos may be used for (clinical record vs broader use); v1's default is the clinical record only ('stored securely, never on personal devices, never shared without permission' — ADR-0009). The granted/withdrawn state shows as a chip on the patient header (Client 360 / charting) and the client can self-manage it in the client app privacy screen.
Because it is separate, the treatment gate (GATING) does NOT require image-use consent — declining photos never blocks treatment; it only governs whether photo features are available.

## Requirements

- To give separate consent for photo use and withdraw it whenever I want.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Image-use consent is separate from treatment consent and scoped.
- [ ] Withdrawing it immediately stops further use and is audited.
- [ ] Downstream media features (PRD-05/09) check this consent.
- [ ] Granted/withdrawn state is visible on the patient header chip.

## UI designs / screenshots

- Client app: a separate image-use consent toggle with scope + a withdraw control (client-app.png) — intake step 'Photos (optional)… separate from treatment consent. Withdraw any time'; Privacy & consents screen lists consents with toggles ('Consent withdrawn' toast on withdraw).
- Staff: the image-use chip on the Client 360 / charting header ('Image use ✓') (charting.png); photo galleries note 'image-use consent on file'.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ImageConsent** — id, tenant_id, client_id, scope, granted_at, withdrawn_at, status(granted|withdrawn)
  - _withdrawn_at IMMEDIATELY blocks media use (PRD-05/09 checks); audited (C14); separate from treatment consent (never blocks treatment)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **ImageConsent entity (separate, scoped) + grant/withdraw**
  Behaviour: model ImageConsent (scope, granted_at, withdrawn_at, status) separate from ConsentSignature, with grant/withdraw endpoints. Requirements: withdraw sets withdrawn_at + status and emits a domain event (a fact emitted when something happens in the system); audited (C14); it is NOT an input to the treatment gate — declining or withdrawing never blocks treatment, only media features.
- [ ] **Downstream media-use enforcement on withdraw**
  Behaviour: media operations check current image-use consent before proceeding so a withdrawal immediately stops further use. Requirements: PRD-05/09 media ops (serve signed URL, capture, share) check current ImageConsent.status server-side first; on the withdraw event no new signed URLs are issued (ADR-0009: media never on personal devices, always via consent-gated signed URLs (a temporary, expiring link)); audited.
- [ ] **Client self-manage toggle (intake + Privacy & consents)**
  Behaviour: the client controls image-use consent — a scoped toggle in the intake 'Photos (optional)' step and in the client-app Privacy & consents screen, where it can be withdrawn any time. Requirements: withdrawing prompts a confirmation and shows a 'Consent withdrawn' toast; the toggle is clearly framed as separate from treatment consent; state persists immediately.
- [ ] **Staff image-use header chip**
  Behaviour: show the granted/withdrawn state to staff. Requirements: render an 'Image use ✓ / withdrawn' chip on the Client 360 + charting header; photo galleries note 'image-use consent on file' and hide when withdrawn (ties to PRD-02/PHOTOS-GALLERY).
