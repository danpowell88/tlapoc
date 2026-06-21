# Separate, withdrawable image-use consent

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/IMAGE-CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/CONSENT`

## Background

Intake, consent & compliance gating — Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s.

As a client, I want to give separate consent for photo use and withdraw it whenever I want, so that I control how my images are used.

Photo use requires its own scoped consent, withdrawable at any time, which immediately stops downstream use (C14).

## Requirements

- To give separate consent for photo use and withdraw it whenever I want.
- Traces to requirement(s): REQ-CONS-5.
- Must satisfy compliance obligation(s): C14.

## Acceptance Criteria

- [ ] Image-use consent is separate from treatment consent and scoped.
- [ ] Withdrawing it immediately stops further use and is audited.
- [ ] Downstream media features (PRD-05/09) check this consent.
- [ ] Granted/withdrawn state is visible on the patient header chip.

## UI designs / screenshots

prototype.html — Forms & consent; client-app.html intake/consent; checkin.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-03/CONSENT.

## Other

Epic: PRD-03 — Intake, consent & compliance gating.
Source PRD: docs/prds/PRD-03-intake-consent-gating.md.
Backlog key: PRD-03/IMAGE-CONSENT.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C14.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
