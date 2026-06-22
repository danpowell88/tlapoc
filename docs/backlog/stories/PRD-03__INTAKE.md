# Pre-visit intake forms

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** client-app, backend
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a client, I want to complete my medical history, medications, allergies and contraindications before my visit on my phone, so that my practitioner has what they need and my treatment is safe.
Pre-visit intake is the first step of Intake & Consent (PRD-03), which sits between booking (PRD-02) and treatment and enforces what must be true before a clinician can proceed. Intake collects the medical history a practitioner must see, and it is triggered by a booking (PRD-02/ONLINE-BOOK or the booking wizard). In the flow it precedes and feeds the rest of PRD-03 — the BDD screen (PRD-03/BDD), the e-signed consent (PRD-03/CONSENT) and the treatment gate (PRD-03/GATING) — and its responses auto-link to the chart so the consult (PRD-04) and charting (PRD-05) downstream see them. Incomplete required intake is one of the inputs that blocks treatment.  Clients complete medical history, meds, allergies and contraindications on their phone before the visit; responses auto-link to the chart.

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

- [ ] **IntakeResponse capture + auto-link to chart/appointment**
  Behaviour: an endpoint that submits an IntakeResponse from the client app / web / kiosk. Requirements: stamp form_version, store answers(json), derive contraindication_flags, set submitted_at, and auto-link to client_id + appointment_id so it appears on the chart; the response is validated server-side against the form's JSON schema; required-and-current responses feed the GATING evaluation; audited.
- [ ] **Re-screen vs full form (new/returning)**
  Behaviour: a returning client gets a quick medical re-screen; a new client gets the full intake form. Requirements: the form variant is chosen from the booking's new_or_returning flag (PRD-02); both stamp the form_version they were answered against; the quick re-screen still captures any changed contraindications.
- [ ] **Medical-history step + quick safety check**
  Behaviour: the intake wizard's medical-history step (checkboxes incl. pregnancy/breastfeeding, blood thinners, cold-sore history, latex/lidocaine allergies, and 'None of the above') followed by a 'quick safety check' summary. Requirements: selections derive contraindication_flags; the safety check summarises whether any contraindication was flagged for the nurse; rendered identically in the client app and at the reception check-in tablet.
- [ ] **Staff Forms & consent: intake status + send/chase**
  Behaviour: the staff Forms & consent screen showing recent submissions with per-client intake status (complete / pending — link sent) and actions to send or chase an intake link. Requirements: send/chase goes via PRD-07; status reflects whether a required, current IntakeResponse exists; rows deep-link to the client.
