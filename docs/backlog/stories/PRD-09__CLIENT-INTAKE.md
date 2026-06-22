# Client app: intake + consent, e-signed on device

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-INTAKE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-JOURNEY`, `PRD-03/CONSENT`

## Background

As a client, I want to complete my intake and e-sign consent in the app before my visit, so that I'm ready for my visit without paperwork at the desk.
Plainly: the pre-visit forms screen in the client app — complete the medical-history intake and e-sign consent (including a separate image-use consent) on the phone before the visit. Where it fits: a follow-up to the client-app basic (PRD-09/CLIENT-JOURNEY) that adds the pre-visit intake/consent journey; it is a surface over the intake & consent module (PRD-03), with the treatment gate enforced server-side. It pairs with in-app booking (PRD-09/CLIENT-BOOK), which triggers the intake/consent send, and lights up the Home pre-visit nudge.

## How it works

The pre-visit forms screen completes the PRD-03 medical-history / BDD (body dysmorphic disorder) intake and e-signs per-treatment consent plus a SEPARATE, withdrawable image-use consent, ending on 'All set — thank you'. The on-device signature is captured and posted to the API (records live server-side, no parallel app store); the treatment gate stays server-enforced — the app only reflects outstanding items.
The Home tab gains the amber 'Finish your pre-visit forms' nudge: it is driven by the server-side gate state (PRD-03) and deep-links into the forms, and quick actions route to the relevant screens. Image-use consent is its own toggle the client can later withdraw, gating the before/after gallery (PHOTO-COMPARE).

## Requirements

- To complete my intake and e-sign consent in the app before my visit.

## Acceptance Criteria

- [ ] The pre-visit forms screen completes the PRD-03 medical-history / BDD intake and e-signs per-treatment consent, ending on 'All set'.
- [ ] A separate, withdrawable image-use consent is its own toggle the client can later withdraw.
- [ ] The on-device signature is captured and posted to the API — records live server-side, no parallel app store.
- [ ] The Home pre-visit nudge ('Finish your pre-visit forms') reflects the server-side gate state and deep-links into the forms.

## UI designs / screenshots

- Prototype: client-app — pre-visit forms (medical history / BDD intake + per-treatment consent + separate image-use consent), ending 'All set — thank you'.
- Home gains the amber 'Finish your pre-visit forms' nudge driven by the server-side gate, deep-linking into the forms.
- Image-use consent is a separate, withdrawable toggle.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) IntakeResponse/ConsentSignature** — PRD-03 — medical history, per-treatment + image-use consent, e-signed
  - _Extends CLIENT-JOURNEY; server holds records, signatures posted from device — no app-local store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Intake + per-treatment consent + image-use consent (PRD-03), e-signed on device**
  Behaviour: the pre-visit forms screen completes the PRD-03 medical-history / BDD (body dysmorphic disorder) intake and e-signs per-treatment consent plus a SEPARATE, withdrawable image-use consent, ending on 'All set'. Requirements: the on-device signature is captured and posted to the API (records live server-side, no parallel app store); the treatment gate stays server-enforced — the app only reflects outstanding items; image-use consent is its own toggle the client can later withdraw.
- [ ] **Home pre-visit nudge driven by the server-side gate**
  Behaviour: the Home tab shows the amber 'Finish your pre-visit forms' nudge when intake/consent is outstanding and deep-links into the forms. Requirements: the nudge reflects the server-side gate state (PRD-03) — it is never the source of truth; it clears once outstanding items are completed; quick actions route to the relevant screens.
