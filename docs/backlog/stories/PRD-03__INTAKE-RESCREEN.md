# Pre-visit intake: re-screen vs full form (new/returning)

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE-RESCREEN`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a client, I want a quick re-screen if I'm a returning client and the full form if I'm new, so that I only answer what's needed for my visit.
Plainly: choosing the right intake variant — a quick medical re-screen for returning clients, the full intake form for new ones. Where it fits: a follow-up to the pre-visit intake basic capture (PRD-03/INTAKE) that adds the new/returning variant on top of the basic submission. The variant is chosen from the booking's new_or_returning flag (PRD-02). It sits in Intake & Consent (PRD-03), between booking and treatment.

## How it works

The basic story captures a single intake form; this follow-up selects the right variant for the client. A returning client gets a quick medical re-screen (confirming what's changed), while a new client gets the full intake form.
The variant is chosen from the booking's new_or_returning flag (PRD-02/LIFECYCLE-BOOKING-CAPTURE), so the right form is presented automatically without the desk choosing.
Both variants stamp the form_version they were answered against (so a response stays bound to its form), and the quick re-screen still captures any changed contraindications so safety is never skipped for a returning client.

## Requirements

- A quick re-screen if I'm a returning client and the full form if I'm new.

## Acceptance Criteria

- [ ] A returning client gets a quick medical re-screen; a new client gets the full intake form.
- [ ] The form variant is chosen from the booking's new_or_returning flag (PRD-02).
- [ ] Both stamp the form_version they were answered against.
- [ ] The quick re-screen still captures any changed contraindications.

## UI designs / screenshots

- Client app / public: a quick re-screen for returning clients, the full intake wizard for new clients (client-app.png).
- The variant is selected from the booking's new/returning flag; both stamp form_version.
- The re-screen still captures changed contraindications.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeResponse (extends INTAKE)** — form_version (full vs re-screen variant)
  - _Variant chosen from the booking's new_or_returning flag (PRD-02); both stamp the form_version answered against._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Re-screen vs full form (new/returning)**
  Behaviour: a returning client gets a quick medical re-screen; a new client gets the full intake form. Requirements: the form variant is chosen from the booking's new_or_returning flag (PRD-02); both stamp the form_version they were answered against; the quick re-screen still captures any changed contraindications.
