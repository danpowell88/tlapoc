# Architecture Decision Log — Aesthetic Clinic Platform

Records the significant technical decisions and their rationale. Format per entry: **Context →
Decision → Consequences → Alternatives**. Status: `Accepted` unless noted. These can be split
into individual `ADR-NNNN-*.md` files later; kept as one log for a lean team.

> Anchored to [02-requirements.md](../02-requirements.md). Each PRD cites the ADRs it depends on.

---

## ADR-0001 — Cloud platform: **Azure** (primary), AWS as documented fallback
**Status:** Accepted<br>
**Context:** Hard AU data-residency requirement; lean cost; staff already on Microsoft 365/Entra; backend is .NET. (REQ-SEC-1, C10/C21, decision table §2.)<br>
**Decision:** Build on **Azure, Australia East (Sydney)**. Use managed PaaS only. Keep an AWS-equivalent mapping documented (Cognito↔Entra, RDS↔Azure DB, S3↔Blob, Fargate↔Container Apps) so the choice is reversible.<br>
**Consequences:** First-class .NET + Entra integration; single identity vendor; cheap burstable tiers. Lock-in mitigated by containerised .NET + Postgres (portable).<br>
**Alternatives:** AWS (viable, weaker ecosystem fit for M365 shops); multi-cloud (needless complexity for v1).

## ADR-0002 — Relational database: **PostgreSQL** (Azure DB for PostgreSQL Flexible Server)
**Status:** Accepted (confirm Postgres vs Azure SQL at Phase 0 — open item §10.7)<br>
**Context:** Need transactions, strong constraints, **Row-Level Security**, low cost, EF Core support.<br>
**Decision:** **PostgreSQL** with EF Core/Npgsql; burstable tier to start. RLS for tenancy (ADR-0003).<br>
**Consequences:** Cheap, portable, RLS-capable; mature .NET tooling.<br>
**Alternatives:** **Azure SQL** (equally native to .NET, also RLS — the leading alternative); Cosmos/NoSQL (rejected — relational integrity + multi-row invariants are core to compliance).

## ADR-0003 — Multi-tenancy: **single database, `tenant_id` + Postgres RLS**
**Status:** Accepted<br>
**Context:** Internal-first but **SaaS-ready** without a rewrite (decision §2).<br>
**Decision:** Shared schema; `tenant_id` on every table; **RLS** policies keyed off a per-request session setting (`SET app.tenant_id`), with tenant context also enforced in the API as defense-in-depth.<br>
**Consequences:** Cheapest ops, strong isolation, one migration path; can shard/extract noisy tenants later. SaaS = onboard a tenant row + Entra federation.<br>
**Alternatives:** DB-per-tenant (ops/cost heavy); schema-per-tenant (migration pain).

## ADR-0004 — Identity: **Microsoft Entra** — staff = Entra ID (workforce SSO); clients = Entra External ID (CIAM)
**Status:** Accepted<br>
**Context:** Staff already have M365 accounts; clients need social + email/password + OTP. (REQ-TEN-2.)<br>
**Decision:** **Entra ID** for staff SSO + MFA; **Entra External ID** for customers (Google/Apple social, local password, email/SMS OTP). For SaaS, each clinic tenant can federate its own Entra tenant for staff.<br>
**Consequences:** Unified Microsoft identity; offload auth/MFA/breach-surface to the platform; per-tenant federation is a clean SaaS story.<br>
**Alternatives:** AWS Cognito (fallback if AWS chosen); Auth0/Okta (cost); custom auth (**rejected** — never hand-roll auth for health data).

## ADR-0005 — App architecture: **Angular SPA + ASP.NET Core API as a modular monolith**
**Status:** Accepted<br>
**Context:** Lean team; one backend serving the web admin/booking and two Flutter apps.<br>
**Decision:** A single **.NET (ASP.NET Core) Web API**, internally a **modular monolith** with clear bounded modules (Tenancy, Clients, Booking, Clinical, Consent, Rx, Medicines, Payments, Memberships/Rewards, Notifications, Reporting, Integrations, Facility). **Angular** for the web client. REST + JSON; OpenAPI contract shared with Flutter.<br>
**Consequences:** Far simpler to build/operate than microservices; module seams allow later extraction; one deployable.<br>
**Alternatives:** Microservices (premature); serverless-only (cold-start + transaction friction for OLTP).

## ADR-0006 — Mobile: **Flutter** for both client and provider apps
**Status:** Accepted<br>
**Context:** Two apps, lean team, camera + offline needs. (Decision §2; user-directed.)<br>
**Decision:** **Flutter (Dart)**, one codebase with shared packages (auth, API client, design system), two app flavours (client, provider). Talks to the .NET API.<br>
**Consequences:** One mobile codebase, near-native UX, good camera/offline support; adds Dart as a third language alongside Angular/TS and C#.<br>
**Alternatives:** Native iOS+Android (2× cost); React Native (declined by user); PWA-in-shell (weaker camera/offline for charting).

