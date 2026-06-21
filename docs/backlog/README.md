# Backlog — The Lounge Aesthetics Platform

> **Generated file.** Source of truth is `docs/backlog/data/*.json`. Regenerate with `python scripts/backlog.py render`. Seed GitHub with `python scripts/backlog.py all-repo`.

This backlog slices the 11 PRDs (+ a Sprint 0) into **epics** and **stories**. Every story carries context, a user story, acceptance criteria (its definition of done) and traceability back to `REQ-*` / `C*` / `ADR-*`.

## Delivery stages (milestones)

| # | Milestone | What lands |
|---|-----------|------------|
| M0 | Sprint 0 — Foundations & setup | Technical enablement before feature work: repos, CI/CD, environments (AU East), auth wiring, data + RLS baseline, API/web/app shells, design system, observability, security baseline, and the de-risk spikes. Phase 0. |
| M1 | Foundations & tenancy (PRD-01) | Multi-tenant domain core: tenancy/RLS, RBAC + scope-of-practice, audit, retention & destruction, breach workflow, privacy rights. Unblocks everything. |
| M2 | Booking, CRM, intake & consent (PRD-02, PRD-03) | Front-of-house + pre-visit: scope-aware calendar/booking, client 360, then digital intake, BDD screen, versioned e-consent, image-use consent, cooling-off and gating. |
| M3 | Consult, prescribing, S4 & charting (PRD-04, PRD-05) | The compliance moat + the clinical record: synchronous consult, individual Rx, S4 medicines governance, injection mapping, photos, immutable notes, adverse events. |
| M4 | Commerce, comms & integrations (PRD-06, PRD-07, PRD-10) | In-person POS, memberships/autopay, non-S4 rewards; reminders/aftercare/recall; Xero + calendar sync. |
| M5 | Reporting & apps (PRD-08, PRD-09) | Business + compliance dashboards and exports; the Flutter client & provider apps. |
| M6 | Facility & complaints (PRD-11) | Facility accreditation, infection-control logs, emergency kit, complaints register (lightweight in v1). |
| M7 | Phase 2+ (later / placeholders) | Deliberately deferred capability — tracked as placeholders so scope is visible and can be pulled forward. |

**13 epics · 118 stories.**

## Labels

Type: `type:epic` `type:story` `type:spike` `type:chore` · Phase: `phase:0` `phase:1` `phase:2plus` · Area: `area:backend` `area:web` `area:client-app` `area:provider-app` `area:infra` `area:data` `area:design` `area:integration` · Priority: `priority:P0/P1/P2` · plus `compliance` and a per-epic key label.

---

## SPRINT-0 — Sprint 0 — Foundations & setup
*M0 · Sprint 0 — Foundations & setup · Phase 0 · 24 stories*

Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index. Nothing here ships clinical value on its own — it makes M1+ possible and safe.

### REPO — Monorepo & solution scaffolding
`P0` · type:chore, SPRINT-0, phase:0, area:infra

A single, well-structured repo (or workspace) for the .NET API, Angular web, two Flutter apps and shared packages keeps versioning, CI and code-sharing sane from day one.

> **As a developer**, I want a scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together, so that everyone builds against one consistent structure and shared code has an obvious home.

**Acceptance criteria**

- [ ] Repo layout documented in a top-level README (api/, web/, apps/, packages/, infra/, scripts/).
- [ ] .NET solution builds; Angular workspace serves; both Flutter app shells run on a simulator.
- [ ] Shared design-system and API-client packages exist as empty-but-buildable libraries.
- [ ] Editorconfig, formatter and linter configs committed and enforced locally.

**ADR:** ADR-0005, ADR-0006

### CICD — CI/CD pipelines (build, test, deploy)
`P0` · type:chore, SPRINT-0, phase:0, area:infra

Continuous build/test on every PR and automated deploys to environments prevent integration drift and make the compliance posture (tests, scans) enforceable.

> **As a developer**, I want pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge, so that broken code is caught early and releases are repeatable.

**Acceptance criteria**

- [ ] PR pipeline runs build + unit/integration tests for API, web and apps and blocks merge on failure.
- [ ] Merge to main deploys API + web to the dev environment automatically.
- [ ] Mobile app builds produce installable artifacts for internal distribution.
- [ ] Pipeline status is required for merge (branch protection ties in via S0-GOV).

**Depends on:** SPRINT-0/REPO

### IAC — Cloud environments & infrastructure-as-code (AU East)
`P0` · type:chore, SPRINT-0, phase:0, area:infra, compliance

All PII/PHI must resolve to Australia East (C21/ADR-0016). Defining dev/staging/prod as code makes residency, isolation and reproducibility provable.

> **As a platform engineer**, I want dev, staging and prod environments provisioned via IaC, all pinned to Australia East, so that data residency is guaranteed and environments are reproducible.

**Acceptance criteria**

- [ ] IaC provisions compute, Postgres, blob storage and networking in Australia East for each environment.
- [ ] A non-AU region for any PII/PHI resource fails the IaC policy check.
- [ ] Environments are isolated (separate data stores, secrets, identities).
- [ ] Tear-down/re-create of a non-prod environment is a single command.

**Compliance:** C21 · **ADR:** ADR-0001, ADR-0016

### DB — Postgres + EF Core baseline & migrations
`P0` · type:chore, SPRINT-0, phase:0, area:data

A migrations-first data layer with a base entity convention (tenant_id, audit columns) underpins every module.

> **As a backend developer**, I want a Postgres database with EF Core, a migration pipeline and base entity/columns conventions, so that every module adds schema consistently and migrations run automatically per environment.

**Acceptance criteria**

- [ ] EF Core connects to Postgres; migrations apply automatically on deploy.
- [ ] Base entity convention includes tenant_id and created/updated audit columns.
- [ ] A sample entity round-trips through repository + migration in tests.
- [ ] Local dev uses a containerised Postgres seeded by S0-SEED.

**ADR:** ADR-0002

**Depends on:** SPRINT-0/IAC

### RLS — Row-level-security multi-tenancy baseline
`P0` · type:chore, SPRINT-0, phase:0, area:data, compliance

Tenant isolation is enforced in the database via RLS, with the API setting tenant context per request (ADR-0003). This is the single most important safety property of the data layer.

> **As a platform engineer**, I want Postgres RLS policies keyed on tenant_id, with EF Core setting the session tenant context on every request, so that a query can never return another tenant's rows, even on a developer mistake.

**Acceptance criteria**

- [ ] RLS policies are applied to all tenant-scoped tables.
- [ ] API middleware sets the session tenant from the authenticated principal on every request.
- [ ] An integration test proves Tenant A cannot read Tenant B rows and a cross-tenant id returns not-found.
- [ ] Bypassing tenant context (e.g. background jobs) uses an explicit, audited elevated path.

**ADR:** ADR-0003 · **PRD AC:** PRD-01 AC2

**Depends on:** SPRINT-0/DB, SPRINT-0/SPIKE-RLS

### AUTH-STAFF — Staff identity: Entra ID SSO + MFA wiring
`P0` · type:chore, SPRINT-0, phase:0, area:backend

Staff sign in with the clinic's existing Microsoft 365 accounts via Entra ID with MFA (ADR-0004). This is the plumbing; the RBAC/scope rules are PRD-01.

> **As a staff member**, I want to sign in to the web and provider app with my Microsoft 365 account and MFA, so that I use one secure corporate identity and no extra password.

**Acceptance criteria**

- [ ] Entra ID app registration configured; web + provider app complete SSO + MFA.
- [ ] Tokens carry the tenant and a stable user id usable by the API.
- [ ] Sign-out and token refresh work across web and app.
- [ ] Sessions are scoped to a single tenant.

**ADR:** ADR-0004 · **PRD AC:** PRD-01 AC3

**Depends on:** SPRINT-0/SPIKE-AUTH

### AUTH-CLIENT — Client identity: Entra External ID (social / email / OTP) wiring
`P0` · type:chore, SPRINT-0, phase:0, area:backend

Clients create accounts with Google/Apple, email+password, or email/SMS OTP via Entra External ID (CIAM).

> **As a client**, I want to create an account and sign in with social login, email+password, or a one-time code, so that I can access booking, intake and my records easily and securely.

**Acceptance criteria**

- [ ] Entra External ID configured for social, local (email+password) and OTP flows.
- [ ] Client app and public web complete each of the three sign-in methods.
- [ ] Client identities are tenant-scoped and distinct from staff identities.
- [ ] Account recovery (password reset / OTP resend) works.

**ADR:** ADR-0004 · **PRD AC:** PRD-01 AC3

**Depends on:** SPRINT-0/SPIKE-AUTH

### API — .NET API skeleton: architecture, tenant context, error model
`P0` · type:chore, SPRINT-0, phase:0, area:backend

A consistent API skeleton (clean/layered architecture, request pipeline, problem-details errors, pagination) means every feature module plugs in the same way.

> **As a backend developer**, I want an API skeleton with auth middleware, tenant-context resolution, a standard error/response model and health checks, so that feature modules are added consistently and cross-cutting concerns are solved once.

**Acceptance criteria**

- [ ] Auth middleware validates Entra tokens (staff + client) and resolves tenant context for RLS.
- [ ] Standard problem-details error responses and consistent pagination/filtering conventions.
- [ ] Health/readiness endpoints and structured request logging in place.
- [ ] A vertical-slice sample endpoint demonstrates the full pattern end-to-end.

**ADR:** ADR-0005

**Depends on:** SPRINT-0/RLS, SPRINT-0/AUTH-STAFF

### AUDIT-INFRA — Append-only audit infrastructure baseline
`P0` · type:chore, SPRINT-0, phase:0, area:data, compliance

C10/ADR-0010 require an immutable record of who read/changed clinical, medicines and PII data. Building the append-only AuditEvent plumbing now lets every later module just emit events.

> **As a platform engineer**, I want an append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes, so that auditability is a built-in default rather than a per-feature afterthought.

**Acceptance criteria**

- [ ] AuditEvent table is append-only (no update/delete path) and carries who/what/when/tenant.
- [ ] A reusable interceptor/helper records create/update/read for annotated entities or endpoints.
- [ ] Events are queryable and exportable (full register UI is PRD-01/PRD-08).
- [ ] Tampering attempts (update/delete) are rejected at the data layer.

**Compliance:** C10 · **ADR:** ADR-0010

**Depends on:** SPRINT-0/DB

### OPENAPI — OpenAPI contract + typed client generation
`P1` · type:chore, SPRINT-0, phase:0, area:backend

Generating typed clients for Angular and Flutter from the API's OpenAPI spec keeps the three surfaces in lock-step and removes hand-written DTO drift (ADR-0006).

> **As a developer**, I want the API to publish an OpenAPI document and CI to generate typed clients for web and Flutter, so that front-ends always match the API contract.

**Acceptance criteria**

- [ ] API serves a versioned OpenAPI document.
- [ ] Typed clients are generated for Angular and Flutter and published to the shared packages.
- [ ] Client generation runs in CI and fails on a breaking contract change without a version bump.
- [ ] The sample endpoint is consumed via the generated client in both web and app.

**ADR:** ADR-0006

**Depends on:** SPRINT-0/API

### WEB-SHELL — Angular web shell: routing, auth guard, layout
`P1` · type:chore, SPRINT-0, phase:0, area:web

The admin/front-desk web app needs a shell — auth guard, role-aware nav, layout — before feature screens land.

> **As a front-end developer**, I want an Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied, so that feature screens drop into a consistent, authenticated layout.

**Acceptance criteria**

- [ ] Unauthenticated users are redirected to Entra sign-in; authenticated users land on a shell.
- [ ] Navigation is driven by capabilities/role (placeholder until PRD-01 RBAC lands).
- [ ] Design-system theme + tokens applied globally.
- [ ] A sample feature route renders inside the shell using the generated API client.

**ADR:** ADR-0005

**Depends on:** SPRINT-0/AUTH-STAFF, SPRINT-0/DESIGN

### DESIGN — Design system / shared component library + tokens
`P1` · type:chore, SPRINT-0, phase:0, area:design

One design system (tokens, components) shared across web and the two Flutter apps delivers the 'fast and modern, thumb-first' UX the docs demand and avoids re-styling per surface.

> **As a designer/developer**, I want a shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables), so that all surfaces look consistent and the compliance UX patterns are reusable.

**Acceptance criteria**

- [ ] Tokens (colour, type, spacing) defined once and consumed by web + Flutter.
- [ ] Core components include the cross-cutting patterns from UX §4 (blocked-action banner, consent/age chips, S4 guardrail tag, offline indicator).
- [ ] Components are documented in a simple gallery/storybook.
- [ ] Accessibility basics (contrast, focus, hit-target size) verified for core components.

**ADR:** ADR-0006

### FLUTTER — Flutter app shells (client + provider) + shared packages
`P1` · type:chore, SPRINT-0, phase:0, area:client-app, area:provider-app

