# Feature flags & per-tenant configuration

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/FEATURE-FLAGS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/API`

## Background

As a platform engineer, I want feature flags and a typed per-tenant configuration store, so that we can ship features progressively and tailor behaviour per clinic.
The build is staged and many capabilities are configurable per tenant (cooling-off policy, S4 naming, telehealth path risk, modality availability, deferred features). A flag + config mechanism lets features ship dark and toggle per tenant.

## How it works

Feature flags can be toggled globally and overridden per tenant, so a feature can ship dark (off everywhere), be enabled for a pilot tenant, then rolled out — without a deploy. Per-tenant configuration is typed and validated (not free-form strings): cooling-off N days, S4 naming policy, modality availability and similar are bound to typed options with validation, so an invalid value is rejected rather than silently misbehaving.
Flag and config reads are cached (with bounded refresh) so the hot path isn't hitting the store on every request, and reads/changes are observable via OBS. Every change to a flag or config value is audited (AUDIT-INFRA) — who changed which clinic's setting, when — because these settings drive compliance-relevant behaviour (e.g. cooling-off duration).
The two records are a FeatureFlag (key, scope global|tenant, enabled, optional tenant_id) and a typed TenantConfig (tenant_id, key, typed value). Later stories read these rather than hard-coding policy, which is what makes the platform tailorable per clinic and lets the staged build hide unfinished work.

## Requirements

- Feature flags and a typed per-tenant configuration store.

## Acceptance Criteria

- [ ] Feature flags can be toggled globally and per tenant.
- [ ] Per-tenant configuration (e.g. cooling-off N days, S4 naming, modality availability) is typed and validated.
- [ ] Flag/config reads are cached and observable.
- [ ] Changing a flag/config is audited.

## Suggested data model

- **FeatureFlag** — key, scope(global|tenant), enabled, tenant_id?
  - _Ship dark globally; per-tenant override; toggled without deploy; changes audited._
- **TenantConfig** — tenant_id, key, value(typed)
  - _Typed + validated (e.g. cooling_off_days, s4_naming, modality availability); read by COOLING-OFF, booking page, MODALITY etc._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build feature flags (global + per-tenant) and a typed, validated per-tenant config store**
  Provide toggles and tailorable settings the staged build and per-clinic behaviour rely on.
  - Feature flags toggleable globally and overridable per tenant — ship dark, pilot, roll out, all without a deploy.
  - TenantConfig bound to TYPED options with validation (cooling_off_days, s4_naming, modality availability, telehealth path risk, deferred-feature switches) — invalid values rejected, not silently mishandled.
  - Flag/config reads cached with bounded refresh so the hot path stays fast; reads observable via OBS.
- [ ] **Audit flag/config changes and document the model**
  Make compliance-relevant settings traceable and the mechanism reusable.
  - Every flag/config change emits an AuditEvent (who/which tenant/which key/old->new) via AUDIT-INFRA — these settings drive compliance behaviour (e.g. cooling-off duration), so changes must be on the trail.
  - Document how a feature ships dark, how to add a typed tenant-config key, and which later stories read which keys (COOLING-OFF, booking page S4 naming, MODALITY availability).
