# Glossary & app-flow map

Shared reference for the backlog. Every story should (a) explain acronyms and
non-obvious concepts on first use — using the wording below for consistency —
and (b) say where it sits in the wider app and the build timeline (see the flow
map at the end). This file is the single source of truth for both.

> **Setting.** "The Lounge Aesthetics" is a single aesthetic clinic (cosmetic
> injectables and skin treatments) in Queensland, Australia. The platform is a
> staff-facing web app plus two mobile apps, backed by one API and database.
> Everything is multi-tenant from day one so the product can serve other clinics
> later, but v1 ships for one clinic.

---

## Regulatory & compliance

- **AHPRA** — Australian Health Practitioner Regulation Agency. Registers health
  practitioners (nurses, doctors) and sets the rules they must follow; a
  practitioner's registration and endorsements determine what they may legally do.
- **Scope of practice** — what an individual practitioner is qualified, registered
  and authorised to do. The platform encodes this so the system, not the person,
  enforces the boundary.
- **TGA** — Therapeutic Goods Administration. Regulates medicines and medical
  devices in Australia, including how they may be advertised.
- **Poisons Standard (SUSMP)** — the national scheme that classifies medicines into
  Schedules by how tightly they must be controlled.
- **S4 — Schedule 4 "Prescription Only Medicine."** Cosmetic injectables such as
  botulinum toxin are S4: they may only be administered against a valid
  prescription written for a specific patient by an authorised prescriber after a
  consultation. This consult → prescription → administration chain is the
  platform's central compliance rule (the "S4 gate"). Dermal fillers are regulated
  medical devices rather than scheduled medicines, but are governed through the
  same clinical controls.
- **Rx** — a prescription.
- **Prescriber** — a practitioner authorised to write a prescription (e.g. a
  doctor, or a nurse practitioner within scope).
- **DAEN** — Database of Adverse Event Notifications. The TGA's system for
  reporting adverse events (an adverse event = an unwanted medical occurrence after
  a treatment, e.g. a reaction or complication). Serious events must be reported.
- **Cooling-off period** — a mandatory wait before a cosmetic procedure can
  proceed. Under current Ahpra guidance a **7-day cooling-off applies to patients
  under 18**; there is **no mandated cooling-off for adults**. The platform blocks
  booking/payment for minors until the period elapses.
- **Privacy Act 1988 / APP** — the Australian Privacy Principles. **APP-8** governs
  cross-border disclosure: personal information must not leave Australia to a party
  that isn't bound by equivalent protection. The platform keeps data in-country and
  gates any overseas sub-processor.
- **DSAR** — Data Subject Access Request: a person's legal request to access or
  correct the personal information held about them. The platform answers these
  within the statutory window (30 days).
- **Spam Act 2003** — governs commercial electronic messages: they need consent,
  must identify the sender, and must offer a working unsubscribe. Transactional
  messages (e.g. appointment reminders) are treated differently from marketing.
- **IPC** — Infection Prevention and Control: clinical hygiene practice (sterile
  technique, cleaning, sharps/waste handling) and the logs that evidence it.
- **Cold chain** — the unbroken temperature-controlled storage required for
  medicines; a fridge breach can spoil stock, so temperature is logged and breaches
  quarantine the affected lot.
- **Lot / batch** — the manufacturer's batch number of a medicine vial. Recorded
  against every dose so stock can be traced and recalled.
- **Cn (C1–C24)** — the project's own compliance criteria, defined in
  `docs/02-requirements.md`; stories link to the specific ones they satisfy.
- **QLD** — Queensland; the state whose private-health-facility and advertising
  rules apply to this clinic.

## Clinical

- **Consult (consultation)** — the assessment appointment where suitability is
  established and (for S4) a prescription can be written. Required before any S4
  treatment.
- **Charting** — the clinical record of what was actually done in a treatment.
- **Injection mapping** — marking each injection point on a face/body diagram with
  the product, dose (in **units** for toxin), depth and technique, plus the **lot**
  used — the core of the injectables chart.
- **Finalise / immutable record** — once a chart is finalised it cannot be edited;
  corrections are added as appended, attributed **amendments**, preserving the
  original. Finalising also deducts the used stock from inventory.
- **Modality** — a category of treatment or device (e.g. energy-based/laser
  devices) beyond injectables; v1 leaves non-injectable modalities as placeholders.

## Architecture & technical

- **Multi-tenancy / tenant** — one clinic's data, isolated within the shared
  platform. Every record carries a tenant id.
- **RLS — Row-Level Security** — a Postgres feature that filters every query to the
  current tenant at the database level, so one clinic can never read another's
  data even if application code has a bug. The tenant is set per request.
- **RBAC — Role-Based Access Control** — permissions granted by role (Owner,
  Practitioner, Reception, …) rather than per person. Combined with scope-of-
  practice to decide what each user can see and do.
- **`canInject`** — the derived gate that decides whether a given staff member may
  administer injectables right now, from their registration, scope and current
  credential/indemnity status. Used across booking, consult and charting.
- **MFA** — Multi-Factor Authentication. **Step-up auth** — re-prompting for a
  second factor before an especially sensitive action.
- **Audit log (append-only / immutable)** — a tamper-evident record of who did what
  and when; entries are never edited or deleted.
