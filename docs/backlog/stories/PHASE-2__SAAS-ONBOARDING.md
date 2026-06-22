# SaaS onboarding & billing UI (placeholder)

> **Epic:** [PHASE-2 — Phase 2+ / scale (cross-cutting placeholders)](../epics/PHASE-2.md)  ·  **Key:** `PHASE-2/SAAS-ONBOARDING`  ·  **Type:** Story  ·  **Stage:** M7  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a prospective clinic, I want to sign up for the platform myself and pay a subscription, so that onboarding doesn't need manual provisioning.
Plainly: this would let a brand-new clinic sign itself up and pay a subscription with no manual setup by our team. Where it fits: a deferred Phase 3 placeholder — the platform is multi-tenant (each clinic isolated in shared infrastructure) from day one, but v1 onboards this single clinic by hand, so self-service sign-up only matters once we sell the platform to other clinics.  Placeholder (Phase 3): self-service tenant sign-up, subscription billing and per-tenant Entra (Microsoft identity platform) federation to sell the platform as SaaS (software-as-a-service) (a PRD-01 non-goal).

## How it works

Placeholder (Phase 3): self-service tenant sign-up, subscription billing and per-tenant Entra federation to sell the platform as SaaS. v1 provisions tenants manually; tenancy/identity are already SaaS-ready (RLS isolation, Entra auth). Captured so tenancy/identity stay SaaS-ready.

## Requirements

- To sign up for the platform myself and pay a subscription.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 3; v1 provisions tenants manually.
- [ ] Captured so tenancy/identity stay SaaS-ready.

## Suggested data model

- **(future) Subscription** — tenant_id, plan, billing_status
  - _Phase 3._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Placeholder: self-service onboarding + subscription billing (Phase 3)**
  Deferred. Self-service tenant sign-up, subscription billing and per-tenant Entra federation on top of the already SaaS-ready tenancy/identity. Not built in v1.
