# BDD screening: wellbeing questions in the intake wizard

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD-WELLBEING-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/BDD`

## Background

As a client, I want to answer a few wellbeing questions as part of intake, so that the clinic can screen for psychological suitability routinely.
Plainly: the 'A few wellbeing questions' step rendered inside the client-app/kiosk intake wizard, whose answers feed the BDD scoring. Where it fits: a follow-up to the BDD screening basic instrument & scoring (PRD-03/BDD) that adds the client-facing question UI on top of the scored instrument. It renders identically in the client app and the reception check-in tablet. It sits in Intake & Consent (PRD-03).

## How it works

The basic story owns the instrument and scoring; this follow-up adds the client-facing questions that produce the answers. The 'A few wellbeing questions' step renders inside the intake wizard (e.g. how often the concern is thought about, daily-life impact, realistic expectations) with radio options.
The same step renders identically in the client app and at the reception check-in tablet, and the answers feed the scoring rule the basic owns.
It is framed as routine for all cosmetic treatments so clients understand it is a standard wellbeing check, not a singling-out.

## Requirements

- To answer a few wellbeing questions as part of intake.

## Acceptance Criteria

- [ ] The 'A few wellbeing questions' step renders inside the client-app/kiosk intake wizard (how often the concern is thought about, daily-life impact, realistic expectations) with radio options.
- [ ] The same step renders in the client app and at the reception check-in tablet.
- [ ] Answers feed the scoring rule.
- [ ] It is framed as routine for all cosmetic treatments.

## UI designs / screenshots

- Client app: the BDD/wellbeing screen within the intake wizard (client-app.png) — 'A few wellbeing questions', radio options (Rarely/Sometimes/A lot · No/A little/A lot · Realistic/Unsure).
- The same step renders in the client app and at the reception check-in tablet.
- Framed as routine for all cosmetic treatments; answers feed the scoring rule.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ScreeningResult (extends BDD)** — answers(json)
  - _Wellbeing-question answers feed the scoring rule; same step in client app and kiosk._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Wellbeing questions in the intake wizard (client/kiosk)**
  Behaviour: render the 'A few wellbeing questions' step inside the client-app/kiosk intake wizard (e.g. how often the concern is thought about, daily-life impact, realistic expectations) with radio options. Requirements: the same step renders in the client app and at the reception check-in tablet; answers feed the scoring rule; framed as routine for all cosmetic treatments.
