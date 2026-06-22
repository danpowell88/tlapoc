# Retention policy engine & destruction register

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RETENTION`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a admin, I want retention timers and a destruction register that surfaces records due for destruction and logs their destruction, so that we keep records exactly as long as the law requires, no more, no less.
Records must be retained per legal periods (adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation) and destroyed with a register + certificate (C18).

## How it works

A retention engine keeps records exactly as long as the law requires (C18, REQ-SEC-4): adults >=7 years from last contact; minors until age 25 (or 7 years from last entry, whichever is later); indefinite where a complaint / adverse-outcome / litigation flag is set. The per-record-type policy drives a retention timer computed from the relevant anchor (last-contact date, or DOB for the minors rule via CLIENT-CORE's under-18/age derivation).
Records past their period surface on a 'records due for destruction' list, each showing its retention basis (which rule made it eligible) so destruction is a reviewed decision, not an automatic delete. Destroying a record writes an immutable, audited DestructionRecord (patient, period covered, disposal date) plus a certificate reference — AC5 — and removes the live data; the register entry persists forever as the evidence that destruction happened lawfully.
A litigation/complaint hold overrides the timer: a held record never becomes eligible until the hold is cleared, even past 7 years. A transfer log records records handed to another provider (e.g. when a client moves clinics) so the chain of custody is documented. The client app's privacy copy reflects this: 'some clinical records must be retained for a legally required period even after deletion'.
Built on the audit spine (AUDIT) and surfaced in Governance (ADR-0030); it does not relocate any guardrail, it projects the retention state into one place to do the work.

## Requirements

- Retention timers and a destruction register that surfaces records due for destruction and logs their destruction.
- Compliance: [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Retention rules: adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation.
- [ ] Records past retention surface for destruction with their retention basis.
- [ ] Destroying a record writes a destruction-register entry (patient, period, date) + certificate reference.
- [ ] A transfer log records records handed to another provider.

## UI designs / screenshots

- Surfaces in Governance: a 'records due for destruction' list (each row showing retention basis), the destruction register (immutable entries with certificate references), and the transfer log.
- Destruction is an explicit, reviewed, audited action — never a silent auto-delete; held records are visibly excluded.

## Suggested data model

- **RetentionPolicy** — id, tenant_id, record_type, basis(adult7y|minor25|indefinite_on_flag), period, anchor(last_contact|dob)
  - _Per record-type rule; minors rule uses DOB/age (CLIENT-CORE)._
- **RetentionHold** — id, tenant_id, record_ref, reason(complaint|adverse|litigation), set_by, set_at, cleared_at
  - _Overrides the timer; record never eligible while an uncleared hold exists._
- **DestructionRecord** — id, tenant_id, record_ref, patient, period_covered, destroyed_at, destroyed_by, certificate_ref
  - _Immutable + audited (ADR-0010); the lawful-destruction evidence._
- **TransferLog** — id, tenant_id, record_ref, to_provider, transferred_at, transferred_by
  - _Documents records handed to another provider._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Retention policy engine, timers & holds**
  Model RetentionPolicy (per record type, with basis + anchor) and RetentionHold. Compute each record's eligibility from its anchor: adults >=7y from last contact; minors until age 25 / 7y-from-last-entry whichever is later (uses CLIENT-CORE age derivation); indefinite while a complaint/adverse/litigation hold is set. A scheduled scan marks records past period as due-for-destruction with their retention basis; held records are never marked eligible until the hold clears.
- [ ] **Destruction register, certificates & transfer log**
  Implement the explicit, reviewed destruction action that removes the live record and writes an immutable, audited DestructionRecord (patient, period covered, disposal date) + certificate reference (AC5). Model the TransferLog for records handed to another provider. Both append-only (ADR-0010); destruction can never be invoked on a held record. Every destruction/transfer writes an AuditEvent.
- [ ] **Governance UI: due-for-destruction, register & transfer log**
  Build the Governance surfaces: the 'records due for destruction' list with per-row retention basis and a guarded destroy action (confirm + certificate capture), the immutable destruction register, and the transfer log. Make held records visibly excluded with their hold reason. Capability-gate to compliance/owner; no silent auto-delete anywhere.
