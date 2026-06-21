# Pre-visit intake forms

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** client-app, backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a client, I want to complete my medical history, medications, allergies and contraindications before my visit on my phone, so that my practitioner has what they need and my treatment is safe.
Clients complete medical history, meds, allergies and contraindications on their phone before the visit; responses auto-link to the chart.

## How it works

Pre-visit intake collects the medical history, medications, allergies and contraindications a practitioner must see before treating. It is sent on booking and completed by the client on their phone, then auto-linked to the chart.
Incomplete required intake contributes to the treatment block (GATING) — the clinic can't safely or lawfully proceed without it.

## Requirements

- To complete my medical history, medications, allergies and contraindications before my visit on my phone.

## Acceptance Criteria

- [ ] Configurable pre-visit forms capture history, meds, allergies/contraindications.
- [ ] Intake is sent on booking and completable in the client app/web.
- [ ] Responses auto-link to the client's chart.
- [ ] Incomplete required intake contributes to the treatment block.

## UI designs / screenshots

_Prototype screen: prototype.html — Forms & consent; client-app.html intake/consent; checkin.html._

- Client app / public: a pre-visit intake wizard (medical history -> meds -> allergies/contraindications) — see client-app.png; also completable at the reception check-in tablet (checkin.png).
- Staff: Forms & consent (forms-consent.png) shows intake status per client and lets the desk send/chase it.
- Forms are configurable (admin-defined fields).

## Suggested data model

- **IntakeForm** — id, tenant_id, name, version, fields(json schema)
  - _Configurable; versioned._
- **IntakeResponse** — id, tenant_id, client_id, appointment_id, form_version, answers(json), submitted_at
  - _Auto-linked to the chart; contributes to the gate._

## Technical notes (high level)

- Stack: Flutter client app; .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
