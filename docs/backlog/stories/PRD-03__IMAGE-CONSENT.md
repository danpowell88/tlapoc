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
  Model ImageConsent (scope, granted_at, withdrawn_at, status) separate from ConsentSignature. Grant/withdraw endpoints; withdraw sets withdrawn_at + status and emits a domain event. Audited (C14). It is NOT an input to the treatment gate — declining/withdrawing never blocks treatment, only media features.
- [ ] **Downstream media-use enforcement on withdraw**
  PRD-05/09 media operations (serve signed URL, capture, share) must check current ImageConsent.status server-side before proceeding, so withdrawal IMMEDIATELY stops further use (ADR-0009: media never on personal devices, always via consent-gated signed URLs). On the withdraw event, ensure no new signed URLs are issued. Audited.
- [ ] **Client self-manage toggle + staff header chip UI**
  Client app: image-use toggle with scope in the intake 'Photos (optional)' step and in Privacy & consents (withdraw with confirmation/toast). Staff: 'Image use ✓ / withdrawn' chip on the Client 360 + charting header; photo galleries show 'image-use consent on file' and hide when withdrawn.
