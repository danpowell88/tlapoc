# Sprint plan & sequencing

> Generated from `docs/backlog/data/*.json`. Regenerate with `python scripts/storydocs.py`.

**Assumptions.** One developer, AI-assisted, ~1–2 days/week (a side project — elapsed time is not the constraint). Sprints are *work-sized*, not calendar-boxed: ~19 story points each (≈5–6 items). Sequencing is dependency-ordered (a story never precedes something it depends on) and grouped by delivery stage.

**Totals.** 136 scheduled stories across 25 sprints (~429 pts), plus 21 deferred items in the backlog.

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
| 01 | Setup | 6 | 18 |
| 02 | Setup | 7 | 19 |
| 03 | Setup | 6 | 18 |
| 04 | Setup | 7 | 18 |
| 05 | Setup | 4 | 16 |
| 06 | Foundations | 4 | 18 |
| 07 | Foundations | 6 | 18 |
| 08 | Foundations | 5 | 17 |
| 09 | App shell | 5 | 15 |
| 10 | Reception | 5 | 19 |
| 11 | Reception | 5 | 17 |
| 12 | Consent | 4 | 16 |
| 13 | Injectables | 4 | 18 |
| 14 | Injectables | 4 | 18 |
| 15 | Injectables | 5 | 17 |
| 16 | Charting | 4 | 18 |
| 17 | Charting | 6 | 17 |
| 18 | Reporting | 8 | 19 |
| 19 | Compliance ops | 8 | 19 |
| 20 | Payments | 4 | 17 |
| 21 | Payments | 6 | 18 |
| 22 | Comms & growth | 6 | 19 |
| 23 | Integrations | 8 | 18 |
| 24 | Apps | 7 | 18 |
| 25 | Apps | 2 | 4 |


