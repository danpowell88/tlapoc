# Pre-visit intake forms

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** client-app, backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a client, I want to complete my medical history, medications, allergies and contraindications before my visit on my phone, so that my practitioner has what they need and my treatment is safe.
Clients complete medical history, meds, allergies and contraindications on their phone before the visit; responses auto-link to the chart.

## Requirements

- To complete my medical history, medications, allergies and contraindications before my visit on my phone.

## Acceptance Criteria

- [ ] Configurable pre-visit forms capture history, meds, allergies/contraindications.
- [ ] Intake is sent on booking and completable in the client app/web.
- [ ] Responses auto-link to the client's chart.
- [ ] Incomplete required intake contributes to the treatment block.

## UI designs / screenshots

prototype.html — Forms & consent; client-app.html intake/consent; checkin.html.

## Technical notes (high level)

- Stack: Flutter client app; .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
