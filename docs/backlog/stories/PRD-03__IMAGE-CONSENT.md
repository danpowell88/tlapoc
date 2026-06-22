# Separate, withdrawable image-use consent

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/CONSENT`

## Background

As a client, I want to give separate consent for photo use and withdraw it whenever I want, so that I control how my images are used.
Photo use requires its own scoped consent, withdrawable at any time, which immediately stops downstream use (C14).

## How it works

Photo use needs its own scoped consent, separate from treatment consent and withdrawable at any time. Withdrawing it immediately stops downstream use (PRD-05/09 media checks) and is audited.
Granted/withdrawn state shows as a chip on the patient header.

## Requirements

- To give separate consent for photo use and withdraw it whenever I want.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Image-use consent is separate from treatment consent and scoped.
- [ ] Withdrawing it immediately stops further use and is audited.
- [ ] Downstream media features (PRD-05/09) check this consent.
- [ ] Granted/withdrawn state is visible on the patient header chip.

## UI designs / screenshots

- Client app: a separate image-use consent toggle with scope + a withdraw control (client-app.png); staff see the image-use chip on the Client 360 / charting header (charting.png).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ImageConsent** — id, client_id, scope, granted_at, withdrawn_at, status
  - _Withdrawn_at immediately blocks media use; audited (C14)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ImageConsent — id, client_id, scope, granted_at, withdrawn_at, status (Withdrawn_at immediately blocks media use; audited (C14).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Image-use consent is separate from treatment consent and scoped.
  - Rule: Withdrawing it immediately stops further use and is audited.
  - Rule: Downstream media features (PRD-05/09) check this consent.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-03/CONSENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C14 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Image-use consent is separate from treatment consent and scoped.
  - Downstream media features (PRD-05/09) check this consent.
