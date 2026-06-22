# Data-breach assessment & notification workflow

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/BREACH`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a admin, I want a workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry, so that we meet Notifiable Data Breaches obligations.
Plainly: when a data breach is suspected, this walks the clinic through the legal assessment and, if needed, produces the notifications and a permanent register entry. It is a governance story built on the audit trail. It is fed by the security signals and the authentication/authorisation audit, so a suspicious pattern raises a candidate case rather than going unnoticed — the clinic's safety net for its privacy obligations. An eligible data breach (NDB (Notifiable Data Breaches scheme) scheme) must be assessed and, if eligible, notified to OAIC (Office of the Australian Information Commissioner) + individuals, with a breach register (C22).

## How it works

When a potential data breach is flagged, a guided workflow walks the admin/compliance officer through assessment under the Notifiable Data Breaches scheme (C22, REQ-SEC-7): is there unauthorised access/disclosure or loss of personal information, and is serious harm likely. There is a legal clock, so the case tracks detection, assessment and notification dates throughout.
If assessed eligible, the workflow produces OAIC notification + affected-individual notification drafts and creates a breach-register entry that is retained (AC7). If not eligible, the assessment and its reasoning are still recorded — the register is the evidence the clinic assessed every flagged incident, eligible or not.
A case can be opened manually or seeded from security/observability signals (Sprint-0 OBS (the Sprint 0 observability / security-signals capability)) and from the auth/authorisation audit (AUTH-AUDIT) — e.g. anomalous access patterns or a run of scope-blocks can raise a candidate breach case rather than sitting unnoticed in a log. The data-access and auth audit trails (AUDIT/AUTH-AUDIT) are the evidence the assessment draws on.
Workflow states: Detected -> Assessing -> (Eligible | Not eligible) -> Notifying (OAIC + individuals) -> Closed, each with timestamps against the 30-day assessment expectation. Surfaced in Governance (ADR-0030).

## Requirements

- A workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry.
- Compliance: [C22](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Flagging a breach starts an assessment workflow.
- [ ] If assessed eligible, it produces OAIC + individual notification drafts.
- [ ] A breach-register entry is created and retained.
- [ ] Observability/security signals (Sprint 0 OBS) can seed a breach case.

## UI designs / screenshots

- Surfaces in Governance: a breach register (list of cases with status + key dates) and a case workflow (assess -> notify -> close) showing the legal clock, the assessment questions, generated OAIC + individual notification drafts, and a close-out.
- A 'flag a breach' entry point, plus auto-seeded candidate cases from OBS / auth-audit signals.

## Suggested data model

- **DataBreach** — id, tenant_id, detected_at, source(manual|obs|auth_audit), description, assessment(json), eligible(bool), oaic_notified_at, individuals_notified_at, status(detected|assessing|eligible|not_eligible|notifying|closed)
  - _Tracks the legal clock; retained as register evidence whether or not eligible._
- **BreachNotification** — id, breach_id, audience(oaic|individual), draft_ref, sent_at
  - _Generated drafts for OAIC + affected individuals._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Breach case model & assessment workflow (with the legal clock)**
  Model DataBreach as a state machine (detected -> assessing -> eligible|not_eligible -> notifying -> closed) capturing detection/assessment/notification timestamps against the 30-day expectation. Build the guided NDB (Notifiable Data Breaches scheme) assessment (unauthorised access/disclosure or loss; serious-harm likelihood) that records the reasoning whether or not eligible. Append-only audited (ADR-0010); retained as register evidence.
- [ ] **OAIC + individual notification generation & breach register**
  On an eligible assessment, generate OAIC (Office of the Australian Information Commissioner) and affected-individual notification drafts (BreachNotification) from the case data and create the retained breach-register entry (AC7). Track sent dates against the clock. Provide the register list/query for the compliance officer.
- [ ] **Seed cases from OBS / auth-audit signals + Governance UI**
  Let security/observability signals (Sprint-0 OBS (the Sprint 0 observability / security-signals capability)) and auth-audit anomalies (AUTH-AUDIT — e.g. a run of scope-blocks or anomalous access) raise candidate breach cases automatically, plus a manual 'flag a breach' entry. Build the Governance breach register + case workflow UI (assess -> notify -> close) showing the clock, assessment questions, generated drafts and close-out. Capability-gate to compliance/owner.
