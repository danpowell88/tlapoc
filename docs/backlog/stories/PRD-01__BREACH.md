# Data-breach assessment & notification workflow

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/BREACH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a admin, I want a workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry, so that we meet Notifiable Data Breaches obligations.
An eligible data breach (NDB scheme) must be assessed and, if eligible, notified to OAIC + individuals, with a breach register (C22).

## How it works

When a potential data breach is flagged, a guided workflow assesses eligibility under the Notifiable Data Breaches scheme; if eligible it produces OAIC + individual notification drafts and a register entry. Observability/security signals (Sprint-0 OBS) can seed a case.
There is a legal clock, so the workflow tracks assessment and notification dates.

## Requirements

- A workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry.
- Compliance: [C22](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Flagging a breach starts an assessment workflow.
- [ ] If assessed eligible, it produces OAIC + individual notification drafts.
- [ ] A breach-register entry is created and retained.
- [ ] Observability/security signals (Sprint 0 OBS) can seed a breach case.

## UI designs / screenshots

- Surfaces in Governance: a breach register + a case workflow (assess -> notify -> close) with status and dates.

## Suggested data model

- **DataBreach** — id, tenant_id, detected_at, description, assessment(json), eligible(bool), oaic_notified_at, individuals_notified_at, status

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C22); blocked path explains why.