## ADR-0007 — Payments: **`IPaymentProvider` abstraction, Square first**; in-person POS + cash + gift cards; card-on-file recurring for autopay
**Status:** Accepted<br>
**Context:** In-person POS first; "Square but pluggable"; **automatic** membership autopay; gift cards; online one-off checkout deferred. (PAY, MEMB.)<br>
**Decision:** Define `IPaymentProvider` (authorize/capture, refund, void, **tokenize/card-on-file**, **recurring charge**, gift-card issue/redeem). **SquareAdapter** first (card-present terminal + card-on-file). **Cash** recorded as an internal tender (no processor). Membership cards tokenised (added online/in-app or at desk) and auto-charged on schedule.<br>
**Consequences:** Provider-swappable (Stripe/Tyro later); **no PAN stored** (tokens only) → minimal PCI scope; cash and card reconciled in one ledger.<br>
**Alternatives:** Hard-couple to Square (rejected — reversibility); Stripe-first (user chose Square).

## ADR-0008 — **Compliance by construction**: enforce regulatory invariants in the domain + database, not just UI
**Status:** Accepted<br>
**Context:** The product's moat is compliance (C1–C24); UI-only checks are bypassable and won't survive an audit.<br>
**Decision:** Encode the hard rules as **domain invariants + DB constraints/triggers**:
- An `Administration` cannot persist without valid FKs to a `Consult`, an unconsumed `Prescription` for the *same* client, a current `Consent`, and a `lot/expiry` (C1, C2, C5, C8).
- Cooling-off + payment block enforced server-side for under-18 (C6).
- `RewardRule`/redemption restricted to **non-S4** catalog items by constraint (C9, REQ-MEMB-7).
- Scope-of-practice + registration currency checked in the auth pipeline (C4, C19).

**Consequences:** Hard to bypass; every block is logged and explainable to a regulator.<br>
**Alternatives:** UI/validation-layer only (**rejected**).

## ADR-0009 — Clinical media: **Azure Blob private + short-lived signed URLs; never stored on personal devices**
**Status:** Accepted<br>
**Context:** AHPRA image-use rules (C14); residency (C10/C21); known competitor failure mode of lost photos.<br>
**Decision:** Direct-to-Blob upload via short-lived signed URLs; image metadata + **image-use consent** in DB; provider app caches transiently (encrypted) only until synced, then purges. Access always via signed URL gated by role + consent.<br>
**Consequences:** Residency + access control; no device retention; resilient capture (ADR-0015).<br>
**Alternatives:** Store blobs in DB (bad at scale); third-party media SaaS (residency risk).

## ADR-0010 — **Append-only audit + immutable finalized records**
**Status:** Accepted<br>
**Context:** QLD Health / AHPRA / Privacy audits (C10, REQ-SEC-3).<br>
**Decision:** Single **append-only `AuditEvent`** stream for all PHI/clinical/medicines **read and write**; finalized `ChartEntry` and every `Administration`/medicine-register row are **immutable** (corrections are appended + linked, never edited).<br>
**Consequences:** Defensible, exportable trail; tamper-evident.<br>
**Alternatives:** Mutable rows + history table (weaker integrity guarantees).

## ADR-0011 — Telehealth: **out of platform**; record consult metadata only
**Status:** Accepted<br>
**Context:** Clinic uses an existing external telehealth app; building video is out of scope.<br>
**Decision:** No video. The `Consult` entity records modality (in-person/telehealth), prescriber, timestamp, external reference and notes — enough to satisfy the **synchronous-consult-before-script** linkage (C1).<br>
**Consequences:** Much less to build; depends on staff recording the consult (enforced by the script gate).<br>
**Alternatives:** Build/integrate video (deferred to a later phase).

## ADR-0012 — External integrations via **ports-and-adapters** (`INotifier`, `ICalendarProvider`, `IAccountingExport`)
**Status:** Accepted<br>
**Context:** SMS, calendar (M365/Google), Xero — must be swappable and AU-appropriate; webhooks/public API deferred.<br>
**Decision:** Each integration sits behind a .NET port. Adapters: **AU SMS** (MessageMedia/Twilio), **MS Graph + Google Calendar**, **Xero**. Outbound only in v1.<br>
**Consequences:** Providers swap without touching core; testable via fakes.<br>
**Alternatives:** Direct SDK coupling (rejected); event bus/webhooks now (deferred — REQ-INT-3).

