# PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)

> **Stage / Milestone:** M1 · Foundations & tenancy (PRD-01)  ·  **Phase:** 0  ·  **Stories:** 16

The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights. Everything else builds on this.

**Source PRD:** `docs/prds/PRD-01-foundations-tenancy.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `TENANT` | [Tenant provisioning & staff invitation](../stories/PRD-01__TENANT.md) | Story | P0 | 5 | 2 |
| `RBAC` | [RBAC + scope-of-practice matrix enforcement](../stories/PRD-01__RBAC.md) | Story | P0 | 5 | 3 |
| `CREDENTIALS` | [Staff credentials + canInject compliance gate](../stories/PRD-01__CREDENTIALS.md) | Story | P0 | 5 | 4 |
| `REG-WATCH` | [Registration / PII / CPD expiry alerting](../stories/PRD-01__REG-WATCH.md) | Story | P1 | 3 | 5 |
| `ROSTER` | [Rosters & engagement type](../stories/PRD-01__ROSTER.md) | Story | P1 | 3 | 4 |
| `AUDIT` | [Exportable audit trail for clinical / medicines / PII](../stories/PRD-01__AUDIT.md) | Story | P0 | 5 | 3 |
| `RETENTION` | [Retention policy engine & destruction register](../stories/PRD-01__RETENTION.md) | Story | P1 | 3 | 3 |
| `BREACH` | [Data-breach assessment & notification workflow](../stories/PRD-01__BREACH.md) | Story | P1 | 3 | 3 |
| `PRIVACY-RIGHTS` | [Client privacy: collection notice, access & correction (DSAR)](../stories/PRD-01__PRIVACY-RIGHTS.md) | Story | P1 | 3 | 3 |
| `RESIDENCY` | [Data residency & sub-processor controls](../stories/PRD-01__RESIDENCY.md) | Story | P1 | 3 | 3 |
| `CLIENT-CORE` | [Client core record: DOB & under-18 flag](../stories/PRD-01__CLIENT-CORE.md) | Story | P1 | 3 | 4 |
| `ROLE-BUILDER` | [Custom-role builder (placeholder)](../stories/PRD-01__ROLE-BUILDER.md) | Story | P2 | 1 | 1 |
| `SIGNIN-UI` | [Sign-in / sign-out screens & session management](../stories/PRD-01__SIGNIN-UI.md) | Story | P0 | 5 | 4 |
| `MFA-STEPUP` | [MFA & step-up authentication for sensitive actions](../stories/PRD-01__MFA-STEPUP.md) | Story | P1 | 3 | 3 |
| `MULTI-ROLE` | [Multi-role staff & active-role context](../stories/PRD-01__MULTI-ROLE.md) | Story | P1 | 3 | 3 |
| `AUTH-AUDIT` | [Authentication & authorisation audit events](../stories/PRD-01__AUTH-AUDIT.md) | Story | P1 | 3 | 3 |

_Totals: 16 stories · 51 tasks._
