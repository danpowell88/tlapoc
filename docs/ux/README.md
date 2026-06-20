# UX — Principles, Information Architecture & Screen Inventory

How the Aesthetic Clinic Platform should *feel* and how it's organised across its three surfaces.
The end-to-end journeys live in [flows.md](flows.md).

> Surfaces: **Web (Angular)** — admin/front-desk + public booking · **Client app (Flutter)** ·
> **Provider app (Flutter)**. All over the one .NET API (ADR-0005/0006).

## 1. Design principles
1. **Compliance is invisible until it matters.** The compliant path is the default path; gates only surface when something's missing, and always say **what's missing and how to fix it** (never a dead-end "blocked").
2. **Room-side is thumb-first.** The provider app is usable one-handed, gloves-on, in minimal taps; the injection-mapping canvas is the hero screen.
3. **Fast and modern.** Instant calendar/charting; no Mindbody-era clutter. Directly answers the "clunky/slow" pain.
4. **Never lose work.** Explicit save-state + offline queue; a visible sync indicator on the provider app (ADR-0015).
5. **Plain, honest language.** Consent and risk content in plain English; no hype; the public booking page uses generic, non-S4 service names by policy (C9 — advertising itself is produced in the clinic's external tools, not the platform).
6. **Trust signals.** Clear "your data stays in Australia", visible audit of who saw what, easy access/correction for clients (C10/C21).

## 2. Information architecture

### Web (Angular) — staff/admin + public booking
- **Public booking site** (unauthenticated): service (generic names) → practitioner → slot → account → intake/consent. *(No public S4 names/prices — C9.)*
- **Front desk:** Today (waiting / in-room / checked-out), Calendar, Check-in, POS/Checkout, Quick client search.
- **Clients:** Directory → 360° profile (overview, medical/contraindications, consents, photos, visits, memberships, balance, comms, complaints).
- **Clinical:** Charts, Medicines register & stock, Prescriptions/consults.
- **Commerce:** Sales/closeout, Memberships & plans, Rewards rules, Gift cards, Packages.
- **Comms:** Templates, Recall worklist, Marketing consent.
- **Reports:** Business dashboards, Compliance dashboards, Data quality.
- **Admin:** Staff & roles/credentials, Services & products (incl. **S4/non-S4** flag), Facility/accreditation, Integrations (Xero/calendar/SMS), Tenant settings, Audit log.

### Client app (Flutter) — bottom-tab nav
`Home` (next appt, recall nudge) · `Book` · `My care` (photos w/ consent, visit history) · `Membership & rewards` · `Account` (profile, balances, card-on-file, privacy/access-correction).

### Provider app (Flutter) — bottom-tab nav
`Schedule` (my day) · `Patient` (open record → consult/consent status → **map + photos** → finalise) · `Medicines` (stock, administer, wastage) · `Tasks/alerts`. Persistent **sync/offline** indicator.

## 3. Screen inventory (→ PRD)

| Surface | Screen | PRD |
|---|---|---|
| Public web | Booking wizard, account create, intake/consent | PRD-02, 03 |
| Front desk | Today board, Calendar, Check-in | PRD-02 |
| Front desk | Checkout/POS (card/cash/gift), membership sign-up, closeout | PRD-06 |
| Web | Client 360° profile | PRD-02, 05, 06, 11 |
| Web | Charts & injection map (read), Medicines register & stock | PRD-04, 05 |
| Web | Memberships/plans, Rewards rules, Gift cards | PRD-06 |
| Web | Recall worklist, Templates, Marketing consent | PRD-07 |
| Web | Business + Compliance dashboards, DAEN export | PRD-08 |
| Web | Staff/roles/credentials, Services & products (S4 flag), Facility, Integrations, Audit | PRD-01, 10, 11 |
| Client app | Home, Book, Intake/Consent, My care/photos, Membership & rewards, Account/card-on-file | PRD-02,03,05,06,09 |
| Provider app | Schedule, Patient, Injection-mapping canvas, Camera/photo, Consult/Rx, Finalise, Medicines/administer | PRD-04,05,09 |

## 4. Cross-cutting UX patterns
- **Blocked-action banner:** whenever a compliance gate stops an action (no consult, no consent, under-18 cooling-off, lapsed registration, S4 reward attempt), show a calm banner: *what's blocked · why (which rule) · the action to resolve · who can resolve it.*
- **Consent/age chips** on the patient header (consent current ✓ / image-use ✓ / under-18 ⏳ cooling-off).
- **S4 guardrail:** S4 items in the catalog are visibly tagged; reward/discount controls are disabled on them with a tooltip (C9/REQ-MEMB-7).
- **Offline state:** provider app shows queued-items count + last-sync time; finalise is disabled until synced.
- **Audit-friendly confirms:** destructive/clinical confirmations state that the action is logged.
- **Privacy surfaces:** client Account has "Your data & privacy" (residency note, access copy, request correction).
