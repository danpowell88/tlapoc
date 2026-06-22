# Client core record: DOB & under-18 flag

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a system, I want to capture client DOB and derive an under-18 flag, so that downstream cooling-off and pricing rules can enforce age-based requirements.
Plainly: this is the bare-bones client record — enough to capture date of birth and work out whether the client is under 18, which several later rules depend on. It is a small Foundations story built on tenancy. The full client directory and profile come later in the Reception epic; this story exists early only so that age-based rules (cooling-off, advertising/pricing) have a single trustworthy source. The client record captures DOB (date of birth) and derives an under-18 flag that feeds cooling-off (C6) and advertising/pricing (C9) elsewhere.

## How it works

The core client record captures DOB and derives an under-18 flag (and current age) that downstream rules consume (REQ-CLI-3, C6): the under-18 cooling-off requirement (PRD-03/C6) and the S4 advertising/pricing rules (C9). Deriving age once, server-side, means every consumer reads the same answer instead of re-implementing date maths.
The flag is computed, not stored as a static field, so it updates correctly across a birthday — a client who is 17 today is automatically 18 (and no longer under-18-gated) on their birthday with no batch job needed. It is exposed to PRD-03/06/07 and shown as the age chip on the patient header (the Client 360 header age, e.g. '34 · Brisbane').
This story is the underlying record + age derivation + lifecycle plumbing only — the full client directory, search and 360 profile are PRD-02. It supports soft-delete with audit (a deleted client is excluded from active views but the row and its history remain for retention/audit, never hard-deleted here — destruction is RETENTION's job) and duplicate handling (merge candidates surfaced, not auto-merged, to avoid a false merge of two real people).
Edge cases: an unknown/estimated DOB still derives a defensible age band; a soft-deleted client cannot be booked or appear in active search; merge is a reviewed action that re-points history and writes an audit event.

## Requirements

- To capture client DOB and derive an under-18 flag.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] DOB captured; under-18 flag derived and exposed to PRD-03/PRD-06/PRD-07.
- [ ] The flag updates correctly across a birthday.
- [ ] Soft-delete with audit and duplicate handling supported (full CRM (the client relationship / directory management in PRD-02) in PRD-02).
- [ ] Under-18 status is visible on the patient header (consumed by UX age chip).

## UI designs / screenshots

- Prototype: the Client 360 header (client-360.png) shows the age (e.g. '34') alongside consent chips ('Consent current', 'Image use', 'Allergy: none') and VIP/member tag; DOB sits on the profile.
- The under-18/age chip is consumed by the UX age chip on the patient header (the visible signal staff always see); the directory + full profile are PRD-02.

![client-360 — prototype screen](../screens/client-360.png)

## Suggested data model

- **Client** — id, tenant_id, name, dob, contacts, flags(json), under18(derived), age(derived), deleted_at
  - _under18/age recomputed across birthdays (not stored static); soft-delete excluded from active views; FK target for clinical/booking records (full CRM in PRD-02)._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Client core record + server-side age / under-18 derivation**
  Behaviour: model the Client core (tenant_id + RLS (row-level security)) with DOB (date of birth) and derive under18 + current age server-side AT READ TIME so they stay correct across a birthday with no batch job (a client who is 17 today is 18 on their birthday automatically). Requirements: expose the derived flag/age to PRD-03/06/07 (the under-18 cooling-off C6 and the S4 advertising/pricing C9 rules) so every consumer reads one answer instead of re-implementing date maths; an unknown/estimated DOB still derives a defensible age band.
- [ ] **Soft-delete with audit (retention/destruction stays RETENTION's job)**
  Behaviour: support soft-delete (deleted_at) so a deleted client is excluded from active/bookable/search views but the row and its history remain. Requirements: never hard-delete here — destruction is RETENTION's job; a soft-deleted client cannot be booked or appear in active search; the delete writes an audit event.
- [ ] **Duplicate detection & reviewed merge**
  Behaviour: surface duplicate/merge candidates (matching name + DOB (date of birth) + contact) as suggestions, never auto-merging two real people. Requirements: merge is a reviewed action that re-points history to the surviving record and writes an audit event; soft-deleted and merged-away records stay out of active views (full client directory + 360 profile are PRD-02).
- [ ] **Patient-header age / under-18 chip surface**
  Behaviour: expose the derived age + under-18 status as the patient-header age chip (the visible signal staff always see, e.g. '34 · Brisbane'), consumed by the Client 360 header (PRD-02/CLIENT-360). Requirements: the chip reads the server-derived age/flag (never a hand-set field); the under-18 state is the at-a-glance gate signal a clinician sees before charting; the directory + full profile that host it are PRD-02.
