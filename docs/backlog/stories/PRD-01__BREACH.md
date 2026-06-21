# Data-breach assessment & notification workflow

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/BREACH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a admin, I want a workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry, so that we meet Notifiable Data Breaches obligations.

An eligible data breach (NDB scheme) must be assessed and, if eligible, notified to OAIC + individuals, with a breach register (C22).

## Requirements

- A workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry.
- Traces to requirement(s): REQ-SEC-7.
- Must satisfy compliance obligation(s): C22.

## Acceptance Criteria

- [ ] Flagging a breach starts an assessment workflow.
- [ ] If assessed eligible, it produces OAIC + individual notification drafts.
- [ ] A breach-register entry is created and retained.
- [ ] Observability/security signals (Sprint 0 OBS) can seed a breach case.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-01/AUDIT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/BREACH.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C22.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C22); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
