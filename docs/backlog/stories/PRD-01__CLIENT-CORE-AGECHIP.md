# Client core: patient-header age / under-18 chip

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE-AGECHIP`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/CLIENT-CORE`

## Background

As a clinician, I want the client's age and under-18 status shown as a chip on the patient header, so that I see the at-a-glance age/gate signal before I chart.
Plainly: the little age chip on the patient header (e.g. '34 · Brisbane') that shows a client's age and, when relevant, their under-18 status — the at-a-glance signal a clinician sees before charting. Where it fits: a follow-up to the client core record (PRD-01/CLIENT-CORE) that surfaces the server-derived age/flag visually; it is consumed by the Client 360 header (PRD-02/CLIENT-360). The chip is purely a read surface over the core's derivation — never a hand-set field — so it can't drift from the gate rules that depend on it.

## How it works

The patient-header age chip is the visible surface of the core's server-side age derivation (PRD-01/CLIENT-CORE): the client's current age and, where relevant, their under-18 status, shown at-a-glance (the prototype's Client 360 header age, e.g. '34 · Brisbane', alongside the consent/VIP chips).
It reads the server-derived age/flag at read time and is never a hand-set field, so it always agrees with the cooling-off (C6) and advertising/pricing (C9) rules that consume the same derivation. The under-18 state is the gate signal a clinician sees before charting. The chip is hosted by the Client 360 header (PRD-02/CLIENT-360); the directory and full profile around it are PRD-02.

## Requirements

- The client's age and under-18 status shown as a chip on the patient header.

## Acceptance Criteria

- [ ] The derived age + under-18 status render as the patient-header age chip (e.g. '34 · Brisbane').
- [ ] The chip reads the server-derived age/flag (never a hand-set field).
- [ ] The under-18 state is the at-a-glance gate signal a clinician sees before charting.
- [ ] It is consumed by the Client 360 header (PRD-02/CLIENT-360); the directory + full profile that host it are PRD-02.

## UI designs / screenshots

- Prototype: the Client 360 header (client-360.png) shows the age (e.g. '34') alongside consent chips ('Consent current', 'Image use', 'Allergy: none') and VIP/member tag.
- The under-18/age chip reads the server-derived age/flag (never hand-set); consumed by the UX age chip on the patient header (PRD-02/CLIENT-360).

## Suggested data model

- **(read) PatientHeaderAgeChip** — from Client.under18 / age (derived, PRD-01/CLIENT-CORE)
  - _Read-only surface over the core's age derivation; never a hand-set field; hosted by the Client 360 header (PRD-02)._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Patient-header age / under-18 chip surface**
  Behaviour: expose the derived age + under-18 status as the patient-header age chip (the visible signal staff always see, e.g. '34 · Brisbane'), consumed by the Client 360 header (PRD-02/CLIENT-360). Requirements: the chip reads the server-derived age/flag (never a hand-set field); the under-18 state is the at-a-glance gate signal a clinician sees before charting; the directory + full profile that host it are PRD-02.
