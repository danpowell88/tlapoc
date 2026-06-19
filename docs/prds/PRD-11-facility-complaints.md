# PRD-11 — Facility, Infection Control, Emergency & Complaints

> **▸ Option A alignment (rev 2, 2026-06-19).** No material change — facility/infection-control/emergency stay **lightweight record-keeping** in v1. One linkage worth noting: a **complaint** raised from a conversation (inbox, ADR-0019) should surface the **AHPRA** complaint pathway (C24). See [requirements §12](../02-requirements.md#12-option-a-prototype-alignment--feasibility-register).

> **Phase:** 1–2 (lightweight in v1) · **Status:** Draft
> **Requirements:** REQ-FAC-1…3, REQ-CLI-4 (complaints) · **Compliance:** C20, C24
> **ADRs:** 0008 (compliance-by-construction), 0010 (audit) · **Depends on:** PRD-01

## 1. Summary
The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus
a **complaints register** with the mandated AHPRA pathway. Deliberately **lightweight in v1**
(registers + reminders), with fuller workflows later — the clinic owns the accreditation itself; the
platform proves it.

## 2. Goals & non-goals
**Goals:** record facility accreditation (ACSQHC/NSQHS) + expiry; infection-control logs
(sterilisation/single-use, sharps & clinical-waste); emergency-kit (hyaluronidase, anaphylaxis)
availability/expiry; continuity-of-care contact; complaints register surfacing AHPRA.
**Non-goals (v1):** full IPC workflow/automation; equipment maintenance scheduling; deep incident
case management (Phase 2).

## 3. Users
Owner/manager (accreditation, kit, complaints), clinical staff (logs), compliance officer.

## 4. User stories
- As an **owner**, I record our **facility accreditation** and get alerted before it expires.
- As **staff**, I keep simple **infection-control logs** (sterilisation/single-use, sharps & clinical-waste disposal).
- As an **owner**, I track the **emergency kit** (incl. **hyaluronidase**, anaphylaxis) and am alerted on expiry, and I record a **continuity-of-care** contact for when the treating practitioner/prescriber is unavailable.
- As a **manager**, I log a **complaint/adverse outcome** against a client/treatment and the system surfaces complaint pathways incl. **AHPRA** (noting an NDA doesn't remove that right).

## 5. Key flow
```mermaid
flowchart TD
  A[Facility profile] --> B[Accreditation + expiry alerts]
  A --> C[Emergency kit register\n(hyaluronidase/anaphylaxis) + expiry]
  A --> D[Continuity-of-care contact]
  E[IPC logs: sterilisation/\nsharps/clinical-waste] --> F[(Audit)]
  G[Complaint logged] --> H[Link client/treatment\n+ surface AHPRA pathway]
  H --> F
```

## 6. Functional scope
- **Facility accreditation** (REQ-FAC-1, C20): per-location accreditation status + expiry alerts.
- **Infection control** (REQ-FAC-2, C20): sterilisation/single-use, sharps & clinical-waste disposal logs.
- **Emergency preparedness** (REQ-FAC-3, C20): emergency/complication protocol links; emergency-kit availability/expiry (hyaluronidase, anaphylaxis); continuity-of-care contact.
- **Complaints** (REQ-CLI-4, C24): complaints/adverse-outcome register linked to client/treatment; surfaces complaint mechanisms incl. AHPRA (and NDA-doesn't-remove-the-right); feeds retention (complaint → indefinite, C18) and reporting (PRD-08).

## 7. Data & entities
`FacilityAccreditation`, `InfectionControlLog`, `EmergencyKitItem` (expiry), `ContinuityContact`,
`Complaint` (client, treatment, status, pathway). All audited (ADR-0010).

## 8. Acceptance criteria
- **AC1 (C20):** Accreditation and emergency-kit items raise expiry alerts before lapse.
- **AC2 (C20):** Infection-control disposals/sterilisation can be logged and are audited.
- **AC3 (C24):** A complaint links to the client/treatment, surfaces the AHPRA pathway, and is retained; a complaint flag drives indefinite retention of the related record (C18, PRD-01).
- **AC4:** A continuity-of-care contact is recorded and visible when the treating practitioner/prescriber is unavailable.

## 9. Dependencies & sequencing
After PRD-01. Lowest build priority in Phase 1; complaints register pairs with PRD-08 reporting and PRD-01 retention.

## 10. Out of scope
Full IPC automation, equipment maintenance scheduling, deep incident case management (Phase 2).

## 11. Open questions
- Which IPC log fields are genuinely needed in v1 vs Phase 2.
- Whether facility accreditation is mandatory-blocking or advisory in the product.
