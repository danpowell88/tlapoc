# Sprint plan & sequencing

> Generated from `docs/backlog/data/*.json`. Regenerate with `python scripts/storydocs.py`.

**Assumptions.** One developer, AI-assisted, ~1–2 days/week (a side project — elapsed time is not the constraint). Sprints are *work-sized*, not calendar-boxed: ~37 story points each (≈5–6 items). Sequencing is dependency-ordered (a story never precedes something it depends on) and grouped by delivery stage.

**Totals.** 330 scheduled stories across 24 sprints (~834 pts), plus 21 deferred items in the backlog.

## Sequence rationale

1. **Sprints 1–5 — Sprint 0 foundations:** repo/CI/CD/IaC, Postgres+RLS, auth wiring, API/web/app shells, design system, observability, security + the de-risk spikes. Nothing clinical ships until the platform is safe to build on.
2. **Foundations & tenancy:** RBAC + scope-of-practice, the canInject gate, audit, retention, breach, sign-in/MFA and owner-only financial gating — unblocks everything.
3. **Booking → intake/consent:** front-of-house + the pre-visit gates.
4. **Consult → prescribing → S4 → charting:** the compliance moat and the clinical record.
5. **Commerce, comms & integrations**, then **reporting & the apps**, then **facility & complaints**.
6. **Backlog (Phase 2+):** deferred placeholders, pulled forward only if the case appears.

## Sprints

| Sprint | Theme | Items | Points |
|---|---|---|---|
| 01 | Setup | 13 | 37 |
| 02 | Setup | 13 | 36 |
| 03 | Foundations | 9 | 37 |
| 04 | Foundations | 14 | 36 |
| 05 | App shell | 13 | 35 |
| 06 | Reception | 13 | 37 |
| 07 | Reception | 18 | 36 |
| 08 | Reception | 14 | 37 |
| 09 | Consent | 14 | 36 |
| 10 | Consent | 16 | 35 |
| 11 | Reception | 11 | 36 |
| 12 | Injectables | 13 | 37 |
| 13 | Charting | 11 | 37 |
| 14 | Charting | 18 | 37 |
| 15 | Reporting | 16 | 36 |
| 16 | Reporting | 15 | 35 |
| 17 | Compliance ops | 16 | 34 |
| 18 | Payments | 10 | 36 |
| 19 | Payments | 18 | 36 |
| 20 | Payments | 15 | 37 |
| 21 | Comms & growth | 18 | 37 |
| 22 | Apps | 13 | 35 |
| 23 | Apps | 18 | 37 |
| 24 | Apps | 1 | 2 |


