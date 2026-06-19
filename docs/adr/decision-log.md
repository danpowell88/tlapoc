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

---

> **ADRs 0017–0022 added rev 2 (2026-06-19)** after building the **Option A** clickable prototype.
> They record decisions the prototype surfaced and flag items that **need feasibility research**
> before commit (🔬). See `02-requirements.md` §12 for the full alignment & feasibility register.

## ADR-0017 — Access model: **capability flags + "concerns"**, with custom roles (future)
**Status:** Accepted
**Context:** Option A prototyped a richer role set than the original §3 matrix — **NP, Lead Nurse (RN), RN, Dermal/laser tech, Reception, Owner (non-clinical business owner)**, plus combined **Solo-NP** and **Nurse-led-RN** presets. The owner is non-clinical (read-only clinical/stock oversight, full financials); clinical staff should mostly see information *concerning them* (e.g. stock-expiry matters to Lead/NP/owner, not every RN). (REQ-TEN-3/4, §3.)
**Decision:** Model access on two orthogonal axes: **capabilities** (atomic permissions — `chart`, `chartView`, `prescribe`, `stock`, `receiveStock`, `financials`, `takePayment`, `configure`…) and **concerns** (relevance tags that drive what a role sees first — `ops, clinical, stock, stockAlert, financial, business, recall, consent`). Built-in roles are presets of (capabilities × concerns); a future **custom-role builder** lets a tenant compose roles by ticking capabilities + concern tiles. **Owner = business role:** financials + read-only clinical/stock, no prescribe/chart/custody.
**Consequences:** Implements the §3 scope matrix while supporting per-tenant roles and role-tailored dashboards. Enforcement stays server-side (ADR-0008): **capabilities gate API actions; concerns only affect presentation.**
**Alternatives:** Fixed role enum (less flexible); full ABAC/policy engine (overkill for v1).

## ADR-0018 — Omnichannel conversations: unified-inbox **sync model** — 🔬 *feasibility research required*
**Status:** Proposed (Phase 2 for social channels; v1 stays SMS/email — see PRD-07)
**Context:** Option A prototypes a **unified inbox** across **Instagram, Facebook/Messenger, SMS and email** with categorisation and suggested replies. Real platform support — especially Meta — is constrained, and staff often reply on the native platform too.
**Decision:** Model conversations channel-agnostically — `Conversation`/`Message` with `channel`, `direction`, `sentVia` — behind an **`IMessagingChannel`** adapter per channel (extends the `INotifier` port, ADR-0012). **Inbound** via provider **webhooks**; **outbound** via each provider's Send API; **reconcile/backfill** (incl. replies staff send natively + pre-connection history) via the provider **Conversations/history API**; capture native-sent replies via **message echoes**; coexist with the platform's own inbox via Meta's **Handover Protocol** (secondary receiver + standby). Enforce **send-time guardrails**: messaging window, message tags, opt-in, and the advertising linter (ADR-0014, C9). **Suggested replies are templated/keyword-based in v1 (no AI, decision §2); LLM-assisted drafting deferred.**
**🔬 Feasibility / research (validate before commit):** Meta requires **Professional accounts**, (often) a linked Page, **App Review + Business Verification**; a **24-hour messaging window** limits outbound to specific tags — **promotional/marketing DMs are largely *not* permitted** outside it; you can't cold-DM; IG echo/standby support is weaker than Messenger and changes often. **Implication:** treat **IG/FB/WhatsApp as reactive/service** channels; do **proactive marketing (recall/promos) via SMS/email (consented)** or **WhatsApp templates**. Assess WhatsApp Business Cloud API, per-channel rate limits, and validate scopes against current Meta docs.
**Consequences:** A faithful "mirror" inbox is achievable for *service* conversations; *marketing* automation stays on SMS/email. Adds per-clinic OAuth onboarding, token lifecycle and webhook infra.
**Alternatives:** SMS/email only (loses the social-inbox value); rely on Meta's native inbox (no unification/automation).

## ADR-0019 — Conversation ↔ client **identity resolution**
**Status:** Accepted
**Context:** Inbound messages arrive with a channel handle (IG @handle, Messenger PSID, phone, email) often **not yet linked** to a `Client`; the prototype lets staff link a conversation to a client and **capture the handle** so replies/suggestions use client history.
**Decision:** A **`ChannelIdentity`** (channel, external id/handle, `client_id?`) joins conversations to clients. **Auto-match** on phone/email; otherwise offer a **link/merge** action that, on confirm, **stores the handle on the client** for future auto-routing. Personalised (templated) suggestions read client history only **after** linking.
**Consequences:** Better service + personalised suggestions; captured handles are **personal data** (consent/retention, APP — C21).
**Alternatives:** Never link (loses context); auto-link on fuzzy name (false-merge risk).

