# Sub-processor residency posture (APP-8)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/SUBPROCESSOR-POSTURE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-01/RESIDENCY`

## Background

As a owner, I want assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors, so that integrations don't breach cross-border rules.
This story is the cross-border privacy gate over every integration: it ensures no client data leaves Australia to an outside service unless a documented cross-border assessment and consent exist, blocking the flow otherwise. It sits in the Integrations layer (step 10 of the clinic-first build) and extends the in-country data-residency guarantee from Foundations (PRD-01 RESIDENCY) to the outbound edge where data leaves the platform (Xero, calendar, SMS), so it depends on that. This is a compliance control, not a financial feature. No integration sends PII (personal information) to a non-AU sub-processor unless an APP-8 (Australian Privacy Principle 8, cross-border disclosure) assessment + consent record exists (REQ-INT-3, C21/ADR-0016).

## How it works

The cross-border privacy gate over every integration: no integration sends PII to a sub-processor outside Australia unless a documented APP-8 cross-border assessment and a client consent record exist (C21, ADR-0016). It ties into PRD-01 RESIDENCY enforcement — all PII/PHI is pinned to Australia East — and extends that guarantee to the outbound edge where data leaves the platform (Xero, calendar, SMS).
Every sub-processor data flow is registered: a SubProcessor record (shared with PRD-01) capturing the provider, the region it processes in, the APP-8 assessment reference and the consent reference. Before an integration dispatches PII, a residency check evaluates the sub-processor's region; an AU-resident provider passes, a non-AU provider passes only if the APP-8 assessment + consent are present, otherwise the flow is blocked (fail-closed). All integrations are outbound and swappable (ADR-0012), which keeps the set of sub-processors small and enumerable.
Surfaced on the Integrations screen: each integration card shows its data-residency posture, and an admin sub-processor register lists the flows with their APP-8 status. This is a compliance control, not a financial feature.

## Requirements

- Assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] No integration dispatches PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists (fail-closed otherwise).
- [ ] Every sub-processor data flow is registered (provider, region, APP-8 assessment ref, consent ref).
- [ ] A residency check evaluates the sub-processor region before dispatch and blocks non-compliant flows.
- [ ] All integrations are outbound and swappable; ties into PRD-01/RESIDENCY enforcement.
- [ ] Each integration card shows its residency posture; an admin register lists flows + APP-8 status.

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — each integration card shows its data-residency posture.
- Admin sub-processor register: provider, region (AU / non-AU), APP-8 assessment status, consent reference, linked flows.
- A non-compliant flow is visibly blocked / flagged (not silently dropped).

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **SubProcessor** — (shared with PRD-01) id, name, provider, region, app8_assessment_ref?, consent_ref?, flows[]
  - _Non-AU blocked unless app8_assessment_ref + consent_ref present (C21/ADR-0016)._
- **(check) ResidencyCheck** — evaluates sub_processor.region before PII dispatch -> allow|block
  - _Fail-closed; ties to PRD-01 RESIDENCY._

## Technical notes (high level)

- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Sub-processor register + residency check (fail-closed)**
  Behaviour: register every sub-processor data flow and gate it on region before any PII (personal information) leaves the platform. Requirements: model the SubProcessor register (shared with PRD-01: provider, region, APP-8 (Australian Privacy Principle 8, cross-border disclosure) assessment ref, consent ref, linked flows); the pre-dispatch residency check allows an AU region, allows non-AU only if the APP-8 assessment + consent are present, else blocks (fail-closed) and flags; ties into PRD-01 RESIDENCY (all PII/PHI AU-pinned).
- [ ] **Enforce posture across the integration ports + audit**
  Behaviour: no adapter can dispatch PII without passing the gate. Requirements: wire the residency check into the IAccountingExport / ICalendarProvider / INotifier dispatch paths; audit registration changes and any blocked flow (ADR-0010); all integrations stay outbound + swappable (ADR-0012); compliance concern, capability-gated.
- [ ] **Web UI: residency posture on cards + admin register**
  Behaviour: make the posture visible and the register manageable. Requirements: show each integration card's data-residency posture on Settings → Integrations; build the admin sub-processor register (provider, region, APP-8 status, consent ref, linked flows) with non-compliant flows visibly flagged/blocked (not silently dropped); admin/compliance-gated; no money figures.