### Sprint 01 — Setup  ·  13 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Monorepo & solution scaffolding](stories/SPRINT-0__REPO.md) | SPRINT-0 | Chore | P0 | 3 | — |
| [CI/CD pipelines (build, test, deploy)](stories/SPRINT-0__CICD.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/REPO |
| [Cloud environments & infrastructure-as-code (AU East)](stories/SPRINT-0__IAC.md) | SPRINT-0 | Chore | P0 | 3 | — |
| [Postgres + EF Core baseline & migrations](stories/SPRINT-0__DB.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/IAC |
| [Append-only audit infrastructure baseline](stories/SPRINT-0__AUDIT-INFRA.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/DB |
| [Security baseline: encryption, headers, dependency & secret scanning](stories/SPRINT-0__SEC-BASE.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/CICD |
| [Spike — Entra External ID ↔ Flutter ↔ .NET auth](stories/SPRINT-0__SPIKE-AUTH.md) | SPRINT-0 | Spike | P0 | 2 | — |
| [Staff identity: Entra ID SSO + MFA wiring](stories/SPRINT-0__AUTH-STAFF.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/SPIKE-AUTH |
| [Client identity: Entra External ID (social / email / OTP) wiring](stories/SPRINT-0__AUTH-CLIENT.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/SPIKE-AUTH |
| [Spike — Postgres RLS with EF Core session context](stories/SPRINT-0__SPIKE-RLS.md) | SPRINT-0 | Spike | P0 | 2 | — |
| [Row-level-security multi-tenancy baseline](stories/SPRINT-0__RLS.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/DB, SPRINT-0/SPIKE-RLS |
| [.NET API skeleton: architecture, tenant context, error model](stories/SPRINT-0__API.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/RLS, SPRINT-0/AUTH-STAFF |
| [Background jobs & scheduler infrastructure](stories/SPRINT-0__JOBS-SCHEDULER.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/API, SPRINT-0/RLS |

### Sprint 02 — Setup  ·  13 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [OpenAPI contract + typed client generation](stories/SPRINT-0__OPENAPI.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/API |
| [Design system / shared component library + tokens](stories/SPRINT-0__DESIGN.md) | SPRINT-0 | Chore | P1 | 3 | — |
| [Angular web shell: routing, auth guard, layout](stories/SPRINT-0__WEB-SHELL.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUTH-STAFF, SPRINT-0/DESIGN |
| [Flutter app shells (client + provider) + shared packages](stories/SPRINT-0__FLUTTER.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT, SPRINT-0/DESIGN |
| [Secrets & configuration management](stories/SPRINT-0__SECRETS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/IAC |
| [Observability: logging, tracing, metrics, alerting](stories/SPRINT-0__OBS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/API |
| [Test strategy & harness + quality gates](stories/SPRINT-0__TEST.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/CICD, SPRINT-0/RLS |
| [Spike — Square AU card-on-file recurring autopay](stories/SPRINT-0__SPIKE-SQUARE.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Spike — Flutter injection-mapping canvas](stories/SPRINT-0__SPIKE-CANVAS.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Spike — offline queue & sync integrity (provider app)](stories/SPRINT-0__SPIKE-OFFLINE.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Media storage & signed-URL service](stories/SPRINT-0__MEDIA-STORAGE.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/IAC, SPRINT-0/API |
| [Domain-event / messaging backbone](stories/SPRINT-0__DOMAIN-EVENTS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUDIT-INFRA |
| [Synthetic seed data & local dev environment](stories/SPRINT-0__SEED.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/DB |

### Sprint 03 — Foundations  ·  9 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Repo governance: branch protection, PR & env protection](stories/SPRINT-0__GOV.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/CICD |
| [Feature flags & per-tenant configuration](stories/SPRINT-0__FEATURE-FLAGS.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/API |
| [Tenant provisioning & staff invitation](stories/PRD-01__TENANT.md) | PRD-01 | Story | P0 | 5 | — |
| [RBAC + scope-of-practice matrix enforcement](stories/PRD-01__RBAC.md) | PRD-01 | Story | P0 | 5 | PRD-01/TENANT |
| [Staff credentials + canInject compliance gate (core: records + derivation)](stories/PRD-01__CREDENTIALS.md) | PRD-01 | Story | P0 | 5 | PRD-01/RBAC |
| [Exportable audit trail for clinical / medicines / PII](stories/PRD-01__AUDIT.md) | PRD-01 | Story | P0 | 5 | PRD-01/TENANT |
| [Sign-in / sign-out screens & session management](stories/PRD-01__SIGNIN-UI.md) | PRD-01 | Story | P0 | 5 | SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT |
| [Registration / PII / CPD expiry alerting (core: scheduled watch + auto-lapse)](stories/PRD-01__REG-WATCH.md) | PRD-01 | Story | P1 | 3 | PRD-01/CREDENTIALS |
| [Rosters & engagement type (core: roster grid + availability)](stories/PRD-01__ROSTER.md) | PRD-01 | Story | P1 | 3 | PRD-01/CREDENTIALS |

### Sprint 04 — Foundations  ·  14 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Retention policy engine & destruction register](stories/PRD-01__RETENTION.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT |
| [Data-breach assessment & notification workflow](stories/PRD-01__BREACH.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT |
| [Client privacy: collection notice, access & correction (DSAR)](stories/PRD-01__PRIVACY-RIGHTS.md) | PRD-01 | Story | P1 | 3 | PRD-01/TENANT |
| [Data residency & sub-processor controls](stories/PRD-01__RESIDENCY.md) | PRD-01 | Story | P1 | 3 | SPRINT-0/IAC |
| [Client core record: DOB & under-18 flag (core: record + age derivation)](stories/PRD-01__CLIENT-CORE.md) | PRD-01 | Story | P1 | 3 | PRD-01/TENANT |
| [MFA & step-up authentication for sensitive actions](stories/PRD-01__MFA-STEPUP.md) | PRD-01 | Story | P1 | 3 | PRD-01/SIGNIN-UI |
| [Multi-role staff & active-role context](stories/PRD-01__MULTI-ROLE.md) | PRD-01 | Story | P1 | 3 | PRD-01/RBAC |
| [Authentication & authorisation audit events](stories/PRD-01__AUTH-AUDIT.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT, PRD-01/RBAC |
| [Credentials: AHPRA PIE register auto-verification](stories/PRD-01__CREDENTIALS-PIE.md) | PRD-01 | Story | P2 | 2 | PRD-01/CREDENTIALS |
| [Reg-watch: role-targeted routing to digest + Follow-ups](stories/PRD-01__REG-WATCH-ROUTING.md) | PRD-01 | Story | P2 | 2 | PRD-01/REG-WATCH |
| [Reg-watch: 'who is cleared to inject today' compliance board](stories/PRD-01__REG-WATCH-BOARD.md) | PRD-01 | Story | P2 | 2 | PRD-01/REG-WATCH |
| [Reg-watch: amber early-warning countdown chips](stories/PRD-01__REG-WATCH-CHIPS.md) | PRD-01 | Story | P2 | 2 | PRD-01/REG-WATCH |
| [Roster: time-off / leave list with approval](stories/PRD-01__ROSTER-LEAVE.md) | PRD-01 | Story | P2 | 2 | PRD-01/ROSTER |
| [Roster: engagement-type recording for attribution](stories/PRD-01__ROSTER-ENGAGEMENT.md) | PRD-01 | Story | P2 | 2 | PRD-01/ROSTER |

### Sprint 05 — App shell  ·  13 items · 35 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Client core: soft-delete with audit](stories/PRD-01__CLIENT-CORE-SOFTDELETE.md) | PRD-01 | Story | P2 | 2 | PRD-01/CLIENT-CORE |
| [Client core: duplicate detection & reviewed merge](stories/PRD-01__CLIENT-CORE-DEDUPE.md) | PRD-01 | Story | P2 | 2 | PRD-01/CLIENT-CORE |
| [Client core: patient-header age / under-18 chip](stories/PRD-01__CLIENT-CORE-AGECHIP.md) | PRD-01 | Story | P2 | 2 | PRD-01/CLIENT-CORE |
| [Owner-only financial (.fin) capability gating](stories/PLATFORM__FIN-GATING.md) | PLATFORM | Story | P0 | 5 | PRD-01/RBAC |
| [App shell & collapsible workspace navigation](stories/PLATFORM__APP-NAV.md) | PLATFORM | Story | P1 | 3 | SPRINT-0/WEB-SHELL, PRD-01/RBAC |
| [Role-tailored Today dashboard (core: greeting + today's schedule)](stories/PLATFORM__TODAY.md) | PLATFORM | Story | P1 | 3 | PLATFORM/APP-NAV |
| [Active-role context, scope display & multi-role switching](stories/PLATFORM__ROLE-CONTEXT.md) | PLATFORM | Story | P1 | 3 | PRD-01/RBAC, PRD-01/MULTI-ROLE |
| [Today: at-a-glance stat cards](stories/PLATFORM__TODAY-STATCARDS.md) | PLATFORM | Story | P2 | 2 | PLATFORM/TODAY |
| [Today: lifecycle next-action pills + 'WITH YOU NOW' strip](stories/PLATFORM__TODAY-PILLS.md) | PLATFORM | Story | P2 | 2 | PLATFORM/TODAY |
| [Today: Follow-ups preview + needs-attention digest](stories/PLATFORM__TODAY-DIGEST.md) | PLATFORM | Story | P2 | 2 | PLATFORM/TODAY |
| [Global search (clients, appointments, invoices)](stories/PLATFORM__SEARCH.md) | PLATFORM | Story | P2 | 2 | PLATFORM/APP-NAV |
| [Clinic / location switcher](stories/PLATFORM__CLINIC-SWITCH.md) | PLATFORM | Story | P2 | 2 | PRD-01/TENANT |
| [Multi-resource calendar — basic grid & booking](stories/PRD-02__CALENDAR.md) | PRD-02 | Story | P0 | 5 | PRD-01/ROSTER |

### Sprint 06 — Reception  ·  13 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Online self-booking — basic scope-aware flow](stories/PRD-02__ONLINE-BOOK.md) | PRD-02 | Story | P0 | 5 | PRD-02/CALENDAR, PRD-01/CREDENTIALS |
| [Consult gate on injectable appointments](stories/PRD-02__CONSULT-GATE.md) | PRD-02 | Story | P0 | 5 | PRD-02/ONLINE-BOOK |
| [Quiet windows — basic idle-slot detection & list](stories/PRD-02__QUIET-WINDOWS.md) | PRD-02 | Story | P1 | 3 | PRD-02/CALENDAR |
| [Visit lifecycle — basic status state-machine](stories/PRD-02__LIFECYCLE.md) | PRD-02 | Story | P1 | 3 | PRD-02/CALENDAR |
| [Reminders — basic scheduling & dispatch](stories/PRD-02__REMINDERS.md) | PRD-02 | Story | P1 | 3 | PRD-02/LIFECYCLE |
| [Waitlist — basic entries & management](stories/PRD-02__WAITLIST.md) | PRD-02 | Story | P1 | 3 | PRD-02/REMINDERS |
| [Client 360° profile — basic aggregation & header](stories/PRD-02__CLIENT-360.md) | PRD-02 | Story | P1 | 3 | PRD-01/CLIENT-CORE |
| [Calendar: header & date navigation](stories/PRD-02__CALENDAR-HEADER-NAV.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Calendar: day / week view toggle & time-axis layout](stories/PRD-02__CALENDAR-DAYWEEK.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Calendar: resource & practitioner filters](stories/PRD-02__CALENDAR-FILTERS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Calendar: drag-to-book, move & resize](stories/PRD-02__CALENDAR-DRAG.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Calendar: appointment cards, status colours & summary strip](stories/PRD-02__CALENDAR-STATUS-CARDS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Quiet windows: cost-per-treatment / savings framing](stories/PRD-02__QUIET-WINDOWS-COST.md) | PRD-02 | Story | P2 | 2 | PRD-02/QUIET-WINDOWS |

### Sprint 07 — Reception  ·  18 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Quiet windows: stock-expiry / FEFO tie-in](stories/PRD-02__QUIET-WINDOWS-FEFO.md) | PRD-02 | Story | P2 | 2 | PRD-02/QUIET-WINDOWS |
| [Quiet windows: one-click fill (recall / waitlist / campaign)](stories/PRD-02__QUIET-WINDOWS-FILL.md) | PRD-02 | Story | P2 | 2 | PRD-02/QUIET-WINDOWS |
| [Online self-booking: generic names & withheld S4 prices (C9)](stories/PRD-02__ONLINE-BOOK-GENERIC-NAMES.md) | PRD-02 | Story | P2 | 2 | PRD-02/ONLINE-BOOK |
| [Online self-booking: DOB capture & under-18 flag](stories/PRD-02__ONLINE-BOOK-DOB.md) | PRD-02 | Story | P2 | 2 | PRD-02/ONLINE-BOOK |
| [Online self-booking: owner customise & embed panel](stories/PRD-02__ONLINE-BOOK-CUSTOMISE.md) | PRD-02 | Story | P2 | 2 | PRD-02/ONLINE-BOOK |
| [Visit lifecycle: booking capture (new/returning, reason, roster)](stories/PRD-02__LIFECYCLE-BOOKING-CAPTURE.md) | PRD-02 | Story | P2 | 2 | PRD-02/LIFECYCLE |
| [Visit lifecycle: no-show flag → auto follow-up job](stories/PRD-02__LIFECYCLE-NOSHOW-JOB.md) | PRD-02 | Story | P2 | 2 | PRD-02/LIFECYCLE |
| [Visit lifecycle: Today KPI tiles & in-room strip](stories/PRD-02__LIFECYCLE-TODAY-BOARD.md) | PRD-02 | Story | P2 | 2 | PRD-02/LIFECYCLE |
| [Visit lifecycle: per-row role-appropriate next actions](stories/PRD-02__LIFECYCLE-ROW-ACTIONS.md) | PRD-02 | Story | P2 | 2 | PRD-02/LIFECYCLE |
| [Reminders: confirm / decline handling](stories/PRD-02__REMINDERS-CONFIRM-DECLINE.md) | PRD-02 | Story | P2 | 2 | PRD-02/REMINDERS |
| [Reminders: self-service reschedule / cancel within policy](stories/PRD-02__REMINDERS-SELF-SERVICE.md) | PRD-02 | Story | P2 | 2 | PRD-02/REMINDERS |
| [Reminders: cancellation / no-show policy settings](stories/PRD-02__REMINDERS-POLICY.md) | PRD-02 | Story | P2 | 2 | PRD-02/REMINDERS |
| [Waitlist: matching / backfill engine on slot-freed](stories/PRD-02__WAITLIST-MATCHING.md) | PRD-02 | Story | P2 | 2 | PRD-02/WAITLIST |
| [Waitlist: offer lifecycle (offered → accepted / expired)](stories/PRD-02__WAITLIST-OFFER-LIFECYCLE.md) | PRD-02 | Story | P2 | 2 | PRD-02/WAITLIST, PRD-02/WAITLIST-MATCHING |
| [Waitlist: cancel/no-show backfill prompt](stories/PRD-02__WAITLIST-BACKFILL-PROMPT.md) | PRD-02 | Story | P2 | 2 | PRD-02/WAITLIST, PRD-02/WAITLIST-MATCHING |
| [Walk-ins — basic gate-respecting booking](stories/PRD-02__WALKINS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Walk-ins: same-day add-on to an in-progress visit](stories/PRD-02__WALKINS-ADDON.md) | PRD-02 | Story | P2 | 2 | PRD-02/WALKINS |
| [Walk-ins: resource conflict-flagging before confirm](stories/PRD-02__WALKINS-CONFLICT.md) | PRD-02 | Story | P2 | 2 | PRD-02/WALKINS |

### Sprint 08 — Reception  ·  14 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Walk-ins: VIP / first-time tags & distinct rendering](stories/PRD-02__WALKINS-TAGS.md) | PRD-02 | Story | P2 | 2 | PRD-02/WALKINS |
| [Client 360: Overview tab (recent activity & at-a-glance)](stories/PRD-02__CLIENT-360-OVERVIEW.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360 |
| [Client 360: clinical & visit tabs (Visits / Treatment plan / Consents & forms)](stories/PRD-02__CLIENT-360-CLINICAL-TABS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360 |
| [Client 360: commercial tabs (Membership & rewards / Billing / Notes & comms)](stories/PRD-02__CLIENT-360-COMMERCIAL-TABS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360 |
| [Client directory — basic search & list](stories/PRD-02__CLIENT-DIR.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360 |
| [Client directory: segment filters (All / Members / At-risk / New)](stories/PRD-02__CLIENT-DIR-SEGMENTS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-DIR |
| [Client directory: audited soft-delete](stories/PRD-02__CLIENT-DIR-SOFT-DELETE.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-DIR |
| [Client directory: global header search wiring](stories/PRD-02__CLIENT-DIR-HEADER-SEARCH.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-DIR |
| [Client merge — basic duplicate detection & review](stories/PRD-02__CLIENT-MERGE.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-DIR |
| [Client merge: re-point all child records + MergeLog](stories/PRD-02__CLIENT-MERGE-TRANSACTION.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-MERGE |
| [Client merge: confirmation UI & post-merge retirement](stories/PRD-02__CLIENT-MERGE-CONFIRM-UI.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-MERGE, PRD-02/CLIENT-MERGE-TRANSACTION |
| [Pre-visit intake — basic capture & chart-link](stories/PRD-03__INTAKE.md) | PRD-03 | Story | P0 | 5 | PRD-02/ONLINE-BOOK |
| [BDD / psychological screening — basic instrument & scoring](stories/PRD-03__BDD.md) | PRD-03 | Story | P0 | 5 | PRD-03/INTAKE |
| [Versioned e-signed consent — basic signature capture](stories/PRD-03__CONSENT.md) | PRD-03 | Story | P0 | 5 | PRD-03/INTAKE |

### Sprint 09 — Consent  ·  14 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Server-enforced treatment gating](stories/PRD-03__GATING.md) | PRD-03 | Story | P0 | 5 | PRD-03/CONSENT, PRD-03/BDD |
| [Intake-form builder — basic versioned templates](stories/PRD-03__FORM-BUILDER.md) | PRD-03 | Story | P1 | 3 | PRD-03/INTAKE |
| [Consent templates — basic versioned per-treatment templates](stories/PRD-03__CONSENT-TEMPLATE-ADMIN.md) | PRD-03 | Story | P1 | 3 | PRD-03/CONSENT |
| [Image-use consent — basic entity & grant/withdraw](stories/PRD-03__IMAGE-CONSENT.md) | PRD-03 | Story | P1 | 3 | PRD-03/CONSENT |
| [Before/after photo gallery — basic consent-gated view](stories/PRD-02__PHOTOS-GALLERY.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360, PRD-03/IMAGE-CONSENT |
| [Before/after photo gallery: compare & grouping UI](stories/PRD-02__PHOTOS-GALLERY-COMPARE.md) | PRD-02 | Story | P2 | 2 | PRD-02/PHOTOS-GALLERY |
| [Before/after photo gallery: photo-view audit events](stories/PRD-02__PHOTOS-GALLERY-AUDIT.md) | PRD-02 | Story | P2 | 2 | PRD-02/PHOTOS-GALLERY |
| [Cooling-off — basic under-18 7-day enforcement](stories/PRD-03__COOLING-OFF.md) | PRD-03 | Story | P1 | 3 | PRD-01/CLIENT-CORE, PRD-03/CONSENT |
| [Under-18 guardian consent — basic guardian co-signature](stories/PRD-03__GUARDIAN-CONSENT.md) | PRD-03 | Story | P1 | 3 | PRD-03/COOLING-OFF, PRD-03/CONSENT |
| [Pre-visit intake: re-screen vs full form (new/returning)](stories/PRD-03__INTAKE-RESCREEN.md) | PRD-03 | Story | P2 | 2 | PRD-03/INTAKE |
| [Pre-visit intake: medical-history step & quick safety check](stories/PRD-03__INTAKE-MEDICAL-HISTORY.md) | PRD-03 | Story | P2 | 2 | PRD-03/INTAKE |
| [Pre-visit intake: staff status + send/chase](stories/PRD-03__INTAKE-STAFF-STATUS.md) | PRD-03 | Story | P2 | 2 | PRD-03/INTAKE |
| [Intake-form builder: server-side answer validation](stories/PRD-03__FORM-BUILDER-VALIDATION.md) | PRD-03 | Story | P2 | 2 | PRD-03/FORM-BUILDER |
| [Intake-form builder: form-builder admin UI](stories/PRD-03__FORM-BUILDER-ADMIN-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/FORM-BUILDER |

### Sprint 10 — Consent  ·  16 items · 35 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [BDD screening: positive-flag surfacing & RN/NP review requirement](stories/PRD-03__BDD-REVIEW-GATE.md) | PRD-03 | Story | P2 | 2 | PRD-03/BDD |
| [BDD screening: wellbeing questions in the intake wizard](stories/PRD-03__BDD-WELLBEING-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/BDD |
| [BDD screening: prescriber/staff screening chip UI](stories/PRD-03__BDD-STAFF-CHIP.md) | PRD-03 | Story | P2 | 2 | PRD-03/BDD |
| [Consent: plain-language reader & type-to-sign](stories/PRD-03__CONSENT-READER-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/CONSENT |
| [Consent: status chip & blocked-action banner](stories/PRD-03__CONSENT-STATUS-CHIP.md) | PRD-03 | Story | P2 | 2 | PRD-03/CONSENT |
| [Consent templates: mandated-content validation gate on publish](stories/PRD-03__CONSENT-TEMPLATE-MANDATED-GATE.md) | PRD-03 | Story | P2 | 2 | PRD-03/CONSENT-TEMPLATE-ADMIN |
| [Consent templates: authoring UI & audit](stories/PRD-03__CONSENT-TEMPLATE-AUTHORING-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/CONSENT-TEMPLATE-ADMIN |
| [Image-use consent: downstream media-use enforcement on withdraw](stories/PRD-03__IMAGE-CONSENT-ENFORCEMENT.md) | PRD-03 | Story | P2 | 2 | PRD-03/IMAGE-CONSENT |
| [Image-use consent: client self-manage toggle](stories/PRD-03__IMAGE-CONSENT-CLIENT-TOGGLE.md) | PRD-03 | Story | P2 | 2 | PRD-03/IMAGE-CONSENT |
| [Image-use consent: staff header chip](stories/PRD-03__IMAGE-CONSENT-STAFF-CHIP.md) | PRD-03 | Story | P2 | 2 | PRD-03/IMAGE-CONSENT |
| [Cooling-off: payment-block coordination & deposit suppression (F14)](stories/PRD-03__COOLING-OFF-PAYMENT-BLOCK.md) | PRD-03 | Story | P2 | 2 | PRD-03/COOLING-OFF |
| [Cooling-off: optional adult cooling-off config (not a gate)](stories/PRD-03__COOLING-OFF-ADULT-CONFIG.md) | PRD-03 | Story | P2 | 2 | PRD-03/COOLING-OFF |
| [Cooling-off: header chip & done-screen note](stories/PRD-03__COOLING-OFF-CHIP-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/COOLING-OFF |
| [Under-18 guardian consent: recorded second consultation](stories/PRD-03__GUARDIAN-CONSENT-SECOND-CONSULT.md) | PRD-03 | Story | P2 | 2 | PRD-03/GUARDIAN-CONSENT |
| [Under-18 guardian consent: co-sign step in the consent flow](stories/PRD-03__GUARDIAN-CONSENT-COSIGN-UI.md) | PRD-03 | Story | P2 | 2 | PRD-03/GUARDIAN-CONSENT |
| [Synchronous consult record](stories/PRD-04__CONSULT.md) | PRD-04 | Story | P0 | 5 | PRD-02/CONSULT-GATE, PRD-03/GATING |

### Sprint 11 — Reception  ·  11 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Individual prescription (no batch / no async)](stories/PRD-04__PRESCRIPTION.md) | PRD-04 | Story | P0 | 5 | PRD-04/CONSULT, PRD-01/CREDENTIALS |
| [Medicines & product catalogue — core typed catalogue + S4 classification (MVP)](stories/PRD-04__PRODUCT-CATALOGUE.md) | PRD-04 | Story | P0 | 5 | — |
| [Services & treatment menu — basic catalogue & S4 flag](stories/PRD-02__SERVICE-CATALOGUE.md) | PRD-02 | Story | P1 | 3 | PRD-04/PRODUCT-CATALOGUE |
| [Staff booking wizard — basic scope-aware flow](stories/PRD-02__BOOKING-WIZARD.md) | PRD-02 | Story | P1 | 3 | PRD-02/CALENDAR, PRD-02/SERVICE-CATALOGUE |
| [Staff booking wizard: new-client creation, under-18 & intake/consent send](stories/PRD-02__BOOKING-WIZARD-CLIENT-STEP.md) | PRD-02 | Story | P2 | 2 | PRD-02/BOOKING-WIZARD |
| [Staff booking wizard: confirm with policy & reminder scheduling](stories/PRD-02__BOOKING-WIZARD-CONFIRM.md) | PRD-02 | Story | P2 | 2 | PRD-02/BOOKING-WIZARD |
| [Service catalogue: schedule flag wired to scope, rewards & public naming](stories/PRD-02__SERVICE-CATALOGUE-WIRING.md) | PRD-02 | Story | P2 | 2 | PRD-02/SERVICE-CATALOGUE |
| [Service catalogue: capability-gated admin & audit](stories/PRD-02__SERVICE-CATALOGUE-ADMIN.md) | PRD-02 | Story | P2 | 2 | PRD-02/SERVICE-CATALOGUE |
| [Service catalogue: treatment-menu card UI & status filter](stories/PRD-02__SERVICE-CATALOGUE-CARD-UI.md) | PRD-02 | Story | P2 | 2 | PRD-02/SERVICE-CATALOGUE |
| [Stock receipt: ARTG & lawful-supply provenance per lot (MVP)](stories/PRD-04__STOCK-RECEIVE.md) | PRD-04 | Story | P0 | 5 | PRD-04/PRODUCT-CATALOGUE |
| [Administration gating & immutable record](stories/PRD-04__ADMIN-GATE.md) | PRD-04 | Story | P0 | 5 | PRD-04/PRESCRIPTION, PRD-04/STOCK-RECEIVE |

### Sprint 12 — Injectables  ·  13 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Custody & secure storage: exclusive-custody binding (MVP)](stories/PRD-04__CUSTODY-STORAGE.md) | PRD-04 | Story | P0 | 5 | PRD-04/STOCK-RECEIVE |
| [Lot → clients recall lookup & medicine register (MVP)](stories/PRD-04__RECALL-LOOKUP.md) | PRD-04 | Story | P0 | 5 | PRD-04/ADMIN-GATE |
| [Stock at-a-glance: KPI tiles (MVP)](stories/PRD-04__STOCK-OVERVIEW.md) | PRD-04 | Story | P1 | 3 | PRD-04/STOCK-RECEIVE |
| [Temperature logging & excursion alerts (manual + ESP32) (MVP)](stories/PRD-04__COLD-CHAIN.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |
| [Vial / unit reconciliation](stories/PRD-04__VIAL-RECON.md) | PRD-04 | Story | P1 | 3 | PRD-04/ADMIN-GATE |
| [Wastage recording (partial-vial) (MVP)](stories/PRD-04__WASTAGE-DESTRUCTION.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |
| [Stocktake & discrepancy surfacing (MVP)](stories/PRD-04__STOCKTAKE.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |
| [Product catalogue: per-product on-hand cards, usage history & below-par](stories/PRD-04__PRODUCT-CATALOGUE-CARDS.md) | PRD-04 | Story | P2 | 2 | PRD-04/PRODUCT-CATALOGUE |
| [Product catalogue: schedule-change classification fan-out + audit](stories/PRD-04__PRODUCT-CATALOGUE-FANOUT.md) | PRD-04 | Story | P2 | 2 | PRD-04/PRODUCT-CATALOGUE |
| [S4 purchase orders: prescriber-signer & approved-wholesaler gate](stories/PRD-04__STOCK-RECEIVE-PO-SIGNER.md) | PRD-04 | Story | P2 | 2 | PRD-04/STOCK-RECEIVE |
| [Stock overview: usage-history chart](stories/PRD-04__STOCK-OVERVIEW-USAGE.md) | PRD-04 | Story | P2 | 2 | PRD-04/STOCK-OVERVIEW |
| [Stock overview: reduce-waste & lift-margin nudges (FEFO, non-S4)](stories/PRD-04__STOCK-OVERVIEW-NUDGES.md) | PRD-04 | Story | P2 | 2 | PRD-04/STOCK-OVERVIEW |
| [Custody & storage: access-logged cabinet monitor (CM-01)](stories/PRD-04__CUSTODY-CABINET-MONITOR.md) | PRD-04 | Story | P2 | 2 | PRD-04/CUSTODY-STORAGE |

### Sprint 13 — Charting  ·  11 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Cold chain: commercial-logger adapters (Testo / Dickson / LogTag)](stories/PRD-04__COLD-CHAIN-COMMERCIAL-LOGGERS.md) | PRD-04 | Story | P2 | 2 | PRD-04/COLD-CHAIN |
| [Recall execution & acknowledgement tracking](stories/PRD-04__RECALL-EXECUTION.md) | PRD-04 | Story | P2 | 2 | PRD-04/RECALL-LOOKUP |
| [Witnessed destruction & disposal records (licensed/RUM + certificate)](stories/PRD-04__DESTRUCTION-RECORDS.md) | PRD-04 | Story | P2 | 2 | PRD-04/WASTAGE-DESTRUCTION |
| [Loss / theft reporting from a stock discrepancy](stories/PRD-04__STOCK-LOSS-THEFT.md) | PRD-04 | Story | P2 | 2 | PRD-04/STOCKTAKE |
| [Guided toxin note: pre-treatment review & gate (MVP)](stories/PRD-05__NOTE-TEMPLATE.md) | PRD-05 | Story | P0 | 5 | PRD-04/ADMIN-GATE |
| [Injection-mapping canvas: add/edit points + save draft (MVP)](stories/PRD-05__MAPPING.md) | PRD-05 | Story | P0 | 5 | SPRINT-0/SPIKE-CANVAS, PRD-04/RECALL-LOOKUP |
| [Charting product & batch (lot) selector (MVP)](stories/PRD-05__PRODUCT-LOT-PICKER.md) | PRD-05 | Story | P0 | 5 | PRD-05/MAPPING |
| [Immutable finalisation & audited amendments](stories/PRD-05__IMMUTABILITY.md) | PRD-05 | Story | P0 | 5 | PRD-05/MAPPING |
| [Clinical photo capture: signed-URL storage & consent gate (MVP)](stories/PRD-05__PHOTOS.md) | PRD-05 | Story | P1 | 3 | PRD-03/IMAGE-CONSENT |
| [Offline queue & sync for room-side charting](stories/PRD-05__OFFLINE.md) | PRD-05 | Story | P1 | 3 | SPRINT-0/SPIKE-OFFLINE, PRD-05/IMMUTABILITY |
| [Adverse-event capture & DAEN routing (MVP)](stories/PRD-05__ADVERSE-EVENT.md) | PRD-05 | Story | P1 | 3 | PRD-05/IMMUTABILITY |

### Sprint 14 — Charting  ·  18 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Complication protocol library & timestamped response (MVP)](stories/PRD-05__COMPLICATION-LIBRARY.md) | PRD-05 | Story | P1 | 3 | PRD-05/ADVERSE-EVENT |
| [Charting: treatment-type toggle (toxin / non-S4 skin)](stories/PRD-05__NOTE-TEMPLATE-TYPE-TOGGLE.md) | PRD-05 | Story | P2 | 2 | PRD-05/NOTE-TEMPLATE |
| [Charting: configurable, versioned note-template engine + snippet admin](stories/PRD-05__NOTE-TEMPLATE-ENGINE.md) | PRD-05 | Story | P2 | 2 | PRD-05/NOTE-TEMPLATE |
| [Injection map: finalise → transactional stock deduction + register link](stories/PRD-05__MAPPING-FINALISE.md) | PRD-05 | Story | P2 | 2 | PRD-05/MAPPING |
| [Injection map: per-point depth, technique & multi-product lot](stories/PRD-05__MAPPING-POINT-DEPTH.md) | PRD-05 | Story | P2 | 2 | PRD-05/MAPPING |
| [Charting: non-S4 skin-note variant fields](stories/PRD-05__MAPPING-SKIN-NOTE.md) | PRD-05 | Story | P2 | 2 | PRD-05/MAPPING |
| [Charting lot picker: lot-required-before-points gate](stories/PRD-05__PRODUCT-LOT-PICKER-GATE.md) | PRD-05 | Story | P2 | 2 | PRD-05/PRODUCT-LOT-PICKER |
| [Clinical photos: before/after compare, per-pose gallery & annotation](stories/PRD-05__PHOTOS-COMPARE.md) | PRD-05 | Story | P2 | 2 | PRD-05/PHOTOS |
| [Clinical photos: on-device transient cache & post-sync purge](stories/PRD-05__PHOTOS-OFFLINE-CACHE.md) | PRD-05 | Story | P2 | 2 | PRD-05/PHOTOS |
| [Adverse event: follow-up jobs & route to Governance](stories/PRD-05__ADVERSE-EVENT-JOBS.md) | PRD-05 | Story | P2 | 2 | PRD-05/ADVERSE-EVENT |
| [Treatment plans & protocol templates (MVP)](stories/PRD-05__TREATMENT-PLANS.md) | PRD-05 | Story | P2 | 2 | PRD-05/NOTE-TEMPLATE |
| [Treatment plans: project upcoming sessions as recall jobs](stories/PRD-05__TREATMENT-PLANS-RECALL.md) | PRD-05 | Story | P2 | 2 | PRD-05/TREATMENT-PLANS |
| [Treatment plans: protocol builder, Client 360 progress & in-room list](stories/PRD-05__TREATMENT-PLANS-VIEWS.md) | PRD-05 | Story | P2 | 2 | PRD-05/TREATMENT-PLANS |
| [Skin analysis: recommended-plan chips feeding treatment plans](stories/PRD-05__SKIN-ANALYSIS-RECOMMEND.md) | PRD-05 | Story | P2 | 2 | PRD-05/SKIN-ANALYSIS |
| [Skin analysis: consent-respecting push to client app](stories/PRD-05__SKIN-ANALYSIS-PUSH.md) | PRD-05 | Story | P2 | 2 | PRD-05/SKIN-ANALYSIS |
| [Body contouring: consumable cost roll-up into true cost & margin](stories/PRD-05__BODY-CONTOURING-COST.md) | PRD-05 | Story | P2 | 2 | PRD-05/BODY-CONTOURING |
| [Body contouring: standardised body photos & measurements over the course](stories/PRD-05__BODY-CONTOURING-PROGRESS.md) | PRD-05 | Story | P2 | 2 | PRD-05/BODY-CONTOURING |
| [Complication protocols: emergency-kit register linkage & expiry surfacing](stories/PRD-05__COMPLICATION-KIT-LINK.md) | PRD-05 | Story | P2 | 2 | PRD-05/COMPLICATION-LIBRARY |

### Sprint 15 — Reporting  ·  16 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Outcomes: per-treatment/practitioner aggregation & reporting feed](stories/PRD-05__OUTCOMES-REPORTING.md) | PRD-05 | Story | P2 | 2 | PRD-05/OUTCOMES |
| [Reporting read-models / materialized views](stories/PRD-08__READ-MODELS.md) | PRD-08 | Story | P1 | 3 | PRD-01/AUDIT |
| [Business analytics dashboards (core: metrics read-model + headline tiles)](stories/PRD-08__BUSINESS-DASH.md) | PRD-08 | Story | P1 | 3 | PRD-08/READ-MODELS |
| [Compliance dashboards (core: overview band + consent & consult adherence)](stories/PRD-08__COMPLIANCE-DASH.md) | PRD-08 | Story | P1 | 3 | PRD-08/READ-MODELS, PRD-04/RECALL-LOOKUP |
| [Adverse-event / DAEN prefilled submission](stories/PRD-08__DAEN.md) | PRD-08 | Story | P1 | 3 | PRD-05/ADVERSE-EVENT |
| [Business dashboards: custom range & per-practitioner filter](stories/PRD-08__BUSINESS-DASH-FILTERS.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Business dashboards: GROWTH band tiles](stories/PRD-08__BUSINESS-DASH-GROWTH.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Business dashboards: PERFORMANCE band tiles](stories/PRD-08__BUSINESS-DASH-PERF.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Business dashboards: FINANCE band tiles](stories/PRD-08__BUSINESS-DASH-FINANCE.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Business dashboards: Insights strip + reward-cost-vs-retention](stories/PRD-08__BUSINESS-DASH-INSIGHTS.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Business dashboards: owner Targets editor](stories/PRD-08__BUSINESS-DASH-TARGETS.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Retention cohort analysis (core: cohort grid)](stories/PRD-08__RETENTION-COHORTS.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Retention: at-risk / lapsed worklist + reactivation hand-off](stories/PRD-08__RETENTION-ATRISK.md) | PRD-08 | Story | P2 | 2 | PRD-08/RETENTION-COHORTS |
| [Compliance: S4 register export](stories/PRD-08__COMPLIANCE-DASH-S4REGISTER.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Compliance: lot → clients recall lookup](stories/PRD-08__COMPLIANCE-DASH-RECALL.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH, PRD-04/RECALL-LOOKUP |
| [Compliance: breach & complaints registers](stories/PRD-08__COMPLIANCE-DASH-REGISTERS.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |

### Sprint 16 — Reporting  ·  15 items · 35 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Compliance: registration-expiry watch & records-due lists](stories/PRD-08__COMPLIANCE-DASH-EXPIRY.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Data-quality checks](stories/PRD-08__DATA-QUALITY.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS |
| [Owner 'needs attention' exceptions digest](stories/PRD-08__ATTENTION-DIGEST.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Inspection-readiness pack & governance hub](stories/PRD-08__INSPECTION-PACK.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Policies & procedures sign-off](stories/PRD-08__POLICIES.md) | PRD-08 | Story | P1 | 3 | PRD-08/INSPECTION-PACK |
| [Practitioner scorecard](stories/PRD-08__SCORECARD.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Capacity & utilisation report](stories/PRD-08__CAPACITY.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS |
| [True-cost / margin (COGS) reporting](stories/PRD-08__TRUE-COST.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS, PRD-04/VIAL-RECON |
| [Per-procedure cost catalogue (core: cost model + editor)](stories/PRD-08__COST-CATALOGUE.md) | PRD-08 | Story | P2 | 2 | PRD-08/TRUE-COST |
| [Cost catalogue: single-source feed to margin report + pricing planner](stories/PRD-08__COST-CATALOGUE-FEED.md) | PRD-08 | Story | P2 | 2 | PRD-08/COST-CATALOGUE |
| [Cost catalogue: consumable → Stock auto-decrement](stories/PRD-08__COST-CATALOGUE-STOCK.md) | PRD-08 | Story | P2 | 2 | PRD-08/COST-CATALOGUE |
| [Complaints register with AHPRA pathway (basic)](stories/PRD-11__COMPLAINTS.md) | PRD-11 | Story | P1 | 3 | — |
| [Complaint → indefinite retention flag](stories/PRD-11__COMPLAINT-RETENTION.md) | PRD-11 | Story | P1 | 3 | PRD-11/COMPLAINTS, PRD-01/PRIVACY-RIGHTS |
| [Daily open/close checklist (basic)](stories/PRD-11__OPENCLOSE.md) | PRD-11 | Story | P1 | 3 | PRD-04/COLD-CHAIN |
| [Open/close: manual fridge-temp log + breach pathway](stories/PRD-11__OPENCLOSE-FRIDGE.md) | PRD-11 | Story | P1 | 3 | PRD-11/OPENCLOSE, PRD-04/COLD-CHAIN |

### Sprint 17 — Compliance ops  ·  16 items · 34 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Temperature monitor management (basic)](stories/PRD-11__TEMP-MONITORS.md) | PRD-11 | Story | P1 | 3 | PRD-04/COLD-CHAIN |
| [Cold-chain: reconcile device + manual readings](stories/PRD-11__MONITOR-RECONCILE.md) | PRD-11 | Story | P1 | 3 | PRD-11/TEMP-MONITORS, PRD-11/OPENCLOSE-FRIDGE |
| [Facility accreditation register (basic)](stories/PRD-11__FACILITY.md) | PRD-11 | Story | P2 | 2 | — |
| [Facility: accreditation expiry alerts](stories/PRD-11__FACILITY-ALERTS.md) | PRD-11 | Story | P2 | 2 | PRD-11/FACILITY |
| [Facility: blocking-vs-advisory enforcement](stories/PRD-11__FACILITY-ENFORCE.md) | PRD-11 | Story | P2 | 2 | PRD-11/FACILITY |
| [Infection-control & waste logs](stories/PRD-11__IPC-LOGS.md) | PRD-11 | Story | P2 | 2 | — |
| [Emergency kit register (basic)](stories/PRD-11__EMERGENCY-KIT.md) | PRD-11 | Story | P2 | 2 | — |
| [Emergency kit: expiry alerts](stories/PRD-11__KIT-ALERTS.md) | PRD-11 | Story | P2 | 2 | PRD-11/EMERGENCY-KIT |
| [Emergency kit: complication protocols + 'Start response'](stories/PRD-11__KIT-PROTOCOLS.md) | PRD-11 | Story | P2 | 2 | PRD-11/EMERGENCY-KIT, PRD-05/ADVERSE-EVENT |
| [Continuity-of-care contact](stories/PRD-11__CONTINUITY-CONTACT.md) | PRD-11 | Story | P2 | 2 | PRD-11/EMERGENCY-KIT |
| [Rooms & devices register (basic)](stories/PRD-11__ROOMS-DEVICES.md) | PRD-11 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Resources: calendar exposure + conflict-flagging](stories/PRD-11__RESOURCE-CALENDAR.md) | PRD-11 | Story | P2 | 2 | PRD-11/ROOMS-DEVICES, PRD-02/CALENDAR |
| [Equipment & maintenance register (basic)](stories/PRD-11__EQUIPMENT.md) | PRD-11 | Story | P2 | 2 | PRD-11/ROOMS-DEVICES |
| [Resources: out-of-service + equipment-maintenance link](stories/PRD-11__RESOURCE-SERVICE.md) | PRD-11 | Story | P2 | 2 | PRD-11/ROOMS-DEVICES, PRD-11/EQUIPMENT |
| [Equipment: due/overdue maintenance alerts](stories/PRD-11__EQUIPMENT-ALERTS.md) | PRD-11 | Story | P2 | 2 | PRD-11/EQUIPMENT |
| [Equipment: log service events with evidence](stories/PRD-11__EQUIPMENT-EVIDENCE.md) | PRD-11 | Story | P2 | 2 | PRD-11/EQUIPMENT |

### Sprint 18 — Payments  ·  10 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Payment provider abstraction + Square adapter](stories/PRD-06__PAYMENT-PROVIDER.md) | PRD-06 | Story | P0 | 5 | SPRINT-0/SPIKE-SQUARE |
| [In-person POS checkout — basic cart + single tender (core)](stories/PRD-06__POS.md) | PRD-06 | Story | P0 | 5 | PRD-06/PAYMENT-PROVIDER |
| [Membership join + card-on-file — basic enrolment (core)](stories/PRD-06__MEMBERSHIP.md) | PRD-06 | Story | P0 | 5 | PRD-06/PAYMENT-PROVIDER |
| [Rewards engine — non-S4 points earn/redeem + S4 block (core)](stories/PRD-06__REWARDS-ENGINE.md) | PRD-06 | Story | P0 | 5 | PRD-04/PRODUCT-CATALOGUE |
| [Packages/series: sell & redeem (visits remaining) — basic pre-paid value (core)](stories/PRD-06__PACKAGES-GIFT.md) | PRD-06 | Story | P1 | 3 | PRD-06/POS |
| [Daily closeout — card + cash rollup, count & lock (core)](stories/PRD-06__CLOSEOUT.md) | PRD-06 | Story | P1 | 3 | PRD-06/POS |
| [Membership plans & tiers — define plans + non-S4 benefit constraint (core)](stories/PRD-06__MEMBERSHIP-PLANS.md) | PRD-06 | Story | P1 | 3 | PRD-06/MEMBERSHIP |
| [Margin-aware reward rules](stories/PRD-06__MARGIN-RULES.md) | PRD-06 | Story | P1 | 3 | PRD-06/REWARDS-ENGINE |
| [Checkout: per-line GST (goods and services tax)](stories/PRD-06__POS-GST.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Checkout: split / partial tenders, tips & card surcharge](stories/PRD-06__POS-SPLIT-TENDER.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |

### Sprint 19 — Payments  ·  18 items · 36 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Checkout: member-reward & store-credit deduction lines (non-S4)](stories/PRD-06__POS-DEDUCTIONS.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Checkout: Square-terminal modal (Processing → Approved) + decline path](stories/PRD-06__POS-TERMINAL-MODAL.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Checkout: post completed sale to Xero (per-line tax mapping)](stories/PRD-06__POS-XERO-POST.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Gift cards: issue, balance-track & partial redeem](stories/PRD-06__PACKAGES-GIFTCARD.md) | PRD-06 | Story | P2 | 2 | PRD-06/PACKAGES-GIFT |
| [Client store-credit & AR (accounts receivable) ageing](stories/PRD-06__PACKAGES-CREDIT-AR.md) | PRD-06 | Story | P2 | 2 | PRD-06/PACKAGES-GIFT |
| [Closeout: Square-batch variance detection & annotation](stories/PRD-06__CLOSEOUT-VARIANCE.md) | PRD-06 | Story | P2 | 2 | PRD-06/CLOSEOUT |
| [Closeout: reconcile to the Xero posting](stories/PRD-06__CLOSEOUT-XERO-RECONCILE.md) | PRD-06 | Story | P2 | 2 | PRD-06/CLOSEOUT |
| [Closeout: back-office tablet surface](stories/PRD-06__CLOSEOUT-BACKROOM.md) | PRD-06 | Story | P2 | 2 | PRD-06/CLOSEOUT |
| [Membership: autopay scheduler (off-session recurring charge)](stories/PRD-06__MEMBERSHIP-AUTOPAY.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP |
| [Membership: failed-payment dunning (retry-and-chase) + manual Retry](stories/PRD-06__MEMBERSHIP-DUNNING.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP-AUTOPAY |
| [Membership: lifecycle (pause / cancel / win-back) → MRR/churn](stories/PRD-06__MEMBERSHIP-LIFECYCLE.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP |
| [Membership: benefits & credits auto-apply at checkout (non-S4)](stories/PRD-06__MEMBERSHIP-BENEFITS.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP |
| [Membership: members & billing list + overview KPIs](stories/PRD-06__MEMBERSHIP-MEMBERS.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP |
| [Membership plans: capability-gated admin, audit & member-term preservation](stories/PRD-06__MEMBERSHIP-PLANS-ADMIN.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP-PLANS |
| [Membership plans: Plans & packages tab UI (tier cards + per-tier MRR)](stories/PRD-06__MEMBERSHIP-PLANS-UI.md) | PRD-06 | Story | P2 | 2 | PRD-06/MEMBERSHIP-PLANS |
| [Rewards: loyalty tiers (Silver / Gold / Platinum) + top balances](stories/PRD-06__REWARDS-TIERS.md) | PRD-06 | Story | P2 | 2 | PRD-06/REWARDS-ENGINE |
| [Rewards: Loyalty screen UI](stories/PRD-06__REWARDS-LOYALTY-UI.md) | PRD-06 | Story | P2 | 2 | PRD-06/REWARDS-ENGINE |
| [Post-visit rebooking on the treatment interval (core)](stories/PRD-06__CHECKOUT-ASSIST.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |

### Sprint 20 — Payments  ·  15 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Checkout: 'Worth mentioning' upsell panel (membership / restock / rebook cue)](stories/PRD-06__CHECKOUT-UPSELL.md) | PRD-06 | Story | P2 | 2 | PRD-06/CHECKOUT-ASSIST |
| [Checkout: client-rapport panel (derived from history)](stories/PRD-06__CHECKOUT-RAPPORT.md) | PRD-06 | Story | P2 | 2 | PRD-06/CHECKOUT-ASSIST |
| [Checkout: 'Pairs well with today's treatment' non-S4 cross-sell](stories/PRD-06__CHECKOUT-CROSSSELL.md) | PRD-06 | Story | P2 | 2 | PRD-06/CHECKOUT-ASSIST |
| [Pricing & what-if — editable plan prices + projected impact (core)](stories/PRD-06__PRICING-WHATIF.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Pricing & what-if: churn-sensitivity slider](stories/PRD-06__PRICING-CHURN-SLIDER.md) | PRD-06 | Story | P2 | 2 | PRD-06/PRICING-WHATIF |
| [Pricing & what-if: editable service-pricing rows](stories/PRD-06__PRICING-SERVICE-ROWS.md) | PRD-06 | Story | P2 | 2 | PRD-06/PRICING-WHATIF |
| [Pricing & what-if: save scenario + apply-via-admin handoff](stories/PRD-06__PRICING-SAVE-APPLY.md) | PRD-06 | Story | P2 | 2 | PRD-06/PRICING-WHATIF |
| [Pricing & what-if: Finance hub framing (defers to Xero)](stories/PRD-06__PRICING-FINANCE-HUB.md) | PRD-06 | Story | P2 | 2 | PRD-06/PRICING-WHATIF |
| [Notification channels (SMS / email / push)](stories/PRD-07__CHANNELS.md) | PRD-07 | Story | P0 | 5 | — |
| [In-app notification centre](stories/PLATFORM__NOTIFICATIONS.md) | PLATFORM | Story | P2 | 2 | PLATFORM/APP-NAV, PRD-07/CHANNELS |
| [Appointment reminders & confirmations — basic sequence (core)](stories/PRD-07__REMINDERS-CARE.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Recall / recare worklist](stories/PRD-07__RECALL.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Marketing consent & functional unsubscribe (Spam Act)](stories/PRD-07__MARKETING-CONSENT.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Public booking page: schedule-driven generic names & withheld S4 prices (core)](stories/PRD-07__BOOKING-PAGE.md) | PRD-07 | Story | P1 | 3 | PRD-02/ONLINE-BOOK |
| [Pre-care instruction sequences (per treatment type)](stories/PRD-07__PRECARE.md) | PRD-07 | Story | P2 | 2 | PRD-07/REMINDERS-CARE |

### Sprint 21 — Comms & growth  ·  18 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Aftercare instruction sequences (day-0 + day-3, per treatment type)](stories/PRD-07__AFTERCARE.md) | PRD-07 | Story | P2 | 2 | PRD-07/REMINDERS-CARE |
| [Public booking page: Settings config screen + live preview](stories/PRD-07__BOOKING-PAGE-SETTINGS.md) | PRD-07 | Story | P2 | 2 | PRD-07/BOOKING-PAGE |
| [Unified follow-up / job queue — projected signals + lifecycle (core)](stories/PRD-07__FOLLOWUPS.md) | PRD-07 | Story | P2 | 2 | PRD-07/CHANNELS |
| [Complaints: reporting feed + raise-from-conversation](stories/PRD-11__COMPLAINT-REPORTING.md) | PRD-11 | Story | P2 | 2 | PRD-11/COMPLAINTS, PRD-07/FOLLOWUPS |
| [Call / phone log (basic)](stories/PRD-11__CALL-LOG.md) | PRD-11 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Call log: callback job + comms history](stories/PRD-11__CALL-FOLLOWUP.md) | PRD-11 | Story | P2 | 2 | PRD-11/CALL-LOG, PRD-07/FOLLOWUPS |
| [Call log: shared follow-up queue (walk-ins / waitlist)](stories/PRD-11__CALL-QUEUE.md) | PRD-11 | Story | P2 | 2 | PRD-11/CALL-LOG, PRD-07/FOLLOWUPS |
| [Shift handover notes](stories/PRD-11__SHIFT-HANDOVER.md) | PRD-11 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Follow-ups: manual flag → Job](stories/PRD-07__FOLLOWUPS-FLAG.md) | PRD-07 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Follow-ups: rules/keyword auto-categorisation (no AI)](stories/PRD-07__FOLLOWUPS-AUTOCAT.md) | PRD-07 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Automation builder — toggleable automations + consent split (core)](stories/PRD-07__AUTOMATIONS.md) | PRD-07 | Story | P2 | 2 | PRD-07/REMINDERS-CARE |
| [Automations: per-treatment-type editing](stories/PRD-07__AUTOMATIONS-PER-TREATMENT.md) | PRD-07 | Story | P2 | 2 | PRD-07/AUTOMATIONS |
| [Automations: live stats (sent / booked / returned)](stories/PRD-07__AUTOMATIONS-STATS.md) | PRD-07 | Story | P2 | 2 | PRD-07/AUTOMATIONS |
| [Reviews: auto-detect negative reviews / complaint keywords → Job](stories/PRD-07__REVIEWS-AUTODETECT.md) | PRD-07 | Story | P2 | 2 | PRD-07/REVIEWS |
| [Reviews: screen UI + reputation KPIs](stories/PRD-07__REVIEWS-SCREEN-KPI.md) | PRD-07 | Story | P2 | 2 | PRD-07/REVIEWS |
| [Leads: consent-gated outbound nudges (1:1 replies exempt, C23)](stories/PRD-07__LEADS-NUDGES.md) | PRD-07 | Story | P2 | 2 | PRD-07/LEADS-CRM |
| [Leads: conversion KPIs + Follow-ups queue projection](stories/PRD-07__LEADS-KPI-FOLLOWUPS.md) | PRD-07 | Story | P2 | 2 | PRD-07/LEADS-CRM |
| [Xero invoice/payment sync (basic)](stories/PRD-10__XERO.md) | PRD-10 | Story | P1 | 3 | PRD-06/POS |

### Sprint 22 — Apps  ·  13 items · 35 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Xero: resilient idempotent SyncJob + OAuth lifecycle](stories/PRD-10__XERO-SYNCJOB.md) | PRD-10 | Story | P1 | 3 | PRD-10/XERO |
| [Xero: Settings card + mapping editor + reconciliation list](stories/PRD-10__XERO-RECON-UI.md) | PRD-10 | Story | P2 | 2 | PRD-10/XERO, PRD-10/XERO-SYNCJOB |
| [Calendar sync: outbound push (basic)](stories/PRD-10__CALENDAR-SYNC.md) | PRD-10 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Calendar sync: inbound busy-time → availability blocks](stories/PRD-10__CALENDAR-INBOUND.md) | PRD-10 | Story | P2 | 2 | PRD-10/CALENDAR-SYNC, PRD-02/CALENDAR |
| [Sub-processor residency posture (APP-8)](stories/PRD-10__SUBPROCESSOR-POSTURE.md) | PRD-10 | Story | P2 | 2 | PRD-01/RESIDENCY |
| [Client app: shell, sign-in & home (basic)](stories/PRD-09__CLIENT-JOURNEY.md) | PRD-09 | Story | P1 | 3 | PRD-02/ONLINE-BOOK, PRD-03/CONSENT |
| [Provider app: day schedule & open patient](stories/PRD-09__PROVIDER-DAY.md) | PRD-09 | Story | P1 | 3 | PRD-05/NOTE-TEMPLATE |
| [Provider app: room-side injection mapping (basic)](stories/PRD-09__PROVIDER-ROOMSIDE.md) | PRD-09 | Story | P1 | 3 | PRD-09/PROVIDER-DAY, PRD-05/MAPPING |
| [Provider app: native-camera before/after capture](stories/PRD-09__PROVIDER-CAMERA.md) | PRD-09 | Story | P1 | 3 | PRD-09/PROVIDER-ROOMSIDE, PRD-05/PHOTOS |
| [Provider app: server-side finalise → immutable record](stories/PRD-09__PROVIDER-FINALISE.md) | PRD-09 | Story | P1 | 3 | PRD-09/PROVIDER-ROOMSIDE, PRD-05/MAPPING |
| [Provider app: offline-tolerant workflows + sync indicator](stories/PRD-09__PROVIDER-OFFLINE.md) | PRD-09 | Story | P1 | 3 | PRD-05/OFFLINE |
| [Client 'report a concern' → follow-up bridge (basic)](stories/PRD-09__CLIENT-CONCERN.md) | PRD-09 | Story | P1 | 3 | PRD-07/FOLLOWUPS |
| [Staff Follow-ups: view / call back / resolve a concern](stories/PRD-09__CONCERN-TRIAGE.md) | PRD-09 | Story | P1 | 3 | PRD-09/CLIENT-CONCERN, PRD-07/FOLLOWUPS |

### Sprint 23 — Apps  ·  18 items · 37 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Concern: escalate to adverse event / complaint](stories/PRD-09__CONCERN-ESCALATE.md) | PRD-09 | Story | P1 | 3 | PRD-09/CLIENT-CONCERN, PRD-05/ADVERSE-EVENT |
| [Client app: in-app booking over PRD-02](stories/PRD-09__CLIENT-BOOK.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-JOURNEY, PRD-02/ONLINE-BOOK |
| [Client app: intake + consent, e-signed on device](stories/PRD-09__CLIENT-INTAKE.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-JOURNEY, PRD-03/CONSENT |
| [Client app: push token + notification inbox](stories/PRD-09__CLIENT-PUSH.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-JOURNEY, PRD-07/FOLLOWUPS |
| [Client app: my care health hub (basic)](stories/PRD-09__CLIENT-CARE.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-JOURNEY, PRD-05/PHOTOS |
| [Client app: rewards, perks & referrals](stories/PRD-09__CLIENT-REWARDS.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-CARE, PRD-06/MEMBERSHIP |
| [Client app: account, memberships & card-on-file](stories/PRD-09__CLIENT-ACCOUNT.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-CARE, PRD-06/MEMBERSHIP |
| [Client app: consent-gated before/after gallery with drag-to-compare](stories/PRD-09__PHOTO-COMPARE.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-CARE, PRD-02/PHOTOS-GALLERY |
| [Client app: day-by-day aftercare guidance + escalation](stories/PRD-09__AFTERCARE-GUIDE.md) | PRD-09 | Story | P2 | 2 | PRD-09/CLIENT-CARE, PRD-09/CLIENT-CONCERN |
| [Client app: account, privacy & access/correction](stories/PRD-09__CLIENT-PRIVACY.md) | PRD-09 | Story | P2 | 2 | PRD-01/PRIVACY-RIGHTS |
| [App distribution & code-push posture](stories/PRD-09__APP-DISTRIBUTION.md) | PRD-09 | Story | P2 | 2 | SPRINT-0/FLUTTER |
| [Reception self-check-in surface (basic)](stories/PRD-09__CHECKIN-KIOSK.md) | PRD-09 | Story | P2 | 2 | PRD-02/LIFECYCLE |
| [Kiosk: details review + today's health check](stories/PRD-09__CHECKIN-DETAILS.md) | PRD-09 | Story | P2 | 2 | PRD-09/CHECKIN-KIOSK, PRD-03/GATING |
| [Kiosk: outstanding intake/consent at the desk](stories/PRD-09__CHECKIN-FORMS.md) | PRD-09 | Story | P2 | 2 | PRD-09/CHECKIN-KIOSK, PRD-03/GATING |
| [Kiosk: reception arrivals board feed](stories/PRD-09__CHECKIN-ARRIVALS.md) | PRD-09 | Story | P2 | 2 | PRD-09/CHECKIN-KIOSK, PRD-02/LIFECYCLE |
| [Back-office / bench tablet surface (basic)](stories/PRD-09__BACKOFFICE-TABLET.md) | PRD-09 | Story | P2 | 2 | PRD-11/OPENCLOSE, PRD-07/FOLLOWUPS |
| [Back-office tablet: open/close + cold-chain panels](stories/PRD-09__BACKOFFICE-OPENCOLD.md) | PRD-09 | Story | P2 | 2 | PRD-09/BACKOFFICE-TABLET, PRD-11/OPENCLOSE |
| [Back-office tablet: stock + S4 register + waste panels](stories/PRD-09__BACKOFFICE-STOCK.md) | PRD-09 | Story | P2 | 2 | PRD-09/BACKOFFICE-TABLET, PRD-11/OPENCLOSE |

### Sprint 24 — Apps  ·  1 items · 2 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Back-office tablet: tasks + shift-handover panels](stories/PRD-09__BACKOFFICE-TASKS.md) | PRD-09 | Story | P2 | 2 | PRD-09/BACKOFFICE-TABLET, PRD-07/FOLLOWUPS |

### Backlog — Phase 2+ (later)  ·  21 items · 21 pts

| Story | Epic | Pri | Est |
|---|---|---|---|
| [Custom-role builder (placeholder)](stories/PRD-01__ROLE-BUILDER.md) | PRD-01 | P2 | 1 |
| [Booking deposits / card-on-file hold (placeholder)](stories/PRD-02__DEPOSITS.md) | PRD-02 | P2 | 1 |
| [Mode B pharmacy-dispensing model (placeholder)](stories/PRD-04__MODE-B.md) | PRD-04 | P2 | 1 |
| [Other-modality charting: filler / energy / weight-loss (placeholder)](stories/PRD-05__MODALITY.md) | PRD-05 | P2 | 1 |
| [AI note dictation / auto-detect injection points (placeholder)](stories/PRD-05__AI-SCRIBE.md) | PRD-05 | P2 | 1 |
| [Skin analysis: structured assessment & zone scoring (MVP)](stories/PRD-05__SKIN-ANALYSIS.md) | PRD-05 | P2 | 1 |
| [Body contouring charting: body map & applicator/cycle capture (MVP)](stories/PRD-05__BODY-CONTOURING.md) | PRD-05 | P2 | 1 |
| [Outcomes & revision capture (MVP)](stories/PRD-05__OUTCOMES.md) | PRD-05 | P2 | 1 |
| [Referrals & affiliate credit (non-S4) (placeholder)](stories/PRD-06__REFERRALS.md) | PRD-06 | P2 | 1 |
| [Omnichannel inbox + lead/reviews (placeholder)](stories/PRD-07__INBOX.md) | PRD-07 | P2 | 1 |
| [Reviews & reputation — request-all, reply/acknowledge/flag + S4 caution (core)](stories/PRD-07__REVIEWS.md) | PRD-07 | P2 | 1 |
| [Lead / prospect CRM — pipeline, stages & convert (core)](stories/PRD-07__LEADS-CRM.md) | PRD-07 | P2 | 1 |
| [Campaigns (external-tool handoff) (placeholder)](stories/PRD-07__CAMPAIGNS.md) | PRD-07 | P2 | 1 |
| [Custom report builder / external BI (placeholder)](stories/PRD-08__REPORT-BUILDER.md) | PRD-08 | P2 | 1 |
| [Online checkout, e-prescribing, webhooks/API (placeholder)](stories/PRD-10__INTEGRATIONS-LATER.md) | PRD-10 | P2 | 1 |
| [Fuller facility workflows (placeholder)](stories/PRD-11__FAC-WORKFLOWS.md) | PRD-11 | P2 | 1 |
| [Multi-location switching UI (placeholder)](stories/PHASE-2__MULTI-LOCATION.md) | PHASE-2 | P2 | 1 |
| [SaaS onboarding & billing UI (placeholder)](stories/PHASE-2__SAAS-ONBOARDING.md) | PHASE-2 | P2 | 1 |
| [Per-tenant white-label theming (placeholder)](stories/PHASE-2__WHITE-LABEL.md) | PHASE-2 | P2 | 1 |
| [Public API & webhooks (placeholder)](stories/PHASE-2__PUBLIC-API.md) | PHASE-2 | P2 | 1 |
| [Native POS hardware & tablet kiosk mode (placeholder)](stories/PHASE-2__NATIVE-POS-KIOSK.md) | PHASE-2 | P2 | 1 |