One Flutter codebase, two flavours (client, provider), sharing auth, the API client and the design system (ADR-0006).

> **As a mobile developer**, I want client and provider app shells with bottom-tab navigation, shared auth/API/design packages and secure token storage, so that the two apps are built from one codebase with consistent plumbing.

**Acceptance criteria**

- [ ] Client app shell has the Home/Book/My care/Membership/Account tabs; provider app shell has Schedule/Patient/Medicines/Tasks tabs (empty screens).
- [ ] Both apps sign in (client = External ID, provider = Entra) and call the sample endpoint.
- [ ] Auth tokens stored in secure storage; design-system theme applied.
- [ ] Builds are produced by CI for internal distribution.

**ADR:** ADR-0004, ADR-0006

**Depends on:** SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT, SPRINT-0/DESIGN

### SECRETS — Secrets & configuration management
`P1` · type:chore, SPRINT-0, phase:0, area:infra

Connection strings, provider keys (Square, SMS, Xero) and signing secrets must live in a managed vault, never in code or config files.

> **As a platform engineer**, I want a managed secret store (Key Vault) wired into each environment and a typed config story for the API and apps, so that no secret is ever committed and rotation is possible.

**Acceptance criteria**

- [ ] API and pipelines read secrets from the vault per environment; none in source control.
- [ ] A secret-scanning check fails the build on a committed secret.
- [ ] Config is environment-specific and typed; missing required config fails fast at startup.
- [ ] Rotating a secret requires no code change.

**Depends on:** SPRINT-0/IAC

### OBS — Observability: logging, tracing, metrics, alerting
`P1` · type:chore, SPRINT-0, phase:0, area:infra

You cannot run a compliance-critical platform blind. Centralised logs, distributed traces, metrics and alerting are needed from the first deploy.

> **As a platform engineer**, I want structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps, so that we can diagnose issues and detect incidents (feeding the breach workflow) quickly.

**Acceptance criteria**

- [ ] Structured logs and traces flow to a central store with correlation ids across web/app/API.
- [ ] Dashboards cover request rate, latency, errors and key resource health.
- [ ] Alerts fire for error-rate and availability thresholds.
- [ ] Audit/security-relevant signals are distinguishable to feed the breach workflow (PRD-01).

**Depends on:** SPRINT-0/API

### SEC-BASE — Security baseline: encryption, headers, dependency & secret scanning
`P0` · type:chore, SPRINT-0, phase:0, area:infra, compliance

Encryption in transit + at rest, least-privilege, secure headers and automated scanning establish the security posture the compliance docs assume (C10/C21).

> **As a security-minded engineer**, I want TLS everywhere, encryption at rest, hardened HTTP headers, least-privilege identities and dependency/secret/code scanning in CI, so that the platform meets its baseline security obligations from day one.

**Acceptance criteria**

- [ ] All traffic is TLS; data stores are encrypted at rest.
- [ ] Security headers (CSP, HSTS, etc.) applied to web; CORS locked down.
- [ ] Dependency, secret and SAST scans run in CI and gate merges on high-severity findings.
- [ ] Service identities follow least-privilege; no shared admin credentials.

**Compliance:** C10, C21 · **ADR:** ADR-0016

**Depends on:** SPRINT-0/CICD

### TEST — Test strategy & harness + quality gates
`P1` · type:chore, SPRINT-0, phase:0, area:backend

A clinical platform needs a serious automated-test culture: unit, integration (incl. RLS/auth/audit invariants) and end-to-end, with coverage gates.

> **As a developer**, I want test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI, so that compliance invariants are protected by tests and regressions are caught automatically.

**Acceptance criteria**

- [ ] Unit + integration test projects exist for the API (integration tests run against a real Postgres with RLS).
- [ ] Web and app unit/widget test setups in place; an e2e smoke test covers sign-in + the sample flow.
- [ ] Coverage threshold enforced in CI.
- [ ] A documented convention for writing 'compliance invariant' tests (gate must block) exists.

**Depends on:** SPRINT-0/CICD, SPRINT-0/RLS

### SEED — Synthetic seed data & local dev environment
`P2` · type:chore, SPRINT-0, phase:0, area:data

Realistic synthetic data (clinic, staff with credentials, clients, services incl. S4/non-S4, stock) lets every module be developed and demoed without real PII. All data must stay synthetic (project rule).

> **As a developer**, I want a one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock, so that I can run and demo any module locally without touching real data.

**Acceptance criteria**

- [ ] A script spins up Postgres + API + web locally and seeds a synthetic tenant.
- [ ] Seed covers staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots.
- [ ] All seed data is clearly synthetic; no real client/staff/business info.
- [ ] Seed is reproducible and used by integration/e2e tests.

**Depends on:** SPRINT-0/DB

### GOV — Repo governance: branch protection, PR & env protection
`P2` · type:chore, SPRINT-0, phase:0, area:infra

Branch protection, required checks, PR templates and environment protection rules keep the main branch deployable and reviewable.

> **As a maintainer**, I want protected main with required status checks and reviews, PR/issue templates, and protected prod deployments, so that quality gates can't be bypassed and changes are traceable.

**Acceptance criteria**

- [ ] main requires passing checks + at least one review before merge.
- [ ] PR and issue templates committed (PR template references the backlog item).
- [ ] Production deploys require an approval gate.
- [ ] CODEOWNERS routes reviews for sensitive areas (auth, medicines, compliance).

**Depends on:** SPRINT-0/CICD

### SPIKE-AUTH — Spike — Entra External ID ↔ Flutter ↔ .NET auth
`P0` · type:spike, spike, SPRINT-0, phase:0, area:backend

End-to-end auth across Entra (staff), Entra External ID (clients), Flutter and .NET is novel enough to de-risk before committing the auth wiring stories.

> **As a engineer**, I want a time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls, so that the auth wiring stories proceed on a proven approach.

**Acceptance criteria**

- [ ] A throwaway prototype completes Entra (staff) and External ID (client) sign-in from Flutter and web.
- [ ] An authorised call reaches a .NET endpoint with tenant + role claims usable for RLS/RBAC.
- [ ] Findings, library choices and gotchas written up; risks/decisions captured (ADR if needed).
- [ ] Outcome explicitly feeds AUTH-STAFF / AUTH-CLIENT.

**ADR:** ADR-0004

### SPIKE-RLS — Spike — Postgres RLS with EF Core session context
`P0` · type:spike, spike, SPRINT-0, phase:0, area:data

Setting the per-request tenant for RLS through EF Core's connection/session lifecycle has known sharp edges (pooling, background jobs). Prove it before building on it.

> **As a engineer**, I want a spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async, so that the RLS baseline is built on a verified pattern.

**Acceptance criteria**

- [ ] Prototype shows RLS isolation holds across pooled connections and async requests.
- [ ] A safe elevated/bypass path for background jobs is demonstrated and audited.
- [ ] Performance impact measured and acceptable.
- [ ] Pattern documented and feeds SPRINT-0/RLS.

**ADR:** ADR-0002, ADR-0003

### SPIKE-SQUARE — Spike — Square AU card-on-file recurring autopay
`P1` · type:spike, spike, SPRINT-0, phase:0, area:integration

Membership autopay depends on Square AU supporting tokenised card-on-file recurring charges with dunning — flagged 🔬 in the docs. De-risk before committing PRD-06 memberships.

> **As a engineer**, I want a spike confirming Square AU can tokenise a card and run recurring charges with failure/dunning handling, so that the membership autopay design is viable (or an alternative is chosen early).

**Acceptance criteria**

- [ ] Prototype tokenises a test card and runs a scheduled recurring charge in Square AU sandbox.
- [ ] Failed-charge / retry behaviour observed; dunning approach outlined.
- [ ] PCI posture confirmed: no PAN stored, only provider tokens (ADR-0007).
- [ ] Go/no-go + findings recorded; feeds PRD-06 memberships.

**ADR:** ADR-0007

### SPIKE-CANVAS — Spike — Flutter injection-mapping canvas
`P1` · type:spike, spike, SPRINT-0, phase:0, area:provider-app

The injection-mapping canvas is the hero clinical screen and the highest app risk (tap-to-add + drag points on a facial diagram/photo, per-point metadata). Prove the approach before PRD-05.

> **As a mobile engineer**, I want a spike of the Flutter canvas: tap-to-add and drag injection points over a facial diagram and a photo, each holding metadata, so that PRD-05 charting builds on a proven, performant canvas.

**Acceptance criteria**

- [ ] Prototype supports tap-to-add, drag-to-move and per-point metadata over both a diagram and an image.
- [ ] Performs smoothly on a mid-range device with many points.
- [ ] Coordinate model survives image scaling/rotation and is persistable.
- [ ] Approach documented; feeds PRD-05 mapping stories.

**ADR:** ADR-0006

### SPIKE-OFFLINE — Spike — offline queue & sync integrity (provider app)
`P1` · type:spike, spike, SPRINT-0, phase:0, area:provider-app

Treatment rooms drop Wi-Fi; the provider app must queue notes/photos encrypted and sync without loss, with server-side finalisation (ADR-0015/0010). De-risk before PRD-05/09.

> **As a mobile engineer**, I want a spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts, so that the offline-tolerant charting design is viable.

**Acceptance criteria**

- [ ] Prototype queues drafts + a photo offline (encrypted) and syncs cleanly on reconnect with no loss.
- [ ] Conflict handling (last-write-wins for drafts) demonstrated; finalisation is server-side.
- [ ] Photos never persist on device beyond a transient sync cache (C14/ADR-0009).
- [ ] Approach documented; feeds PRD-05 / PRD-09.

**Compliance:** C14 · **ADR:** ADR-0009, ADR-0010, ADR-0015

---

## PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)
*M1 · Foundations & tenancy (PRD-01) · Phase 0 · 12 stories*

The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights. Everything else builds on this.

### TENANT — Tenant provisioning & staff invitation
`P0` · type:story, PRD-01, phase:0, area:backend

An owner provisions their clinic (tenant) and invites staff to sign in with existing Microsoft 365 accounts.

> **As a owner**, I want to provision my clinic and invite staff who then sign in with our Microsoft 365 accounts, so that my team can access the platform under one isolated tenant.

**Acceptance criteria**

- [ ] Provisioning creates a tenant with locations and an owner account.
- [ ] Invited staff complete Entra SSO and are bound to the tenant.
- [ ] All records created carry tenant_id and are RLS-isolated.
- [ ] Re-inviting / deactivating a staff member is supported and audited.

**REQ:** REQ-TEN-1, REQ-TEN-2 · **ADR:** ADR-0003, ADR-0004 · **PRD AC:** AC2, AC3

### RBAC — RBAC + scope-of-practice matrix enforcement
`P0` · type:story, PRD-01, phase:1, area:backend, compliance

Roles map to the §3 scope matrix; the auth pipeline blocks actions outside a user's scope. Capabilities gate API actions, concerns drive role-tailored dashboards (ADR-0017).

> **As a owner**, I want roles mapped to capabilities so the system blocks any action outside a user's scope of practice, so that people can only do what they're trained and legally allowed to do.

**Acceptance criteria**

- [ ] Capabilities × concerns model implemented; each API action checks a capability.
- [ ] The persona set (NP, Lead RN, RN, dermal, reception, owner-business) maps to the matrix.
- [ ] An out-of-scope action is blocked with a clear reason and an audit event.
- [ ] Owner-business is read-only for clinical/stock unless they hold the credential.

**REQ:** REQ-TEN-3, REQ-TEN-4 · **Compliance:** C4, C19 · **ADR:** ADR-0017 · **PRD AC:** AC1

**Depends on:** PRD-01/TENANT

### CREDENTIALS — Staff credentials + canInject compliance gate
`P0` · type:story, PRD-01, phase:1, area:backend, compliance

Staff profiles hold AHPRA reg #, type, status/expiry, conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII; these derive a single canInject gate. Must accept the new designated RN prescriber role.

> **As a owner**, I want structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject, so that only registered, insured, in-scope staff can be booked and can treat.

**Acceptance criteria**

- [ ] Profiles capture AHPRA reg/type/status/expiry/conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII.
- [ ] A practitioner whose PII excludes cosmetic, or whose registration has lapsed, is flagged not-cleared.
- [ ] The designated RN prescriber role is supported (endorsement + recorded partnered prescriber).
- [ ] canInject is a single derived signal consumed by booking (PRD-02) and treatment gates.

**REQ:** REQ-TEN-6, REQ-TEN-7, REQ-TEN-8, REQ-TEN-9 · **Compliance:** C4, C19 · **ADR:** ADR-0028, ADR-0029 · **PRD AC:** AC1

**Depends on:** PRD-01/RBAC

### REG-WATCH — Registration / PII / CPD expiry alerting
`P1` · type:story, PRD-01, phase:1, area:backend, compliance

