# Kiosk: outstanding intake/consent at the desk

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-FORMS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CHECKIN-KIOSK`, `PRD-03/GATING`

## Background

As a client arriving for a visit, I want to finish any unsigned intake or consent at the kiosk, so that I'm ready for the room without paperwork there.
Plainly: the kiosk step that prompts and completes anything still unsigned — outstanding intake and consent — finished at the desk rather than in the room. Where it fits: a follow-up to the kiosk basic (PRD-09/CHECKIN-KIOSK) that adds form completion; it reuses the SAME intake/consent modules (PRD-03) as the client app, with the compliance gate staying server-enforced. The kiosk only completes what's outstanding.

## How it works

'Outstanding before your visit' prompts and completes anything unsigned — outstanding intake (medical history) and consent — finished here rather than in the room. It reuses the SAME PRD-03 intake/consent modules as the client app (no parallel store); the on-device signature posts to the API.
The compliance gate stays server-enforced — the kiosk only completes what's outstanding, it never bypasses the gate. This step slots before the client is marked fully ready and feeds the arrivals board (CHECKIN-ARRIVALS).

## Requirements

- To finish any unsigned intake or consent at the kiosk.

## Acceptance Criteria

- [ ] 'Outstanding before your visit' prompts and completes anything unsigned — outstanding intake (medical history) and consent.
- [ ] It reuses the SAME PRD-03 intake/consent modules as the client app (no parallel store).
- [ ] The on-device signature posts to the API.
- [ ] The compliance gate stays server-enforced — the kiosk only completes what's outstanding.

## UI designs / screenshots

- Prototype: checkin — step Sign consent / 'Outstanding before your visit' (completes unsigned intake + consent).
- Reuses the client-app PRD-03 modules; on-device signature posts to the API; gate stays server-enforced.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) IntakeResponse/ConsentSignature** — PRD-03 — outstanding intake/consent completed at the desk
  - _Extends CHECKIN-KIOSK; same modules as the client app, no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Outstanding intake/consent completion at the desk (PRD-03)**
  Behaviour: 'Outstanding before your visit' prompts and completes anything unsigned — outstanding intake (medical history) and consent — finished here rather than in the room. Requirements: reuses the SAME PRD-03 intake/consent modules as the client app (no parallel store); the on-device signature posts to the API; the compliance gate stays server-enforced — the kiosk only completes what's outstanding.
