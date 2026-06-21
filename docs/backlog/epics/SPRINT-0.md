# SPRINT-0 — Engineering foundations & setup

> **Stage / Milestone:** M0 · Sprint 0 — Foundations & setup  ·  **Phase:** 0  ·  **Stories:** 28

Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index. Nothing here ships clinical value on its own — it makes M1+ possible and safe.

**Source PRD:** `docs/prds/PRD-01-foundations-tenancy.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `REPO` | [Monorepo & solution scaffolding](../stories/SPRINT-0__REPO.md) | Chore | P0 | 3 | 4 |
| `CICD` | [CI/CD pipelines (build, test, deploy)](../stories/SPRINT-0__CICD.md) | Chore | P0 | 3 | 4 |
| `IAC` | [Cloud environments & infrastructure-as-code (AU East)](../stories/SPRINT-0__IAC.md) | Chore | P0 | 3 | 4 |
| `DB` | [Postgres + EF Core baseline & migrations](../stories/SPRINT-0__DB.md) | Chore | P0 | 3 | 4 |
| `RLS` | [Row-level-security multi-tenancy baseline](../stories/SPRINT-0__RLS.md) | Chore | P0 | 3 | 4 |
| `AUTH-STAFF` | [Staff identity: Entra ID SSO + MFA wiring](../stories/SPRINT-0__AUTH-STAFF.md) | Chore | P0 | 3 | 3 |
| `AUTH-CLIENT` | [Client identity: Entra External ID (social / email / OTP) wiring](../stories/SPRINT-0__AUTH-CLIENT.md) | Chore | P0 | 3 | 3 |
| `API` | [.NET API skeleton: architecture, tenant context, error model](../stories/SPRINT-0__API.md) | Chore | P0 | 3 | 3 |
| `AUDIT-INFRA` | [Append-only audit infrastructure baseline](../stories/SPRINT-0__AUDIT-INFRA.md) | Chore | P0 | 3 | 4 |
| `OPENAPI` | [OpenAPI contract + typed client generation](../stories/SPRINT-0__OPENAPI.md) | Chore | P1 | 3 | 3 |
| `WEB-SHELL` | [Angular web shell: routing, auth guard, layout](../stories/SPRINT-0__WEB-SHELL.md) | Chore | P1 | 3 | 3 |
| `DESIGN` | [Design system / shared component library + tokens](../stories/SPRINT-0__DESIGN.md) | Chore | P1 | 3 | 3 |
| `FLUTTER` | [Flutter app shells (client + provider) + shared packages](../stories/SPRINT-0__FLUTTER.md) | Chore | P1 | 3 | 3 |
| `SECRETS` | [Secrets & configuration management](../stories/SPRINT-0__SECRETS.md) | Chore | P1 | 3 | 4 |
| `OBS` | [Observability: logging, tracing, metrics, alerting](../stories/SPRINT-0__OBS.md) | Chore | P1 | 3 | 4 |
| `SEC-BASE` | [Security baseline: encryption, headers, dependency & secret scanning](../stories/SPRINT-0__SEC-BASE.md) | Chore | P0 | 3 | 4 |
| `TEST` | [Test strategy & harness + quality gates](../stories/SPRINT-0__TEST.md) | Chore | P1 | 3 | 3 |
| `SEED` | [Synthetic seed data & local dev environment](../stories/SPRINT-0__SEED.md) | Chore | P2 | 3 | 4 |
| `GOV` | [Repo governance: branch protection, PR & env protection](../stories/SPRINT-0__GOV.md) | Chore | P2 | 3 | 4 |
| `SPIKE-AUTH` | [Spike — Entra External ID ↔ Flutter ↔ .NET auth](../stories/SPRINT-0__SPIKE-AUTH.md) | Spike | P0 | 2 | 4 |
| `SPIKE-RLS` | [Spike — Postgres RLS with EF Core session context](../stories/SPRINT-0__SPIKE-RLS.md) | Spike | P0 | 2 | 4 |
| `SPIKE-SQUARE` | [Spike — Square AU card-on-file recurring autopay](../stories/SPRINT-0__SPIKE-SQUARE.md) | Spike | P1 | 2 | 4 |
| `SPIKE-CANVAS` | [Spike — Flutter injection-mapping canvas](../stories/SPRINT-0__SPIKE-CANVAS.md) | Spike | P1 | 2 | 4 |
| `SPIKE-OFFLINE` | [Spike — offline queue & sync integrity (provider app)](../stories/SPRINT-0__SPIKE-OFFLINE.md) | Spike | P1 | 2 | 4 |
| `JOBS-SCHEDULER` | [Background jobs & scheduler infrastructure](../stories/SPRINT-0__JOBS-SCHEDULER.md) | Chore | P0 | 3 | 4 |
| `MEDIA-STORAGE` | [Media storage & signed-URL service](../stories/SPRINT-0__MEDIA-STORAGE.md) | Chore | P1 | 3 | 4 |
| `DOMAIN-EVENTS` | [Domain-event / messaging backbone](../stories/SPRINT-0__DOMAIN-EVENTS.md) | Chore | P1 | 3 | 4 |
| `FEATURE-FLAGS` | [Feature flags & per-tenant configuration](../stories/SPRINT-0__FEATURE-FLAGS.md) | Chore | P2 | 3 | 3 |

_Totals: 28 stories · 103 tasks._