Staff must be alerted before registration, insurance or CPD lapses so the clinic is never unknowingly non-compliant.

> **As a owner**, I want to be alerted before a practitioner's registration, cosmetic insurance or CPD lapses, so that we never treat with an unregistered or uninsured practitioner.

**Acceptance criteria**

- [ ] Items within N days of expiry surface on an alert/watchlist (also feeds PRD-08).
- [ ] On lapse, the practitioner's canInject flips to not-cleared automatically.
- [ ] Alerts are role-targeted and dismiss/acknowledge is audited.
- [ ] AHPRA register auto-verification (PIE) is supported with a first-class manual-verify fallback.

**REQ:** REQ-TEN-7 · **Compliance:** C19 · **ADR:** ADR-0029 · **PRD AC:** AC1

**Depends on:** PRD-01/CREDENTIALS

### ROSTER — Rosters & engagement type
`P1` · type:story, PRD-01, phase:1, area:backend

A roster (plus employee/contractor engagement type) drives booking availability and feeds commission/pay attribution downstream.

> **As a manager**, I want to record staff rosters/time-off and each person's engagement type, so that booking availability reflects who is actually working and cleared.

**Acceptance criteria**

- [ ] Rosters and time-off are recorded per staff member and location.
- [ ] Booking availability is derived from roster ∩ canInject (consumed by PRD-02).
- [ ] Engagement type (employee/contractor) is recorded per staff member.
- [ ] Roster changes are audited.

**REQ:** REQ-TEN-8, REQ-TEN-9 · **ADR:** ADR-0028, ADR-0029

**Depends on:** PRD-01/CREDENTIALS

### AUDIT — Exportable audit trail for clinical / medicines / PII
`P0` · type:story, PRD-01, phase:1, area:data, compliance

Every read/write of clinical, medicines and PII data must produce an immutable AuditEvent that a compliance officer can export (C10/ADR-0010). Built on the Sprint 0 audit infra.

> **As a compliance officer**, I want to export an audit trail of who viewed or changed clinical, medicines and PII data, so that we can evidence access and changes in an inspection.

**Acceptance criteria**

- [ ] Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
- [ ] The log cannot be edited or deleted.
- [ ] A compliance officer can filter and export the trail.
- [ ] Sensitive-data reads (not just writes) are captured.

**REQ:** REQ-SEC-3 · **Compliance:** C10 · **ADR:** ADR-0010 · **PRD AC:** AC4

**Depends on:** PRD-01/TENANT

### RETENTION — Retention policy engine & destruction register
`P1` · type:story, PRD-01, phase:1, area:backend, compliance

Records must be retained per legal periods (adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation) and destroyed with a register + certificate (C18).

> **As a admin**, I want retention timers and a destruction register that surfaces records due for destruction and logs their destruction, so that we keep records exactly as long as the law requires, no more, no less.

**Acceptance criteria**

- [ ] Retention rules: adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation.
- [ ] Records past retention surface for destruction with their retention basis.
- [ ] Destroying a record writes a destruction-register entry (patient, period, date) + certificate reference.
- [ ] A transfer log records records handed to another provider.

**REQ:** REQ-SEC-4 · **Compliance:** C18 · **PRD AC:** AC5

**Depends on:** PRD-01/AUDIT

### BREACH — Data-breach assessment & notification workflow
`P1` · type:story, PRD-01, phase:1, area:backend, compliance

An eligible data breach (NDB scheme) must be assessed and, if eligible, notified to OAIC + individuals, with a breach register (C22).

> **As a admin**, I want a workflow that, when a breach is flagged, guides assessment and produces OAIC + individual notifications and a register entry, so that we meet Notifiable Data Breaches obligations.

**Acceptance criteria**

- [ ] Flagging a breach starts an assessment workflow.
- [ ] If assessed eligible, it produces OAIC + individual notification drafts.
- [ ] A breach-register entry is created and retained.
- [ ] Observability/security signals (Sprint 0 OBS) can seed a breach case.

**REQ:** REQ-SEC-7 · **Compliance:** C22 · **PRD AC:** AC7

**Depends on:** PRD-01/AUDIT

### PRIVACY-RIGHTS — Client privacy: collection notice, access & correction (DSAR)
`P1` · type:story, PRD-01, phase:1, area:backend, compliance

Clients have APP 12/13 rights: a collection notice/consent at sign-up, and the ability to access and request correction of their own data (DSAR clock ≤30 days).

> **As a client**, I want to see a clear collection notice, access a copy of my data and request a correction, so that my privacy rights under the Privacy Act are respected.

**Acceptance criteria**

- [ ] Collection notice + consent shown and recorded at sign-up.
- [ ] A client can view/export their own personal/health data.
- [ ] A correction request is tracked to resolution against the DSAR clock.
- [ ] All access/correction actions are audited.

**REQ:** REQ-SEC-5, REQ-SEC-8, REQ-SEC-9 · **Compliance:** C21 · **PRD AC:** AC6

**Depends on:** PRD-01/TENANT

### RESIDENCY — Data residency & sub-processor controls
`P1` · type:story, PRD-01, phase:1, area:infra, compliance

All PII/PHI storage + compute must resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 assessment + consent exists (C21/ADR-0016).

> **As a compliance officer**, I want assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment, so that we meet residency and cross-border obligations.

**Acceptance criteria**

- [ ] All PII/PHI resources resolve to Australia East (verified, ties to Sprint 0 IAC policy).
- [ ] An integration to a non-AU sub-processor is blocked unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are documented in a register.
- [ ] Signed-URL media access enforces the same residency.

**REQ:** REQ-SEC-1, REQ-SEC-2, REQ-SEC-6 · **Compliance:** C21 · **ADR:** ADR-0016 · **PRD AC:** AC8

**Depends on:** SPRINT-0/IAC

### CLIENT-CORE — Client core record: DOB & under-18 flag
`P1` · type:story, PRD-01, phase:1, area:backend

The client record captures DOB and derives an under-18 flag that feeds cooling-off (C6) and advertising/pricing (C9) elsewhere.

> **As a system**, I want to capture client DOB and derive an under-18 flag, so that downstream cooling-off and pricing rules can enforce age-based requirements.

**Acceptance criteria**

- [ ] DOB captured; under-18 flag derived and exposed to PRD-03/PRD-06/PRD-07.
- [ ] The flag updates correctly across a birthday.
- [ ] Soft-delete with audit and duplicate handling supported (full CRM in PRD-02).
- [ ] Under-18 status is visible on the patient header (consumed by UX age chip).

**REQ:** REQ-CLI-3 · **Compliance:** C6

**Depends on:** PRD-01/TENANT

### ROLE-BUILDER — Custom-role builder (placeholder)
`P2` · type:story, PRD-01, phase:2plus, area:backend

Beyond the preset personas, a future custom-role builder lets owners define bespoke capability sets. Deferred — placeholder.

> **As a owner**, I want to define custom roles from capabilities, so that I can model staff arrangements that don't fit the presets.

**Acceptance criteria**

- [ ] Placeholder — design only in v1; presets are sufficient for launch.
- [ ] Captured so the capability model stays builder-ready.

**REQ:** REQ-TEN-5 · **ADR:** ADR-0017

---

## PRD-02 — Booking & scheduling (+ client/CRM basics)
*M2 · Booking, CRM, intake & consent (PRD-02, PRD-03) · Phase 1 · 10 stories*

The calendar that runs the front desk and the 360° client record everything hangs off. Bookings are scope-aware (only cleared RN/NP can be booked for injectables) and an injectable booking is gated so it can't proceed to charting without a consult. Includes online self-booking, the visit lifecycle, reminders/reschedule/cancel, waitlist, walk-ins, resources and the client directory.

### CALENDAR — Multi-resource calendar (practitioner + room)
`P0` · type:story, PRD-02, phase:1, area:web

Front desk needs a fast day/week/room calendar with service durations, buffers and rosters — the core of the diary.

> **As a front desk**, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.

**Acceptance criteria**

- [ ] Resources = practitioner + room; service durations include buffer/processing/turnaround.
- [ ] Day, week and room views render; rosters and time-off block availability.
- [ ] Drag to move an appointment; conflicts on room/chair/device are flagged.
- [ ] Per-day and per-treatment-type counts + utilisation surfaced.

**REQ:** REQ-BOOK-1 · **ADR:** ADR-0024, ADR-0026

**Depends on:** PRD-01/ROSTER

### ONLINE-BOOK — Online self-booking (scope-aware)
`P0` · type:story, PRD-02, phase:1, area:web, compliance

Clients self-book service → practitioner → slot online; injectable services only offer cleared RN/NP and the public page uses generic names (C4/C9).

> **As a client**, I want to book a consult/treatment online by choosing service, practitioner and time, so that I can book without calling the clinic.

**Acceptance criteria**

- [ ] Booking wizard: service → practitioner → time → client → confirm.
- [ ] Injectable services offer only cleared RN/NP (scope-aware, per C4); others never appear bookable for it.
- [ ] Public service names are generic and S4 prices withheld by configuration (C9, see PRD-07).
- [ ] Under-18 bookings are flagged for downstream cooling-off (feeds PRD-03).

**REQ:** REQ-BOOK-2 · **Compliance:** C4, C6, C9 · **PRD AC:** AC1, AC5

**Depends on:** PRD-02/CALENDAR, PRD-01/CREDENTIALS

### CONSULT-GATE — Consult gate on injectable appointments
`P0` · type:story, PRD-02, phase:1, area:backend, compliance

An injectable appointment cannot move to charting without a linked Consult — the booking-side half of the moat (REQ-BOOK-5).

> **As a system**, I want to block a checked-in injectable appointment from opening charting unless a consult is linked, so that no S4 treatment can proceed without the required consult.

**Acceptance criteria**

- [ ] A checked-in injectable appointment with no linked consult cannot open the charting screen.
- [ ] The blocked-action banner explains what's missing and who can resolve it.
- [ ] Once a consult is recorded the gate clears (handoff to PRD-04).
- [ ] The block is server-enforced, not just UI.

**REQ:** REQ-BOOK-5 · **Compliance:** C1 · **PRD AC:** AC2

**Depends on:** PRD-02/ONLINE-BOOK

### LIFECYCLE — Visit lifecycle & status state-machine
`P1` · type:story, PRD-02, phase:1, area:web

Bookings move through booked → reminded → checked-in → in-room → checked-out, with late/no-show flags and role hand-offs (REQ-BOOK-7).

> **As a front desk**, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.

**Acceptance criteria**

- [ ] Status state-machine with role hand-offs; check-in on arrival.
- [ ] An 'in-room now' indicator with quick links to chart/profile.
- [ ] Late and no-show flags; a no-show raises a follow-up call (feeds PRD-07 jobs).
- [ ] New-vs-returning, reason and roster captured on the booking.

**REQ:** REQ-BOOK-4, REQ-BOOK-7 · **ADR:** ADR-0024

**Depends on:** PRD-02/CALENDAR

### REMINDERS — Reminders & self-service reschedule/cancel
`P1` · type:story, PRD-02, phase:1, area:web

Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling.

> **As a client**, I want appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself, so that I don't need to call and the clinic's diary stays accurate.

**Acceptance criteria**

- [ ] Reminders fire per template (SMS/app/email); confirm/decline updates status.
- [ ] Self-reschedule/cancel within policy; outside policy the configured rule applies (no auto-charge in v1).
- [ ] Cancellation/no-show policy is configurable.
- [ ] Reminder channel is provided by PRD-07.

**REQ:** REQ-BOOK-3, REQ-BOOK-4 · **PRD AC:** AC3, AC6

**Depends on:** PRD-02/LIFECYCLE

### WAITLIST — Waitlist & cancellation backfill
`P1` · type:story, PRD-02, phase:1, area:web

Clients can join a waitlist; cancellations/no-shows auto-offer the freed slot to fill quiet windows.

> **As a front desk**, I want a waitlist that auto-offers a freed slot when an appointment cancels or no-shows, so that we keep the diary full.

**Acceptance criteria**

- [ ] Clients can be added to a waitlist for a service/window.
- [ ] Cancelling/no-showing a slot offers it to the waitlist.
- [ ] Quiet-window fill suggestions surface from utilisation data.
- [ ] Offered/accepted/expired waitlist states are tracked.

**REQ:** REQ-BOOK-4 · **ADR:** ADR-0026 · **PRD AC:** AC4

**Depends on:** PRD-02/REMINDERS

### WALKINS — Walk-ins, same-day add-ons & resources
`P2` · type:story, PRD-02, phase:1, area:web

Walk-ins and same-day add-ons are supported but gate-respecting (an injectable walk-in still needs a consult first); room/chair/device resources are scheduled with conflict-flagging.

> **As a front desk**, I want to add walk-ins and same-day add-ons against available rooms/chairs/devices, so that we capture opportunistic demand without breaking the rules or double-booking resources.

**Acceptance criteria**

