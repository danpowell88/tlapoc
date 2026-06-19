# Architecture Decision Log — Aesthetic Clinic Platform

Records the significant technical decisions and their rationale. Format per entry: **Context →
Decision → Consequences → Alternatives**. Status: `Accepted` unless noted. These can be split
into individual `ADR-NNNN-*.md` files later; kept as one log for a lean team.

> Anchored to [02-requirements.md](../02-requirements.md). Each PRD cites the ADRs it depends on.

---

## ADR-0001 — Cloud platform: **Azure** (primary), AWS as documented fallback
**Status:** Accepted
**Context:** Hard AU data-residency requirement; lean cost; staff already on Microsoft 365/Entra; backend is .NET. (REQ-SEC-1, C10/C21, decision table §2.)
**Decision:** Build on **Azure, Australia East (Sydney)**. Use managed PaaS only. Keep an AWS-equivalent mapping documented (Cognito↔Entra, RDS↔Azure DB, S3↔Blob, Fargate↔Container Apps) so the choice is reversible.
**Consequences:** First-class .NET + Entra integration; single identity vendor; cheap burstable tiers. Lock-in mitigated by containerised .NET + Postgres (portable).
**Alternatives:** AWS (viable, weaker ecosystem fit for M365 shops); multi-cloud (needless complexity for v1).

## ADR-0002 — Relational database: **PostgreSQL** (Azure DB for PostgreSQL Flexible Server)
**Status:** Accepted (confirm Postgres vs Azure SQL at Phase 0 — open item §10.7)
**Context:** Need transactions, strong constraints, **Row-Level Security**, low cost, EF Core support.
**Decision:** **PostgreSQL** with EF Core/Npgsql; burstable tier to start. RLS for tenancy (ADR-0003).
**Consequences:** Cheap, portable, RLS-capable; mature .NET tooling.
**Alternatives:** **Azure SQL** (equally native to .NET, also RLS — the leading alternative); Cosmos/NoSQL (rejected — relational integrity + multi-row invariants are core to compliance).

## ADR-0003 — Multi-tenancy: **single database, `tenant_id` + Postgres RLS**
**Status:** Accepted
**Context:** Internal-first but **SaaS-ready** without a rewrite (decision §2).
**Decision:** Shared schema; `tenant_id` on every table; **RLS** policies keyed off a per-request session setting (`SET app.tenant_id`), with tenant context also enforced in the API as defense-in-depth.
**Consequences:** Cheapest ops, strong isolation, one migration path; can shard/extract noisy tenants later. SaaS = onboard a tenant row + Entra federation.
**Alternatives:** DB-per-tenant (ops/cost heavy); schema-per-tenant (migration pain).

## ADR-0004 — Identity: **Microsoft Entra** — staff = Entra ID (workforce SSO); clients = Entra External ID (CIAM)
**Status:** Accepted
**Context:** Staff already have M365 accounts; clients need social + email/password + OTP. (REQ-TEN-2.)
**Decision:** **Entra ID** for staff SSO + MFA; **Entra External ID** for customers (Google/Apple social, local password, email/SMS OTP). For SaaS, each clinic tenant can federate its own Entra tenant for staff.
**Consequences:** Unified Microsoft identity; offload auth/MFA/breach-surface to the platform; per-tenant federation is a clean SaaS story.
**Alternatives:** AWS Cognito (fallback if AWS chosen); Auth0/Okta (cost); custom auth (**rejected** — never hand-roll auth for health data).

## ADR-0005 — App architecture: **Angular SPA + ASP.NET Core API as a modular monolith**
**Status:** Accepted
**Context:** Lean team; one backend serving the web admin/booking and two Flutter apps.
**Decision:** A single **.NET (ASP.NET Core) Web API**, internally a **modular monolith** with clear bounded modules (Tenancy, Clients, Booking, Clinical, Consent, Rx, Medicines, Payments, Memberships/Rewards, Notifications, Reporting, Integrations, Facility). **Angular** for the web client. REST + JSON; OpenAPI contract shared with Flutter.
**Consequences:** Far simpler to build/operate than microservices; module seams allow later extraction; one deployable.
**Alternatives:** Microservices (premature); serverless-only (cold-start + transaction friction for OLTP).

## ADR-0006 — Mobile: **Flutter** for both client and provider apps
**Status:** Accepted
**Context:** Two apps, lean team, camera + offline needs. (Decision §2; user-directed.)
**Decision:** **Flutter (Dart)**, one codebase with shared packages (auth, API client, design system), two app flavours (client, provider). Talks to the .NET API.
**Consequences:** One mobile codebase, near-native UX, good camera/offline support; adds Dart as a third language alongside Angular/TS and C#.
**Alternatives:** Native iOS+Android (2× cost); React Native (declined by user); PWA-in-shell (weaker camera/offline for charting).

## ADR-0007 — Payments: **`IPaymentProvider` abstraction, Square first**; in-person POS + cash + gift cards; card-on-file recurring for autopay
**Status:** Accepted
**Context:** In-person POS first; "Square but pluggable"; **automatic** membership autopay; gift cards; online one-off checkout deferred. (PAY, MEMB.)
**Decision:** Define `IPaymentProvider` (authorize/capture, refund, void, **tokenize/card-on-file**, **recurring charge**, gift-card issue/redeem). **SquareAdapter** first (card-present terminal + card-on-file). **Cash** recorded as an internal tender (no processor). Membership cards tokenised (added online/in-app or at desk) and auto-charged on schedule.
**Consequences:** Provider-swappable (Stripe/Tyro later); **no PAN stored** (tokens only) → minimal PCI scope; cash and card reconciled in one ledger.
**Alternatives:** Hard-couple to Square (rejected — reversibility); Stripe-first (user chose Square).

