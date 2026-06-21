# Registration / PII / CPD expiry alerting

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/REG-WATCH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/CREDENTIALS`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a owner, I want to be alerted before a practitioner's registration, cosmetic insurance or CPD lapses, so that we never treat with an unregistered or uninsured practitioner.

Staff must be alerted before registration, insurance or CPD lapses so the clinic is never unknowingly non-compliant.

## Requirements

- To be alerted before a practitioner's registration, cosmetic insurance or CPD lapses.
- Traces to requirement(s): REQ-TEN-7.
- Must satisfy compliance obligation(s): C19.

## Acceptance Criteria

- [ ] Items within N days of expiry surface on an alert/watchlist (also feeds PRD-08).
- [ ] On lapse, the practitioner's canInject flips to not-cleared automatically.
- [ ] Alerts are role-targeted and dismiss/acknowledge is audited.
- [ ] AHPRA register auto-verification (PIE) is supported with a first-class manual-verify fallback.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0029 (see docs/adr/decision-log.md).
Depends on: PRD-01/CREDENTIALS.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/REG-WATCH.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C19.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