- [ ] Walk-in and same-day add-on flows exist; an injectable walk-in still requires a consult first.
- [ ] Room/chair/device resources are bookable with conflict-flagging and utilisation.
- [ ] VIP / first-time appointment tags supported.
- [ ] Resource conflicts are surfaced before confirmation.

**REQ:** REQ-BOOK-3, REQ-BOOK-6 · **ADR:** ADR-0026

**Depends on:** PRD-02/CALENDAR

### CLIENT-360 — Client 360° profile
`P1` · type:story, PRD-02, phase:1, area:web

Any staff member can open a client's full profile: history, contacts, medical flags, consents, photos, memberships, balances, comms and complaints.

> **As a staff member**, I want a single 360° client profile pulling together history, medical flags, consents, photos, memberships, balances and comms, so that I have the full picture in one place.

**Acceptance criteria**

- [ ] Profile aggregates overview, medical/contraindications, consents, photos, visits, memberships, balance, comms, complaints.
- [ ] Consent/age chips render on the header (consent ✓ / image-use ✓ / under-18 cooling-off).
- [ ] Access is RBAC-scoped (reception sees limited clinical info) and audited.
- [ ] Surfaces data owned by PRD-03/04/05/06/11 via the API.

**REQ:** REQ-CLI-1, REQ-CLI-2 · **Compliance:** C10

**Depends on:** PRD-01/CLIENT-CORE

### CLIENT-DIR — Client directory: search, filter, merge, soft-delete
`P2` · type:story, PRD-02, phase:1, area:web

A searchable client directory with duplicate merge and audited soft-delete keeps the record clean.

> **As a front desk**, I want to search and filter clients, merge duplicates and soft-delete with audit, so that the client list stays accurate and findable.

**Acceptance criteria**

- [ ] Fast search/filter across the directory.
- [ ] Duplicate detection + merge that preserves history and audit.
- [ ] Soft-delete with audit; deleted clients excluded from active views.
- [ ] Quick client search is reachable from the front-desk shell.

**REQ:** REQ-CLI-1, REQ-CLI-2 · **Compliance:** C10

**Depends on:** PRD-02/CLIENT-360

### DEPOSITS — Booking deposits / card-on-file hold (placeholder)
`P2` · type:story, PRD-02, phase:2plus, area:backend

An opt-in, ACL-fair booking deposit / card-on-file hold, suppressed during cooling-off (F14 invariant). Deferred to Phase 2 — placeholder.

> **As a owner**, I want to optionally require a booking deposit or card-on-file hold, so that no-shows cost less.

**Acceptance criteria**

- [ ] Placeholder — not in v1 (no deposits/holds in v1).
- [ ] Design must keep the cooling-off suppression invariant (F14): no hold during a cooling-off period.

**REQ:** REQ-BOOK-3 · **ADR:** ADR-0036

---

## PRD-03 — Intake, consent & compliance gating
*M2 · Booking, CRM, intake & consent (PRD-02, PRD-03) · Phase 1 · 6 stories*

Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s. Treatment is blocked until required intake/consent is complete and current.

### INTAKE — Pre-visit intake forms
`P0` · type:story, PRD-03, phase:1, area:client-app, area:backend

Clients complete medical history, meds, allergies and contraindications on their phone before the visit; responses auto-link to the chart.

> **As a client**, I want to complete my medical history, medications, allergies and contraindications before my visit on my phone, so that my practitioner has what they need and my treatment is safe.

**Acceptance criteria**

- [ ] Configurable pre-visit forms capture history, meds, allergies/contraindications.
- [ ] Intake is sent on booking and completable in the client app/web.
- [ ] Responses auto-link to the client's chart.
- [ ] Incomplete required intake contributes to the treatment block.

**REQ:** REQ-CONS-2, REQ-CONS-3

**Depends on:** PRD-02/ONLINE-BOOK

### BDD — BDD / psychological screening instrument
`P0` · type:story, PRD-03, phase:1, area:backend, compliance

Cosmetic guidelines require BDD screening; a positive result must be surfaced to the prescriber before treatment (C3).

> **As a RN/NP**, I want a BDD/psychological screen completed and surfaced before I proceed, so that I can avoid harm for at-risk patients per the guidelines.

**Acceptance criteria**

- [ ] A validated BDD/psychological screening instrument is embedded in intake.
- [ ] A completed screen authored/reviewed by an RN/NP is present before treatment.
- [ ] A positive flag is surfaced to the prescriber and recorded.
- [ ] Which instrument is used is configurable (open question to confirm).

**REQ:** REQ-CONS-2 · **Compliance:** C3 · **PRD AC:** AC2

**Depends on:** PRD-03/INTAKE

### CONSENT — Versioned e-signed consent with mandated content
`P0` · type:story, PRD-03, phase:1, area:backend, compliance

Consent must be versioned, e-signed, plain-language and contain mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA) (C5).

> **As a client**, I want to read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it, so that I give genuinely informed consent.

**Acceptance criteria**

- [ ] Consent is versioned, e-signed and contains all mandated content.
- [ ] Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
- [ ] Changing a template creates a new version; previously signed consents stay bound to their version.
- [ ] Consent versions are retained per the retention policy (C18).

**REQ:** REQ-CONS-1 · **Compliance:** C5, C18 · **PRD AC:** AC1, AC6

**Depends on:** PRD-03/INTAKE

### IMAGE-CONSENT — Separate, withdrawable image-use consent
`P1` · type:story, PRD-03, phase:1, area:backend, compliance

Photo use requires its own scoped consent, withdrawable at any time, which immediately stops downstream use (C14).

> **As a client**, I want to give separate consent for photo use and withdraw it whenever I want, so that I control how my images are used.

**Acceptance criteria**

- [ ] Image-use consent is separate from treatment consent and scoped.
- [ ] Withdrawing it immediately stops further use and is audited.
- [ ] Downstream media features (PRD-05/09) check this consent.
- [ ] Granted/withdrawn state is visible on the patient header chip.

**REQ:** REQ-CONS-5 · **Compliance:** C14 · **PRD AC:** AC4

**Depends on:** PRD-03/CONSENT

### COOLING-OFF — Cooling-off & under-18 payment block
`P1` · type:story, PRD-03, phase:1, area:backend, compliance

Under-18s require ≥7 days between consent and procedure plus a payment block (except the consult) and a recorded second consultation; an optional adult cooling-off is configurable (C6).

> **As a system**, I want to enforce a 7-day cooling-off and payment block for under-18s and record a second consultation, so that minors are protected per the rules.

**Acceptance criteria**

- [ ] For under-18: ≥7 days enforced between consent and procedure; payment blocked except the consult until elapsed.
- [ ] A second-consultation offer is recorded.
- [ ] Optional adult cooling-off is configurable (default per legal read).
- [ ] Payment block coordinates with PRD-06.

**REQ:** REQ-CONS-4 · **Compliance:** C6 · **PRD AC:** AC3

**Depends on:** PRD-01/CLIENT-CORE, PRD-03/CONSENT

### GATING — Server-enforced treatment gating
`P0` · type:story, PRD-03, phase:1, area:backend, compliance

Treatment cannot start unless required intake + consent are complete and current — enforced server-side, surfaced via the blocked-action banner (ADR-0008).

> **As a RN/NP**, I want the system to block treatment until required intake and consent are complete and current, telling me exactly what's missing, so that the compliant path is the only path.

**Acceptance criteria**

- [ ] Treatment is blocked server-side unless required intake + current consent exist.
- [ ] The block states what's missing and how to resolve it (never a dead-end).
- [ ] The gate is the shared mechanism consumed by PRD-04/05.
- [ ] Gate decisions are audited.

**Compliance:** C5 · **ADR:** ADR-0008 · **PRD AC:** AC1

**Depends on:** PRD-03/CONSENT, PRD-03/BDD

---

## PRD-04 — Consult, prescribing & S4 medicines governance (the moat)
*M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05) · Phase 1 · 12 stories*

The defensible core. Every S4 administration is provably tied to a synchronous consult, an individual prescription, valid consent, and a batch/lot drawn from lawfully-supplied, ARTG-approved stock held under correct custody. QLD S4 + TGA rules implemented as enforced invariants, producing an audit-ready medicine register and a lot→clients recall lookup. Highest-risk module — build right after PRD-01, with a legal review of the requirements first.

### CONSULT — Synchronous consult record
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

A Consult (in-person or external-telehealth) records modality, prescriber, timestamp, external reference and notes — required before any script (C1).

> **As a prescriber**, I want to record a synchronous consult (in person or from our external telehealth app) before writing any script, so that every prescription is backed by a real assessment.

**Acceptance criteria**

- [ ] Consult records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes.
- [ ] A prescription cannot be saved without a linked synchronous consult at/just-before script time.
- [ ] The remote-prescriber path links the externally-conducted consult to the resulting script.
- [ ] Consult creation is audited.

**REQ:** REQ-RX-1, REQ-RX-4 · **Compliance:** C1 · **ADR:** ADR-0011 · **PRD AC:** AC1

**Depends on:** PRD-02/CONSULT-GATE, PRD-03/GATING

### PRESCRIPTION — Individual prescription (no batch / no async)
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

An individual prescription per client per consult — never batch/standing-order, never async (text/email/online-only) (C2). Supports the designated RN prescriber identity.

> **As a prescriber**, I want to write an individual prescription for this patient tied to their consult, so that prescribing is lawful and patient-specific.

**Acceptance criteria**

- [ ] One prescription per client per consult; applying one script to multiple clients is rejected.
- [ ] Standing-order/batch scripts and async-only prescribing are impossible to create.
- [ ] Prescriber may be NP, remote prescriber, or designated RN prescriber (with recorded partnered prescriber).
- [ ] Off-label is flagged on the script and requires consent covering off-label use.

**REQ:** REQ-RX-2, REQ-RX-5 · **Compliance:** C2, C5 · **PRD AC:** AC2, AC8

**Depends on:** PRD-04/CONSULT, PRD-01/CREDENTIALS

### PRODUCT-CATALOGUE — Medicines & product catalogue (S4 classification)
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

A typed, multi-unit catalogue (toxin/filler/skin/retail) with the S4 flag — the single classification driving rewards eligibility and public-page naming — plus regClass/ARTG/compounded for GLP-1 handling (ADR-0014/0021).

> **As a owner**, I want a product catalogue where each product has a type, unit, S4 flag and regulatory metadata, so that the right rules apply to each product across the platform.

**Acceptance criteria**

- [ ] Typed products each with their own unit (units vs syringes), par, expiry tracking.
- [ ] Capability-gated product admin sets the S4 flag (drives PRD-06 rewards + PRD-07 naming).
- [ ] Products carry regClass/artg/compounded; prohibited compounded GLP-1 is blocked.
- [ ] Retail (non-S4) SKUs supported alongside medicines.

**REQ:** REQ-MED-11, REQ-MED-12, REQ-MED-13 · **ADR:** ADR-0014, ADR-0021, ADR-0025

### ADMIN-GATE — Administration gating & immutable record
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

An RN can only administer S4 against a valid, unconsumed prescription for that same client, with current consent and a selected in-date lot; the record is immutable once saved (C8).

> **As a RN**, I want to administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry, so that every dose is lawful, traceable and tamper-proof.

**Acceptance criteria**

- [ ] An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
- [ ] It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
- [ ] A blocked attempt shows the reason and writes an audit event.
- [ ] The administration appears in the medicine register.

**REQ:** REQ-RX-3, REQ-MED-4 · **Compliance:** C8 · **ADR:** ADR-0010 · **PRD AC:** AC3

**Depends on:** PRD-04/PRESCRIPTION, PRD-04/STOCK-RECEIVE

### STOCK-RECEIVE — Stock receipt, ARTG & lawful-supply provenance
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

S4 stock is received from a TGA-approved wholesaler with ARTG status, brand, sponsor and lawful supply source recorded; non-ARTG/unverified source is warned/blocked (C11). S4 POs require a prescriber signer.

> **As a prescriber/owner**, I want to receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source, so that we only hold lawfully-supplied, approved medicine.

**Acceptance criteria**

- [ ] Receiving records ARTG status, brand, sponsor and supply source per lot.
- [ ] Receiving non-ARTG or unverified-source stock is warned/blocked per config.
- [ ] S4 purchase orders require a prescriber signer + TGA-approved wholesaler.
- [ ] ARTG validation supports manual entry (lookup against an ARTG dataset is an open option).

**REQ:** REQ-MED-6, REQ-MED-2 · **Compliance:** C11 · **PRD AC:** AC7

**Depends on:** PRD-04/PRODUCT-CATALOGUE

### CUSTODY-STORAGE — Custody & secure storage
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

Only NP/prescriber roles may take custody; stock is bound to a secure, access-logged location. Mode-A custodian must physically work at the clinic with exclusive custody (C7/C15).