- **Domain event** — a fact emitted when something happens in the system (e.g.
  "chart finalised"). **Read-model / projection** — a query-optimised view built by
  consuming those events, kept **eventually consistent** (updated a moment after the
  event, not in the same transaction). This is how dashboards and reports are built
  without slowing the clinical write path.
- **`.fin` capability / financial gating** — money figures (revenue, MRR, pricing,
  margins) are owner-only; the server strips them for non-owner roles. See **MRR**,
  **COGS**.
- **IaC — Infrastructure as Code**; **CI/CD — Continuous Integration / Continuous
  Delivery** (automated build/test/deploy). **AU East** — the Azure Australia East
  (Sydney) region used for **data residency** (keeping data in Australia).
- **Idempotent** — an operation safe to repeat without double-applying (e.g. a
  retried payment or sync must not charge or write twice).
- **Last-write-wins** — the conflict rule for offline sync: the most recent edit
  wins when a device reconnects.
- **Signed URL** — a temporary, expiring link that grants access to a stored photo
  without exposing the file or storing it on the device.
- **Webhook** — an inbound HTTP callback from an external system (e.g. a payment or
  calendar provider) notifying us of an event.

## Commerce, comms & operations

- **POS — Point of Sale** — taking payment in-clinic at the front desk.
- **PCI-DSS / PAN / tokenization** — the card-security standard; the **PAN** is the
  raw card number, which we never store — the payment provider returns a **token**
  that stands in for the card.
- **Autopay** — automatic recurring billing (memberships). **Dunning** — the
  scheduled retry-and-chase process when a recurring payment fails.
- **Closeout** — end-of-day reconciliation of takings against recorded payments.
- **MRR — Monthly Recurring Revenue**; **COGS — Cost of Goods Sold** (the product
  cost behind a treatment); **GST** — Australia's 10% Goods and Services Tax.
- **Membership / package / gift card** — prepaid or recurring commercial products.
- **Rewards / loyalty** — points/perks; by rule rewards may **never** be applied to
  S4 medicines (you can't discount or incentivise a prescription medicine).
- **Recall** — proactively bringing a client back for follow-up or repeat
  treatment, worked from a list. **Waitlist** — clients waiting for an earlier slot.
- **Follow-up / job queue** — the unified worklist of tasks the clinic must action
  (no-shows, recalls, review responses, complications).
- **Lead / CRM** — a prospective client and the Customer Relationship Management of
  enquiries through to booking.

## Apps & surfaces

- **Provider app / client app** — the two flavours built from one Flutter codebase:
  staff-facing (day list, room-side charting) and client-facing (book, intake,
  consent, care, rewards).
- **Kiosk** — the in-clinic self-service **check-in** surface.
- **Back-office tablet** — the back-room operations surface (open/close, cold chain,
  stock, tasks).

## Project artifacts

- **PRD — Product Requirements Document**; **ADR — Architecture Decision Record**
  (a logged design decision and its rationale).
- **Epic / Story / Sub-task** — the backlog hierarchy. **Spike** — a time-boxed
  investigation that produces findings + a go/no-go, not production code.

---

## How the app fits together (flow & build timeline)

The backlog is sequenced **clinic-first**: the staff-facing clinical and
operational core is built before anything online, external or client-app facing.
A story's "how it fits" should place it on this spine.

1. **Setup (Sprint 0)** — repo, CI/CD, infrastructure, Postgres+RLS, app shells,
   security and the de-risk spikes. Nothing clinical ships until the platform is
   safe to build on. *Everything below depends on this.*
2. **Foundations (PRD-01) + App shell (PLATFORM)** — multi-tenancy, RBAC + scope-of-
   practice (the `canInject` gate), audit, retention, breach, sign-in/MFA, the
   owner-only financial gate, and the staff app shell (navigation, Today, search).
   *Unblocks every feature.*
3. **Reception (PRD-02)** — booking, calendar/availability, client records,
   check-in. The front-of-house entry point to a visit.
4. **Consent & gating (PRD-03)** — intake forms, versioned consent, the pre-treatment
   gate. Sits between booking and treatment; enforces what must be true before a
   clinician can proceed.
5. **Injectables (PRD-04)** — consult, prescribing and S4 governance: the compliance
   moat. Then **Charting (PRD-05)** — the injection-mapping clinical record and
   stock deduction. This is the clinical heart of the product.
6. **Reporting (PRD-08)** — read-models, business and compliance dashboards,
   register exports, DAEN prefill, inspection-readiness. Reads from everything above.
7. **Compliance ops (PRD-11)** — facility accreditation, IPC/waste logs, cold chain,
   complaints, open/close. The operational backbone around the clinical core.
8. **Payments (PRD-06)** — POS, packages, memberships + autopay/dunning, the
   S4-safe rewards engine, closeout. Commerce on top of the booked/charted visit.
9. **Comms & growth (PRD-07)** — reminders, recall, marketing consent, and the
   **client-facing/online** items (public booking page, reviews, leads). These come
   late because they face outward.
10. **Integrations (PRD-10)** — Xero accounting and two-way calendar sync; external
    systems, built once the internal data is solid.
11. **Apps (PRD-09)** — the Flutter client and provider apps and the kiosk/back-office
    surfaces; the client-facing mobile experience comes last, reusing the modules above.
12. **Backlog — Phase 2+ (PHASE-2)** — multi-location, SaaS onboarding, white-label,
    public API, native POS/kiosk. Deferred placeholders, pulled forward only if the
    case appears.