## ADR-0013 — Reporting: **dedicated read models / materialized views**, refreshed from domain events
**Status:** Accepted<br>
**Context:** Rich analytics + compliance dashboards without slowing the transactional path (RPT).<br>
**Decision:** A separate **read schema** (materialized views / projections) feeds dashboards; rebuild the already-prototyped analytics logic here. Compliance dashboards (C-coverage, S4 register, lot-recall, registration/retention watch, breach/complaints) are queries over this layer + audit stream.<br>
**Consequences:** Fast dashboards, OLTP isolation; eventual consistency is acceptable for reporting.<br>
**Alternatives:** Query OLTP directly (won't scale, risks locks); external warehouse (overkill for v1).

## ADR-0014 — **Catalog with S4 classification** governs rewards eligibility and public-naming policy
**Status:** Accepted<br>
**Context:** Rewards must apply to **non-S4 only**; the public booking page must avoid S4 references (REQ-MEMB-7, C9).<br>
**Decision:** Every `Service`/`Product` carries **`schedule` (S4 | non-S4)** + category. `RewardRule` eligibility and redemption are constrained to non-S4 items; the **public booking-page naming policy** reuses the same flag. *(There is no advertising linter — advertising is out of product scope; see ADR-0034 withdrawn.)*<br>
**Consequences:** One classification drives the rewards rule and the public-naming policy; auditable.<br>
**Alternatives:** Manual per-offer exclusion (error-prone, non-auditable).

## ADR-0015 — Provider app: **offline-tolerant local queue + sync**
**Status:** Accepted<br>
**Context:** Treatment-room connectivity is unreliable; notes/photos must never be lost (NFR).<br>
**Decision:** The Flutter provider app queues chart edits, photos and (draft) administrations in an **encrypted local store** and syncs when connectivity returns. Drafts = last-write-wins; **finalisation happens server-side** and is then immutable (ADR-0010).<br>
**Consequences:** No silent data loss; smooth room-side UX.<br>
**Alternatives:** Online-only (rejected — fragile in clinics).

## ADR-0016 — **Data residency**: all PII/PHI in Australia; sub-processors AU or APP-8-assessed
**Status:** Accepted<br>
**Context:** Privacy Act / APP 8 (C10, C21); client expectation.<br>
**Decision:** Pin all storage + compute to **Australia East**. Payment/SMS/accounting sub-processors must be AU-resident or covered by a documented APP-8 cross-border assessment + client consent.<br>
**Consequences:** Compliant residency; constrains provider selection (acceptable).<br>
**Alternatives:** Global/multi-region (rejected for v1).

---

> **ADRs 0017–0022 added rev 2 (2026-06-19)** after building the clickable prototype.
> They record decisions the prototype surfaced and flag items that **need feasibility research**
> before commit (🔬). See `02-requirements.md` §12 for the full alignment & feasibility register.

## ADR-0017 — Access model: **capability flags + "concerns"**, with custom roles (future)
**Status:** Accepted<br>
**Context:** The prototype introduced a richer role set than the original §3 matrix — **NP, Lead Nurse (RN), RN, Dermal/laser tech, Reception, Owner (non-clinical business owner)**, plus combined **Solo-NP** and **Nurse-led-RN** presets. The owner is non-clinical (read-only clinical/stock oversight, full financials); clinical staff should mostly see information *concerning them* (e.g. stock-expiry matters to Lead/NP/owner, not every RN). (REQ-TEN-3/4, §3.)<br>
**Decision:** Model access on two orthogonal axes: **capabilities** (atomic permissions — `chart`, `chartView`, `prescribe`, `stock`, `receiveStock`, `financials`, `takePayment`, `configure`…) and **concerns** (relevance tags that drive what a role sees first — `ops, clinical, stock, stockAlert, financial, business, recall, consent`). Built-in roles are presets of (capabilities × concerns); a future **custom-role builder** lets a tenant compose roles by ticking capabilities + concern tiles. **Owner = business role:** financials + read-only clinical/stock, no prescribe/chart/custody.<br>
**Consequences:** Implements the §3 scope matrix while supporting per-tenant roles and role-tailored dashboards. Enforcement stays server-side (ADR-0008): **capabilities gate API actions; concerns only affect presentation.**<br>
**Alternatives:** Fixed role enum (less flexible); full ABAC/policy engine (overkill for v1).

## ADR-0018 — Omnichannel conversations: unified-inbox **sync model** — 🔬 *feasibility research required*
**Status:** Proposed (Phase 2 for social channels; v1 stays SMS/email — see PRD-07)<br>
**Context:** The prototype includes a **unified inbox** across **Instagram, Facebook/Messenger, SMS and email** with categorisation and suggested replies. Real platform support — especially Meta — is constrained, and staff often reply on the native platform too.<br>
**Decision:** Model conversations channel-agnostically — `Conversation`/`Message` with `channel`, `direction`, `sentVia` — behind an **`IMessagingChannel`** adapter per channel (extends the `INotifier` port, ADR-0012). **Inbound** via provider **webhooks**; **outbound** via each provider's Send API; **reconcile/backfill** (incl. replies staff send natively + pre-connection history) via the provider **Conversations/history API**; capture native-sent replies via **message echoes**; coexist with the platform's own inbox via Meta's **Handover Protocol** (secondary receiver + standby). Enforce **send-time guardrails**: messaging window, message tags, opt-in, and the advertising linter (ADR-0014, C9). **Suggested replies are templated/keyword-based in v1 (no AI, decision §2); LLM-assisted drafting deferred.**<br>
**🔬 Feasibility / research (validate before commit):** Meta requires **Professional accounts**, (often) a linked Page, **App Review + Business Verification**; a **24-hour messaging window** limits outbound to specific tags — **promotional/marketing DMs are largely *not* permitted** outside it; you can't cold-DM; IG echo/standby support is weaker than Messenger and changes often. **Implication:** treat **IG/FB/WhatsApp as reactive/service** channels; do **proactive marketing (recall/promos) via SMS/email (consented)** or **WhatsApp templates**. Assess WhatsApp Business Cloud API, per-channel rate limits, and validate scopes against current Meta docs.<br>
**Consequences:** A faithful "mirror" inbox is achievable for *service* conversations; *marketing* automation stays on SMS/email. Adds per-clinic OAuth onboarding, token lifecycle and webhook infra.<br>
**Alternatives:** SMS/email only (loses the social-inbox value); rely on Meta's native inbox (no unification/automation).

## ADR-0019 — Conversation ↔ client **identity resolution**
**Status:** Accepted<br>
**Context:** Inbound messages arrive with a channel handle (IG @handle, Messenger PSID, phone, email) often **not yet linked** to a `Client`; the prototype lets staff link a conversation to a client and **capture the handle** so replies/suggestions use client history.<br>
**Decision:** A **`ChannelIdentity`** (channel, external id/handle, `client_id?`) joins conversations to clients. **Auto-match** on phone/email; otherwise offer a **link/merge** action that, on confirm, **stores the handle on the client** for future auto-routing. Personalised (templated) suggestions read client history only **after** linking.<br>
**Consequences:** Better service + personalised suggestions; captured handles are **personal data** (consent/retention, APP — C21).<br>
**Alternatives:** Never link (loses context); auto-link on fuzzy name (false-merge risk).

## ADR-0020 — Injection-point **auto-detect: advisory ML, human-confirmed** — 🔬 *feasibility research required*
**Status:** Proposed (Phase 2; v1 ships manual mapping only)<br>
**Context:** The charting prototype offers "auto-detect" of injection points with manual fine-tune/add — implying facial-landmark detection. Decision §2 says **no AI in v1**.<br>
**Decision:** If built, auto-detect is **advisory only** — it proposes candidate points from facial landmarks that the clinician **must review, adjust and confirm**; it never sets product/units, never auto-finalises, never auto-administers. Prefer **on-device/edge** landmarking (privacy, latency); if server-side, stay within AU residency (ADR-0016) and image-use consent (ADR-0009). **v1 = manual tap-to-add + drag only.**<br>
**🔬 Feasibility / research:** landmark accuracy on real treatment angles/lighting; on-device libraries (MediaPipe / ML Kit face mesh) vs server; keep firmly **advisory** to avoid SaMD/medical-device classification; confirm it saves time without adding clinical risk.<br>
**Consequences:** A later time-saver with no clinical-safety/regulatory exposure; v1 unaffected.<br>
**Alternatives:** Always-manual (fine for v1); fully-automatic placement (**rejected** — clinical risk).

## ADR-0021 — Stock as a **multi-product, multi-unit catalogue** (extends ADR-0014)
**Status:** Accepted<br>
**Context:** The stock prototype tracks several distinct products (two toxin brands + a filler) with **different units** (toxin "units" vs filler "syringes/mL") — a single aggregate "units on hand" is meaningless. Prescriber/owner add/remove products and set the **S4 flag** + par levels.<br>
**Decision:** `Product` carries `type` (toxin/filler/skin/other), `unit`, `par`, **`schedule` (S4|non-S4)** and ARTG fields; **lots** belong to a product; all on-hand/usage/wastage/expiry aggregate **per product + unit**, never across units. A **catalogue admin** (capability-gated to prescriber/owner) manages products and the S4 flag — the single source of truth that drives rewards/public-naming (ADR-0014) everywhere. Usage history, reorder and par signals are **per product**.<br>
**Consequences:** Correct, unit-safe stock and reporting; one S4 classification point.<br>
**Alternatives:** Single product/unit model (wrong for real formularies).

## ADR-0022 — **Pricing & "what-if" planning** on read models
**Status:** Accepted<br>
**Context:** The owner view includes a **pricing & what-if simulator** — edit plan/service prices and see projected MRR/revenue impact under a churn-sensitivity assumption.<br>
**Decision:** A **read-only planning tool** computed over the reporting read models (ADR-0013) + configurable elasticity/churn assumptions; it **proposes** changes and projects impact but does **not** mutate live pricing until explicitly **applied** through the normal catalogue/membership admin (capability-gated, audited — ADR-0010).<br>
**Consequences:** Owners plan price/membership changes safely; reuses analytics; clean apply/audit path.<br>
**Alternatives:** Off-platform spreadsheet (loses live data); auto-apply (unsafe).

## ADR-0023 — Unified follow-up / task queue ("Jobs")
**Status:** Accepted<br>
**Context:** Follow-ups were scattered (recall worklist, dashboard "needs attention", unanswered inbox messages) and could be **lost if no one replied**. The prototype adds one **Follow-ups** queue.<br>
**Decision:** A single **`Job`** entity — `type` (reply/callback/recall/consent/stock/restock/admin), title, **linked** client/conversation/appointment, **assignee** (role/person), `due`, **`status`** (open/snoozed/done), **`source`** (manual/auto/recall/system). Existing signals (recall due, consent pending, stock/expiry alerts, unanswered conversations) **project into** the same queue rather than living in separate UIs. Staff can **manually flag** any message/client → a Job. Inbound comms are **auto-categorised into Jobs by rules/keywords** (reuse the inbox categoriser) — **no AI in v1**; LLM-assisted triage is a later option. Role-scoped **"my queue"** (concerns model, ADR-0017); all status changes audited (ADR-0010).<br>
**Consequences:** Nothing falls through; one place to work the day. Auto-categorisation accuracy is a **UX, not safety**, concern — jobs are advisory and human-actioned.<br>
**Alternatives:** Keep separate recall/attention lists (status quo — things get lost); a full ticketing system (overkill for v1).

## ADR-0024 — Visit lifecycle & role hand-offs (the appointment is the spine)
**Status:** Accepted<br>
**Context:** Strong individual screens existed, but the *visit* didn't carry the client between roles — staff had to know "what's next". (Workflow review, 2026-06-20.)<br>
**Decision:** The `Appointment`/`Visit` is a **state machine** — Booked → Confirmed → (Late / No-show) → In treatment → For checkout → Done (→ Recall set) — and each state surfaces the **next action for whoever's responsible now**, handing off automatically: reception flags **late / no-show** (a no-show auto-creates a **follow-up call** job, ADR-0023) and a clinician **starts** treatment; on **finalise**, a close-out (send aftercare · set recall · 2-day **wellbeing call** · adverse-event) sets the visit **For checkout**, lighting up reception's queue; payment marks it **Done**. Small clinics skip a formal **check-in** — *late attendance* and *no-shows* are the flags that matter. Capabilities (ADR-0017) gate the per-state actions; charting is **treatment-type-aware** (toxin injection-map + S4 lot vs a non-S4 skin note).<br>
**Consequences:** One spine ties booking → charting → checkout → recall → follow-ups together; the "what's next" is always visible to the right role.<br>
**Alternatives:** Independent screens with manual status (status quo — easy to drop the ball); a formal check-in/queue-management module (heavier than a small clinic needs).

---

> **ADR-0025…0036 (rev 4, 2026-06-20)** — the **gap-area build**. Six research/design passes (treatments & clinical depth, front desk & operations, money & retail, staff & HR, compliance & governance, growth & integrations) extended the staff prototype with new POC flows. Each agent independently proposed "ADR-0025"; the numbers below are the **reconciled, canonical** assignment. The client app remains out of scope.

## ADR-0025 — Treatment **modality model**: typed charts, product-class routing & licence gating
**Status:** Proposed (Phase 2; v1 ships toxin + non-S4 skin only)<br>
**Context:** Beyond the toxin slice, real clinics run dermal filler, energy devices (laser/IPL/RF), threads/PRP/boosters/fat-dissolving/IV, and weight-loss (GLP-1) programs. Each differs on four axes the toxin spine doesn't capture: **schedule** (S4 vs non-S4), **regulatory class** (medicine vs Class III device vs autologous/consumable), **adverse-event routing** (DAEN-medicines vs DAEN-devices vs none) and **who may legally perform it** — filler is **dual-natured** (S4 for prescribing/custody/advertising but device-class for DAEN); energy devices need a **state radiation/laser licence** (QLD/WA/TAS only; IPL only TAS) not an S4 capability; pharmacy-**compounded GLP-1 is prohibited (1 Oct 2024)** so only ARTG brands may be supplied.<br>
**Decision:** Model treatment as a typed **modality** carrying `{schedule, regClass, daenRoute, unit, advertisable, requires:[consult|rx|s4Lot|laserLicence|patchTest]}`. Charting becomes **modality-aware** (extends ADR-0024): filler = multi-area / multi-syringe / per-area lot + **VO/blindness consent gate**; energy device = **settings/fluence logbook** + safety checks + **licence gate** (no S4); weight-loss = **titration protocol** + ARTG/compounded enforcement. The catalogue **`s4` flag (ADR-0014/0021) is extended**, not replaced, with `regClass`, `artg`, `compounded`, `daenRoute`. A new **`laserLicence` credential** (per state/class) gates energy-device booking/charting.<br>
**Consequences:** One classification record drives charting surface, consent clauses, custody, rewards/public-naming and AE routing — no per-modality bespoke logic. v1 unaffected (toxin + skin only).<br>
**Alternatives:** Per-treatment bespoke screens (unmaintainable, drifts on compliance); treat all injectables as "S4 like toxin" (wrong DAEN routing, misses device class & laser-licence gate & the GLP-1 ban).

## ADR-0026 — Front-desk **operations** & opt-in booking deposits
**Status:** Accepted (re-opens the v1 "no deposits" decision)<br>
**Context:** The prototype lacked the front-desk/facility layer a clinic is audited on — walk-ins, waitlist fill, room/device conflicts, a **daily cold-chain log** ("Strive for 5" wants twice-daily min/max/current even with a data-logger; we only alerted on excursion), sterilisation/equipment maintenance (**AS 5369:2023**, superseding AS/NZS 4815), open/close checklists and inbound phone. Deposits were deferred, but lawful ACL-fair deposit practice and no-show loss make a front-desk-controlled, opt-in deposit worth re-scoping.<br>
**Decision:** Add an **Operations** area (reception/facility concerns, ADR-0017) extending existing spines: cold-chain log + breach pathway hang off the **stock ledger** (C13); equipment/open-close are lightweight registers projecting **Jobs** (ADR-0023); walk-ins/waitlist/resources extend the **visit lifecycle & calendar** (ADR-0024); phone becomes a **channel + Job**. **Booking deposits are opt-in, ACL-fair, disclosed-at-booking, refundable on notice and suppressed during cooling-off (C6)** — never a pressure mechanism. Equipment/sterilisation tracking is **optional per tenant**.<br>
**Consequences:** Reception gets a real home; the clinic can evidence cold-chain, sterilisation & emergency-kit currency at audit; cancelled chair-time and missed calls are recoverable.<br>
**Alternatives:** Keep deposits deferred (leaves no-show loss); a heavyweight CMMS (overkill); bypass gates for walk-ins (rejected — breaks C1–C3).

## ADR-0027 — Money **read models**: commission/pay-run, AP/PO, retail & BAS — attribution & export, **not** a payroll/tax engine
**Status:** Accepted (v1 builds per-line GST + PO/receive + retail SKUs; full pay-run/BNPL Phase 2)<br>
**Context:** Contractor injectors are paid by service/product split, but AU super (SGAA s12(3)) and state payroll-tax "relevant contract" rules largely catch individual injector splits regardless of the "contractor" label, and Payday Super starts 1 Jul 2026. GST: aesthetic services **and** retail are both taxable; the prototype's flat `total/11` GST is wrong. We receive stock but never order it.<br>
**Decision:** Compute money views as **read models** over the reporting layer (ADR-0013): commission pay-run = attributed service+product revenue × a configured split, exported as CSV / Xero bill — we do **not** calculate super/PAYG/payroll tax; an **engagement-type flag** drives a compliance banner. `PurchaseOrder` + receiving extends the catalogue (ADR-0021); **S4 POs require a prescriber signer** + ARTG/lawful supply (C11). Retail SKUs are non-S4 catalogue items. Every catalogue item carries a **`taxCode`**; invoices compute **GST per line** + a BAS summary (G1/1A/1B) to Xero. Refunds/disputes use `IPaymentProvider.refund` (ADR-0007) + the Jobs queue (ADR-0023) and **restock non-S4 only**; BNPL (Afterpay/Zip) are tenders, not new processors.<br>
**Consequences:** Faithful money attribution and correct GST without owning payroll/tax liability (stays with the accountant). Risk: clinics may read commission output as tax-ready — mitigated by an explicit non-advice banner.<br>
**Alternatives:** Build a payroll/super engine (rejected — liability + scope); off-platform spreadsheets (loses live attribution).
> **Revised 2026-06-20 (scope cut):** the books move to **Xero & integrations**. The app keeps **pricing / what-if** (ADR-0022) and **high-level reporting** (ADR-0013) only; in-app **commission pay-run, supplier POs/AP, refund/dispute management and BAS/GST tooling are dropped** (handled in Xero / payroll / the bookkeeper). Per-line tax coding + invoice/payment sync to Xero remains so the books stay correct. The **Finance screen becomes a light pricing + reporting hub** that defers the ledger to Xero. (REQ-RPT-6 narrows to pricing + reporting; REQ-MED-14 PO/AP and REQ-PAY-7 dispute-management move to "external / Xero".)

## ADR-0028 — Credential, CPD & **insurance currency** as first-class gating data
**Status:** Accepted (POC simulates AHPRA verification)<br>
**Context:** ADR-0017 gates clinical actions on capabilities × concerns and on credentials, but credential/CPD/PII data was implicit. AU law (s129 National Law, NMBA standards, Sept-2025 cosmetic guidelines) makes registration currency, CPD (RN/EN 20h, NP 30h) and **cosmetic-scope** professional-indemnity insurance hard preconditions for lawful injectable practice — and standard nursing PII policies often **exclude** cosmetic.<br>
**Decision:** Model credential, CPD and PII as structured per-practitioner records. Derive a single **compliance status** (`canInject`) and feed it into (a) booking availability, (b) charting gates, (c) the owner exceptions digest, (d) the Follow-ups queue as expiry tasks. Auto-verify via the **AHPRA Practitioner Information Exchange (PIE)** where approved, degrading to **manual verification with a stored "verified-on" date** (🔬 PIE is approval-gated SOAP).<br>
**Consequences:** "Are we legal to operate today?" becomes a board, not a memory; a practitioner whose PII excludes cosmetic is flagged not-bookable for S4.<br>
**Alternatives:** Keep credentials implicit (status quo — risk of a lapsed/uncovered injector treating).

## ADR-0029 — **Roster** as the source of truth for booking availability
**Status:** Accepted (single location; multi-location & payroll Phase 2)<br>
**Context:** Booking step 2 only *hinted* a roster ("availability respects their shifts"). The roster *is* availability: a practitioner is bookable only when rostered at that location AND compliant for the service scope.<br>
**Decision:** A per-location roster of shifts & leave (Owner/Lead manage; Reception read-only). A practitioner is bookable for a service **iff rostered that day AND `canInject`/scope-compliant** (ADR-0028). Multi-location/locum roster and payroll/commission are deferred (commission lives in ADR-0027).<br>
**Consequences:** Turns booking-step hint copy into real behaviour; roster + insurance status gate who can be scheduled.<br>
**Alternatives:** Free-for-all availability (double-books, schedules non-compliant injectors).

## ADR-0030 — **Governance hub**: cross-case compliance surface, guardrails stay woven
**Status:** Accepted<br>
**Context:** The prototype wove compliance into each workflow (consult-gated scripts, consent blocks, cold-chain, lot→client recall lookup, adverse-event concept, complaints in the inbox). But *execution & evidence* work — DAEN submission, recall campaigns, incident case-management, P&P sign-off, waste manifests, audit packs, DSAR/breach — is owner/compliance-officer work done **across** cases, with no home.<br>
**Decision:** Add a single **Governance** module, capability-gated (financials or a `compliance` concern; default-on for owner/solo/nurse-led). It is a **read/manage surface** that launches the existing woven-in flows and **projects** existing signals into governance worklists — it does **not** relocate any guardrail. Per-treatment invariants stay enforced in the domain (ADR-0008); all governance actions are append-only audited (ADR-0010) and read from the reporting read models (ADR-0013).<br>
**Consequences:** The compliance officer gets one place to *do governance and produce evidence*; the moat's hard rules remain un-bypassable and un-moved.<br>
**Alternatives:** Pure-woven, no hub (cross-case work has nowhere to live); a separate compliance product (overkill, breaks single-clinic feel).

## ADR-0031 — DAEN / regulatory **submission via prefilled export + portal hand-off** (no direct API in v1) — 🔬
**Status:** Proposed (v1 = prefill + mark-submitted; electronic submit later)<br>
**Context:** TGA runs two databases (DAEN-medicines vs DAEN-devices) and, for facility mandatory device reports, **ASDER** (from 21 Mar 2026, day-hospital facilities, 10-day window); state EPAs run their own waste-tracking systems (NSW IWTS CA+TC, QLD WTC). Direct integration is uncertain and jurisdiction-specific.<br>
**Decision:** v1 **classifies and prefills** the correct report (route by product `schedule`/`type`), **flags mandatory triggers**, opens the official portal and records submission status + reference in the audit trail. State waste tracking is captured as **recorded manifest numbers**, not API-integrated. Most room-based cosmetic clinics fall *outside* the mandatory device rule — the system flags the obligation rather than asserting it universally.<br>
**Consequences:** Faithful, low-risk; clean upgrade path to electronic submit.<br>
**Alternatives:** Build direct submission now (unproven APIs, high maintenance); leave fully manual (misses the moat).

## ADR-0032 — Reviews & reputation: **request-all (no gating), reply-yes, repost-S4-no**
**Status:** Accepted<br>
**Context:** Patients posting organic reviews is fine, but (a) reposting/embedding a review that endorses an S4 outcome becomes a prohibited **testimonial** (National Law s133; TGA Code Part 6) and (b) **review gating** — soliciting only happy clients — is **misleading conduct under the ACL** (ACCC).<br>
**Decision:** Post-visit review requests go to **all** eligible clients with no sentiment pre-screen. Staff may **reply** to any review. The platform has **no feature that reposts or embeds a review as marketing**, so an S4-endorsing review can't be turned into a prohibited testimonial; where a review names an S4 result, staff are shown a **caution** against resharing it publicly. *(The earlier `s4`-flag advertising linter is withdrawn — 2026-06-20 scope cut, ADR-0034.)*<br>
**Consequences:** Defensible under both AHPRA and ACL; the reputation feature can't be weaponised into non-compliant testimonials.<br>
**Alternatives:** Gated review requests (illegal); free reposting (prohibited testimonials).
> **Extended 2026-06-20:** reviews can be **acknowledged** and **flagged for follow-up**; negative reviews (≤3★) and complaint-keyword matches are **auto-detected** and raised as review jobs in the Follow-ups queue (Lead Nurse for unhappy/clinical, Reception otherwise) — closing the loop between a public review and the action it needs.

## ADR-0033 — Lead / prospect **CRM as a projection over conversations**
**Status:** Accepted<br>
**Context:** Most enquiries arrive via IG/FB DM, website and phone asking the one thing clinics can't answer publicly ("how much is Botox?"). A pipeline lets reception convert privately — 1:1 service replies are out of scope of public-advertising rules.<br>
**Decision:** A `Lead` (stage, source, interest, `client_id?`, `conversation_id?`, consent) is a thin pipeline layer over the inbox (ADR-0018/0019); stage transitions feed conversion read models (ADR-0013). Outbound nudges gate on **marketing consent (C23)**; advertising compliance (C9) is the clinic's responsibility in its external tools (no platform linter).<br>
**Consequences:** Enquiries don't get lost; conversion is measurable; the consent gate keeps outreach Spam-Act-safe.<br>
**Alternatives:** Work enquiries only in the inbox (no pipeline/conversion view).

## ADR-0034 — ~~One advertising linter for all public/outbound content~~ — **Withdrawn**
**Status:** **Withdrawn (2026-06-20)** — advertising tooling removed from scope.<br>
**Context:** Originally, every public surface (newsletter builder, social scheduler, public booking page/SEO, review/inbox replies) was to reuse a single advertising-linter service so a clinic couldn't accidentally promote an S4 good.<br>
**Decision (withdrawn):** The platform now provides **no advertising linter and no ad-material production tooling**. Email campaigns, social posting and all advertising live in the clinic's **external tools** (Mailchimp, Meta Business Suite), and TGA/AHPRA advertising compliance is the **clinic's responsibility** (C9, reframed as clinic-owned). The only public surface the app owns — the **public booking page / SEO** — uses generic service names + withheld S4 prices **by configuration**, not an automated linter.<br>
**Consequences:** Smaller scope and no false confidence in an automated check; advertising risk sits with the clinic, where the content is actually produced. **REQ-NOTIF-4 withdrawn**; REQ-NOTIF-10/11 already withdrawn. Reviews/inbox keep a passive staff *caution* (ADR-0032) but no blocking linter.<br>
**Alternatives:** Keep a reduced linter on the surfaces the app owns (the prior 'revised' position) — rejected: still builds advertising-checking tooling the clinic didn't want.

## ADR-0035 — **e-Prescribing** via `IPrescribingProvider` adapter (eRx/ETP) — 🔬 *feasibility research required*
**Status:** Proposed (deferred; research)<br>
**Context:** AU electronic prescribing uses token (SMS/email) or Active Script List via exchanges (eRx, MediSecure), built around PBS but supporting **private** scripts. A cosmetic prescriber could issue a compliant electronic private S4 script — a heavier integration (conformance, prescriber HPI-I).<br>
**Decision:** If built, electronic private S4 scripts issue behind an `IPrescribingProvider` port, bound to the synchronous consult (C1, ADR-0011), prescriber identity and the S4 register (ADR-0008/0021). No PBS assumptions for cosmetic use. v1 keeps paper/PDF private scripts.<br>
**Consequences:** A future convenience with the same custody/consult guarantees; deferred until feasibility is proven.<br>
**Alternatives:** Build now (unproven, heavy); never (loses a real convenience).

## ADR-0036 — Online checkout, **deposits**, two-way calendar & public API — phasing
**Status:** Proposed (deferred — §9 later phases)<br>
**Context:** Online checkout + booking deposits reduce no-shows; two-way calendar sync (M365/Google) is real demand; webhooks/public API are Phase 3. Medicare/HICAPS is non-applicable to cosmetic (claimable only for therapeutic exceptions).<br>
**Decision:** Online checkout + deposits sit behind the existing `IPaymentProvider` (ADR-0007); **S4 is never priced or sold online** (ADR-0014). Two-way calendar promotes ADR-0012 to **bidirectional** under `ICalendarProvider` (external busy events block availability; clinic appts push out). Webhooks/event-bus/public API stay **Phase 3**. Medicare/HICAPS is surfaced as "not applicable to cosmetic" and otherwise out of scope.<br>
**Consequences:** A clear, honest roadmap for growth integrations without overpromising in v1.<br>
**Alternatives:** Pull everything forward (scope blow-out, unproven feasibility); ignore the demand (loses competitiveness later).