> **As a owner**, I want stock custody limited to an on-site prescriber and bound to a secure, access-logged location, so that S4 custody meets the exclusive-custody rule.

**Acceptance criteria**

- [ ] Only NP/prescriber roles can take custody of stock.
- [ ] Stock is bound to a secure location; access is logged.
- [ ] A custodian + exclusive-custody attestation + designated medicine-store contact are recorded.
- [ ] A remote prescriber consigning stock is flagged non-compliant.

**REQ:** REQ-MED-2, REQ-MED-8 · **Compliance:** C7, C15 · **PRD AC:** AC5

**Depends on:** PRD-04/STOCK-RECEIVE

### COLD-CHAIN — Temperature logging & excursion alerts
`P1` · type:story, PRD-04, phase:1, area:backend, area:integration, compliance

Toxin must stay 2–8°C; temperature logging raises excursion alerts and flags affected stock (C13). Integrates with the optional ESP32 cold-chain monitor.

> **As a owner**, I want temperature logging for the medicine fridge with excursion alerts, so that we never use medicine that breached cold-chain.

**Acceptance criteria**

- [ ] Temperature can be logged (manual + via the device API) for storage locations.
- [ ] An excursion raises an alert and flags affected stock for quarantine.
- [ ] A breach pathway can quarantine a lot and raise a job (links PRD-11).
- [ ] Excursion history is retained and visible.

**REQ:** REQ-MED-7 · **Compliance:** C13 · **PRD AC:** AC6

**Depends on:** PRD-04/CUSTODY-STORAGE

### VIAL-RECON — Vial / unit reconciliation
`P1` · type:story, PRD-04, phase:1, area:backend, compliance

Units drawn vs vial size + wastage must reconcile so stock, billing and the register agree (C8).

> **As a owner**, I want vial/unit reconciliation across draws and wastage, so that stock, billing and the medicine register always agree.

**Acceptance criteria**

- [ ] Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
- [ ] Discrepancies are surfaced.
- [ ] Reconciliation data feeds reporting (PRD-08).
- [ ] Partial-vial handling is supported.

**REQ:** REQ-MED-5 · **Compliance:** C8

**Depends on:** PRD-04/ADMIN-GATE

### RECALL-LOOKUP — Lot → clients recall lookup & medicine register
`P0` · type:story, PRD-04, phase:1, area:backend, compliance

Given a lot, the system must instantly list every client/administration for that lot, and export an audit-ready medicine register (C8).

> **As a prescriber/owner**, I want to enter a lot number and instantly see every client who received it, plus export the medicine register, so that we can run a recall in minutes and evidence the register.

**Acceptance criteria**

- [ ] A lot lookup returns all clients/administrations for that lot.
- [ ] The S4 register exports a complete, immutable record of administrations.
- [ ] Recall execution + acknowledgement tracking is available (full hub in PRD-08/11).
- [ ] The register is queryable by date, product, prescriber, administrator.

**REQ:** REQ-MED-4 · **Compliance:** C8 · **PRD AC:** AC4

**Depends on:** PRD-04/ADMIN-GATE

### WASTAGE-DESTRUCTION — Wastage, disposal & destruction records
`P1` · type:story, PRD-04, phase:1, area:backend, compliance

Wastage and destruction (incl. partial vials) must be recorded via a licensed/RUM pathway with certificates (C16).

> **As a owner**, I want to record wastage, disposal and destruction (including partial vials) with certificates, so that we evidence lawful disposal of S4 medicine.

**Acceptance criteria**

- [ ] Wastage/destruction records capture quantity, reason, pathway and certificate reference.
- [ ] Partial-vial destruction is supported.
- [ ] Licensed/RUM disposal pathway is recorded.
- [ ] Records are immutable and audited.

**REQ:** REQ-MED-9 · **Compliance:** C16 · **PRD AC:** AC9

**Depends on:** PRD-04/CUSTODY-STORAGE

### STOCKTAKE — Stocktake, discrepancy & loss/theft reporting
`P1` · type:story, PRD-04, phase:1, area:backend, compliance

Stocktakes and discrepancy handling, with loss/theft reporting, close the medicines-governance loop (C17).

> **As a owner**, I want to run a stocktake and have discrepancies surfaced with a loss/theft reporting path, so that stock integrity is provable and losses are reported.

**Acceptance criteria**

- [ ] A stocktake compares expected vs counted stock per lot.
- [ ] Discrepancies are recorded; a discrepancy can trigger a loss/theft report.
- [ ] Expiry alerts surface near-expiry lots.
- [ ] Stocktake results feed the compliance dashboard (PRD-08).

**REQ:** REQ-MED-10 · **Compliance:** C17 · **PRD AC:** AC9

**Depends on:** PRD-04/CUSTODY-STORAGE

### MODE-B — Mode B pharmacy-dispensing model (placeholder)
`P2` · type:story, PRD-04, phase:2plus, area:backend

An alternative dispensing model where a pharmacy partner holds/dispenses stock. No pharmacy partner yet — deferred, placeholder. (DispensedItem entity reserved.)

> **As a owner**, I want a pharmacy-dispensing mode for clinics without on-site custody, so that the platform fits a pharmacy-partner arrangement.

**Acceptance criteria**

- [ ] Placeholder — v1 is Mode A only; tenant mode switch already anticipates Mode B.
- [ ] Captured so the medicines model stays mode-aware.

**REQ:** REQ-MED-1 · **Compliance:** C7

---

## PRD-05 — Clinical charting: injection mapping & before/after
*M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05) · Phase 1 · 9 stories*

The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway — usable room-side on the provider app, even offline.

### NOTE-TEMPLATE — Guided toxin treatment note & pre-treatment review
`P0` · type:story, PRD-05, phase:1, area:provider-app

Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/Rx surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

> **As a injector**, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.

**Acceptance criteria**

- [ ] Pre-treatment review surfaces safety flags, last treatment and the linked consult/Rx (verified before opening).
- [ ] Configurable toxin template with structured fields, free text and reusable phrases/snippets.
- [ ] A non-S4 skin note variant exists (treatment-type-aware).
- [ ] Charting cannot open unless the consult+consent gate is satisfied (PRD-03/04).

**REQ:** REQ-CLIN-1, REQ-CLIN-9 · **ADR:** ADR-0024

**Depends on:** PRD-04/ADMIN-GATE

### MAPPING — Injection-mapping canvas (per-point lot)
`P0` · type:story, PRD-05, phase:1, area:provider-app, compliance

On a facial diagram and/or patient photo, tap-to-add and drag injection points, each capturing product, units, depth, technique and batch-lot/expiry; charted units deduct from the selected lot on finalise (REQ-CLIN-2, C8).

> **As a injector**, I want to drop and drag injection points on a facial diagram or photo, each recording product, units, depth, technique and lot, so that the treatment is precisely charted and traceable to a batch.

**Acceptance criteria**

- [ ] Charting opens with product & batch (lot) selection, restricted to in-date/ARTG/in-custody stock.
- [ ] Each point records product, units, depth, technique and batch-lot/expiry.
- [ ] On finalise, charted units deduct from the selected lot and link to the medicine register + recall (PRD-04).
- [ ] Built on the SPIKE-CANVAS approach; performs smoothly with many points.

**REQ:** REQ-CLIN-2, REQ-MED-4 · **Compliance:** C8 · **PRD AC:** AC1

**Depends on:** SPRINT-0/SPIKE-CANVAS, PRD-04/RECALL-LOOKUP

### PHOTOS — Standardised before/after photos + compare
`P1` · type:story, PRD-05, phase:1, area:provider-app, compliance

Capture standardised before/after photos room-side (framing/ghosting guide), compare side-by-side across visits; media stored centrally via signed URLs, never on personal devices, gated by image-use consent (REQ-CLIN-3, C14/ADR-0009).

> **As a injector**, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.

**Acceptance criteria**

- [ ] Camera/upload with standardised framing/ghosting guide; side-by-side compare across visits.
- [ ] Capture requires current image-use consent (PRD-03).
- [ ] Photos stored centrally via signed URLs; never persisted on device beyond a transient sync cache.
- [ ] Annotation supported.

**REQ:** REQ-CLIN-3 · **Compliance:** C14 · **ADR:** ADR-0009 · **PRD AC:** AC2, AC6

**Depends on:** PRD-03/IMAGE-CONSENT

### IMMUTABILITY — Immutable finalisation & audited amendments
`P0` · type:story, PRD-05, phase:1, area:backend, compliance

A finalised note is locked; any later change is an appended, audited amendment preserving the original (REQ-CLIN-4, ADR-0010).

> **As a injector**, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.

**Acceptance criteria**

- [ ] A finalised note cannot be edited.
- [ ] An amendment creates a new linked, audited entry preserving the original.
- [ ] Finalisation happens server-side.
- [ ] The finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event.

**REQ:** REQ-CLIN-4 · **ADR:** ADR-0010 · **PRD AC:** AC3

**Depends on:** PRD-05/MAPPING

### OFFLINE — Offline queue & sync for room-side charting
`P1` · type:story, PRD-05, phase:1, area:provider-app

If Wi-Fi drops mid-visit, notes/photos queue locally (encrypted) and sync on reconnect with no loss; finalisation is server-side (REQ-CLIN/APP, ADR-0015).

> **As a injector**, I want my notes and photos to queue locally and sync when back online if the room loses Wi-Fi, so that I never lose work mid-treatment.

**Acceptance criteria**

- [ ] With connectivity dropped, notes/photos queue locally (encrypted) and sync on reconnect with no loss.
- [ ] Drafts use last-write-wins; finalisation occurs server-side.
- [ ] A sync/offline indicator shows queued count + last-sync time; finalise disabled until synced.
- [ ] Built on SPIKE-OFFLINE.

**REQ:** REQ-APP-3 · **ADR:** ADR-0015, ADR-0010 · **PRD AC:** AC4

**Depends on:** SPRINT-0/SPIKE-OFFLINE, PRD-05/IMMUTABILITY

### ADVERSE-EVENT — Adverse-event capture → DAEN pathway
`P1` · type:story, PRD-05, phase:1, area:provider-app, compliance

Log an adverse event/complication linked to the treatment, product and lot, classify seriousness and target the correct DAEN database (REQ-CLIN-5, C12). Includes the VO/anaphylaxis complication-response flow.

> **As a injector**, I want to log an adverse event linked to the treatment, product and lot, so that it feeds the TGA report and the right follow-ups happen.

**Acceptance criteria**

- [ ] An adverse event captures the data a TGA report needs, classifies seriousness and targets the correct DAEN database (medicine vs device).
- [ ] It links to the treatment, product and lot.
- [ ] A complication-response flow (VO/anaphylaxis → log hyaluronidase/adrenaline) routes the AE + raises jobs.
- [ ] Full submission/prefill lives in the Governance hub (PRD-08).

**REQ:** REQ-CLIN-5 · **Compliance:** C12 · **PRD AC:** AC5

**Depends on:** PRD-05/IMMUTABILITY

### TREATMENT-PLANS — Treatment plans & protocol templates
`P2` · type:story, PRD-05, phase:1, area:provider-app

Multi-session treatment plans + applyable protocol templates feed recall and structure ongoing care (REQ-CLIN-7).

> **As a injector**, I want to build multi-session treatment plans from protocol templates, so that ongoing care is structured and drives recall.

**Acceptance criteria**

- [ ] Protocol templates can be applied to create a multi-session plan.
- [ ] Plans feed the recall worklist (PRD-07).
- [ ] Plan progress is visible on the client 360.
- [ ] A charting overview / 'in-room now' entry point lists active plans.

**REQ:** REQ-CLIN-7 · **ADR:** ADR-0024

**Depends on:** PRD-05/NOTE-TEMPLATE

### MODALITY — Other-modality charting: filler / energy / weight-loss (placeholder)
`P2` · type:story, PRD-05, phase:2plus, area:provider-app

Phase 2 adds dermal filler (multi-area, per-area lot, VO/blindness consent gate), energy-device charting (per-pass settings, laser-licence gated), weight-loss titration and ghost-overlay photo alignment (REQ-CLIN-10..13). Placeholder.

> **As a injector**, I want modality-aware charting for filler, energy devices and weight-loss, so that the platform covers the full treatment menu.

**Acceptance criteria**

- [ ] Placeholder — v1 ships toxin + non-S4 skin notes; the modality model already anticipates these.
- [ ] Each modality's specific gates (e.g. filler VO consent, laser licence) are captured for later build.

**REQ:** REQ-CLIN-10, REQ-CLIN-11, REQ-CLIN-12, REQ-CLIN-13 · **ADR:** ADR-0025

### AI-SCRIBE — AI note dictation / auto-detect injection points (placeholder)
`P2` · type:story, PRD-05, phase:2plus, area:provider-app

AI scribe and advisory auto-detection of injection points are explicitly out for v1 (no AI; everything manual + human-confirmed). Placeholder (REQ-CLIN-6, ADR-0020).

