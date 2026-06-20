# Product Requirements — Aesthetic Clinic Platform

> A purpose-built operating platform for aesthetic injectable & cosmetic clinics — the
> modern, compliance-native replacement for Mindbody. This document turns the
> [market research](01-market-research.md) and the scoping decisions into a v1 requirements
> spec, and ends with the **PRD breakdown** we'll write next.
>
> _Status: DRAFT for review, 2026-06-18 (rev 2). Working title only — no product name chosen yet._

---

## 1. Vision & positioning

**The wedge (from research §5):** no product today combines (a) modern UX (Mangomint/Boulevard),
(b) true injectable clinical depth (Aesthetic Record/Pabau), and (c) native **Australian
TGA / QLD-S4 / AHPRA-2025 compliance**. The platform sits in the middle of all three and makes the
**compliant path the default path**.

**Design principles**
1. **Compliance by construction** — you can't record an S4 administration without the consult, consent, prescription and batch/lot it legally requires. Guardrails > checklists.
2. **One loop, done well** — v1 nails a single treatment end-to-end before going wide.
3. **Lean & cheap** — cloud-native managed services, near-zero fixed cost until real volume; AU-hosted.
4. **Reporting is a feature, not an afterthought** — the analytics already prototyped become a first-class in-app module (fixes a top Mindbody pain).
5. **SaaS-ready, single-clinic-feeling** — multi-tenant under the hood (RLS), but day-one UX is tuned for one clinic.

---

## 2. Decisions locked (scoping Q&A, 2026-06-18)

| Decision | Choice | Implication |
|---|---|---|
| Audience | Internal-first, **SaaS-ready** | Multi-tenant data model + Row-Level-Security from day one; no customer billing/onboarding UI in v1 |
| Hosting / data | AU cloud, **Azure/AWS native** (no Supabase), cheapest first | AU data residency (Sydney); managed services only |
| v1 shape | **Thin end-to-end slice** | One treatment, full loop; depth-limited elsewhere |
| v1 treatment | **Anti-wrinkle (botulinum toxin)** | Highest volume, clear S4 profile, ~3–4mo recall |
| Charting depth | **Injection mapping + before/after** | On-image/diagram mapping w/ product·units·**batch-lot** per site |
| Auth | **Staff: Office 365 / Entra ID SSO**; **Clients: social + email/password + OTP** | Workforce SSO via Entra ID (reuse existing org accounts); customer identity via Entra External ID [Cognito]; MFA throughout |
| Apps | **Two apps in v1 — client + provider** | Built in **Flutter** (cross-platform, *not* native) |
| Web & backend API | **Angular SPA + .NET (ASP.NET Core) API** | TypeScript/Angular web · C#/.NET backend on Azure · Flutter apps share the same API |
| Payments | **In-person first** for POS — Square (card) + recorded **cash**; pluggable; **gift cards** | `IPaymentProvider`; one-off online checkout later (membership autopay excepted) |
| Memberships & rewards | **Inside v1** | **Automatic recurring autopay** (card-on-file, *not* in person) + **visit/membership rewards on non-S4 items only**, margin-aware |
| Migration | **None — greenfield** | Assume no Mindbody account and no existing data to import |
| AI features | **None now (far future)** | No AI scribe / AI in v1 or near-term |
| Webhooks / public API | **Much later** | Not in v1; internal events only as needed |
| Build team | **Lean (owner + Claude Code)** | Ruthless scope; managed/cheap services over custom infra |
| S4 model | **Configurable; v1 = on-site stock (Mode A)** | Mode B (nurse-led + pharmacy) deferred — no pharmacy partner yet |
| Team mix | RNs + NP(s) + dermal/admin | Scope-of-practice role gating required |
| Prescriber | On-site NP and/or remote telehealth (varies) | Both consult paths supported |
| Mindbody pains to fix | **All four**: no clinical/compliance, clunky UX, reporting gaps, cost | Product must be deep, compliant, fast *and* cheap |
| Timeline | No fixed date | Phase for quality |
| Integrations (v1) | **Xero, M365/Google calendar, SMS** | Each behind an adapter |
| Telehealth | **External app** | Platform records consult metadata/notes only; no video built |
| Booking deposits | **None in v1** | No deposit/card-on-file enforced for bookings |

---

## 3. Users, roles & scope-of-practice

### Personas
- **Client / patient** — books, completes intake/consent, views history, photos, memberships, balances (web + app).
- **Front desk / admin** — scheduling, check-in, payments, comms; limited clinical visibility.
- **Dermal therapist** — non-S4 skin services + their charting; **cannot** assess for or administer injectables.
- **Registered Nurse (RN)** — assesses, administers S4 **on a valid individual prescription**; may hold only **individually-dispensed** S4 (QLD); cannot prescribe or hold bulk stock.
- **Lead Nurse (senior RN)** — an RN who additionally **oversees stock & the clinical team**; same clinical scope as RN (administers on a valid script; no prescribing/custody), plus stock oversight and stock-expiry concerns.
- **Designated RN prescriber** *(new role — QLD endorsement available from Sept 2025; see §6.1)* — an RN holding the AHPRA *endorsement for scheduled medicines — designated registered nurse prescriber*, who may **prescribe S2–S4 (incl. cosmetic injectables) in partnership with an authorised prescriber** (doctor/NP), administer on that script, but **not hold bulk S4 stock** unless they are also the on-site custodian. A middle tier between administer-only RN and NP; the `prescribe-S4` capability is gated by the verified endorsement **and** a recorded partnered prescriber.
- **Nurse Practitioner (NP) / on-site prescriber** — assesses, **prescribes**, may hold S4 stock on-site, administers.
- **Remote prescriber (doctor/NP via telehealth)** — synchronous consult + prescribe only; no on-site stock.
- **Clinic owner (business)** — runs the business: **financials, reporting, configuration & audit**, plus **read-only** oversight of clinical records & stock; **non-clinical by default** (cannot prescribe, chart or hold S4) unless they personally hold the credential (`●*`).

### Scope-of-practice matrix (enforced defaults; configurable per tenant)

| Capability | Client | Admin | Dermal | RN | NP/On-site Rx | Remote Rx | Owner |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Book / reschedule | ● (self) | ● | ● | ● | ● | – | ● |
| Take payment / POS | – | ● | ● | ● | ● | – | ● |
| Holistic assessment + BDD screen | – | – | – | ● | ● | ● | ●* |
| Prescribe S4 (per synchronous consult) | – | – | – | – | ● | ● | ●* |
| Administer S4 (on valid Rx) | – | – | – | ● | ● | – | ●* |
| Hold S4 stock (custody) | – | – | – | dispensed-only | ● | – | – |
| Chart / injection map | – | – | ●(skin) | ● | ● | – | ●* |
| View full clinical record | – | restricted | own scope | ● | ● | ● | ● |
| Configure clinic / view audit | – | – | – | – | – | – | ● |

`●* = only if the owner also holds that clinical credential.` Credentials (registration #, AHPRA
type, ≥1yr non-cosmetic experience flag, training) live on the staff profile and gate the actions.

> **Access model (rev 3 — see ADR-0017).** Implemented as **capabilities** (atomic permissions that gate
> API actions) × **concerns** (relevance tags that decide what a role sees first). Built-in roles —
> **NP, Lead Nurse, RN, dermal, reception, owner(business)**, plus combined **Solo-NP**, **Nurse-led-RN**
> and **Designated-RN-prescriber** presets — are compositions of the two; a **custom-role builder** (tick
> capabilities + concern tiles) is a future addition. The matrix above is the default capability set per role.
> The **Designated-RN-prescriber** preset = the RN row **plus** the `prescribe-S4` capability, but that
> capability stays gated on (a) a verified AHPRA *designated RN prescriber* endorsement and (b) a recorded
> **partnered authorised prescriber** — without both, it behaves as a plain RN (see §6.1).

---

## 4. v1 scope — the toxin slice

**In scope (the loop):**
1. **Book** a toxin consult/treatment (web + client app), with a cancellation policy (no deposit in v1).
2. **Pre-visit intake & consent** sent ahead, completed on phone, incl. **medical history, contraindications, BDD screen**; **under-18 cooling-off** enforced.
3. **Synchronous consult** (in-person, or telehealth conducted in an external app) → record the consult (prescriber, datetime, modality, reference/notes) and the linked **individual prescription**. No batch/async scripts.
4. **Treatment charting** — injection mapping on a facial diagram + photo, **product · units · depth · batch-lot · expiry per site**; before/after photo capture & compare.
5. **S4 governance** — **Mode A on-site stock ledger** in v1 (mode abstraction retained for future pharmacy/Mode B); records custody and decrements stock on administration.
6. **Payment** — in-person POS via **Square** (card-present) or **recorded cash**; **gift cards**; package/series redemption; **membership sign-up with automatic recurring autopay** (card-on-file; can be added online/in-app, not required in person); apply member/visit **rewards (non-S4 items only)**.
7. **Recall** — automated ~12-week rebooking/recare prompt (SMS/app), aftercare sequence.
8. **Reporting** — rebuild the analytics (revenue, retention, no-shows, conversion, at-risk, membership MRR/churn) on live data, **plus compliance reports** (consent coverage, S4 ledger, lot-recall lookup).
9. **Both apps (Flutter)** — client (book/intake/consent/photos/balances/memberships/rewards) + provider (room-side mapping + photo capture + consult/Rx).
10. **Integrations** — Xero (invoices/payments), M365/Google calendar sync, SMS provider.

