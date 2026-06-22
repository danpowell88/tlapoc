# Sub-processor residency posture (APP-8)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/SUBPROCESSOR-POSTURE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-01/RESIDENCY`

## Background

As a owner, I want assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors, so that integrations don't breach cross-border rules.
No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists (REQ-INT-3, C21/ADR-0016).

## How it works

No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists; flows are registered, and all integrations are outbound and swappable (ADR-0012/0016). Ties into PRD-01/RESIDENCY enforcement.
Keeps integrations inside cross-border privacy rules (C21).

## Requirements

- Assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are registered.
- [ ] All integrations are outbound and swappable.
- [ ] Ties into PRD-01/RESIDENCY enforcement.

## UI designs / screenshots

- Prototype: Settings -> Integrations (settings-integrations.png) — each integration shows its data-residency posture; an admin sub-processor register lists flows + APP-8 status.

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **SubProcessor** — (shared with PRD-01) id, name, region, app8_assessment_ref, consent_ref
  - _Non-AU blocked unless assessed + consented._

## Technical notes (high level)

- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - SubProcessor — (shared with PRD-01) id, name, region, app8_assessment_ref, consent_ref (Non-AU blocked unless assessed + consented.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Enforce compliance gate + audit events**
  Enforce C21 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists.
- [ ] **Integration adapter, sync & config**
  Implement the provider behind its swappable port:
  - Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.
  - Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.
  - Handle partial failures + replays; surface errors to the user.
  - Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).