> **As a injector**, I want optional AI assistance for notes and injection-point suggestions, so that charting is faster (with human confirmation).

**Acceptance criteria**

- [ ] Placeholder — explicitly no AI in v1; any future feature is advisory + human-confirmed only.
- [ ] Captured to keep the data model ready.

**REQ:** REQ-CLIN-6 · **ADR:** ADR-0020

---

## PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards
*M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10) · Phase 1 · 9 stories*

Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law. Financials stay owner-only; the ledger defers to Xero.

### PAYMENT-PROVIDER — Payment provider abstraction + Square adapter
`P0` · type:story, PRD-06, phase:1, area:backend, area:integration

An IPaymentProvider port (authorize/capture, refund, void, tokenize, recurring, gift-card) with a Square adapter first and cash as an internal tender; no PAN stored, only tokens (ADR-0007).

> **As a developer**, I want a payment-provider abstraction with a Square adapter and cash tender, so that payments are swappable and PCI-safe.

**Acceptance criteria**

- [ ] IPaymentProvider exposes authorize/capture, refund, void, tokenize, recurring and gift-card.
- [ ] Square adapter implemented; cash is an internal tender.
- [ ] No PAN is ever stored — only provider tokens.
- [ ] Built on SPIKE-SQUARE findings.

**REQ:** REQ-PAY-1 · **ADR:** ADR-0007 · **PRD AC:** AC5

**Depends on:** SPRINT-0/SPIKE-SQUARE

### POS — In-person POS checkout (card + cash)
`P0` · type:story, PRD-06, phase:1, area:web

Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split, tips and surcharge config (REQ-PAY-2). Financial figures are owner-gated.

> **As a front desk**, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.

**Acceptance criteria**

- [ ] A sale completes by Square card or recorded cash; both appear in the daily closeout.
- [ ] Receipts, partial/split payments, tips and surcharge config supported.
- [ ] Money figures respect the owner-only financial capability (reception sees no money totals beyond the sale).
- [ ] Online one-off checkout is not exposed (deferred).

**REQ:** REQ-PAY-2 · **PRD AC:** AC1

**Depends on:** PRD-06/PAYMENT-PROVIDER

### PACKAGES-GIFT — Packages/series, gift cards & client balances
`P1` · type:story, PRD-06, phase:1, area:web

Sell/redeem packages (visits remaining) and gift cards, track client balances/credit and AR ageing (REQ-PAY-3/5).

> **As a front desk**, I want to sell and redeem packages and gift cards and track client balances, so that clients can pre-pay and carry credit.

**Acceptance criteria**

- [ ] Package/series sale + redemption with 'visits remaining'.
- [ ] Gift cards can be sold, balance-tracked and redeemed.
- [ ] Client balance/credit and AR ageing tracked.
- [ ] Redemptions appear in the closeout and post to Xero (PRD-10).

**REQ:** REQ-PAY-3, REQ-PAY-5 · **PRD AC:** AC6

**Depends on:** PRD-06/POS

### CLOSEOUT — Daily closeout & reconciliation
`P1` · type:story, PRD-06, phase:1, area:web

End-of-day closeout balances card + cash (REQ-PAY-4).

> **As a owner**, I want a daily closeout that balances card and cash, so that the till reconciles every day.

**Acceptance criteria**

- [ ] Closeout summarises card + cash tenders for the day.
- [ ] Variances are surfaced.
- [ ] Closeout figures are owner-gated.
- [ ] Closeout reconciles to the Xero posting (PRD-10).

**REQ:** REQ-PAY-4 · **PRD AC:** AC1

**Depends on:** PRD-06/POS

### MEMBERSHIP — Memberships with automatic autopay & dunning
`P0` · type:story, PRD-06, phase:1, area:backend

Membership plans/tiers with automatic recurring billing from a tokenised card-on-file (added online/in-app or at desk) and failed-payment dunning (REQ-MEMB-1/2/3).

> **As a client**, I want to join a membership and have my card auto-charged on schedule, so that I get member perks without manual payments.

**Acceptance criteria**

- [ ] A membership auto-charges on schedule from a stored token (card added online/in-app or in person).
- [ ] A failed charge triggers dunning/recovery.
- [ ] Lifecycle (join/pause/cancel/win-back) tracked → MRR/churn reporting (PRD-08).
- [ ] Benefits/credits auto-apply at checkout.

**REQ:** REQ-MEMB-1, REQ-MEMB-2, REQ-MEMB-3 · **PRD AC:** AC2

**Depends on:** PRD-06/PAYMENT-PROVIDER

### REWARDS-ENGINE — Rewards engine — non-S4 only
`P0` · type:story, PRD-06, phase:1, area:backend, compliance

Visit-based + membership rewards that the engine blocks from ever applying to S4 items; configuring an S4 reward is blocked (REQ-MEMB-4/5/7, C9/ADR-0014).

> **As a client**, I want to earn and redeem rewards on non-S4 items only, so that I'm rewarded without breaching S4 advertising rules.

**Acceptance criteria**

- [ ] Visit-based rewards (milestones/every-Nth-visit) + membership perks on non-S4 items, add-ons or account/gift credit.
- [ ] The engine refuses to earn, redeem or discount against any S4-flagged item.
- [ ] Attempting to configure an S4 reward is blocked.
- [ ] Catalog schedule flag (from PRD-04) drives eligibility.

**REQ:** REQ-MEMB-4, REQ-MEMB-5, REQ-MEMB-7 · **Compliance:** C9 · **ADR:** ADR-0014 · **PRD AC:** AC3

**Depends on:** PRD-04/PRODUCT-CATALOGUE

### MARGIN-RULES — Margin-aware reward rules
`P1` · type:story, PRD-06, phase:1, area:backend, compliance

Owners set value caps and eligible items; reporting shows reward-cost vs retention (REQ-MEMB-6). Reward comms respect advertising rules (C9/C23).

> **As a owner**, I want to set margin-aware reward rules with caps and eligible items and see reward-cost vs retention, so that rewards drive retention without eroding margin.

**Acceptance criteria**

- [ ] Reward rules enforce value caps and eligible-item lists.
- [ ] Reward-cost vs retention surfaces in reporting (PRD-08).
- [ ] Reward communications go only to consented, logged-in clients (no public S4 price promotion).
- [ ] Rule config is owner-gated.

**REQ:** REQ-MEMB-6 · **Compliance:** C9, C23 · **PRD AC:** AC4

**Depends on:** PRD-06/REWARDS-ENGINE

### CHECKOUT-ASSIST — Checkout assist & post-visit rebooking
`P2` · type:story, PRD-06, phase:1, area:web

Subtle membership/restock upsell + client rapport panel + post-checkout rebooking on the treatment interval (REQ-PAY-6, ADR-0022).

> **As a front desk**, I want checkout to suggest relevant non-S4 upsells and prompt rebooking at the right interval, so that I help clients and keep them on cadence.

**Acceptance criteria**

- [ ] Checkout shows a subtle membership/restock upsell and a client rapport panel.
- [ ] Post-checkout rebooking is offered on the treatment interval.
- [ ] Upsell suggestions never include S4 discounting.
- [ ] Rebooking integrates with the calendar (PRD-02) and recall (PRD-07).

**REQ:** REQ-PAY-6 · **ADR:** ADR-0022

**Depends on:** PRD-06/POS

### PRICING-WHATIF — Pricing & what-if planning (owner)
`P2` · type:story, PRD-06, phase:1, area:web

An owner pricing + what-if planner over the reporting read-models (REQ-MEMB-9, ADR-0022). The Finance screen is a light pricing + reporting hub; the ledger defers to Xero.

> **As a owner**, I want to model pricing and run what-if scenarios, so that I can set prices and plan membership economics.

**Acceptance criteria**

- [ ] Pricing/what-if planner uses the same read-models as reporting (PRD-08).
- [ ] Scenario outputs are owner-gated.
- [ ] The Finance area is a pricing + reporting hub; in-app ledger/payroll/AP/BAS tooling is out of scope (Xero).
- [ ] Invoices/payments still sync to Xero from checkout.

**REQ:** REQ-MEMB-9 · **ADR:** ADR-0022, ADR-0027

**Depends on:** PRD-06/POS

---

## PRD-07 — Communications, reminders & recall
*M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10) · Phase 1 · 7 stories*

The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in. Advertising content is produced in the clinic's external tools; the platform has no advertising linter, and the public booking page uses generic names with S4 prices withheld by configuration.

### CHANNELS — Notification channels (SMS / email / push)
`P0` · type:story, PRD-07, phase:1, area:backend, area:integration

An INotifier port over an AU SMS provider + email + app push, with per-tenant templates (REQ-NOTIF-1, ADR-0012).

> **As a developer**, I want a notification abstraction over SMS, email and push with per-tenant templates, so that all messaging is consistent and provider-swappable.

**Acceptance criteria**

- [ ] INotifier supports SMS (AU provider), email and app push.
- [ ] Per-tenant message templates supported.
- [ ] Provider is swappable behind the port.
- [ ] All sends log to the client's comms history.

**REQ:** REQ-NOTIF-1 · **ADR:** ADR-0012 · **PRD AC:** AC5

