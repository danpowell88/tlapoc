# RBAC + scope-of-practice matrix enforcement

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RBAC`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a owner, I want roles mapped to capabilities so the system blocks any action outside a user's scope of practice, so that people can only do what they're trained and legally allowed to do.
Roles map to the §3 scope matrix; the auth pipeline blocks actions outside a user's scope. Capabilities gate API actions, concerns drive role-tailored dashboards (ADR-0017).

## How it works

Authorisation is modelled on two orthogonal axes (ADR-0017): capabilities — atomic permissions that gate API actions (chart, chartView, prescribe/inject, stock, receiveStock, finance.read, takePayment, team:manage, configure/integrations) — and concerns — relevance tags that drive what a role sees first (ops, clinical, stock, stockAlert, financial/biz, recall, consent, frontdesk, facility, compliance, hr). Capabilities decide what you may do; concerns decide what you see.
The prototype's persona set is the canonical preset map: NP (full clinical + prescribe + S4 custody, no financials), Lead Nurse/RN (administer on script, manage stock/team/roster, no prescribing/custody/financials), RN (administer on a valid script only), Dermal/laser (non-S4 only), Reception (scheduling/payment, no clinical/stock/financials), and Owner-business (full financials + read-only clinical/stock oversight, cannot prescribe/chart/hold S4). Solo-NP and Nurse-led-RN are combined presets.
Enforcement is server-side by construction (ADR-0008): every API action declares the capability it needs and the pipeline checks it against the caller's active role before the handler runs. Screen-hiding is presentation only — it is never the control. A blocked action returns a structured reason (what is blocked / which rule / how to resolve / who can resolve) that the UI renders as the calm blocked-action banner, and writes a scope_block audit event (see AUTH-AUDIT). This is how AC1 (C4/C19) holds: an out-of-scope or lapsed-registration attempt is blocked with a reason and logged.
Owner-business is deliberately read-only for clinical/stock unless they personally hold the clinical capability — the owner is a business role, not an automatic clinical superuser. The credential gate (canInject) layers on top of capabilities: holding the inject capability is necessary but not sufficient; the practitioner must also be credential-current (CREDENTIALS).

## Requirements

- Roles mapped to capabilities so the system blocks any action outside a user's scope of practice.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Capabilities × concerns model implemented; each API action checks a capability.
- [ ] The persona set (NP, Lead RN, RN, dermal, reception, owner-business) maps to the matrix.
- [ ] An out-of-scope action is blocked with a clear reason and an audit event.
- [ ] Owner-business is read-only for clinical/stock unless they hold the credential.

## UI designs / screenshots

- Surfaces as the header user chip + scope-of-practice tooltip (hover the name/role 'info' icon) and as nav entries showing/hiding per role — driven by the persona's caps/concerns (prototype data-allow gating in setPersona).
- A blocked action shows the blocked-action banner: what is blocked, which rule fired, how to resolve, and who can resolve it (e.g. 'Requires a current prescriber — ask Dr Park').
- Scope is sourced from the role's capabilities, never hard-coded per screen (consumed by PLATFORM/ROLE-CONTEXT and APP-NAV).

## Suggested data model

- **Role** — id, tenant_id, name, is_preset, capability_keys[], concern_keys[]
  - _Preset roles map to the §3 scope matrix; the capability/concern lists make a custom builder (ROLE-BUILDER) a later addition, not a rewrite._
- **Capability** — key, description
  - _Atomic permission gating an API action: chart, chartView, prescribe, inject, stock, receiveStock, finance.read, takePayment, team:manage, configure._
- **Concern** — key, description
  - _Relevance tag driving role-tailored presentation (dashboard widgets, default landing); presentation-only, never a gate._
- **RoleCapability / RoleConcern** — role_id, capability_key | concern_key
  - _Join rows; preset rows seeded from the persona map; editable later by the custom-role builder._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Capability/concern model, preset roles & seed**
  Model Role, Capability, Concern and their joins (all tenant_id + RLS). Seed the canonical preset roles from the prototype persona map (NP, Lead RN, RN, dermal, reception, owner-business + Solo/Nurse-led presets) with their exact capability and concern sets. Capabilities are the atomic API gates; concerns are presentation tags. Keep presets editable-shaped so ROLE-BUILDER can compose custom roles without a schema change.
- [ ] **Server-side authorisation pipeline (capability checks + structured blocked reason)**
  Add an authorisation step that runs before every protected handler: resolve the caller's active role, check the action's declared capability, and on failure short-circuit with a structured, machine-readable reason object {blocked, rule, howToResolve, whoCanResolve}. Capabilities gate; concerns never gate. Owner-business stays read-only for clinical/stock unless it holds the clinical capability. Expose the caller's resolved capabilities + concerns via a session/context endpoint so the web shell can render nav and the scope tooltip from the same source of truth.
- [ ] **Scope-block enforcement & audit on out-of-scope / lapsed actions**
  Wire the blocked path so an out-of-scope action (C4) or a lapsed-registration action (C19, via canInject from CREDENTIALS) is rejected with the reason payload AND writes a scope_block audit event capturing actor, attempted capability, the rule that fired and the active role (peer of AUTH-AUDIT). Surface the reason to the UI for the blocked-action banner. This makes 'only allowed people can act' true by construction, satisfying AC1.