### Sprint 01 — Setup  ·  6 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Monorepo & solution scaffolding](stories/SPRINT-0__REPO.md) | SPRINT-0 | Chore | P0 | 3 | — |
| [CI/CD pipelines (build, test, deploy)](stories/SPRINT-0__CICD.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/REPO |
| [Cloud environments & infrastructure-as-code (AU East)](stories/SPRINT-0__IAC.md) | SPRINT-0 | Chore | P0 | 3 | — |
| [Postgres + EF Core baseline & migrations](stories/SPRINT-0__DB.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/IAC |
| [Append-only audit infrastructure baseline](stories/SPRINT-0__AUDIT-INFRA.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/DB |
| [Security baseline: encryption, headers, dependency & secret scanning](stories/SPRINT-0__SEC-BASE.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/CICD |

### Sprint 02 — Setup  ·  7 items · 19 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Spike — Entra External ID ↔ Flutter ↔ .NET auth](stories/SPRINT-0__SPIKE-AUTH.md) | SPRINT-0 | Spike | P0 | 2 | — |
| [Staff identity: Entra ID SSO + MFA wiring](stories/SPRINT-0__AUTH-STAFF.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/SPIKE-AUTH |
| [Client identity: Entra External ID (social / email / OTP) wiring](stories/SPRINT-0__AUTH-CLIENT.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/SPIKE-AUTH |
| [Spike — Postgres RLS with EF Core session context](stories/SPRINT-0__SPIKE-RLS.md) | SPRINT-0 | Spike | P0 | 2 | — |
| [Row-level-security multi-tenancy baseline](stories/SPRINT-0__RLS.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/DB, SPRINT-0/SPIKE-RLS |
| [.NET API skeleton: architecture, tenant context, error model](stories/SPRINT-0__API.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/RLS, SPRINT-0/AUTH-STAFF |
| [Background jobs & scheduler infrastructure](stories/SPRINT-0__JOBS-SCHEDULER.md) | SPRINT-0 | Chore | P0 | 3 | SPRINT-0/API, SPRINT-0/RLS |

### Sprint 03 — Setup  ·  6 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [OpenAPI contract + typed client generation](stories/SPRINT-0__OPENAPI.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/API |
| [Design system / shared component library + tokens](stories/SPRINT-0__DESIGN.md) | SPRINT-0 | Chore | P1 | 3 | — |
| [Angular web shell: routing, auth guard, layout](stories/SPRINT-0__WEB-SHELL.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUTH-STAFF, SPRINT-0/DESIGN |
| [Flutter app shells (client + provider) + shared packages](stories/SPRINT-0__FLUTTER.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT, SPRINT-0/DESIGN |
| [Secrets & configuration management](stories/SPRINT-0__SECRETS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/IAC |
| [Observability: logging, tracing, metrics, alerting](stories/SPRINT-0__OBS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/API |

### Sprint 04 — Setup  ·  7 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Test strategy & harness + quality gates](stories/SPRINT-0__TEST.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/CICD, SPRINT-0/RLS |
| [Spike — Square AU card-on-file recurring autopay](stories/SPRINT-0__SPIKE-SQUARE.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Spike — Flutter injection-mapping canvas](stories/SPRINT-0__SPIKE-CANVAS.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Spike — offline queue & sync integrity (provider app)](stories/SPRINT-0__SPIKE-OFFLINE.md) | SPRINT-0 | Spike | P1 | 2 | — |
| [Media storage & signed-URL service](stories/SPRINT-0__MEDIA-STORAGE.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/IAC, SPRINT-0/API |
| [Domain-event / messaging backbone](stories/SPRINT-0__DOMAIN-EVENTS.md) | SPRINT-0 | Chore | P1 | 3 | SPRINT-0/AUDIT-INFRA |
| [Synthetic seed data & local dev environment](stories/SPRINT-0__SEED.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/DB |

### Sprint 05 — Setup  ·  4 items · 16 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Repo governance: branch protection, PR & env protection](stories/SPRINT-0__GOV.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/CICD |
| [Feature flags & per-tenant configuration](stories/SPRINT-0__FEATURE-FLAGS.md) | SPRINT-0 | Chore | P2 | 3 | SPRINT-0/API |
| [Tenant provisioning & staff invitation](stories/PRD-01__TENANT.md) | PRD-01 | Story | P0 | 5 | — |
| [RBAC + scope-of-practice matrix enforcement](stories/PRD-01__RBAC.md) | PRD-01 | Story | P0 | 5 | PRD-01/TENANT |

### Sprint 06 — Foundations  ·  4 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Staff credentials + canInject compliance gate](stories/PRD-01__CREDENTIALS.md) | PRD-01 | Story | P0 | 5 | PRD-01/RBAC |
| [Exportable audit trail for clinical / medicines / PII](stories/PRD-01__AUDIT.md) | PRD-01 | Story | P0 | 5 | PRD-01/TENANT |
| [Sign-in / sign-out screens & session management](stories/PRD-01__SIGNIN-UI.md) | PRD-01 | Story | P0 | 5 | SPRINT-0/AUTH-STAFF, SPRINT-0/AUTH-CLIENT |
| [Registration / PII / CPD expiry alerting](stories/PRD-01__REG-WATCH.md) | PRD-01 | Story | P1 | 3 | PRD-01/CREDENTIALS |

### Sprint 07 — Foundations  ·  6 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Rosters & engagement type](stories/PRD-01__ROSTER.md) | PRD-01 | Story | P1 | 3 | PRD-01/CREDENTIALS |
| [Retention policy engine & destruction register](stories/PRD-01__RETENTION.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT |
| [Data-breach assessment & notification workflow](stories/PRD-01__BREACH.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT |
| [Client privacy: collection notice, access & correction (DSAR)](stories/PRD-01__PRIVACY-RIGHTS.md) | PRD-01 | Story | P1 | 3 | PRD-01/TENANT |
| [Data residency & sub-processor controls](stories/PRD-01__RESIDENCY.md) | PRD-01 | Story | P1 | 3 | SPRINT-0/IAC |
| [Client core record: DOB & under-18 flag](stories/PRD-01__CLIENT-CORE.md) | PRD-01 | Story | P1 | 3 | PRD-01/TENANT |

### Sprint 08 — Foundations  ·  5 items · 17 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [MFA & step-up authentication for sensitive actions](stories/PRD-01__MFA-STEPUP.md) | PRD-01 | Story | P1 | 3 | PRD-01/SIGNIN-UI |
| [Multi-role staff & active-role context](stories/PRD-01__MULTI-ROLE.md) | PRD-01 | Story | P1 | 3 | PRD-01/RBAC |
| [Authentication & authorisation audit events](stories/PRD-01__AUTH-AUDIT.md) | PRD-01 | Story | P1 | 3 | PRD-01/AUDIT, PRD-01/RBAC |
| [Owner-only financial (.fin) capability gating](stories/PLATFORM__FIN-GATING.md) | PLATFORM | Story | P0 | 5 | PRD-01/RBAC |
| [App shell & collapsible workspace navigation](stories/PLATFORM__APP-NAV.md) | PLATFORM | Story | P1 | 3 | SPRINT-0/WEB-SHELL, PRD-01/RBAC |

### Sprint 09 — App shell  ·  5 items · 15 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Role-tailored Today dashboard](stories/PLATFORM__TODAY.md) | PLATFORM | Story | P1 | 3 | PLATFORM/APP-NAV |
| [Active-role context, scope display & multi-role switching](stories/PLATFORM__ROLE-CONTEXT.md) | PLATFORM | Story | P1 | 3 | PRD-01/RBAC, PRD-01/MULTI-ROLE |
| [Global search (clients, appointments, invoices)](stories/PLATFORM__SEARCH.md) | PLATFORM | Story | P2 | 2 | PLATFORM/APP-NAV |
| [Clinic / location switcher](stories/PLATFORM__CLINIC-SWITCH.md) | PLATFORM | Story | P2 | 2 | PRD-01/TENANT |
| [Multi-resource calendar (practitioner + room)](stories/PRD-02__CALENDAR.md) | PRD-02 | Story | P0 | 5 | PRD-01/ROSTER |

### Sprint 10 — Reception  ·  5 items · 19 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Online self-booking (scope-aware)](stories/PRD-02__ONLINE-BOOK.md) | PRD-02 | Story | P0 | 5 | PRD-02/CALENDAR, PRD-01/CREDENTIALS |
| [Consult gate on injectable appointments](stories/PRD-02__CONSULT-GATE.md) | PRD-02 | Story | P0 | 5 | PRD-02/ONLINE-BOOK |
| [Visit lifecycle & status state-machine](stories/PRD-02__LIFECYCLE.md) | PRD-02 | Story | P1 | 3 | PRD-02/CALENDAR |
| [Reminders & self-service reschedule/cancel](stories/PRD-02__REMINDERS.md) | PRD-02 | Story | P1 | 3 | PRD-02/LIFECYCLE |
| [Waitlist & cancellation backfill](stories/PRD-02__WAITLIST.md) | PRD-02 | Story | P1 | 3 | PRD-02/REMINDERS |

### Sprint 11 — Reception  ·  5 items · 17 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Client 360° profile](stories/PRD-02__CLIENT-360.md) | PRD-02 | Story | P1 | 3 | PRD-01/CLIENT-CORE |
| [Walk-ins, same-day add-ons & resources](stories/PRD-02__WALKINS.md) | PRD-02 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Client directory: search, filter, merge, soft-delete](stories/PRD-02__CLIENT-DIR.md) | PRD-02 | Story | P2 | 2 | PRD-02/CLIENT-360 |
| [Pre-visit intake forms](stories/PRD-03__INTAKE.md) | PRD-03 | Story | P0 | 5 | PRD-02/ONLINE-BOOK |
| [BDD / psychological screening instrument](stories/PRD-03__BDD.md) | PRD-03 | Story | P0 | 5 | PRD-03/INTAKE |

### Sprint 12 — Consent  ·  4 items · 16 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Versioned e-signed consent with mandated content](stories/PRD-03__CONSENT.md) | PRD-03 | Story | P0 | 5 | PRD-03/INTAKE |
| [Server-enforced treatment gating](stories/PRD-03__GATING.md) | PRD-03 | Story | P0 | 5 | PRD-03/CONSENT, PRD-03/BDD |
| [Separate, withdrawable image-use consent](stories/PRD-03__IMAGE-CONSENT.md) | PRD-03 | Story | P1 | 3 | PRD-03/CONSENT |
| [Cooling-off & under-18 payment block](stories/PRD-03__COOLING-OFF.md) | PRD-03 | Story | P1 | 3 | PRD-01/CLIENT-CORE, PRD-03/CONSENT |

### Sprint 13 — Injectables  ·  4 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Synchronous consult record](stories/PRD-04__CONSULT.md) | PRD-04 | Story | P0 | 5 | PRD-02/CONSULT-GATE, PRD-03/GATING |
| [Individual prescription (no batch / no async)](stories/PRD-04__PRESCRIPTION.md) | PRD-04 | Story | P0 | 5 | PRD-04/CONSULT, PRD-01/CREDENTIALS |
| [Medicines & product catalogue (S4 classification)](stories/PRD-04__PRODUCT-CATALOGUE.md) | PRD-04 | Story | P0 | 5 | — |
| [Services & treatment-menu admin (durations, eligible roles, S4 flag)](stories/PRD-02__SERVICE-CATALOGUE.md) | PRD-02 | Story | P1 | 3 | PRD-04/PRODUCT-CATALOGUE |

### Sprint 14 — Injectables  ·  4 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Staff booking wizard (service → practitioner → time → client → confirm)](stories/PRD-02__BOOKING-WIZARD.md) | PRD-02 | Story | P1 | 3 | PRD-02/CALENDAR, PRD-02/SERVICE-CATALOGUE |
| [Stock receipt, ARTG & lawful-supply provenance](stories/PRD-04__STOCK-RECEIVE.md) | PRD-04 | Story | P0 | 5 | PRD-04/PRODUCT-CATALOGUE |
| [Administration gating & immutable record](stories/PRD-04__ADMIN-GATE.md) | PRD-04 | Story | P0 | 5 | PRD-04/PRESCRIPTION, PRD-04/STOCK-RECEIVE |
| [Custody & secure storage](stories/PRD-04__CUSTODY-STORAGE.md) | PRD-04 | Story | P0 | 5 | PRD-04/STOCK-RECEIVE |

### Sprint 15 — Injectables  ·  5 items · 17 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Lot → clients recall lookup & medicine register](stories/PRD-04__RECALL-LOOKUP.md) | PRD-04 | Story | P0 | 5 | PRD-04/ADMIN-GATE |
| [Temperature logging & excursion alerts](stories/PRD-04__COLD-CHAIN.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |
| [Vial / unit reconciliation](stories/PRD-04__VIAL-RECON.md) | PRD-04 | Story | P1 | 3 | PRD-04/ADMIN-GATE |
| [Wastage, disposal & destruction records](stories/PRD-04__WASTAGE-DESTRUCTION.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |
| [Stocktake, discrepancy & loss/theft reporting](stories/PRD-04__STOCKTAKE.md) | PRD-04 | Story | P1 | 3 | PRD-04/CUSTODY-STORAGE |

### Sprint 16 — Charting  ·  4 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Guided toxin treatment note & pre-treatment review](stories/PRD-05__NOTE-TEMPLATE.md) | PRD-05 | Story | P0 | 5 | PRD-04/ADMIN-GATE |
| [Injection-mapping canvas (per-point lot)](stories/PRD-05__MAPPING.md) | PRD-05 | Story | P0 | 5 | SPRINT-0/SPIKE-CANVAS, PRD-04/RECALL-LOOKUP |
| [Immutable finalisation & audited amendments](stories/PRD-05__IMMUTABILITY.md) | PRD-05 | Story | P0 | 5 | PRD-05/MAPPING |
| [Standardised before/after photos + compare](stories/PRD-05__PHOTOS.md) | PRD-05 | Story | P1 | 3 | PRD-03/IMAGE-CONSENT |

### Sprint 17 — Charting  ·  6 items · 17 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Offline queue & sync for room-side charting](stories/PRD-05__OFFLINE.md) | PRD-05 | Story | P1 | 3 | SPRINT-0/SPIKE-OFFLINE, PRD-05/IMMUTABILITY |
| [Adverse-event capture → DAEN pathway](stories/PRD-05__ADVERSE-EVENT.md) | PRD-05 | Story | P1 | 3 | PRD-05/IMMUTABILITY |
| [Complication protocol library & response kits](stories/PRD-05__COMPLICATION-LIBRARY.md) | PRD-05 | Story | P1 | 3 | PRD-05/ADVERSE-EVENT |
| [Treatment plans & protocol templates](stories/PRD-05__TREATMENT-PLANS.md) | PRD-05 | Story | P2 | 2 | PRD-05/NOTE-TEMPLATE |
| [Reporting read-models / materialized views](stories/PRD-08__READ-MODELS.md) | PRD-08 | Story | P1 | 3 | PRD-01/AUDIT |
| [Business analytics dashboards](stories/PRD-08__BUSINESS-DASH.md) | PRD-08 | Story | P1 | 3 | PRD-08/READ-MODELS |

### Sprint 18 — Reporting  ·  8 items · 19 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Compliance dashboards & register exports](stories/PRD-08__COMPLIANCE-DASH.md) | PRD-08 | Story | P1 | 3 | PRD-08/READ-MODELS, PRD-04/RECALL-LOOKUP |
| [Adverse-event / DAEN prefilled submission](stories/PRD-08__DAEN.md) | PRD-08 | Story | P1 | 3 | PRD-05/ADVERSE-EVENT |
| [Data-quality checks](stories/PRD-08__DATA-QUALITY.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS |
| [Owner 'needs attention' exceptions digest](stories/PRD-08__ATTENTION-DIGEST.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Inspection-readiness pack & governance hub](stories/PRD-08__INSPECTION-PACK.md) | PRD-08 | Story | P2 | 2 | PRD-08/COMPLIANCE-DASH |
| [Policies & procedures sign-off](stories/PRD-08__POLICIES.md) | PRD-08 | Story | P1 | 3 | PRD-08/INSPECTION-PACK |
| [Practitioner scorecard](stories/PRD-08__SCORECARD.md) | PRD-08 | Story | P2 | 2 | PRD-08/BUSINESS-DASH |
| [Capacity & utilisation report](stories/PRD-08__CAPACITY.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS |

### Sprint 19 — Compliance ops  ·  8 items · 19 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [True-cost / margin (COGS) reporting](stories/PRD-08__TRUE-COST.md) | PRD-08 | Story | P2 | 2 | PRD-08/READ-MODELS, PRD-04/VIAL-RECON |
| [Complaints register with AHPRA pathway](stories/PRD-11__COMPLAINTS.md) | PRD-11 | Story | P1 | 3 | — |
| [Daily open/close checklist & fridge log](stories/PRD-11__OPENCLOSE.md) | PRD-11 | Story | P1 | 3 | PRD-04/COLD-CHAIN |
| [Temperature monitor management](stories/PRD-11__TEMP-MONITORS.md) | PRD-11 | Story | P1 | 3 | PRD-04/COLD-CHAIN |
| [Facility accreditation & expiry alerts](stories/PRD-11__FACILITY.md) | PRD-11 | Story | P2 | 2 | — |
| [Infection-control & waste logs](stories/PRD-11__IPC-LOGS.md) | PRD-11 | Story | P2 | 2 | — |
| [Emergency kit & continuity-of-care](stories/PRD-11__EMERGENCY-KIT.md) | PRD-11 | Story | P2 | 2 | — |
| [Rooms & devices register](stories/PRD-11__ROOMS-DEVICES.md) | PRD-11 | Story | P2 | 2 | PRD-02/CALENDAR |

### Sprint 20 — Payments  ·  4 items · 17 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Equipment & maintenance register](stories/PRD-11__EQUIPMENT.md) | PRD-11 | Story | P2 | 2 | PRD-11/ROOMS-DEVICES |
| [Payment provider abstraction + Square adapter](stories/PRD-06__PAYMENT-PROVIDER.md) | PRD-06 | Story | P0 | 5 | SPRINT-0/SPIKE-SQUARE |
| [In-person POS checkout (card + cash)](stories/PRD-06__POS.md) | PRD-06 | Story | P0 | 5 | PRD-06/PAYMENT-PROVIDER |
| [Memberships with automatic autopay & dunning](stories/PRD-06__MEMBERSHIP.md) | PRD-06 | Story | P0 | 5 | PRD-06/PAYMENT-PROVIDER |

### Sprint 21 — Payments  ·  6 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Rewards engine — non-S4 only](stories/PRD-06__REWARDS-ENGINE.md) | PRD-06 | Story | P0 | 5 | PRD-04/PRODUCT-CATALOGUE |
| [Packages/series, gift cards & client balances](stories/PRD-06__PACKAGES-GIFT.md) | PRD-06 | Story | P1 | 3 | PRD-06/POS |
| [Daily closeout & reconciliation](stories/PRD-06__CLOSEOUT.md) | PRD-06 | Story | P1 | 3 | PRD-06/POS |
| [Margin-aware reward rules](stories/PRD-06__MARGIN-RULES.md) | PRD-06 | Story | P1 | 3 | PRD-06/REWARDS-ENGINE |
| [Checkout assist & post-visit rebooking](stories/PRD-06__CHECKOUT-ASSIST.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |
| [Pricing & what-if planning (owner)](stories/PRD-06__PRICING-WHATIF.md) | PRD-06 | Story | P2 | 2 | PRD-06/POS |

### Sprint 22 — Comms & growth  ·  6 items · 19 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Notification channels (SMS / email / push)](stories/PRD-07__CHANNELS.md) | PRD-07 | Story | P0 | 5 | — |
| [In-app notification centre](stories/PLATFORM__NOTIFICATIONS.md) | PLATFORM | Story | P2 | 2 | PLATFORM/APP-NAV, PRD-07/CHANNELS |
| [Reminders, confirmations & care sequences](stories/PRD-07__REMINDERS-CARE.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Recall / recare worklist](stories/PRD-07__RECALL.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Marketing consent & functional unsubscribe (Spam Act)](stories/PRD-07__MARKETING-CONSENT.md) | PRD-07 | Story | P1 | 3 | PRD-07/CHANNELS |
| [Public booking page: generic names, S4 prices withheld](stories/PRD-07__BOOKING-PAGE.md) | PRD-07 | Story | P1 | 3 | PRD-02/ONLINE-BOOK |

### Sprint 23 — Integrations  ·  8 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Unified follow-up / job queue](stories/PRD-07__FOLLOWUPS.md) | PRD-07 | Story | P2 | 2 | PRD-07/CHANNELS |
| [Call / phone log](stories/PRD-11__CALL-LOG.md) | PRD-11 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Shift handover notes](stories/PRD-11__SHIFT-HANDOVER.md) | PRD-11 | Story | P2 | 2 | PRD-07/FOLLOWUPS |
| [Automation builder (triggers → timed messages)](stories/PRD-07__AUTOMATIONS.md) | PRD-07 | Story | P2 | 2 | PRD-07/REMINDERS-CARE |
| [Xero invoice/payment sync](stories/PRD-10__XERO.md) | PRD-10 | Story | P1 | 3 | PRD-06/POS |
| [Two-way calendar sync (M365 / Google)](stories/PRD-10__CALENDAR-SYNC.md) | PRD-10 | Story | P2 | 2 | PRD-02/CALENDAR |
| [Sub-processor residency posture (APP-8)](stories/PRD-10__SUBPROCESSOR-POSTURE.md) | PRD-10 | Story | P2 | 2 | PRD-01/RESIDENCY |
| [Client app: book → intake → consent journey](stories/PRD-09__CLIENT-JOURNEY.md) | PRD-09 | Story | P1 | 3 | PRD-02/ONLINE-BOOK, PRD-03/CONSENT |

### Sprint 24 — Apps  ·  7 items · 18 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Provider app: day schedule & open patient](stories/PRD-09__PROVIDER-DAY.md) | PRD-09 | Story | P1 | 3 | PRD-05/NOTE-TEMPLATE |
| [Provider app: room-side charting, camera & finalise](stories/PRD-09__PROVIDER-ROOMSIDE.md) | PRD-09 | Story | P1 | 3 | PRD-05/MAPPING, PRD-05/PHOTOS |
| [Provider app: offline-tolerant workflows + sync indicator](stories/PRD-09__PROVIDER-OFFLINE.md) | PRD-09 | Story | P1 | 3 | PRD-05/OFFLINE |
| [Client 'report a concern' → follow-up / AE bridge](stories/PRD-09__CLIENT-CONCERN.md) | PRD-09 | Story | P1 | 3 | PRD-07/FOLLOWUPS, PRD-05/ADVERSE-EVENT |
| [Client app: my care, memberships, rewards & card-on-file](stories/PRD-09__CLIENT-CARE.md) | PRD-09 | Story | P2 | 2 | PRD-06/MEMBERSHIP, PRD-05/PHOTOS |
| [Client app: account, privacy & access/correction](stories/PRD-09__CLIENT-PRIVACY.md) | PRD-09 | Story | P2 | 2 | PRD-01/PRIVACY-RIGHTS |
| [App distribution & code-push posture](stories/PRD-09__APP-DISTRIBUTION.md) | PRD-09 | Story | P2 | 2 | SPRINT-0/FLUTTER |

### Sprint 25 — Apps  ·  2 items · 4 pts

| Story | Epic | Type | Pri | Est | Depends on |
|---|---|---|---|---|---|
| [Reception self-check-in surface (tablet)](stories/PRD-09__CHECKIN-KIOSK.md) | PRD-09 | Story | P2 | 2 | PRD-02/LIFECYCLE, PRD-03/GATING |
| [Back-office / bench tablet surface](stories/PRD-09__BACKOFFICE-TABLET.md) | PRD-09 | Story | P2 | 2 | PRD-11/OPENCLOSE, PRD-07/FOLLOWUPS |

### Backlog — Phase 2+ (later)  ·  21 items · 21 pts

| Story | Epic | Pri | Est |
|---|---|---|---|
| [Custom-role builder (placeholder)](stories/PRD-01__ROLE-BUILDER.md) | PRD-01 | P2 | 1 |
| [Booking deposits / card-on-file hold (placeholder)](stories/PRD-02__DEPOSITS.md) | PRD-02 | P2 | 1 |
| [Mode B pharmacy-dispensing model (placeholder)](stories/PRD-04__MODE-B.md) | PRD-04 | P2 | 1 |
| [Other-modality charting: filler / energy / weight-loss (placeholder)](stories/PRD-05__MODALITY.md) | PRD-05 | P2 | 1 |
| [AI note dictation / auto-detect injection points (placeholder)](stories/PRD-05__AI-SCRIBE.md) | PRD-05 | P2 | 1 |
| [Skin analysis & assessment (with AI scan, advisory)](stories/PRD-05__SKIN-ANALYSIS.md) | PRD-05 | P2 | 1 |
| [Body contouring charting (e.g. CoolSculpting)](stories/PRD-05__BODY-CONTOURING.md) | PRD-05 | P2 | 1 |
| [Outcomes & revision tracking](stories/PRD-05__OUTCOMES.md) | PRD-05 | P2 | 1 |
| [Referrals & affiliate credit (non-S4) (placeholder)](stories/PRD-06__REFERRALS.md) | PRD-06 | P2 | 1 |
| [Omnichannel inbox + lead/reviews (placeholder)](stories/PRD-07__INBOX.md) | PRD-07 | P2 | 1 |
| [Reviews & reputation (request, acknowledge, flag, auto-follow-up)](stories/PRD-07__REVIEWS.md) | PRD-07 | P2 | 1 |
| [Lead / prospect CRM](stories/PRD-07__LEADS-CRM.md) | PRD-07 | P2 | 1 |
| [Campaigns (external-tool handoff) (placeholder)](stories/PRD-07__CAMPAIGNS.md) | PRD-07 | P2 | 1 |
| [Custom report builder / external BI (placeholder)](stories/PRD-08__REPORT-BUILDER.md) | PRD-08 | P2 | 1 |
| [Online checkout, e-prescribing, webhooks/API (placeholder)](stories/PRD-10__INTEGRATIONS-LATER.md) | PRD-10 | P2 | 1 |
| [Fuller facility workflows (placeholder)](stories/PRD-11__FAC-WORKFLOWS.md) | PRD-11 | P2 | 1 |
| [Multi-location switching UI (placeholder)](stories/PHASE-2__MULTI-LOCATION.md) | PHASE-2 | P2 | 1 |
| [SaaS onboarding & billing UI (placeholder)](stories/PHASE-2__SAAS-ONBOARDING.md) | PHASE-2 | P2 | 1 |
| [Per-tenant white-label theming (placeholder)](stories/PHASE-2__WHITE-LABEL.md) | PHASE-2 | P2 | 1 |
| [Public API & webhooks (placeholder)](stories/PHASE-2__PUBLIC-API.md) | PHASE-2 | P2 | 1 |
| [Native POS hardware & tablet kiosk mode (placeholder)](stories/PHASE-2__NATIVE-POS-KIOSK.md) | PHASE-2 | P2 | 1 |
