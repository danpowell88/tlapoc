# Synthetic seed data & local dev environment

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEED`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

As a developer, I want a one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock, so that I can run and demo any module locally without touching real data.
Every module needs realistic-but-synthetic data to be developed and demoed without touching real PII — a clinic, staff with credentials, clients (including an under-18 for cooling-off paths), services flagged S4/non-S4, and stock lots. The project rule is absolute: all seed data is synthetic; no real client, staff or business information ever. SEED depends on DB (the schema it populates and the containerised local Postgres) and is reused by the integration/e2e tests (TEST). It's what makes a one-command local environment possible for every later feature.  Realistic synthetic data (clinic, staff with credentials, clients, services incl. S4/non-S4, stock) lets every module be developed and demoed without real PII. All data must stay synthetic (project rule).

## How it works

A single command spins up the local stack — containerised Postgres + API + web — and seeds a synthetic tenant. The seed is broad enough to exercise the real compliance paths: staff with roles and credentials (so RBAC/scope works), clients including at least one under-18 (so the cooling-off and payment-block paths from C6 are testable), services flagged S4 and non-S4 (so the rewards/public-naming classification from ADR-0014 has data), and stock lots (so custody/expiry/recall flows have something to track).
All seed data is clearly synthetic and obviously fake — names, contacts and business details are invented — honouring the project's hard rule. The seed is reproducible (same command, same data) so it's safe to reset and is the fixture the integration and e2e tests build on, keeping tests and local dev in sync.
Because the seed reflects the compliance-relevant edge cases (under-18, S4 vs non-S4, lots) rather than just happy-path rows, it lets developers and demos hit the guardrails (ADR-0008) the product is actually built around.

## Requirements

- A one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock.

## Acceptance Criteria

- [ ] A script spins up Postgres + API + web locally and seeds a synthetic tenant.
- [ ] Seed covers staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots.
- [ ] All seed data is clearly synthetic; no real client/staff/business info.
- [ ] Seed is reproducible and used by integration/e2e tests.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build the one-command local environment and synthetic-tenant seeding**
  Make 'clone and run' produce a full, synthetic, demo-able stack.
  - One command brings up containerised Postgres + API + web and seeds a synthetic tenant (builds on DB's local Postgres).
  - Reproducible: same command, same data; safe to reset.
  - All data clearly synthetic — invented names/contacts/business details — honouring the no-real-data rule absolutely.
- [ ] **Seed the compliance-relevant edge cases (roles/credentials, under-18, S4/non-S4, lots)**
  Make the seed exercise the guardrails, not just happy paths.
  - Staff with roles + credentials so RBAC/scope has data; clients including an under-18 so cooling-off + payment-block (C6) are testable.
  - Services/products flagged S4 (Schedule 4 prescription-only medicine) and non-S4 so rewards/public-naming classification (ADR-0014) has data; stock lots for custody/expiry/recall flows.
  - Coverage chosen so demos and dev can hit the real compliance blocks (ADR-0008).
- [ ] **Make the seed reusable by tests and document it**
  Share the fixture with the test suites and write the how-to.
  - The integration/e2e tests (TEST) build on the same seed so tests and local dev stay in sync.
  - Document the command, the seeded entities and the synthetic-only rule for anyone adding to the seed.
