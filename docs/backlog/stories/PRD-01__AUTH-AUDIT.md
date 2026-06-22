# Authentication & authorisation audit events

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUTH-AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`, `PRD-01/RBAC`

## Background

As a compliance officer, I want an audit of authentication and authorisation events, including blocked out-of-scope attempts, so that we can investigate access and prove the gates work.
Plainly: alongside the record of who saw data, this keeps a record of the security events — sign-ins, lockouts, two-step prompts, role switches and every blocked out-of-scope attempt. It is built on the audit trail and the permission layer. Capturing every blocked attempt is what lets the clinic prove the safety gates actually fire, and a run of suspicious events can seed a breach case. Beyond data-access audit, security needs a record of authentication and authorisation events: sign-in success/failure, lockouts, MFA (multi-factor authentication)/step-up (a fresh re-authentication before a sensitive action), role switches and every scope-block (a blocked out-of-scope action).

## How it works

Beyond the data-access audit (AUDIT), security needs a record of authentication and authorisation events (REQ-SEC-3, C10/C4/C19): sign-in success/failure, account lockout, MFA and step-up, role switches, and — critically — every scope-block: a blocked out-of-scope action (C4) or a lapsed-registration/uncleared action (C19, via canInject (the derived cleared-to-inject gate)), each with the reason that fired.
Capturing scope-blocks is what lets the clinic prove the gates work, not just claim they do: an inspector asks 'show me that an uncleared injector can't administer S4', and the answer is a queryable record of every such attempt and its block. AUTH-AUDIT is the peer of the data-access AuditEvent and shares the same append-only (only ever added to, never edited or deleted) immutability (ADR-0010).
These events are queryable and exportable alongside the data-access trail through the same Governance audit viewer (AUDIT), filtered to auth/authorisation kinds. Suspicious patterns — a burst of sign-in failures, anomalous access, a run of scope-blocks — can seed a breach case (BREACH).
AC mapping: covers AC1 (the block is recorded with its reason) and AC4 (the events are immutable and exportable). It's wired from RBAC's scope-block path, SIGNIN-UI's session events and MFA-STEPUP's assurance events — this story is the unified event type + viewer/feed they all write to.

## Requirements

- An audit of authentication and authorisation events, including blocked out-of-scope attempts.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Sign-in success/failure, lockout, MFA/step-up and role-switch events are recorded.
- [ ] Every blocked out-of-scope or lapsed-registration action writes an audit event with the reason.
- [ ] These events are queryable/exportable alongside the data-access audit.
- [ ] Suspicious patterns can feed the breach workflow (PRD-01/BREACH).

## UI designs / screenshots

- Surfaces in the admin audit viewer / Governance audit pack (gov-audit.png) filtered to auth + authorisation events (sign-in, lockout, MFA/step-up, role-switch, scope-block), with the same filter + export controls as the data-access trail.

## Suggested data model

- **AuthEvent** — id, tenant_id, actor_id, kind(signin_ok|signin_fail|lockout|mfa|stepup|role_switch|scope_block), reason, active_role_id, at, context(json)
  - _Peer of AuditEvent; append-only (ADR-0010). scope_block records the blocked capability + rule; queryable/exportable with the data-access trail; can seed BREACH._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **AuthEvent type (append-only, immutable) covering auth + authorisation**
  Model AuthEvent as a peer of AuditEvent — append-only (only ever added to, never edited or deleted), tenant_id + RLS, no edit/delete path (ADR-0010) — covering signin_ok/fail, lockout, mfa, stepup, role_switch and scope_block, each with a reason and the active role. Index for the viewer filters.
- [ ] **Wire emitters across RBAC / sign-in / MFA**
  Emit AuthEvents from the RBAC scope-block (a blocked out-of-scope action) path (every out-of-scope or lapsed-registration/uncleared attempt, with the rule that fired — AC1), SIGNIN-UI session events (sign-in ok/fail, lockout, sign-out), MFA-STEPUP (mfa/stepup) and MULTI-ROLE (role_switch). One unified stream so 'prove the gate fired' is a single query.
- [ ] **Surface in the audit viewer + breach seeding**
  Make AuthEvents queryable/exportable through the same Governance audit viewer (AUDIT) filtered to auth/authorisation kinds (AC4). Detect suspicious patterns (burst of sign-in failures, anomalous access, a run of scope-blocks) and let them seed a candidate breach case (BREACH).