### REMINDERS-CARE — Reminders, confirmations & care sequences
`P1` · type:story, PRD-07, phase:1, area:backend

Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type) (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

> **As a client**, I want timely reminders I can confirm/decline and pre-/after-care instructions for my treatment, so that I'm prepared and cared for around my visit.

**Acceptance criteria**

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment (PRD-02).
- [ ] Pre-care + aftercare sequences are multi-touch and timed per treatment type.
- [ ] Transactional messages send regardless of marketing opt-in and avoid S4 references.
- [ ] Sends are logged to comms history.

**REQ:** REQ-NOTIF-2 · **PRD AC:** AC3

**Depends on:** PRD-07/CHANNELS

### RECALL — Recall / recare worklist
`P1` · type:story, PRD-07, phase:1, area:backend

Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall worklist for front desk (REQ-NOTIF-3).

> **As a front desk**, I want a recall worklist of clients due to rebook and automatic recall nudges at the treatment interval, so that clients return on cadence and the book stays full.

**Acceptance criteria**

- [ ] A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- [ ] Unbooked recommended sessions prompt a rebook.
- [ ] Front desk can work the recall/rebook worklist.
- [ ] Recall integrates with treatment plans (PRD-05) and rebooking (PRD-06).

**REQ:** REQ-NOTIF-3 · **PRD AC:** AC4

**Depends on:** PRD-07/CHANNELS

### MARKETING-CONSENT — Marketing consent & functional unsubscribe (Spam Act)
`P1` · type:story, PRD-07, phase:1, area:backend, compliance

Opt-in for commercial electronic messages, sender identification and a functional unsubscribe that suppresses immediately on withdrawal (REQ-NOTIF-5, C23).

> **As a client**, I want to only receive marketing I opted into, with a working unsubscribe on every message, so that my consent is respected per the Spam Act.

**Acceptance criteria**

- [ ] Marketing sends only to opted-in clients and always include a working unsubscribe.
- [ ] Unsubscribing suppresses future marketing immediately.
- [ ] Sender identification is included.
- [ ] Suppression list is honoured across channels (and by PRD-06 reward comms).

**REQ:** REQ-NOTIF-5 · **Compliance:** C23 · **PRD AC:** AC1

**Depends on:** PRD-07/CHANNELS

### BOOKING-PAGE — Public booking page: generic names, S4 prices withheld
`P1` · type:story, PRD-07, phase:1, area:web, compliance

The public booking page uses generic service names and withholds S4 prices by configuration (catalog schedule flag), with no advertising linter (REQ-NOTIF-12, C9).

> **As a owner**, I want my public booking page to use generic service names and withhold S4 prices automatically, so that we don't reference S4 in public advertising.

**Acceptance criteria**

- [ ] The booking page renders generic service names and withholds S4 prices for any S4-flagged service (configuration-driven).
- [ ] No brands, 'anti-wrinkle injections', prices or #botox appear for S4 services.
- [ ] Configuration is driven by the catalog schedule flag (PRD-04).
- [ ] Advertising compliance beyond this is clinic-owned (external tools).

**REQ:** REQ-NOTIF-12 · **Compliance:** C9 · **ADR:** ADR-0014 · **PRD AC:** AC2

**Depends on:** PRD-02/ONLINE-BOOK

### FOLLOWUPS — Unified follow-up / job queue
`P2` · type:story, PRD-07, phase:1, area:web

Scattered recall / needs-attention / unanswered-comms items merge into one queue; staff can flag any message; inbound comms auto-categorise into jobs (rules/keyword, no AI) (REQ-NOTIF-7, ADR-0023).

> **As a staff member**, I want one follow-up queue that merges recalls, needs-attention items and flagged messages, so that nothing falls through the cracks.

**Acceptance criteria**

- [ ] Recall, needs-attention and unanswered-comms items merge into a single queue.
- [ ] Any message can be flagged so it isn't lost.
- [ ] Inbound comms auto-categorise into jobs by rules/keyword (no AI).
- [ ] A no-show (PRD-02) and negative reviews raise jobs into this queue.

**REQ:** REQ-NOTIF-7 · **ADR:** ADR-0023

**Depends on:** PRD-07/CHANNELS

### INBOX — Omnichannel inbox + lead/reviews (placeholder)
`P2` · type:story, PRD-07, phase:2plus, area:integration

The omnichannel inbox (IG/FB/SMS/email), lead/prospect CRM and reviews/reputation are scoped to Phase 2; marketing DMs are out (Meta 24-h window). Placeholder (REQ-NOTIF-6/8/9, ADR-0018/0019/0032/0033).

> **As a staff member**, I want a unified inbox with lead tracking and review management, so that all client conversations live in one place.

**Acceptance criteria**

- [ ] Placeholder — Phase 2; IG/FB/WhatsApp are reactive/service channels only (no cold-DM marketing).
- [ ] Reviews acknowledge/flag/auto-detect-follow-up and the lead CRM are captured for later.
- [ ] Meta feasibility (App Review, Business Verification, 24-h window) flagged for validation.

**REQ:** REQ-NOTIF-6, REQ-NOTIF-8, REQ-NOTIF-9 · **ADR:** ADR-0018, ADR-0032, ADR-0033

---

## PRD-08 — Reporting & compliance dashboards (Governance hub)
*M5 · Reporting & apps (PRD-08, PRD-09) · Phase 1 · 8 stories*

Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack. Built on dedicated read-models/materialized views. Financial figures stay owner-gated.

### READ-MODELS — Reporting read-models / materialized views
`P1` · type:story, PRD-08, phase:1, area:data

Dashboards read from dedicated read-models/materialized views fed by domain events + the audit stream; eventual consistency acceptable (ADR-0013). Build incrementally as modules land.

> **As a developer**, I want read-models/materialized views fed by domain events and the audit stream, so that dashboards are fast and don't hammer the transactional DB.

**Acceptance criteria**

- [ ] Read-models are populated from domain events + the audit stream.
- [ ] Dashboards read from materialized views, not OLTP, and load within target on clinic data volumes.
- [ ] Read-models are built incrementally per module.
- [ ] Backfill/rebuild of a read-model is supported.

**REQ:** REQ-RPT-1 · **ADR:** ADR-0013, ADR-0010 · **PRD AC:** AC7

**Depends on:** PRD-01/AUDIT

### BUSINESS-DASH — Business analytics dashboards
`P1` · type:story, PRD-08, phase:1, area:web

Revenue, retention/churn, no-shows, cancellations, conversion, at-risk, big spenders, membership MRR/churn and per-practitioner mix, date-filterable (REQ-RPT-1/2). Money figures owner-gated.

> **As a owner**, I want dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner, so that I can run the business on real numbers.

**Acceptance criteria**

- [ ] Core dashboards match the prototype's metrics on the same date range.
- [ ] Date-range presets + custom filtering; per-practitioner views.
- [ ] Reward-cost vs retention surfaces (from PRD-06).
- [ ] All money figures are gated behind the owner financial capability.

**REQ:** REQ-RPT-1, REQ-RPT-2 · **PRD AC:** AC6

**Depends on:** PRD-08/READ-MODELS

### COMPLIANCE-DASH — Compliance dashboards & register exports
`P1` · type:story, PRD-08, phase:1, area:web, compliance

Consent coverage, consult-before-script adherence (C1), S4 register export (C8), lot→clients recall, cooling-off adherence (C6), registration-expiry watch (C19), records-retention-due (C18), S4 stock discrepancies (C17), breach (C22) & complaints (C24) registers (REQ-RPT-3).

> **As a compliance officer**, I want compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers, so that I can evidence compliance and act on gaps.

**Acceptance criteria**

- [ ] Consult-before-script adherence shows 100% by construction; any exception is flagged.
- [ ] The S4 register exports a complete immutable record; a lot lookup returns all affected clients.
- [ ] Registration-expiry watch and records-due-for-destruction lists render with their basis.
- [ ] Breach and complaints registers are viewable/exportable.

**REQ:** REQ-RPT-3 · **Compliance:** C1, C8, C18, C19, C22, C24 · **PRD AC:** AC1, AC2, AC3, AC4

**Depends on:** PRD-08/READ-MODELS, PRD-04/RECALL-LOOKUP

### DAEN — Adverse-event / DAEN prefilled submission
`P1` · type:story, PRD-08, phase:1, area:web, compliance

Classify seriousness, route medicine vs device, produce a prefilled DAEN export/submission and flag mandatory cases (C12, ADR-0031).

> **As a prescriber**, I want to generate a prefilled DAEN adverse-event report targeting the correct database, so that reporting an adverse event is fast and correct.

**Acceptance criteria**

- [ ] An adverse event produces a prefilled DAEN report with seriousness set, targeting the correct database (medicine vs device).
- [ ] Mandatory-reporting cases are flagged.
- [ ] Recall execution + acknowledgement tracking lives in the hub.
- [ ] Submission is export/file (electronic channel is an open option).

**Compliance:** C12 · **ADR:** ADR-0031 · **PRD AC:** AC5

**Depends on:** PRD-05/ADVERSE-EVENT

### DATA-QUALITY — Data-quality checks
`P2` · type:story, PRD-08, phase:1, area:web

Carry over anomaly checks: active-but-unseen, completed-not-checked-in, duplicates, missing contacts, implausible dates (REQ-RPT-4).

> **As a owner**, I want data-quality checks that flag anomalies in my records, so that the data stays clean and trustworthy.

**Acceptance criteria**

- [ ] Checks flag active-but-unseen, completed-not-checked-in, duplicates, missing contacts and implausible dates.
- [ ] Findings are listed and actionable.
- [ ] Checks run on a schedule.
- [ ] Findings feed the needs-attention digest.

**REQ:** REQ-RPT-4

**Depends on:** PRD-08/READ-MODELS

### ATTENTION-DIGEST — Owner 'needs attention' exceptions digest
`P2` · type:story, PRD-08, phase:1, area:web

An owner digest of exceptions across the platform (REQ-RPT-5).

> **As a owner**, I want a single 'needs attention' digest of exceptions across the clinic, so that I can act on what matters without hunting.

**Acceptance criteria**

- [ ] Digest aggregates expiries, discrepancies, data-quality findings, failed payments and overdue follow-ups.
- [ ] Each item links to its source for action.
- [ ] Digest respects role/financial gating.
- [ ] Available as an at-a-glance owner view.

**REQ:** REQ-RPT-5

**Depends on:** PRD-08/COMPLIANCE-DASH

### INSPECTION-PACK — Inspection-readiness pack & governance hub
`P2` · type:story, PRD-08, phase:1, area:web, compliance

A one-click inspection-readiness pack and the cross-case Governance hub (policies sign-off, waste manifests/IPC, DSAR + breach drill) (REQ-RPT-7, ADR-0030, REQ-SEC-8/9).

> **As a owner**, I want a one-click pack that assembles the evidence an inspector would ask for, so that we're always inspection-ready.

**Acceptance criteria**

- [ ] The pack assembles consent coverage, the S4 register, registration/insurance status, IPC/waste logs and registers.
- [ ] Policies & procedures sign-off is tracked in the hub.
- [ ] DSAR (APP 12/13) and a breach drill are runnable from the hub.
- [ ] Pack generation is audited.

**REQ:** REQ-RPT-7, REQ-SEC-8, REQ-SEC-9 · **Compliance:** C10 · **ADR:** ADR-0030

**Depends on:** PRD-08/COMPLIANCE-DASH

### REPORT-BUILDER — Custom report builder / external BI (placeholder)
`P2` · type:story, PRD-08, phase:2plus, area:web

A custom report builder, external BI warehouse and cross-clinic benchmarking are Phase 2+. Placeholder.

> **As a owner**, I want to build custom reports and benchmark against other clinics, so that I can answer bespoke questions.

**Acceptance criteria**

- [ ] Placeholder — Phase 2+; v1 ships fixed dashboards + exports.
- [ ] Captured so the read-model layer stays export-friendly.

**REQ:** REQ-RPT-1

---

## PRD-09 — Apps (Flutter): client & provider
*M5 · Reporting & apps (PRD-08, PRD-09) · Phase 1 · 7 stories*

Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity. One codebase, two flavours, sharing auth, the API client and the design system.

### CLIENT-JOURNEY — Client app: book → intake → consent journey
`P1` · type:story, PRD-09, phase:1, area:client-app

A client can complete the full pre-visit journey entirely in-app (REQ-APP-1).

> **As a client**, I want to book, complete intake and e-sign consent entirely in the app, so that I'm ready for my visit without paperwork.

**Acceptance criteria**

- [ ] A client completes book → intake → consent (incl. image-use) fully in-app.
- [ ] Surfaces PRD-02 booking and PRD-03 intake/consent.
- [ ] Sign-in via social/email/OTP, tenant-scoped.
- [ ] Reminders/recall (PRD-07) are received in-app.

**REQ:** REQ-APP-1 · **ADR:** ADR-0004 · **PRD AC:** AC1, AC4

**Depends on:** PRD-02/ONLINE-BOOK, PRD-03/CONSENT

### CLIENT-CARE — Client app: my care, memberships, rewards & card-on-file
`P2` · type:story, PRD-09, phase:1, area:client-app

Clients view consented before/after photos, memberships, rewards/perks and balances, and add a card-on-file for autopay (REQ-APP-1).

> **As a client**, I want to view my photos, memberships, rewards and balance and add a card-on-file, so that I can self-serve my care and payments.

**Acceptance criteria**

- [ ] Consent-gated before/after photo viewing.
- [ ] Memberships, rewards/perks and balances visible.
- [ ] Card-on-file can be added in-app (feeds PRD-06 autopay).
- [ ] No one-off online checkout is exposed.

**REQ:** REQ-APP-1 · **Compliance:** C14 · **PRD AC:** AC5

**Depends on:** PRD-06/MEMBERSHIP, PRD-05/PHOTOS

### CLIENT-PRIVACY — Client app: account, privacy & access/correction
`P2` · type:story, PRD-09, phase:1, area:client-app, compliance

The Account area exposes profile, balances, card-on-file and a 'Your data & privacy' surface (residency note, access copy, request correction) (C21).

> **As a client**, I want an account area where I can see my data, know it stays in Australia, and request access or correction, so that I'm in control of my information.

**Acceptance criteria**

- [ ] Account shows profile, balances and card-on-file.
- [ ] 'Your data & privacy' shows the residency note and access-copy/correction actions (PRD-01).
- [ ] Requests are tracked to resolution.
- [ ] Actions are audited.

**REQ:** REQ-APP-1 · **Compliance:** C21

**Depends on:** PRD-01/PRIVACY-RIGHTS

### PROVIDER-DAY — Provider app: day schedule & open patient
`P1` · type:story, PRD-09, phase:1, area:provider-app

The provider sees their day and opens a patient with consult+consent status verified before charting (REQ-APP-2).

> **As a injector/prescriber**, I want to see my day and open a patient with consult/consent status shown before I chart, so that I work room-side with the right context and gates.

**Acceptance criteria**

- [ ] Schedule shows the practitioner's day; opening a patient shows consult+consent status.
- [ ] Provider signs in via Entra SSO, tenant-scoped.
- [ ] The consult+consent gate (PRD-03/04) is enforced before charting opens.
- [ ] Quick links to map/photos/finalise.

**REQ:** REQ-APP-2 · **ADR:** ADR-0004 · **PRD AC:** AC1

**Depends on:** PRD-05/NOTE-TEMPLATE

### PROVIDER-ROOMSIDE — Provider app: room-side charting, camera & finalise
`P1` · type:story, PRD-09, phase:1, area:provider-app, compliance

Map injections, capture photos via signed URLs (never on device), record consult/link script and finalise — all surfacing PRD-04/05 (REQ-APP-2, C14/ADR-0009).

> **As a injector**, I want to map injections, capture photos and finalise the chart room-side, so that the full clinical record is captured at the chair.

**Acceptance criteria**

- [ ] Provider app surfaces PRD-05 mapping/photos and PRD-04 consult/Rx/administration.
- [ ] Photos capture to central storage via signed URLs; none persist on device after sync (C14).
- [ ] Finalisation is server-side; once finalised the entry is read-only.
- [ ] Thumb-first, gloves-on usability (UX §1).

**REQ:** REQ-APP-2 · **Compliance:** C14 · **ADR:** ADR-0009 · **PRD AC:** AC2, AC6

**Depends on:** PRD-05/MAPPING, PRD-05/PHOTOS

### PROVIDER-OFFLINE — Provider app: offline-tolerant workflows + sync indicator
`P1` · type:story, PRD-09, phase:1, area:provider-app

Charting/photos queue locally encrypted and sync on reconnect with no loss; a persistent sync/offline indicator shows queued count + last sync (REQ-APP-3, ADR-0015).

> **As a injector**, I want the app to keep working offline and clearly show my sync state, so that treatment-room Wi-Fi drops never cost me data.

**Acceptance criteria**

- [ ] Charting/photos queue locally (encrypted) offline and sync on reconnect with no loss.
- [ ] Persistent indicator shows queued-items count + last-sync time.
- [ ] Finalise is disabled until synced.
- [ ] Built on SPIKE-OFFLINE and PRD-05/OFFLINE.

**REQ:** REQ-APP-3 · **ADR:** ADR-0015 · **PRD AC:** AC3

**Depends on:** PRD-05/OFFLINE

### APP-DISTRIBUTION — App distribution & code-push posture
`P2` · type:story, PRD-09, phase:1, area:client-app, area:provider-app

Store distribution + code-push (e.g. Shorebird) where the compliance posture allows (open question) (ADR-0006).

> **As a mobile developer**, I want a store-distribution and (where viable) code-push pipeline for both apps, so that we can ship and patch the apps responsibly.

**Acceptance criteria**

- [ ] Both apps distribute via internal/store channels from CI.
- [ ] Code-push viability for the compliance posture is assessed and documented.
- [ ] Versioning + minimum-supported-version handling in place.
- [ ] Crash/usage telemetry feeds observability.

**REQ:** REQ-APP-1, REQ-APP-2 · **ADR:** ADR-0006

**Depends on:** SPRINT-0/FLUTTER

---

## PRD-10 — Integrations: Xero & calendar
*M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10) · Phase 1 · 4 stories*