**Explicitly NOT in v1 (fast-follows / later — see §9):** dermal filler & other treatment types, laser/device scheduling, **customer-facing online checkout for one-off purchases** (membership card-on-file capture *is* in v1), **AI features (scribe etc.)**, **webhooks / public API**, **advanced loyalty campaigns & referrals**, telehealth video (handled by your existing external app), **Mode B pharmacy dispensing**, **booking deposits/card-on-file**, full retail inventory & POS hardware fleet, marketplace listing, marketing campaign builder, commission/payroll, multi-location switching UI, customer-facing SaaS onboarding/billing, e-prescribing via official ETP networks (structured script records + PDF for now). *(No Mindbody migration — greenfield build.)*

---

## 5. Functional requirements by module

> IDs (`REQ-XXX-n`) trace forward into the PRDs. ★ marks compliance-critical requirements.

### 5.1 Tenancy, identity & roles — `TEN`
- REQ-TEN-1: Every record is scoped to a `tenant_id`; isolation enforced by Postgres **Row-Level-Security**.
- REQ-TEN-2: Auth via managed identity, split by audience — **Staff: Office 365 / Entra ID (workforce) SSO + MFA**, reusing the org accounts most clinics already have (and, for SaaS, each tenant can federate its own Entra tenant); **Clients: Entra External ID** [AWS Cognito] with **social login (Google/Apple)**, **email/username + password**, and **email/SMS OTP**. *(No Supabase.)*
- REQ-TEN-3: Role-based access with the §3 scope matrix; roles & permissions configurable per tenant.
- REQ-TEN-4 ★: Staff profiles store credentials (AHPRA reg #, type, **registration status/expiry, conditions/endorsements**, ≥1yr-non-cosmetic flag, training records, scope); the system **blocks** actions outside scope **or when registration is lapsed/restricted**, and alerts before expiry. (→ C19)
- REQ-TEN-5: **Access model = capabilities × concerns** (ADR-0017). **Capabilities** gate API actions; **concerns** drive role-tailored dashboards (each role mostly sees info concerning it). Ship the built-in roles (incl. **Lead Nurse**, **owner-business**, and **Solo-NP**/**Nurse-led** presets); a **custom-role builder** is a future addition.

### 5.2 Clients & CRM — `CLI`
- REQ-CLI-1: 360° client profile: demographics, contacts, medical history, allergies/contraindications, tags, comms log, consents, photos, memberships, balances, visit history.
- REQ-CLI-2: Search/filter directory; merge duplicates; soft-delete with audit.
- REQ-CLI-3 ★: Capture & store **date of birth**; flag **under-18** to drive cooling-off and advertising rules.
- REQ-CLI-4 ★: **Complaints register** — log complaints/adverse outcomes against client/treatment; surface complaint pathways incl. AHPRA. (→ C24)

### 5.3 Booking & scheduling — `BOOK`
- REQ-BOOK-1: Multi-resource calendar (practitioner + room); service durations w/ buffer/processing time.
- REQ-BOOK-2: Online booking (web + app): service → practitioner → slot; respects practitioner scope (e.g., only RN/NP for injectables).
- REQ-BOOK-3: Configurable cancellation/no-show policy. *(No deposits or card-on-file for bookings in v1; deferred.)*
- REQ-BOOK-4: Reminders (SMS/app/email) with confirm/decline; reschedule/cancel self-service; waitlist.
- REQ-BOOK-5 ★: An injectable booking requires a linked **consult** before treatment can be charted (gate, see RX).
- REQ-BOOK-6: Calendar operations — **reschedule (move)** and **cancel** appointments (with reason + audit); show **client tags** on appointments (VIP/member, **first-time**, at-risk); **per-day & per-treatment-type counts**, utilisation and **quiet-window fill** suggestions; an **"in-room now"** indicator with quick links to the current client's chart/profile.
- REQ-BOOK-7: **Visit lifecycle & hand-offs** (ADR-0024) — the appointment is a **state machine** (Booked → Confirmed → Late/No-show → In treatment → For checkout → Done → Recall) that surfaces the **next action per responsible role**; **late-attendance** and **no-show** flags (a no-show **auto-creates a follow-up call** job, REQ-NOTIF-7); booking captures **new vs returning** (full intake vs quick re-screen), **reason/notes**, and respects **practitioner roster/availability**. *(Small clinics — no formal check-in; late/missed flags instead.)*

### 5.4 Clinical charting — `CLIN`
- REQ-CLIN-1: Treatment note from a configurable template (toxin template for v1); structured + free text; phrases/snippets.
- REQ-CLIN-2 ★: **Injection mapping** — annotate a facial diagram (and/or uploaded photo) with points; each point records **product, units, depth, technique, and batch-lot + expiry**.
- REQ-CLIN-3: **Before/after photos** — capture (provider app camera) or upload; standardized framing guide; side-by-side compare across visits; annotation; **secure central storage (signed URLs; never on personal devices)**, gated by image-use consent (→ C14).
- REQ-CLIN-4 ★: Chart entries are **immutable once finalised**; amendments are appended and audit-logged.
- REQ-CLIN-5 ★: Adverse-event / complication logging linked to the treatment, product and batch-lot, feeding the **TGA DAEN reporting pathway** (→ C12).
- REQ-CLIN-6 *(deferred — far future)*: AI scribe (dictation/ambient → note draft). **No AI features in v1 or near-term.**
- REQ-CLIN-7: **Treatment plans & protocols** — a client can have a **multi-session plan** (progress, next-due) and staff can **apply a protocol template** that schedules the sessions into the recall worklist (e.g. anti-ageing maintenance, needling course).
- REQ-CLIN-8 *(deferred — Phase 2, see ADR-0020, 🔬)*: **advisory auto-detect** of injection points — facial-landmark suggestions the clinician must review/adjust/confirm; never auto-sets units or finalises. **v1 = manual tap-to-add + drag only** (no AI per §2).
- REQ-CLIN-9: **Guided treatment flow** (ADR-0024) — charting opens with a **pre-treatment review** (allergies/contraindications, BDD flag, consent/consult status, **last-treatment summary** + "copy last map"); the consult→**individual-Rx**→administer chain is surfaced **inline** (prescriber writes the script; the administrator confirms against it); charting is **treatment-type-aware** — toxin **injection map + S4 lot** vs a **non-S4 skin note** for dermal (areas/device/settings/consumables, no lot/Rx); **finalise → close-out** (send aftercare, set recall, schedule a 2-day **wellbeing call**, log any **adverse event**) before handing to checkout.

### 5.5 Consent & intake — `CONS`
- REQ-CONS-1 ★: Per-treatment digital consent, **versioned**, e-signed; content meets AHPRA — nature, risks/benefits/alternatives, **practitioner qualifications, costs**, realistic-outcome language (no minimising/overstating), plain language, and complaint mechanisms incl. right to complain to AHPRA despite any NDA. (→ C5/C18)
- REQ-CONS-2 ★: Consent + intake completable pre-visit on the client app; auto-linked to the chart; **block treatment** if required consent/intake incomplete.
- REQ-CONS-3 ★: **BDD / psychological screening** instrument in intake; flag for prescriber review.
- REQ-CONS-4 ★: **Cooling-off** — enforce ≥7 days (under-18) between consent and procedure and **block payment** (except initial consult) until elapsed; **offer/record a second consultation** and a **configurable cooling-off for all patients**. (→ C6)
- REQ-CONS-5 ★: **Separate image-use consent** for any use of photos beyond the clinical record; track scope, **withdrawal at any time** (stop downstream use); never stored on personal devices. (→ C14)

### 5.6 Consult & prescribing — `RX`
- REQ-RX-1 ★: Record a **synchronous consult** (in-person, or telehealth held in an external app) — timestamp, practitioner/prescriber, modality, optional reference/notes; required before any S4 prescription.
- REQ-RX-2 ★: **Individual prescription** per client per consult — product, dose, quantity, prescriber; **no batch/bulk/standing-order scripts** and **no async (text/email/online-only) prescribing**.
- REQ-RX-3 ★: Administration of S4 must reference a valid, unexpired, unconsumed prescription for **that** client.
- REQ-RX-4: Remote-prescriber path: telehealth conducted externally; record that the consult occurred and link the resulting script to the client/treatment.
- REQ-RX-5 ★: Flag **off-label use** on the prescription and ensure the linked consent covers it (the prescriber assumes TGA-equivalent responsibility for off-label safety/efficacy + informed consent). (→ C5)

### 5.7 Medicines governance & S4 inventory — `MED`
- REQ-MED-1 ★: Architecture supports a tenant **mode switch** — **(A) on-site prescriber stock** vs **(B) nurse-led + pharmacy per-patient dispensing**. **v1 implements Mode A only** (no pharmacy partner yet); Mode B deferred.
- REQ-MED-2 ★ (Mode A): S4 **stock ledger** — receipt, custodian, storage location, administration (decrement), wastage, disposal, expiry alerts; custody limited to NP/prescriber.
- REQ-MED-3 ★ (Mode B — *deferred, not in v1*): **Per-patient dispensed-item** records (from pharmacy) tied to the client; RN may only hold/administer dispensed items, never bulk stock.
- REQ-MED-4 ★: Every administration writes batch-lot, quantity, prescriber, administrator, client, datetime — producing an **audit-ready medicine register** and a **lot → clients** recall lookup.
- REQ-MED-5 ★: Track **vial/unit reconciliation** — units drawn per patient vs vial size, plus wastage — so stock, billing units and the medicine register reconcile (supports the "named-patient / no-aliquoting" rules emerging in some states). (→ C8)
- REQ-MED-6 ★: Record each product's **ARTG status, brand, sponsor and lawful supply source**; warn on non-ARTG/unverified-source items. (→ C11)
- REQ-MED-7 ★: Support **storage temperature logging** (toxin 2–8°C) with excursion alerts. (→ C13)
- REQ-MED-8 ★: **Secure storage** — assign stock to a locked cabinet/secure room; restrict + log access. (→ C15)
- REQ-MED-9 ★: **Disposal/destruction & wastage records** — witnessed destruction (incl. partial vials), licensed/RUM disposal pathway, retained certificates. (→ C16)
- REQ-MED-10 ★: **Stocktake & discrepancy** — periodic reconciliation; flag discrepancies; loss/theft reporting workflow. (→ C17)
- REQ-MED-11 ★: **Product catalogue & multi-product stock** (ADR-0021/0014) — products are **typed** (toxin/filler/skin) with their own **unit** (units vs syringes/mL) and **par level**; on-hand/usage/wastage/expiry aggregate **per product+unit** (no single "units on hand"); usage history is per product. A capability-gated **catalogue admin** can **add/remove products** and set the **S4 flag** (the single classification that drives rewards & advertising everywhere).

### 5.8 Payments & POS — `PAY`
- REQ-PAY-1: `PaymentProvider` interface (charge, refund, void, **card-on-file/token, recurring**); **Square adapter** first; **cash** recorded as a tender (no processor).
- REQ-PAY-2: **In-person POS payments in v1** — Square card-present + recorded cash; receipts; partial/split; tips; surcharge config. **Membership autopay is automatic recurring (card-on-file)** — see MEMB. *(Customer-facing online checkout for one-off purchases deferred; no booking deposits.)*
- REQ-PAY-3: Package/series sale & redemption ("visits remaining"); client account balance & credit; AR ageing.
- REQ-PAY-4: Daily closeout/reconciliation (card + cash).
- REQ-PAY-5: **Gift cards** — sell, redeem and track balances (Square Gift Cards or internal); usable at checkout.
- REQ-PAY-6: **Checkout assist** — subtle, **staff-facing** prompts at checkout: a **membership** offer if non-member, a **restock** suggestion from purchase history, and a **client rapport/context** panel; on completion, a **post-checkout rebooking** suggestion based on the treatment interval (toxin ~12 wks) feeding the booking flow/recall. Non-intrusive; never auto-charges.

### 5.9 Memberships, rewards & loyalty — `MEMB`
- REQ-MEMB-1: Membership plans (tiers) with **automatic recurring billing** (monthly/annual); card stored (card-on-file) for autopay, **added online/in-app or in person (not required in person)**; failed-payment dunning & recovery.
- REQ-MEMB-2: Auto-apply member benefits/credits at checkout; expirations.
- REQ-MEMB-3: Membership lifecycle (join/pause/cancel/win-back) feeding the churn/MRR reporting.
- REQ-MEMB-4: **Visit-based rewards** — milestones / every-Nth-visit perks to drive return frequency.
- REQ-MEMB-5: **Membership & frequency perks** — tiered benefits and return-cadence incentives (e.g. discounted/complimentary **non-S4** items — skincare/retail, non-S4 add-ons — or gift-card credit) designed to bring clients back more often.
- REQ-MEMB-6: **Margin-aware reward rules** — configurable value caps, eligible (preferably high-margin/low-cost) items, and **reward-cost vs retention** reporting, so incentives don't erode profit. Reward/incentive *communications* must respect advertising rules — no public S4 price promotion; deliver to consented, logged-in clients (→ C9/C23).
- REQ-MEMB-7 ★: **Rewards on non-S4 items only** — the catalog classifies every service/product as **S4 vs non-S4** (with category); the rewards engine **blocks** earning, redeeming or discounting against **S4** items (botox/filler). This both protects margin and reinforces C9 (no S4 price promotion). (→ C9)
- REQ-MEMB-8: **Loyalty, referrals & gift cards** — non-S4 **points**, a **referral** program (give/get **non-S4** credit), gift-card balances and **failed-payment dunning** with retry. *(Full loyalty **campaigns** & referral automation stay Phase 2 — the prototype shows the concept; v1 ships the core ledgers + dunning.)*
- REQ-MEMB-9: **Pricing & what-if planning** (owner; ADR-0022) — model plan/service price changes and see the projected **MRR/revenue impact** under a churn-sensitivity assumption; a change is a **proposal** until applied through the audited catalogue/membership admin.

### 5.10 Communications, reminders & recall — `NOTIF`
- REQ-NOTIF-1: `Notifier` interface; SMS (AU provider) + email + app push; per-tenant templates.
- REQ-NOTIF-2: Appointment reminders/confirmations; pre-care & **aftercare** sequences (multi-touch, timed per treatment).
- REQ-NOTIF-3: **Recall/recare** at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts.
- REQ-NOTIF-4 ★: **Advertising-compliance linter** on all platform-generated public content (campaigns **and the public booking page's service names/prices**) — blocks direct/indirect S4 references (brands, nicknames, generic "anti-wrinkle"/"dermal filler" terms), price promotions, banned hashtags and promotional S4 imagery; inserts mandatory warnings where permitted. (→ C9)
- REQ-NOTIF-5 ★: **Marketing consent & Spam Act** — opt-in consent to receive commercial electronic messages, sender identification, functional unsubscribe; suppress on withdrawal. (→ C23)
- REQ-NOTIF-6 *(social channels Phase 2 — see ADR-0018/0019, 🔬)*: **Omnichannel conversation inbox** — unified two-way threads across **Instagram, Facebook/Messenger, SMS, email** (WhatsApp candidate), with **categorisation**, **client linking** (capture the handle on the client), **templated/keyword suggested replies** (editable; **no AI** in v1), and the **advertising linter** at send time; honour the **24-h messaging window/tags**, opt-in, message **echoes** and **Handover-Protocol** sync so history stays faithful even when staff reply natively. **v1 = SMS/email + recall** (NOTIF-1..5); **IG/FB/WhatsApp are reactive/service channels — proactive marketing stays on SMS/email.**
- REQ-NOTIF-7: **Unified follow-up / task queue** (ADR-0023) — a single queue of **jobs** (reply, callback, recall, consent-chase, stock, restock, admin) that **merges** today's scattered follow-ups (recall worklist, "needs attention", unanswered comms) so nothing is lost. Staff can **manually flag** any message/client; jobs carry **assignee** (role/person), **due**, **status** (open/snoozed/done) and a **source** (manual/auto/recall/system), with a role-scoped **"my queue"**. Inbound comms **auto-categorise into jobs** by **rules/keyword** (*no AI in v1*; LLM-assisted triage later) so an unanswered message becomes a tracked job.

### 5.11 Reporting & analytics — `RPT`
- REQ-RPT-1: Rebuild the prototyped dashboards on live data: revenue, retention/churn, no-shows, cancellations, conversion funnel, at-risk, big spenders, membership MRR/churn, per-practitioner.
- REQ-RPT-2: Date-range filtering parity with the current tool.
- REQ-RPT-3 ★: Compliance dashboards — consent coverage, consult-before-script adherence, S4 register export, **lot-recall lookup**, cooling-off adherence, **registration-expiry watch, records-retention/destruction due, S4 stock discrepancies, and the breach & complaints registers**.
- REQ-RPT-4: Data-quality/anomaly checks (carry over current logic).
- REQ-RPT-5: **Owner "needs attention" digest** — one exceptions view (failed payments, expiring stock, registration/accreditation currency, open complaints, overdue recalls, unbilled visits) that links into the relevant module.

### 5.12 Integrations — `INT`
- REQ-INT-1: **Xero** — push invoices/payments (+ payouts) on checkout; map services/products to accounts; GST.
- REQ-INT-2: **Calendar sync** — two-way with M365 (Graph) and Google Calendar, behind a `CalendarProvider` adapter.
- REQ-INT-3 *(deferred — much later)*: Webhooks / event bus / public API for third-party integrations.

### 5.13 Apps (Flutter) — `APP`
- REQ-APP-1: **Client app** (Flutter) — book/reschedule, intake/consent, view/upload photos, memberships, **rewards/perks**, balances, reminders, recall.
- REQ-APP-2: **Provider app** (Flutter) — schedule, room-side injection mapping, **camera photo capture**, consult/Rx, finalize chart; resilient to flaky connectivity (offline queue & sync) for the treatment-room reality.
- REQ-APP-3: Both apps share the backend API and auth with web; store-distributed, with code-push for fast iteration where feasible (e.g. Shorebird).

### 5.14 Security, privacy & audit — `SEC`
- REQ-SEC-1 ★: **AU data residency** (Sydney region) for all PII/PHI incl. photos.
- REQ-SEC-2 ★: Encryption in transit + at rest; signed URLs for media; least-privilege access.
- REQ-SEC-3 ★: **Comprehensive audit log** (who viewed/changed what, when) for clinical, medicines and PII access — retained and exportable for QLD Health / AHPRA scrutiny.
- REQ-SEC-4: Backups + restore; **retention policy engine** (adults ≥7 yrs from last contact; minors to age 25; indefinite on complaint/litigation), **destruction register** + certificates. (→ C18)
- REQ-SEC-5 ★: **Patient access & correction** of their own health information (APP 12/13); collection notice + consent at sign-up. (→ C21)
- REQ-SEC-6 ★: **Cross-border disclosure controls** — sub-processors (payments, SMS, accounting) kept AU-resident or assessed/consented (APP 8). (→ C21)
- REQ-SEC-7 ★: **Data-breach handling** — detect/assess eligible breaches, notify OAIC + individuals, maintain a breach register. (→ C22)

### 5.15 Facility, infection control & emergency — `FAC`
- REQ-FAC-1 ★: Record **facility accreditation** (ACSQHC/NSQHS) status & expiry per location. (→ C20)
- REQ-FAC-2 ★: **Infection-control logs** — sterilisation/single-use, sharps & clinical-waste disposal. (→ C20)
- REQ-FAC-3 ★: **Emergency preparedness** — emergency/complication protocol links + **emergency kit** (e.g. hyaluronidase, anaphylaxis) availability/expiry; **continuity-of-care** contact when the treating practitioner/prescriber is unavailable. (→ C20)
> v1: lightweight record-keeping (accreditation ref, kit expiry, simple logs); full workflows later.

---

## 6. Compliance requirements (AU/QLD) — restated as acceptance criteria

These are the differentiator; each must be demonstrably testable. (Detail & sources: research §4.)

- ★ **C1 — Consult-gated scripts:** system prevents recording an S4 prescription without a linked synchronous consult (in-person, or a telehealth consult held in the external app and recorded here) at prescription time. *No async, no batch.* (AHPRA)
- ★ **C2 — Individual scripts only:** one prescription per client per consult; standing orders cannot authorise RN administration of S4 cosmetics. (QLD MPMR)
- ★ **C3 — Assessment authorship:** holistic assessment incl. BDD screen recorded by an **RN or NP** before procedure. (AHPRA)
- ★ **C4 — Credential gating:** RN actions require the ≥1yr-non-cosmetic-experience + training flags; EN region/supervision limits enforceable (config for future EN use). (AHPRA)
- ★ **C5 — Consent content & capture:** versioned, e-signed, **verbal + written** plain-language consent covering nature, **risks/benefits/alternatives, the practitioner's qualifications, and costs**, without minimising complexity or overstating outcomes; includes complaint info (incl. right to complain to AHPRA despite any NDA); treatment blocked without it. (AHPRA)
- ★ **C6 — Cooling-off & no-pressure:** under-18 — mandatory **7-day cooling-off** (payment blocked except the consult) and no advertising to minors; **adults — there is *no* mandatory 7-day cooling-off** (a 2025-rev correction; see §6.1), but the practitioner must give **adequate time to consider** and avoid pressure, and the platform offers a **configurable** cool-off/second-consult for adults as a *clinic policy* setting (not a regulatory mandate). (AHPRA, *Guidelines for registered health practitioners who perform non-surgical cosmetic procedures*, eff. 2 Sept 2025)
- ★ **C7 — Medicines custody:** v1 enforces **Mode A** (on-site prescriber stock ledger; RNs never hold bulk S4). Mode B (pharmacy per-patient) deferred. Per the QLD clarification (§6.1), Mode A requires the custodian to be a **prescriber who physically works at the clinic and holds *exclusive* custody and control** of the stock (a remote prescriber consigning stock to a nurse-led clinic is **non-compliant**); record the **custodian + exclusive-custody attestation** and the appointed **designated medicine store/management contact**. (QLD MPA 2019 / Medicines Regulation 2021)
- ★ **C8 — Traceability & recall:** batch-lot + expiry recorded at every administration; lot→clients lookup for adverse events/recalls. (TGA/clinical)
- ★ **C9 — Advertising guardrails (broad):** all platform-generated public content — campaigns **and the public booking page (service names & price displays)** — must avoid **direct *or indirect*** references to the S4: no brand names, nicknames or blurred logos (Botox/"babytox"), no generic substance/service terms a consumer would read as promoting the medicine ("anti-wrinkle injections", "wrinkle-reducing injections", "dermal fillers"), no price promotions, no banned hashtags (#botox), no promotional before/after or syringe/treatment imagery referencing the S4; insert mandatory health warnings where ads are permitted; applies to historical content too. No influencer testimonials; no under-18 targeting. (TGA + AHPRA)
- ★ **C10 — Residency, audit & retention:** AU-hosted PHI; full audit trail; retention configured to obligations. (Privacy Act / record-keeping)
- ★ **C11 — Approved products & lawful supply (TGA):** every S4 product records its **ARTG registration/approval status**, brand/sponsor, and **lawful supply source** (ordered by an authorised prescriber from a TGA-approved wholesaler); the system flags/limits non-ARTG or unverified-source stock. (Importing/using unapproved or counterfeit injectables is a top TGA enforcement target — penalties to $1.65M/breach for individuals.)
- ★ **C12 — Adverse-event reporting pathway (TGA DAEN):** adverse-event records capture the data a TGA report needs, classify **seriousness**, route to the correct database (**DAEN-medicines** for toxin vs **DAEN-medical devices** for device-class fillers), and support a **prefilled export/submission**. Reporting is *voluntary but strongly encouraged* for injectors in most cosmetic settings, and **mandatory** in defined cases (unapproved goods supplied under authority; serious device events at hospital/day-hospital facilities from 21 Mar 2026) — the system flags those.
- ★ **C13 — Cold-chain & storage (TGA/PI):** Mode-A stock storage supports **temperature logging** (botulinum toxin **2–8°C**) with excursion flags, alongside expiry/disposal records.
- ★ **C14 — Image-use consent (separate):** distinct, documented consent for any use of photos/images beyond the clinical record; images held centrally, **never on personal devices**; **withdrawable at any time** with downstream stop-use. (AHPRA)
- ★ **C15 — Secure S4 storage:** stock kept in a locked cabinet/secure room, access limited to authorised personnel and access events logged; associated records held securely. (state poisons law)
- ★ **C16 — S4 disposal & destruction records:** witnessed destruction/wastage logged (including partial vials/ampoules), disposal via a licensed / Return-Unwanted-Medicines pathway, with retained certificates of destruction. (state poisons law / NSQHS)
- ★ **C17 — Stocktake, discrepancy & loss/theft:** periodic S4 reconciliation; discrepancies flagged; a loss/theft reporting workflow.
- ★ **C18 — Records standard & retention:** detailed consultation, assessment, rationale, risk and consent records; retention **adults ≥7 yrs from last contact; minors until age 25 (or 7 yrs from last entry, whichever is later)**; **indefinite** where a complaint/adverse outcome/litigation exists; Medicare claims ≥2 yrs; plus a **destruction register** (patient, period covered, disposal date) and transfer log. (state law + Privacy Act)
- ★ **C19 — Registration currency & scope:** track AHPRA registration status/expiry, conditions/endorsements and training/experience; **block** clinical actions for lapsed/conditioned registration or work outside scope. (AHPRA)
- ★ **C20 — Facility, infection control & emergency:** record facility accreditation (ACSQHC/NSQHS), infection-control/sterilisation/single-use and sharps & clinical-waste logs; **emergency/complication protocols + kit** (e.g. hyaluronidase, anaphylaxis) with availability/expiry; a **continuity-of-care arrangement** when the treating practitioner/prescriber is unavailable. (AHPRA/ACSQHC) — *lightweight record-keeping in v1.*
- ★ **C21 — Privacy (APPs):** collection notice + consent; purpose limitation; **patient access & correction** (APP 12/13); **cross-border disclosure** controls (APP 8) — sub-processors kept AU-resident or assessed. (Privacy Act)
- ★ **C22 — Notifiable Data Breaches:** detect/assess eligible breaches; notify **OAIC + affected individuals**; maintain a breach register. (NDB scheme)
- ★ **C23 — Marketing consent (Spam Act):** opt-in consent for commercial electronic messages, sender identification and a **functional unsubscribe**; suppress on withdrawal. (Spam Act)
- ★ **C24 — Complaints register & pathways:** record complaints/adverse outcomes and surface complaint mechanisms incl. **AHPRA** (and that an NDA does not remove that right). (AHPRA)

---

## 6.1 QLD / national regulatory re-review — gaps & corrections (2026-06-20)

> A fresh re-read of the live Queensland & national standards (not the earlier captured summary) against
> C1–C24. The framework held up well; the items below are the **deltas** — one new role, four corrections,
> and two scoping reconciliations — each traced to the criterion/REQ it changes. Sources are in
> [market research §4 (Regulatory & compliance) + Sources](01-market-research.md).

**Primary instruments checked:** AHPRA *Guidelines for registered health practitioners who perform
non-surgical cosmetic procedures* and *Guidelines for advertising higher-risk non-surgical cosmetic
procedures* (**both effective 2 Sept 2025**, replacing the NMBA *Nurses and cosmetic medical procedures*
position statement); Medical Board *cosmetic surgery & procedures* guidelines (separate, for **doctors**);
QLD *Medicines and Poisons Act 2019* + *Medicines and Poisons (Medicines) Regulation 2021* and the QLD
Health **cosmetic-injectables fact sheet** (Dec 2024; clarified Apr 2025); TGA advertising guidance
(2024 → June 2025 → Nov 2025 social-media update → **2026–27 Compliance Principles**); TGA device
adverse-event reporting (**ASDER, mandatory 21 Mar 2026**); compounded-GLP-1 prohibition (1 Oct 2024).

### GAP-1 ★ NEW ROLE — Designated RN prescriber (QLD endorsement, from Sept 2025)
QLD now recognises a **third** prescriber path between administer-only RN and NP: an RN with the AHPRA
*endorsement for scheduled medicines — designated registered nurse prescriber* may **prescribe S2–S4
(incl. cosmetic injectables) in partnership with an authorised prescriber** (doctor/NP). Eligibility ≈
general RN registration with no relevant conditions + **5,000 hrs clinical experience in 6 yrs** + approved
education; verified on the AHPRA register.
*Impact:* add to §3 personas + scope presets (done); the credential engine (REQ-TEN-4/7, C4/C19) must
store/verify this endorsement and a **partnered prescriber** before unlocking `prescribe-S4`; the consult/Rx
model (RX, C1–C2) gains this as a compliant prescriber identity; the operating-model switch (REQ-MED-1,
C7) gains a third mode. **Recommend a new ADR** ("designated RN prescriber as a gated capability over the
RN role"). *(This is the single biggest gap — the rest of the doc assumed only RN-administer / NP / remote
telehealth prescribers.)*

### GAP-2 — Correction: **no mandatory adult cooling-off** (fixes C6)
The finalised AHPRA guidelines mandate the **7-day cooling-off for under-18s only**. For adults there is
**no** regulatory 7-day mandate — only an obligation to allow adequate time and avoid pressure. The old C6
phrasing ("some guidance extends the 7 days to adults") was wrong and is corrected; adult cool-off is a
**clinic-policy setting**, not a compliance gate.

### GAP-3 — Sharper QLD custody rule (fixes C7 / REQ-MED-2)
The custodian must be a **prescriber who physically works at the clinic and holds *exclusive* custody &
control** of stock; a prescriber **cannot consign/supply stock** to a clinic where they lack that exclusive
custody — this **breaks the legacy "remote telehealth doctor + nurse-held stock" model** (~600 QLD clinics
affected). RNs/ENs/admin **cannot buy** S4 at all; an RN may only **possess** S4 *to administer it*. Also:
appoint a **designated medicine store/management contact**, and hold an **infection-control management plan**
under the QLD *Public Health Act 2005*. (Wording "exclusive/joint custody" → **exclusive**.)

### GAP-4 — Practitioner thresholds + exclusions made explicit (extends C4 / REQ-TEN-4/7)
Encode precisely: **RN** ≥1 yr FT general/specialist nursing (excluding cosmetic injectables) *before*
entering cosmetics + specialised training + **ongoing cosmetic-specific CPD**; **EN** entry level deemed
inadequate — if practising, ≥1 yr FTE post-registration + ≥1 yr FTE in a related area + training +
**ongoing RN supervision**; **midwives cannot** perform cosmetic procedures; **doctors are governed by the
Medical Board guidelines, not these** (the scope model must distinguish prescriber *type*).

### GAP-5 — Advertising: newer prohibited content & reach (extends C9 / REQ-NOTIF-4)
Add to the linter: **facial-mapping / treatment-animation imagery** is promotional (June 2025);
**disguised "educational" content carrying a call-to-action** is still advertising; the **Nov 2025 TGA
social-media update** targets influencer-style promotion (cosmetic injectables *and* Ozempic); permitted
social ads must be flagged **adult content**; the AHPRA advertising guideline binds **marketing agencies and
influencers**, not just the practitioner. Carve-out: advertising **exclusively to health professionals**
(s42AA) is permitted. Cosmetic injectables remain a **named TGA enforcement priority for 2026–27**.

### RECON-1 — Device adverse-event mandatory reporting (ASDER) scoped out for v1 (clarifies C12)
Mandatory device-AE reporting via **ASDER (from 21 Mar 2026)** applies **only to public/private hospitals
and licensed *day hospitals*** — **not** to a non-surgical injectables clinic. For our target clinic, device
AE reporting (DAEN) stays **voluntary but strongly encouraged**; the mandatory-ASDER flag fires **only** if
the tenant is a licensed day hospital. (Reconciles the prototype's earlier removal of "ASDER mandatory
reporting" with C12 — C12 stays, gated behind a tenant facility-type flag, default off.)

### RECON-2 — NSQHS / cosmetic-surgery facility accreditation **not required** for non-surgical (clarifies C20 / REQ-FAC-1)
The **National Safety & Quality Cosmetic Surgery Standards** and **private-health-facility licensing**
(QLD, since 2018) apply to **cosmetic *surgery*** in licensed facilities — **not** to a non-surgical
injectables clinic. So C20/REQ-FAC-1 should treat ACSQHC/NSQHS accreditation as **optional / conditional**
(only if the clinic also performs licensed surgical procedures). What **is** required for our clinic:
the **infection-control management plan** (QLD *Public Health Act 2005*), emergency kit/continuity-of-care,
and the general clinical-governance/record-keeping already specified.

### WATCH-1 ★ — Single-product telehealth prescribing under national review
The Sept-2025 Health Ministers' Meeting tasked the Commonwealth/TGA to **review single-product telehealth
prescribing** of cosmetic injectables and report back **Dec 2025**, with QLD pushing for nationally
consistent rules. The **remote-telehealth-prescriber path (REQ-RX-4) is a regulatory risk, not a stable
assumption** — keep the prescriber model configurable; a national restriction would elevate the on-site-NP
and designated-RN-prescriber models (GAP-1).

### Confirmed still-current (no change): compounded-GLP-1 prohibition (1 Oct 2024) remains in force →
REQ-MED-12 stands; ARTG/lawful-supply (C11), cold-chain 2–8 °C (C13) and consult-gating/individual-scripts
(C1–C2) all align with the live standards.

---

## 7. Architecture & tech stack

**Stack (lean, cloud-native, AU — no Supabase). Lean toward Azure for M365/Entra fit; AWS equivalents in brackets:**
- **Database:** managed **PostgreSQL** — Azure Database for PostgreSQL Flexible Server [AWS RDS/Aurora PostgreSQL]; **Row-Level-Security** for tenancy (EF Core / Npgsql). *(Azure SQL is an equally-native alternative; both support RLS — pick at Phase 0.)*
- **Identity / Auth:** **Entra External ID** [AWS Cognito] — social login (Google/Apple), email/username + password, email/SMS **OTP**, MFA.
- **Media storage:** **Azure Blob** [S3] with signed URLs.
- **API / compute:** **.NET (ASP.NET Core) Web API** on **Azure App Service / Container Apps** [AWS App Runner / ECS]; scheduled/background jobs via **Functions** [Lambda].
- **Web:** **Angular** SPA (front-desk/admin + client web booking) on **Azure Static Web Apps** [S3 + CloudFront].
- **Apps:** **Flutter** (Dart) — client + provider apps, sharing the backend API; native camera for photos.
- **Secrets/keys:** **Key Vault** [Secrets Manager].
- **Domain services (.NET interfaces, swappable & cheap):** `IPaymentProvider` (Square card + cash), `INotifier` (AU SMS + email), `ICalendarProvider` (Graph + Google), `IAccountingExport` (Xero).
- **Compliance/data integrity:** Postgres constraints + RLS + append-only audit tables; immutable finalized chart entries; signed-URL media.

**Multi-tenancy:** single Postgres database, `tenant_id` on every table, RLS policies per role; "single-clinic-feeling" UX with tenant config — flip to multi-tenant SaaS later without schema rework.

**Core data model (sketch):** `Tenant` › `Location`, `StaffProfile`(role, credentials, scope), `Client`(dob, flags), `Service`/`TreatmentType`(+**schedule: S4|non-S4**, category), `Appointment`, `Consult`, `Consent`(version), `Prescription`(+off-label flag), `MedicineMode`, `Product`(type: **medicine|device**, ARTG#, sponsor, supply-source), `StockItem`/`StockLedger`/`DispensedItem`(lot, expiry, storage-temp), `ChartEntry`›`InjectionPoint`, `Photo`, `AdverseEvent`, `Invoice`/`Payment`(card|cash), `GiftCard`, `MembershipPlan`/`Membership`, `Package`/`Series`, `RewardRule`/`RewardLedger`, `Notification`, `ImageConsent`, `Complaint`, `MarketingConsent`, `Stocktake`/`StockDestruction`, `DataBreach`, `FacilityAccreditation`, `AuditEvent`.

---

## 8. Non-functional requirements
- **Cost:** ~$0 fixed until real volume; prefer free/cheap managed tiers; no per-seat SaaS where avoidable.
- **Performance:** calendar & charting feel instant on clinic wifi/4G; provider app usable on flaky connectivity (offline queue + sync).
- **Reliability:** photos/notes never silently lost (a known Aesthetic Record failure mode) — explicit save-state + retry.
- **Accessibility & polish:** modern, fast UI (directly addresses the "clunky Mindbody" pain).
- **Maintainability:** three focused layers — **Dart/Flutter** apps, **Angular/TypeScript** web, and a single **.NET/C#** API — over one shared backend; keep services minimal to suit a lean team.

---

## 9. Phasing / roadmap (no fixed date → quality-first)

- **Phase 0 — Foundations:** tenancy/auth (social/password/OTP)/roles, data model, design system.
- **Phase 1 — v1 toxin slice (this spec §4):** booking → intake/consent → consult/Rx → mapping/photos → S4 governance → in-person payment (Square + cash) + gift cards → memberships + rewards → recall → core + compliance reporting → both Flutter apps → Xero/calendar/SMS.
- **Phase 2 — Fast-follows:** dermal filler + more treatment types, **customer-facing online payments/checkout**, **Mode B pharmacy dispensing**, **booking deposits/card-on-file**, **advanced loyalty campaigns & referrals**, retail inventory & POS hardware, marketing/campaigns, commission/payroll.
- **Phase 3 — Scale:** multi-location UX; **webhooks/events & public API**; then SaaS commercialization (self-serve onboarding, subscription billing, white-label); **AI features (far future)**.

---

## 10. Open items / assumptions to confirm
1. **Product name** — none chosen; generic "Aesthetic Clinic Platform" used as working title.
2. **AWS vs Azure** — pick the cheaper native landing zone at Phase 0; M365/Entra presence leans **Azure** (Entra External ID + Azure Database for PostgreSQL + Blob + Container Apps/Functions + Static Web Apps).
3. **Membership plans & reward rules** — define exact tiers/prices/benefits **and reward rules** (visit milestones, perks, margin caps); no data import needed.
4. **e-Prescribing** — v1 records a structured script + PDF; official ETP-network integration deferred — confirm acceptable.
5. ★ **Remote-prescriber + on-site-stock custody (QLD nuance)** — with telehealth external and **Mode A** only in v1, note that QLD permits on-site S4 stock only under an on-site doctor/NP's custody. The platform records consult, prescriber and custodian faithfully; the lawful custody arrangement itself is an operational/legal decision for the clinic.
6. **Public booking-page naming (TGA advertising)** — because the public booking page is itself "advertising", injectable services likely must be listed **generically** (e.g. "Cosmetic consultation") with **prices withheld publicly**. Default assumption unless you say otherwise.
7. **Database** — Postgres (cheap, RLS) vs Azure SQL (native to .NET, RLS) — pick at Phase 0; both meet tenancy/residency needs.

_Resolved this round (2026-06-18):_ **web = Angular + .NET API** · apps in **Flutter** (not native) · **autopay = automatic recurring** (card-on-file, not in person) · **rewards on non-S4 items only** (catalog classifies S4 vs non-S4) · **greenfield** (no Mindbody/data import) · **no AI** (far future) · **in-person POS payments first** (Square + cash) + **gift cards** · **webhooks/public API much later** · **Azure/AWS native, no Supabase** · auth = **social + password + OTP**. _(Earlier: telehealth external · Mode A only · no booking deposits · no product name.)_

---

## 11. Proposed PRD breakdown (the next step)

Each becomes a focused PRD (problem, user stories, flows, data, acceptance criteria incl. the relevant `C#`/`REQ` IDs, out-of-scope). Suggested order:

1. **PRD-01 Foundations & tenancy** (TEN incl. social/password/OTP auth, SEC, data model)
2. **PRD-02 Booking & scheduling** (BOOK + client/CRM basics CLI)
3. **PRD-03 Intake, consent & compliance gating** (CONS, C1–C6)
4. **PRD-04 Consult, prescribing & S4 medicines governance** (RX, MED, C1–C2, C7–C8) — *the moat*
5. **PRD-05 Clinical charting: injection mapping & before/after** (CLIN)
6. **PRD-06 Payments (in-person POS: Square + cash + gift cards), automatic membership autopay, packages & non-S4 rewards** (PAY, MEMB)
7. **PRD-07 Comms, reminders & recall** (NOTIF, C9)
8. **PRD-08 Reporting & compliance dashboards** (RPT, C10)
9. **PRD-09 Apps (Flutter): client & provider** (APP)
10. **PRD-10 Integrations: Xero & calendar** (INT)
11. **PRD-11 Facility, infection-control, emergency & complaints** (FAC, C20, C24) — lower priority; record-keeping support

> The expanded privacy/records/registration criteria (C18–C23) thread mainly through **PRD-01** (SEC/TEN); S4 storage/disposal (C15–C17) through **PRD-04**; consent/image/cooling-off (C5/C6/C14) through **PRD-03**.

> Recommend writing **PRD-01 → PRD-04** first (they unblock everything and contain the compliance moat), then the rest.

---

## 12. Option A prototype alignment & feasibility register

> Added rev 3 (2026-06-19) after building the **Option A — "Clinical Calm"** clickable prototype
> (`prototype.html`). Reconciles this spec with what the prototype demonstrates and lists the items that
> **need feasibility research** before commit. Legend: ✅ aligned/spec'd · ➕ new (this rev) · 🔬 needs research · ⏭ Phase 2+ (prototype shows the concept).

### 12.1 Feature → requirement / ADR map
| Option A prototype feature | Maps to | Status |
|---|---|---|
| Persona switcher (NP, Lead RN, RN, dermal, reception, owner-business + Solo/Nurse-led); role-tailored dashboards | REQ-TEN-3/5, ADR-0017 | ✅ ➕ |
| Booking wizard, scope-limited to RN/NP for injectables | REQ-BOOK-2/5 | ✅ |
| Week schedule: move/cancel, VIP/first-time tags, per-day & per-type counts, utilisation/quiet-window fill, "in-room now" links | REQ-BOOK-6 ➕ | ✅ ➕ |
| Client 360 + treatment-plan tab with protocols | REQ-CLI-1, REQ-CLIN-7 ➕ | ✅ ➕ |
| Charting: **product & batch (lot) selected first**, injection map (tap-to-add + drag), before/after compare, finalise→deduct selected lot | REQ-CLIN-2/3/4, REQ-MED-4 | ✅ |
| Charting: "auto-detect" injection points | REQ-CLIN-8 ➕, ADR-0020 | 🔬 ⏭ |
| Stock: multi-product/multi-unit, per-type usage history, par/expiry, vial reconciliation, receive | REQ-MED-11 ➕, ADR-0021 | ✅ ➕ |
| Stock: product-catalogue admin (add/remove, set S4 flag, par) | REQ-MED-11 ➕, ADR-0014/0021 | ✅ ➕ |
| Forms/consent: pre-visit intake wizard (history→BDD→consent→image-use), under-18 cooling-off | REQ-CONS-1..5 | ✅ |
| Checkout: in-person POS, member reward (non-S4), upsell cues + rapport, post-pay rebooking | REQ-PAY-6 ➕, MEMB | ✅ ➕ |
| Memberships/packages/loyalty/referrals/gift cards (+ dunning retry) | REQ-MEMB-8 ➕ | ✅ ➕ (full loyalty/referrals ⏭) |
| Pricing & what-if simulator (owner) | REQ-MEMB-9 ➕, ADR-0022 | ✅ ➕ |
| Marketing: omnichannel inbox (IG/FB/SMS/email), categorise, client-link, suggested replies, advertising linter | REQ-NOTIF-6 ➕, ADR-0018/0019 | 🔬 ⏭ (SMS/email in v1) |
| Follow-ups: unified job queue (merges recall/attention/comms), manual flag from inbox, auto-detect/categorise comms into jobs | REQ-NOTIF-7 ➕, ADR-0023 | ✅ ➕ |
| Visit lifecycle: status state-machine, late/no-show flags (→ call job), role hand-offs, finalise close-out | REQ-BOOK-7 ➕, REQ-CLIN-9 ➕, ADR-0024 | ✅ ➕ |
| Guided charting: pre-treatment review, inline consult/Rx, treatment-type-aware (toxin map vs skin note) | REQ-CLIN-9 ➕, RX-1..3 | ✅ ➕ |
| Booking: new-vs-returning, reason/notes, roster hint | REQ-BOOK-7 ➕ | ✅ ➕ |
| Owner "needs attention" exceptions digest | REQ-RPT-5 ➕ | ✅ ➕ |
| Reports dashboard (revenue, mix, top treatments, new vs returning, MRR) | REQ-RPT-1 | ✅ |
| Responsive back-office (phone/tablet) + client-portal screens | REQ-APP-1/2 (UX validated) | ✅ |

### 12.2 Feasibility / research register
| # | Item | Question | Disposition |
|---|------|----------|-------------|
| **F1** | **Meta (IG/FB) messaging** | Receive/send DMs and keep faithful history incl. native-sent replies? | **Feasible for *service* conversations** via webhooks + Send API + **echoes** + Conversations-API reconcile + Handover Protocol — **but the 24-h window, App Review/Business Verification and no-cold-DM mean *marketing DMs are out*** → proactive marketing via **SMS/email/WhatsApp templates**. Validate scopes vs current Meta docs. (ADR-0018) ⏭ Phase 2 |
| **F2** | **Injection-point auto-detect** | Reliable facial-landmark placement, on-device, without regulatory exposure? | **Advisory + human-confirmed** only; on-device preferred; keep out of SaMD classification. Conflicts with "no AI v1" → **Phase 2**; v1 = manual mapping. (ADR-0020) 🔬 |
| **F3** | **Square AU card-on-file recurring** | Does Square AU support tokenised automatic membership autopay + dunning? | De-risk spike; confirm AU capability or fall back to another `IPaymentProvider`. (ADR-0007) 🔬 |
| **F4** | **Suggested replies** | Keyword/template vs LLM? | **v1 = templated/keyword** (no AI per §2); LLM-assisted drafting Phase 2. ✅/⏭ |
| **F5** | **WhatsApp Business** | Add as a service + templated-marketing channel? | Assess Cloud API, opt-in/template rules; strong AU recall fit. 🔬 ⏭ |
| **F6** | **Pricing what-if model** | Is the impact projection meaningful? | Needs real COGS/margin + a defensible churn/elasticity assumption; ship as a **planning estimate**, apply via audited admin. (ADR-0022) 🔬 |
| **F7** | **Conversation↔client identity resolution** | Auto-match handles to clients safely? | Auto-match phone/email; manual link/merge for handles; treat the handle as personal data. (ADR-0019) ✅ |
| **F8** | **Comms auto-categorisation → jobs** | Rules/keyword vs ML triage? | **v1 = rules/keyword** (reuse the inbox categoriser; no AI); LLM-assisted triage later. Jobs are advisory + human-actioned, so accuracy is UX not safety. (ADR-0023) ✅/⏭ |

> **Net:** v1 stays as specified (manual charting; SMS/email comms + recall). The prototype's **social inbox,
> auto-detect, full loyalty/referrals and any LLM assistance are Phase 2+** pending F1/F2/F4/F5. Everything
> else the prototype shows is already spec'd or added as a `REQ`/`ADR` this rev.

### 12.3 Gap-area build (rev 4, 2026-06-20)

> Six research/design passes extended the prototype with POC flows for the areas it didn't yet cover —
> **treatments & clinical depth, front desk & operations, money & retail, staff & HR, compliance & governance, growth & integrations** (client app excluded). New REQ lines are grouped by module; ADRs are the
> reconciled **ADR-0025…0036**. Most are ⏭ Phase 2 with the prototype showing the concept now.
>
> **Scope adjustments (rev 4.1, 2026-06-20):** (1) **Finances move to Xero & integrations** — the app keeps only **pricing / what-if + high-level reporting**; in-app commission pay-run, supplier POs/AP, refund/dispute management and BAS/GST are **dropped** (ADR-0027 revised; REQ-RPT-6 narrowed; REQ-MED-14, REQ-PAY-7 reclassified external). (2) **Newsletter builder & social scheduler removed** — email campaigns & social posting live in the clinic's existing tools (Mailchimp, Meta Business Suite); the advertising linter now covers **review replies + the public booking page** (ADR-0034 revised; REQ-NOTIF-10/11 withdrawn). (3) **Reviews** gain **acknowledge / flag / auto-detect follow-up** for negative reviews & complaints (ADR-0032 extended; REQ-NOTIF-8 strengthened).

**New / extended requirements**

- **Clinical — `CLIN`:** REQ-CLIN-10 ★⏭ **modality-aware charting** (toxin · filler · skin · energy-device · weight-loss; each drives capture surface, S4|non-S4 · medicine|device class, unit and DAEN routing; filler = multi-area/multi-syringe/per-area lot + **VO/blindness consent gate**) · REQ-CLIN-11 ★⏭ **energy-device settings/fluence logbook** + skin-typing + patch-test + safety checks, **blocked without a state laser licence** · REQ-CLIN-12 🔬⏭ **standardised photography** (fixed poses + **ghost-overlay**) · REQ-CLIN-13 ⏭ **outcome & revision tracking** (touch-up/satisfaction/complication per type & practitioner). (→ C5/C8/C12/C14/C20)
- **Consult/medicines — `RX`/`MED`:** REQ-RX-6 ★⏭ **weight-loss GLP-1 programs** as titration protocols · REQ-MED-12 ★⏠ **compounded-GLP-1 block & ARTG-brand enforcement** (prohibited since 1 Oct 2024) · REQ-MED-13 ⏭ **device & energy-equipment register** (class, ARTG, service/calibration) · REQ-MED-14 ★ **supplier purchase orders & receiving** (reorder-to-PO from below-par; **S4 POs need a prescriber signer** + TGA-approved wholesaler) · REQ-MED-15 **retail (non-S4) inventory & POS** (barcode, cost, margin, supplier, par). (→ C8/C11)
- **Facility — `FAC`:** REQ-FAC-4 ★ **complication-response workflow** (VO/anaphylaxis protocol → log hyaluronidase/adrenaline vs kit + client + lot → routed AE record → follow-up/mandatory-report jobs) · REQ-FAC-5 ★ **twice-daily cold-chain log** ("Strive for 5") with a **breach pathway** (quarantine lot · report) · REQ-FAC-6 ★ **sterilisation & equipment maintenance register** (autoclave validation + spore testing, AS 5369:2023; laser service/calibration) · REQ-FAC-7 **daily open/close checklist** · REQ-FAC-8 ★ **clinical & sharps waste manifests** (NSW CA+TC / QLD WTC) · REQ-FAC-9 ★ **policies & procedures register with staff read-&-sign-off** · REQ-FAC-10 ★ **incident & mandatory-reporting case management**. (→ C13/C16/C18/C20/C24)
- **Booking — `BOOK`:** REQ-BOOK-8 ⏭ **walk-ins & same-day add-ons** (gate-respecting) · REQ-BOOK-9 ⏭ **waitlist auto-fill on cancel/no-show** (scope-matched) · REQ-BOOK-10 ⏭ **room/chair/device resources** (conflict-flag + utilisation) · REQ-BOOK-3 *(amended)* **opt-in, ACL-fair booking deposit / card-on-file hold**, suppressed during cooling-off (C6). (→ ADR-0026)
- **Payments — `PAY`:** REQ-PAY-7 **refunds, credit notes & disputes** (restock non-S4 only; dispute → Job) · REQ-PAY-8 ⏭ **BNPL tenders** (Afterpay/Zip) · REQ-PAY-9 **tips** (direct vs employer-pooled flag) · REQ-PAY-10 ★ **per-line GST coding** (services + retail taxable). (→ ADR-0007/0027)
- **Reporting — `RPT`:** REQ-RPT-6 **money read models** (commission/pay-run with engagement-risk flag, retail margin, refunds/disputes, **BAS/GST summary** G1/1A/1B) — attribution & export, **not a payroll/tax engine** · REQ-RPT-7 ★ **inspection-readiness pack** (one-click evidence bundle). (→ ADR-0027, C10/C18/C20)
- **Tenancy/Team — `TEN`:** REQ-TEN-6 **staff engagement type** (employee/contractor) + commission split → compliance banner · REQ-TEN-7 ★ **credential + CPD + cosmetic-cover PII** records driving a `canInject` gate · REQ-TEN-8 🔬 **AHPRA auto-verification (PIE)** with manual fallback · REQ-TEN-9 **roster, shifts & leave** driving booking availability. (→ ADR-0028/0029, C4/C19)
- **Security/privacy — `SEC`:** REQ-SEC-8 ★ **DSAR workflow (APP 12/13)** with a ≤30-day clock · REQ-SEC-9 ★ **breach assessment & drill** (NDB, OAIC). (→ C21/C22)
- **Comms/growth — `NOTIF`:** REQ-NOTIF-8 ★ **reviews/reputation** (request-all, no gating; reply; **block S4 repost**) · REQ-NOTIF-9 ★ **lead/prospect CRM** over the inbox · REQ-NOTIF-10 **email/newsletter builder** (per-block linter) · REQ-NOTIF-11 **social scheduler** (linter + 18+) · REQ-NOTIF-12 **public booking widget + SEO** (generic names, S4 price withheld) · REQ-MEMB-10 **referral/affiliate depth** (non-S4 credit only). (→ ADR-0032/0033/0034, C9/C23)
- **Integrations — `INT`:** REQ-INT-2a 🔬⏭ **two-way calendar sync** · REQ-INT-4 ⏭ **online checkout & deposits** (S4 never priced online) · REQ-INT-5 🔬⏭ **e-prescribing (eRx/ETP)** · REQ-INT-6 **Medicare/HICAPS** non-applicable to cosmetic · REQ-INT-7 ⏭ **webhooks/public API** (Phase 3). (→ ADR-0035/0036)
- **Compliance acceptance — extend `C12`:** adverse-event routing is **modality-derived** (toxin & filler-as-medicine → DAEN-medicines; device-class filler/PDO/RF → DAEN-devices); flag mandatory reporting (ASDER, day-hospital facilities, from 21 Mar 2026).

**12.1 map additions**

| Option A prototype feature | Maps to | Status |
|---|---|---|
| **Clinical** area: treatment-menu modality model; complication-response modal (VO/anaphylaxis → AE + job); photography/ghost-overlay; outcomes | REQ-CLIN-10..13 ➕, REQ-FAC-4 ➕, ADR-0025 | ✅ ➕ (⏭ deep charting) |
| **Operations** area: twice-daily **fridge log + breach → quarantine + job**; open/close checklist; rooms/devices + utilisation; equipment register; call log + walk-in/waitlist | REQ-FAC-5/6/7 ➕, REQ-BOOK-8/9/10 ➕, REQ-MED-13 ➕, REQ-NOTIF-8(phone) ➕, ADR-0026 | ✅ ➕ (hard-conflict ⏭) |
| **Finance** area *(rev 4.1)*: light **pricing + high-level reporting** hub; books deferred to **Xero** (in-app commission/PO/AP/disputes/BAS dropped) | REQ-RPT-6 (narrowed), ADR-0022/0027 (revised) | ✅ |
| **Team** area: roster & leave; people & credentials; **compliance board** (`canInject` gate, PII-excludes-cosmetic block) | REQ-TEN-6..9 ➕, ADR-0028/0029 | ✅ ➕ (PIE auto-verify 🔬) |
| **Governance** area: overview digest; **AE/DAEN routing + submit**; **recall execution + ack tracking**; policy sign-off; waste manifests + IPC; DSAR + breach drill; **audit pack** | REQ-RPT-7 ➕, REQ-FAC-8/9/10 ➕, REQ-SEC-8/9 ➕, REQ-MED-12 ➕, ADR-0030/0031, C12 | ✅ ➕ (electronic submit 🔬) |
| **Growth** area *(rev 4.1)*: leads CRM; reviews with **acknowledge / flag / auto-detect follow-up** + S4-repost block — newsletter & social **removed** (handled in Mailchimp/Meta) | REQ-NOTIF-8/9 ➕, REQ-MEMB-10 ➕, ADR-0032/0033/0034 (revised) | ✅ ➕ |
| **Settings → Integrations** + public-booking-page preview (generic names, S4 price withheld) | REQ-INT-2a/4/5/6/7 ➕, REQ-NOTIF-12 ➕, ADR-0035/0036 | ✅ ➕ (mostly concept ⏭) |

**12.2 register additions**

| # | Item | Question | Disposition |
|---|------|----------|-------------|
| **F9**  | **Filler/device DAEN routing & mandatory reporting** | Split medicine vs device AE routing; detect day-hospital obligation (ASDER, 21 Mar 2026)? | Catalogue `regClass`/`daenRoute` drives routing; tenant facility-type flag drives voluntary vs mandatory; prefill export only. (ADR-0025/0031) ✅/⏭ |
| **F10** | **State laser/IPL licensing gate** | Model a per-state/class credential gate without building each state's licence workflow? | `laserLicence` credential flag (state + class) gates booking/charting; only QLD/WA/TAS regulate (IPL only TAS); soft-warn elsewhere. (ADR-0025) 🔬 ⏭ |
| **F11** | **Compounded-GLP-1 enforcement** | Reliably block compounded/non-ARTG GLP-1 at catalogue/chart? | `compounded`/`artg` flags + hard block (prohibited 1 Oct 2024); shortage/brand-substitution tracking. ✅ ⏭ |
| **F12** | **Standardised photo / ghost-overlay** | Ghost-overlay alignment now; 3D later? | CSS-opacity overlay in v1-style; VECTRA/LifeViz note-as-future; rides ADR-0009 media + C14. 🔬 ⏭ |
| **F13** | **AHPRA PIE auto-verification** | Programmatic register lookup for credentialing? | Approval-gated paid SOAP service; **manual-verify fallback is first-class**; POC simulates. (ADR-0028) 🔬 ⏭ |
| **F14** | **Deposit ⇄ cooling-off** | Can an opt-in deposit coexist with under-18/elective cooling-off? | **No** — deposit suppressed whenever cooling-off applies; only the consult fee is collectable (C6). Encode as an invariant, not config. (ADR-0026) ✅ |
| **F15** | **Reg-system submission APIs (TGA/EPA)** | Electronic submit to AEMS/ASDER or state EPA waste systems, or portals only? | v1 = prefill + portal hand-off + recorded manifest/reference; assess APIs + the day-hospital boundary. (ADR-0031) 🔬 ⏭ |
| **F16** | **Two-way calendar sync** | Bidirectional dedupe across MS Graph + Google without double-booking? | External busy→availability block; clinic appt→external event w/ stable correlation id; platform = source of truth. (ADR-0036) 🔬 ⏭ |
| **F17** | **e-Prescribing (eRx/ETP)** | Can a cosmetic prescriber issue conformant electronic **private** S4 scripts? | Behind `IPrescribingProvider`; needs HPI-I, exchange conformance, token/ASL; bind to consult (C1) + S4 register. (ADR-0035) 🔬 ⏭ |
| **F18** | **Commission output mistaken for tax-ready** | Will clinics treat the pay-run as payroll? | Persistent non-advice banner + engagement-risk flag; ADR-0027 states attribution & export, **not** a tax engine. ✅ |
