# Pre-visit intake forms

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** client-app, backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a client, I want to complete my medical history, medications, allergies and contraindications before my visit on my phone, so that my practitioner has what they need and my treatment is safe.
Clients complete medical history, meds, allergies and contraindications on their phone before the visit; responses auto-link to the chart.

## How it works

Pre-visit intake collects the medical history, current medications, allergies and contraindications a practitioner must see before treating — pregnancy/breastfeeding, blood thinners, cold-sore history, latex/lidocaine allergies, etc. It is sent on booking (BOOKING-WIZARD / ONLINE-BOOK) and completed by the client on their phone in the client app, or at the reception check-in tablet on arrival. A returning client gets a quick re-screen; a new client gets the full form.
Forms are admin-configurable (IntakeForm with a versioned JSON field schema). A submitted IntakeResponse is stamped with the form_version it was answered against and auto-linked to the client's chart and appointment. A 'quick safety check' summarises whether any contraindication was flagged for the nurse.
Incomplete REQUIRED intake contributes to the treatment block (GATING) — the clinic can't safely or lawfully proceed without it; the staff Forms & consent screen shows intake status per client and lets the desk send/chase it.

## Requirements

- To complete my medical history, medications, allergies and contraindications before my visit on my phone.

## Acceptance Criteria

- [ ] Configurable pre-visit forms capture history, meds, allergies/contraindications.
- [ ] Intake is sent on booking and completable in the client app/web.
- [ ] Responses auto-link to the client's chart.
- [ ] Incomplete required intake contributes to the treatment block.

## UI designs / screenshots

_Prototype screen: prototype.html — Forms & consent; client-app.html intake/consent; checkin.html._

- Client app / public: a pre-visit intake wizard (medical history → quick safety check → wellbeing/BDD → consent → image use → done) — see client-app.png; the same self-service flow is available at the reception check-in tablet (checkin.png: find → confirm → details → health check → forms → done).
- Staff: Forms & consent (forms-consent.png) lists templates with type/version/status and recent submissions (e.g. 'Jess Tan · Medical history · pending — link sent'); the desk can send/chase intake.
- Forms are configurable (admin-defined fields); medical-history step uses checkboxes incl. 'None of the above'.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeForm** — id, tenant_id, name, version, fields(json schema), required(bool)
  - _Configurable; versioned; new version on field change._
- **IntakeResponse** — id, tenant_id, client_id, appointment_id, form_version, answers(json), contraindication_flags[], submitted_at
  - _Auto-linked to the chart; presence of required, current responses contributes to the gate (GATING)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Configurable, versioned IntakeForm + JSON field schema**
  Model IntakeForm (name, version, fields as a JSON schema, required flag) so admins can define fields without code; bump version on change. Validate submitted answers against the schema server-side. Tenant-scoped (RLS). Seed the v1 medical-history & screening template (history checkboxes, contraindication items).
- [ ] **IntakeResponse capture + auto-link to chart/appointment**
  Endpoint to submit an IntakeResponse from the client app/web/kiosk: stamp form_version, store answers(json), derive contraindication_flags, set submitted_at, and auto-link to client_id + appointment_id so it appears on the chart. Required-and-current responses feed the GATING evaluation. Re-screen vs full form chosen by new/returning. Audited.
- [ ] **Staff Forms & consent intake status + send/chase UI**
  Forms & consent screen: templates table (form/type/version/status) and recent submissions with per-client intake status (complete / pending — link sent). Actions to send or chase an intake link (via PRD-07). The client-app/kiosk intake wizard (history → safety check → wellbeing → consent → image use → done) renders the configured form.
