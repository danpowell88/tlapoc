# PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)

> **Stage / Milestone:** M1 · Foundations & tenancy (PRD-01)  ·  **Phase:** 0  ·  **Stories:** 25

The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights. Everything else builds on this.

**Source PRD:** `docs/prds/PRD-01-foundations-tenancy.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `TENANT` | [Tenant provisioning & staff invitation](../stories/PRD-01__TENANT.md) | Story | P0 | 5 | 2 |
| `RBAC` | [RBAC + scope-of-practice matrix enforcement](../stories/PRD-01__RBAC.md) | Story | P0 | 5 | 3 |
| `CREDENTIALS` | [Staff credentials + canInject compliance gate (core: records + derivation)](../stories/PRD-01__CREDENTIALS.md) | Story | P0 | 5 | 3 |
| `CREDENTIALS-PIE` | [Credentials: AHPRA PIE register auto-verification](../stories/PRD-01__CREDENTIALS-PIE.md) | Story | P2 | 2 | 2 |
| `REG-WATCH` | [Registration / PII / CPD expiry alerting (core: scheduled watch + auto-lapse)](../stories/PRD-01__REG-WATCH.md) | Story | P1 | 3 | 2 |
| `REG-WATCH-ROUTING` | [Reg-watch: role-targeted routing to digest + Follow-ups](../stories/PRD-01__REG-WATCH-ROUTING.md) | Story | P2 | 2 | 2 |
| `REG-WATCH-BOARD` | [Reg-watch: 'who is cleared to inject today' compliance board](../stories/PRD-01__REG-WATCH-BOARD.md) | Story | P2 | 2 | 1 |
| `REG-WATCH-CHIPS` | [Reg-watch: amber early-warning countdown chips](../stories/PRD-01__REG-WATCH-CHIPS.md) | Story | P2 | 2 | 1 |
| `ROSTER` | [Rosters & engagement type (core: roster grid + availability)](../stories/PRD-01__ROSTER.md) | Story | P1 | 3 | 2 |
| `ROSTER-LEAVE` | [Roster: time-off / leave list with approval](../stories/PRD-01__ROSTER-LEAVE.md) | Story | P2 | 2 | 2 |
| `ROSTER-ENGAGEMENT` | [Roster: engagement-type recording for attribution](../stories/PRD-01__ROSTER-ENGAGEMENT.md) | Story | P2 | 2 | 1 |
| `AUDIT` | [Exportable audit trail for clinical / medicines / PII](../stories/PRD-01__AUDIT.md) | Story | P0 | 5 | 3 |
| `RETENTION` | [Retention policy engine & destruction register](../stories/PRD-01__RETENTION.md) | Story | P1 | 3 | 3 |
| `BREACH` | [Data-breach assessment & notification workflow](../stories/PRD-01__BREACH.md) | Story | P1 | 3 | 3 |
| `PRIVACY-RIGHTS` | [Client privacy: collection notice, access & correction (DSAR)](../stories/PRD-01__PRIVACY-RIGHTS.md) | Story | P1 | 3 | 3 |
| `RESIDENCY` | [Data residency & sub-processor controls](../stories/PRD-01__RESIDENCY.md) | Story | P1 | 3 | 3 |
| `CLIENT-CORE` | [Client core record: DOB & under-18 flag (core: record + age derivation)](../stories/PRD-01__CLIENT-CORE.md) | Story | P1 | 3 | 1 |
| `CLIENT-CORE-SOFTDELETE` | [Client core: soft-delete with audit](../stories/PRD-01__CLIENT-CORE-SOFTDELETE.md) | Story | P2 | 2 | 1 |
| `CLIENT-CORE-DEDUPE` | [Client core: duplicate detection & reviewed merge](../stories/PRD-01__CLIENT-CORE-DEDUPE.md) | Story | P2 | 2 | 1 |
| `CLIENT-CORE-AGECHIP` | [Client core: patient-header age / under-18 chip](../stories/PRD-01__CLIENT-CORE-AGECHIP.md) | Story | P2 | 2 | 1 |
| `ROLE-BUILDER` | [Custom-role builder (placeholder)](../stories/PRD-01__ROLE-BUILDER.md) | Story | P2 | 1 | 1 |
| `SIGNIN-UI` | [Sign-in / sign-out screens & session management](../stories/PRD-01__SIGNIN-UI.md) | Story | P0 | 5 | 4 |
| `MFA-STEPUP` | [MFA & step-up authentication for sensitive actions](../stories/PRD-01__MFA-STEPUP.md) | Story | P1 | 3 | 3 |
| `MULTI-ROLE` | [Multi-role staff & active-role context](../stories/PRD-01__MULTI-ROLE.md) | Story | P1 | 3 | 3 |
| `AUTH-AUDIT` | [Authentication & authorisation audit events](../stories/PRD-01__AUTH-AUDIT.md) | Story | P1 | 3 | 3 |

_Totals: 25 stories · 54 tasks._