Outbound integrations that remove double-entry: push sales/payments to Xero, and keep appointments in sync with staff calendars (M365 / Google) — each behind a swappable adapter, with an AU/APP-8 sub-processor posture.

### XERO — Xero invoice/payment sync
`P1` · type:story, PRD-10, phase:1, area:integration

On checkout, create/sync invoice + payment (and payouts) in Xero with account/GST mapping, retries and reconciliation status, behind IAccountingExport (REQ-INT-1).

> **As a owner**, I want completed sales/payments to post to Xero with the right account and GST, so that my books reconcile without re-keying.

**Acceptance criteria**

- [ ] A completed sale creates the corresponding Xero invoice + payment with correct account + GST.
- [ ] Failures retry and show a reconciliation status.
- [ ] Services vs retail vs memberships map to the right accounts (defaults are an open question).
- [ ] Implemented behind IAccountingExport (swappable).

**REQ:** REQ-INT-1 · **ADR:** ADR-0012 · **PRD AC:** AC1, AC4

**Depends on:** PRD-06/POS

### CALENDAR-SYNC — Two-way calendar sync (M365 / Google)
`P2` · type:story, PRD-10, phase:1, area:integration

Appointments sync both ways with Outlook/Google; external busy events block availability, behind ICalendarProvider (REQ-INT-2).

> **As a practitioner**, I want my appointments to appear in Outlook/Google and external busy-time to block my availability, so that I have one source of truth for my time.

**Acceptance criteria**

- [ ] Creating/moving/cancelling an appointment reflects in the linked Outlook/Google calendar and vice-versa.
- [ ] External busy events block availability in booking (PRD-02).
- [ ] Per-staff opt-in and conflict-resolution rules (open question) supported.
- [ ] Implemented behind ICalendarProvider (swappable).

**REQ:** REQ-INT-2 · **ADR:** ADR-0012 · **PRD AC:** AC2, AC4

**Depends on:** PRD-02/CALENDAR

### SUBPROCESSOR-POSTURE — Sub-processor residency posture (APP-8)
`P2` · type:story, PRD-10, phase:1, area:integration, compliance

No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists (REQ-INT-3, C21/ADR-0016).

> **As a owner**, I want assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors, so that integrations don't breach cross-border rules.

**Acceptance criteria**

- [ ] No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are registered.
- [ ] All integrations are outbound and swappable.
- [ ] Ties into PRD-01/RESIDENCY enforcement.

**REQ:** REQ-INT-3 · **Compliance:** C21 · **ADR:** ADR-0016 · **PRD AC:** AC3

**Depends on:** PRD-01/RESIDENCY

### INTEGRATIONS-LATER — Online checkout, e-prescribing, webhooks/API (placeholder)
`P2` · type:story, PRD-10, phase:2plus, area:integration

Online checkout & deposits (S4 never priced/sold online), e-prescribing (eRx/ETP, 🔬), public API/webhooks (Phase 3) and Medicare/HICAPS (non-applicable to cosmetic). Placeholder (REQ-INT-2a/4/5/6/7, ADR-0035/0036).

> **As a owner**, I want future integrations: online checkout/deposits, e-prescribing and a public API, so that the platform extends as we scale.

**Acceptance criteria**

- [ ] Placeholder — Phase 2/3; each behind its existing port (IPaymentProvider, IPrescribingProvider).
- [ ] S4 is never priced or sold online (invariant carried forward).
- [ ] Medicare/HICAPS recorded as non-applicable to cosmetic.
- [ ] e-prescribing flagged for feasibility validation.

**REQ:** REQ-INT-4, REQ-INT-5, REQ-INT-6, REQ-INT-7 · **ADR:** ADR-0035, ADR-0036

---

## PRD-11 — Facility, infection-control, emergency & complaints
*M6 · Facility & complaints (PRD-11) · Phase 1 · 5 stories*

The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway. Lightweight registers + reminders in v1, with fuller workflows (cold-chain log, open/close checklist, sterilisation register, waste manifests, complication-response) layered on.

### FACILITY — Facility accreditation & expiry alerts
`P2` · type:story, PRD-11, phase:1, area:web, compliance

Per-location accreditation status + expiry alerts before lapse (REQ-FAC-1, C20).

> **As a owner**, I want to record facility accreditation and be alerted before it expires, so that we never lapse on accreditation.

**Acceptance criteria**

- [ ] Per-location accreditation status recorded.
- [ ] Expiry alerts fire before lapse.
- [ ] Whether accreditation is blocking or advisory is configurable (open question).
- [ ] Records are audited.

**REQ:** REQ-FAC-1 · **Compliance:** C20 · **PRD AC:** AC1

### IPC-LOGS — Infection-control & waste logs
`P2` · type:story, PRD-11, phase:1, area:web, compliance

Sterilisation/single-use, sharps & clinical-waste disposal logs, all audited (REQ-FAC-2, C20). Fuller v2 adds manifests + sterilisation register.

> **As a staff member**, I want to keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal, so that we evidence safe practice.

**Acceptance criteria**

- [ ] Sterilisation/single-use and sharps/clinical-waste disposals can be logged and are audited.
- [ ] Logs are retrievable for inspection (feeds PRD-08 pack).
- [ ] A twice-daily cold-chain log with a breach pathway is supported (links PRD-04 cold-chain).
- [ ] Waste manifests/sterilisation register are captured for v2 expansion.

**REQ:** REQ-FAC-2 · **Compliance:** C20 · **PRD AC:** AC2

### EMERGENCY-KIT — Emergency kit & continuity-of-care
`P2` · type:story, PRD-11, phase:1, area:web, compliance

Track the emergency kit (hyaluronidase, anaphylaxis) with expiry alerts and record a continuity-of-care contact (REQ-FAC-3, C20).

> **As a owner**, I want to track the emergency kit with expiry alerts and record a continuity-of-care contact, so that we're prepared for complications and cover when a prescriber is unavailable.

**Acceptance criteria**

- [ ] Emergency-kit items (incl. hyaluronidase, anaphylaxis) raise expiry alerts before lapse.
- [ ] A continuity-of-care contact is recorded and visible when the treating practitioner/prescriber is unavailable.
- [ ] Emergency/complication protocol links are surfaced.
- [ ] Ties into the complication-response flow (PRD-05).

**REQ:** REQ-FAC-3 · **Compliance:** C20 · **PRD AC:** AC1, AC4

### COMPLAINTS — Complaints register with AHPRA pathway
`P1` · type:story, PRD-11, phase:1, area:web, compliance

A complaints/adverse-outcome register linked to client/treatment that surfaces complaint mechanisms incl. AHPRA (NDA doesn't remove the right), feeds retention (complaint → indefinite) and reporting (REQ-CLI-4, C24).

> **As a manager**, I want to log a complaint against a client/treatment and have the system surface the AHPRA pathway, so that complaints are handled correctly and retained.

**Acceptance criteria**

- [ ] A complaint links to the client/treatment and surfaces complaint mechanisms incl. AHPRA (noting NDA doesn't remove the right).
- [ ] A complaint flag drives indefinite retention of the related record (C18, PRD-01).
- [ ] Complaints feed the register/reporting (PRD-08).
- [ ] A complaint can be raised from a conversation (links PRD-07).

**REQ:** REQ-CLI-4 · **Compliance:** C24, C18 · **PRD AC:** AC3

### FAC-WORKFLOWS — Fuller facility workflows (placeholder)
`P2` · type:story, PRD-11, phase:2plus, area:web

Open/close checklist, sterilisation & equipment maintenance register (autoclave validation, spore testing, laser service), deep incident & mandatory-reporting case management — Phase 2 (REQ-FAC-4..10). Placeholder.

> **As a owner**, I want fuller facility workflows: checklists, maintenance registers and incident case management, so that operations and safety are fully systematised.

**Acceptance criteria**

- [ ] Placeholder — v1 is lightweight registers; these workflows are Phase 2.
- [ ] Captured so the facility model anticipates them.

**REQ:** REQ-FAC-4, REQ-FAC-10 · **ADR:** ADR-0026, ADR-0030

---

## PHASE-2 — Phase 2+ / scale (cross-cutting placeholders)
*M7 · Phase 2+ (later / placeholders) · Phase 2+ · 5 stories*

Program-level capability deliberately deferred beyond v1 and not owned by a single feature PRD — the SaaS/scale layer. Tracked as placeholders so scope is visible and can be pulled forward if the business case appears. (Per-feature deferrals live as placeholder stories inside their own PRD epics.)

### MULTI-LOCATION — Multi-location switching UI (placeholder)
`P2` · type:story, PHASE-2, phase:2plus, area:web

Switching between locations/clinics in one tenant. The data model is location-aware; the switching UX is deferred.

> **As a owner of multiple sites**, I want to switch between locations in one place, so that I run several clinics from one login.

**Acceptance criteria**

- [ ] Placeholder — Phase 2+; data model already carries Location.
- [ ] Captured so reporting/booking stay location-aware.

**REQ:** REQ-TEN-1

### SAAS-ONBOARDING — SaaS onboarding & billing UI (placeholder)
`P2` · type:story, PHASE-2, phase:2plus, area:backend

Self-service tenant sign-up, subscription billing and per-tenant Entra federation for selling the platform as SaaS (PRD-01 non-goal; Phase 3).

> **As a prospective clinic**, I want to sign up for the platform myself and pay a subscription, so that onboarding doesn't need manual provisioning.

**Acceptance criteria**

- [ ] Placeholder — Phase 3; v1 provisions tenants manually.
- [ ] Captured so tenancy/identity stay SaaS-ready.

**REQ:** REQ-TEN-1, REQ-TEN-2

### WHITE-LABEL — Per-tenant white-label theming (placeholder)
`P2` · type:story, PHASE-2, phase:2plus, area:design

Per-tenant branding/theming of web and apps (PRD-01 non-goal).

> **As a clinic owner**, I want to brand the platform with my clinic's look, so that clients see my brand.

**Acceptance criteria**

- [ ] Placeholder — Phase 2+; design tokens are themeable by construction.
- [ ] Captured so the design system stays token-driven.

**REQ:** REQ-TEN-1

### PUBLIC-API — Public API & webhooks (placeholder)
`P2` · type:story, PHASE-2, phase:2plus, area:integration

Outbound/inbound public API + webhooks for third parties (PRD-10 deferred; Phase 3).

> **As a integrator**, I want a public API and webhooks, so that third-party tools can integrate.

**Acceptance criteria**

- [ ] Placeholder — Phase 3; internal API is OpenAPI-described already.
- [ ] Captured so the API stays contract-first.

**REQ:** REQ-INT-3

### NATIVE-POS-KIOSK — Native POS hardware & tablet kiosk mode (placeholder)
`P2` · type:story, PHASE-2, phase:2plus, area:web

Native POS hardware integration and a tablet kiosk mode (PRD-06/09 non-goals).

> **As a front desk**, I want native POS hardware and a kiosk check-in mode, so that the desk and waiting room are smoother.

**Acceptance criteria**

- [ ] Placeholder — Phase 2+; v1 uses Square card-present + in-app flows.
- [ ] Captured so checkout/check-in stay hardware-friendly.

**REQ:** REQ-PAY-2, REQ-APP-1