## ADR-0008 — **Compliance by construction**: enforce regulatory invariants in the domain + database, not just UI
**Status:** Accepted
**Context:** The product's moat is compliance (C1–C24); UI-only checks are bypassable and won't survive an audit.
**Decision:** Encode the hard rules as **domain invariants + DB constraints/triggers**:
- An `Administration` cannot persist without valid FKs to a `Consult`, an unconsumed `Prescription` for the *same* client, a current `Consent`, and a `lot/expiry` (C1, C2, C5, C8).
- Cooling-off + payment block enforced server-side for under-18 (C6).
- `RewardRule`/redemption restricted to **non-S4** catalog items by constraint (C9, REQ-MEMB-7).
- Scope-of-practice + registration currency checked in the auth pipeline (C4, C19).
**Consequences:** Hard to bypass; every block is logged and explainable to a regulator.
**Alternatives:** UI/validation-layer only (**rejected**).

## ADR-0009 — Clinical media: **Azure Blob private + short-lived signed URLs; never stored on personal devices**
**Status:** Accepted
**Context:** AHPRA image-use rules (C14); residency (C10/C21); known competitor failure mode of lost photos.
**Decision:** Direct-to-Blob upload via short-lived signed URLs; image metadata + **image-use consent** in DB; provider app caches transiently (encrypted) only until synced, then purges. Access always via signed URL gated by role + consent.
**Consequences:** Residency + access control; no device retention; resilient capture (ADR-0015).
**Alternatives:** Store blobs in DB (bad at scale); third-party media SaaS (residency risk).

## ADR-0010 — **Append-only audit + immutable finalized records**
**Status:** Accepted
**Context:** QLD Health / AHPRA / Privacy audits (C10, REQ-SEC-3).
**Decision:** Single **append-only `AuditEvent`** stream for all PHI/clinical/medicines **read and write**; finalized `ChartEntry` and every `Administration`/medicine-register row are **immutable** (corrections are appended + linked, never edited).
**Consequences:** Defensible, exportable trail; tamper-evident.
**Alternatives:** Mutable rows + history table (weaker integrity guarantees).

## ADR-0011 — Telehealth: **out of platform**; record consult metadata only
**Status:** Accepted
**Context:** Clinic uses an existing external telehealth app; building video is out of scope.
**Decision:** No video. The `Consult` entity records modality (in-person/telehealth), prescriber, timestamp, external reference and notes — enough to satisfy the **synchronous-consult-before-script** linkage (C1).
**Consequences:** Much less to build; depends on staff recording the consult (enforced by the script gate).
**Alternatives:** Build/integrate video (deferred to a later phase).

## ADR-0012 — External integrations via **ports-and-adapters** (`INotifier`, `ICalendarProvider`, `IAccountingExport`)
**Status:** Accepted
**Context:** SMS, calendar (M365/Google), Xero — must be swappable and AU-appropriate; webhooks/public API deferred.
**Decision:** Each integration sits behind a .NET port. Adapters: **AU SMS** (MessageMedia/Twilio), **MS Graph + Google Calendar**, **Xero**. Outbound only in v1.
**Consequences:** Providers swap without touching core; testable via fakes.
**Alternatives:** Direct SDK coupling (rejected); event bus/webhooks now (deferred — REQ-INT-3).

## ADR-0013 — Reporting: **dedicated read models / materialized views**, refreshed from domain events
**Status:** Accepted
**Context:** Rich analytics + compliance dashboards without slowing the transactional path (RPT).
**Decision:** A separate **read schema** (materialized views / projections) feeds dashboards; rebuild the already-prototyped analytics logic here. Compliance dashboards (C-coverage, S4 register, lot-recall, registration/retention watch, breach/complaints) are queries over this layer + audit stream.
**Consequences:** Fast dashboards, OLTP isolation; eventual consistency is acceptable for reporting.
**Alternatives:** Query OLTP directly (won't scale, risks locks); external warehouse (overkill for v1).

## ADR-0014 — **Catalog with S4 classification** governs rewards eligibility and advertising
**Status:** Accepted
**Context:** Rewards must apply to **non-S4 only**; advertising must avoid S4 references (REQ-MEMB-7, C9).
**Decision:** Every `Service`/`Product` carries **`schedule` (S4 | non-S4)** + category. `RewardRule` eligibility and redemption are constrained to non-S4 items; the advertising linter and public booking-page naming reuse the same flag.
**Consequences:** One classification enforces both the rewards rule and the advertising guardrail; auditable.
**Alternatives:** Manual per-offer exclusion (error-prone, non-auditable).

## ADR-0015 — Provider app: **offline-tolerant local queue + sync**
**Status:** Accepted
**Context:** Treatment-room connectivity is unreliable; notes/photos must never be lost (NFR).
**Decision:** The Flutter provider app queues chart edits, photos and (draft) administrations in an **encrypted local store** and syncs when connectivity returns. Drafts = last-write-wins; **finalisation happens server-side** and is then immutable (ADR-0010).
**Consequences:** No silent data loss; smooth room-side UX.
**Alternatives:** Online-only (rejected — fragile in clinics).

## ADR-0016 — **Data residency**: all PII/PHI in Australia; sub-processors AU or APP-8-assessed
**Status:** Accepted
**Context:** Privacy Act / APP 8 (C10, C21); client expectation.
**Decision:** Pin all storage + compute to **Australia East**. Payment/SMS/accounting sub-processors must be AU-resident or covered by a documented APP-8 cross-border assessment + client consent.
**Consequences:** Compliant residency; constrains provider selection (acceptable).
**Alternatives:** Global/multi-region (rejected for v1).
