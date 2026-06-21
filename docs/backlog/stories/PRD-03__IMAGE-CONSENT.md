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

## Suggested data model

- **ImageConsent** — id, client_id, scope, granted_at, withdrawn_at, status
  - _Withdrawn_at immediately blocks media use; audited (C14)._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
