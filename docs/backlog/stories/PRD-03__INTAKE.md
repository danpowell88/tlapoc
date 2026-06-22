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

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeForm** — id, tenant_id, name, version, fields(json schema)
  - _Configurable; versioned._
- **IntakeResponse** — id, tenant_id, client_id, appointment_id, form_version, answers(json), submitted_at
  - _Auto-linked to the chart; contributes to the gate._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - IntakeForm — id, tenant_id, name, version, fields(json schema) (Configurable; versioned.)
  - IntakeResponse — id, tenant_id, client_id, appointment_id, form_version, answers(json), submitted_at (Auto-linked to the chart; contributes to the gate.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Configurable pre-visit forms capture history, meds, allergies/contraindications.
  - Rule: Intake is sent on booking and completable in the client app/web.
  - Rule: Responses auto-link to the client's chart.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/ONLINE-BOOK.
- [ ] **Client app UI (Flutter)**
  Build on the Flutter client app: the forms-consent per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Client app / public: a pre-visit intake wizard (medical history -> meds -> allergies/contraindications) — see client-app.png; also completable at the reception check-in tablet (checkin.png).
  - Staff: Forms & consent (forms-consent.png) shows intake status per client and lets the desk send/chase it.
  - Forms are configurable (admin-defined fields).