## ADR-0020 — Injection-point **auto-detect: advisory ML, human-confirmed** — 🔬 *feasibility research required*
**Status:** Proposed (Phase 2; v1 ships manual mapping only)
**Context:** The charting prototype offers "auto-detect" of injection points with manual fine-tune/add — implying facial-landmark detection. Decision §2 says **no AI in v1**.
**Decision:** If built, auto-detect is **advisory only** — it proposes candidate points from facial landmarks that the clinician **must review, adjust and confirm**; it never sets product/units, never auto-finalises, never auto-administers. Prefer **on-device/edge** landmarking (privacy, latency); if server-side, stay within AU residency (ADR-0016) and image-use consent (ADR-0009). **v1 = manual tap-to-add + drag only.**
**🔬 Feasibility / research:** landmark accuracy on real treatment angles/lighting; on-device libraries (MediaPipe / ML Kit face mesh) vs server; keep firmly **advisory** to avoid SaMD/medical-device classification; confirm it saves time without adding clinical risk.
**Consequences:** A later time-saver with no clinical-safety/regulatory exposure; v1 unaffected.
**Alternatives:** Always-manual (fine for v1); fully-automatic placement (**rejected** — clinical risk).

## ADR-0021 — Stock as a **multi-product, multi-unit catalogue** (extends ADR-0014)
**Status:** Accepted
**Context:** The stock prototype tracks several distinct products (two toxin brands + a filler) with **different units** (toxin "units" vs filler "syringes/mL") — a single aggregate "units on hand" is meaningless. Prescriber/owner add/remove products and set the **S4 flag** + par levels.
**Decision:** `Product` carries `type` (toxin/filler/skin/other), `unit`, `par`, **`schedule` (S4|non-S4)** and ARTG fields; **lots** belong to a product; all on-hand/usage/wastage/expiry aggregate **per product + unit**, never across units. A **catalogue admin** (capability-gated to prescriber/owner) manages products and the S4 flag — the single source of truth that drives rewards/advertising (ADR-0014) everywhere. Usage history, reorder and par signals are **per product**.
**Consequences:** Correct, unit-safe stock and reporting; one S4 classification point.
**Alternatives:** Single product/unit model (wrong for real formularies).

## ADR-0022 — **Pricing & "what-if" planning** on read models
**Status:** Accepted
**Context:** The Option A owner view includes a **pricing & what-if simulator** — edit plan/service prices and see projected MRR/revenue impact under a churn-sensitivity assumption.
**Decision:** A **read-only planning tool** computed over the reporting read models (ADR-0013) + configurable elasticity/churn assumptions; it **proposes** changes and projects impact but does **not** mutate live pricing until explicitly **applied** through the normal catalogue/membership admin (capability-gated, audited — ADR-0010).
**Consequences:** Owners plan price/membership changes safely; reuses analytics; clean apply/audit path.
**Alternatives:** Off-platform spreadsheet (loses live data); auto-apply (unsafe).

## ADR-0023 — Unified follow-up / task queue ("Jobs")
**Status:** Accepted
**Context:** Follow-ups were scattered (recall worklist, dashboard "needs attention", unanswered inbox messages) and could be **lost if no one replied**. The prototype adds one **Follow-ups** queue.
**Decision:** A single **`Job`** entity — `type` (reply/callback/recall/consent/stock/restock/admin), title, **linked** client/conversation/appointment, **assignee** (role/person), `due`, **`status`** (open/snoozed/done), **`source`** (manual/auto/recall/system). Existing signals (recall due, consent pending, stock/expiry alerts, unanswered conversations) **project into** the same queue rather than living in separate UIs. Staff can **manually flag** any message/client → a Job. Inbound comms are **auto-categorised into Jobs by rules/keywords** (reuse the inbox categoriser) — **no AI in v1**; LLM-assisted triage is a later option. Role-scoped **"my queue"** (concerns model, ADR-0017); all status changes audited (ADR-0010).
**Consequences:** Nothing falls through; one place to work the day. Auto-categorisation accuracy is a **UX, not safety**, concern — jobs are advisory and human-actioned.
**Alternatives:** Keep separate recall/attention lists (status quo — things get lost); a full ticketing system (overkill for v1).

## ADR-0024 — Visit lifecycle & role hand-offs (the appointment is the spine)
**Status:** Accepted
**Context:** Strong individual screens existed, but the *visit* didn't carry the client between roles — staff had to know "what's next". (Workflow review, 2026-06-20.)
**Decision:** The `Appointment`/`Visit` is a **state machine** — Booked → Confirmed → (Late / No-show) → In treatment → For checkout → Done (→ Recall set) — and each state surfaces the **next action for whoever's responsible now**, handing off automatically: reception flags **late / no-show** (a no-show auto-creates a **follow-up call** job, ADR-0023) and a clinician **starts** treatment; on **finalise**, a close-out (send aftercare · set recall · 2-day **wellbeing call** · adverse-event) sets the visit **For checkout**, lighting up reception's queue; payment marks it **Done**. Small clinics skip a formal **check-in** — *late attendance* and *no-shows* are the flags that matter. Capabilities (ADR-0017) gate the per-state actions; charting is **treatment-type-aware** (toxin injection-map + S4 lot vs a non-S4 skin note).
**Consequences:** One spine ties booking → charting → checkout → recall → follow-ups together; the "what's next" is always visible to the right role.
**Alternatives:** Independent screens with manual status (status quo — easy to drop the ball); a formal check-in/queue-management module (heavier than a small clinic needs).
