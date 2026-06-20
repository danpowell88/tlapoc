# Mindbody Replacement — Market Research & Feature Landscape

> **Goal:** Plan a purpose-built platform for aesthetic injectables & cosmetic clinics
> to replace Mindbody — covering front office, back office, client booking/management,
> clinical records, payments, and AU/QLD regulatory compliance.
>
> **Context:** The Lounge Aesthetics currently runs on **Mindbody** (confirmed by the
> report exports this repo ingests — Big Spender, Autopay, Contract Sales,
> ScheduleAtAGlance, Pricing Option Expirations, Patients-Per-Instructor). A local
> analytics layer already sits on top of those exports. This document is step 1 of:
> **research → feature list → clarifying questions → requirements → PRDs.**
>
> _Compiled 2026-06-18. Pricing is USD unless noted and indicative only._

---

## 1. The competitive landscape at a glance

The market splits into three camps. Where a new build wins is the **overlap of three things
no incumbent does well at once: a polished modern UX, true aesthetic-injectables clinical
depth, and Australian (TGA / S4 / AHPRA) compliance.**

| Camp | Platforms | What they're good at | Where they fall short for AU injectables |
|------|-----------|----------------------|-------------------------------------------|
| **Horizontal booking/POS** (built for salons/fitness/spas) | Mindbody, Fresha, Vagaro, Boulevard, Mangomint, Timely, Kitomba | Scheduling, POS, memberships, retail, marketing, marketplace reach | Weak/no clinical EMR, no injectable charting, no S4 custody chain, US/HIPAA framing |
| **Aesthetic / medical EMR specialists** | Aesthetic Record, Pabau, AestheticsPro, Nextech, Symplast, Moxie | Injectable charting, before/after photos, consent, e-prescribe, lot/batch tracking | US-centric (HIPAA not Privacy Act), often dated UX or enterprise-heavy, no AU regulatory model |
| **AU health / allied-health PM** | Cliniko, Power Diary, Halaxy, Fresh Clinics | AU data residency, Medicare/health-fund claiming, AU-made | Light on aesthetic-specific tooling (no injection plotting/consent workflows) except Fresh Clinics |

**The gap = the opportunity.** No single product today combines (a) Mangomint/Boulevard-grade
modern UX, (b) Aesthetic Record/Pabau-grade injectable clinical depth, and (c) native
**Australian S4 + AHPRA 2025** compliance. That's the wedge.

---

## 2. Deep dives — the platforms

### Horizontal / booking-first

**1. Mindbody** *(the incumbent we're replacing)*
- **Positioning:** All-in-one for wellness/fitness/spa; huge legacy install base; consumer marketplace (3M+ shoppers).
- **Strengths:** Scheduling, integrated payments (front desk, online, mobile, table-side), memberships & packages, branded apps, Messenger[ai] (24/7 AI front-desk that texts back missed calls, books, captures cards), broad reporting, retail/inventory, payroll.
- **Weaknesses for aesthetics (2026 consensus):** Roots in fitness/yoga show — scheduling logic, pricing and automation reflect that. **No native EMR / SOAP / injectable charting / before-after photo system**, and no integration with the aesthetic EMRs (AR, PatientNow, Nextech) — staff re-key between systems. Pricing has climbed; UI feels dated; steep learning curve; follow-up automation limited to 1–2 generic touchpoints. Reviewers say "no longer the first choice for a new medspa."
- **Why it matters:** It defines the data model the clinic already lives in (the export taxonomy in `site/data/`), and the migration source.

**2. Boulevard** — *premium client-experience platform*
- **Strengths:** "Precision Scheduling" (predictive calendar fill), elegant Front Desk view, integrated EMV POS (Boulevard Duo), card-on-file for no-show/late fees, **HIPAA-compliant client profiles with charting, photo markup for injection sites, before/after compare, and ePrescribe**, AI marketing (Billie assistant), multi-location + Shopify inventory.
- **Weaknesses:** Premium price (Essentials $176 → Aesthetics Bundle $421/mo), limited mobile app (no functional phone POS per one review), smaller integration ecosystem, learning curve on advanced features.
- **Read:** The closest "modern UX + emerging clinical" blend in the US market. Good north-star for client experience.

**3. Mangomint** — *sleekest modern UX*
- **Strengths:** Best-rated UX & satisfaction; smart automations; Express Booking™ (digital link to self-complete & confirm); **Mangomint Connect** (calls + SMS + web chat in one timeline, call transcripts, one synced number); memberships with automated renewals; real-time inventory; Campaigns & Flows marketing; QuickBooks payroll sync.
- **Weaknesses:** Clinical depth is an add-on — **Forms & Charting is +$50/mo**, and it lacks robust side-by-side before/after photo analysis. Broad (salons, med spas, tattoo) rather than aesthetics-pure.
- **Pricing:** $165 / $245 / $375 per month.
- **Read:** Best reference for *interaction design, automation and unified comms*.

**4. Fresha** — *marketplace + free-to-start*
- **Strengths:** Strong scheduling/POS/inventory/reporting; **consumer marketplace** for discovery; book via Instagram/Facebook/Google; card-on-file, deposits, cancellation policies; low/zero subscription (takes payment & new-client fees).
- **Weaknesses:** **No clinical charting** (client records + consultation/patch-test forms only); generic, non-brandable booking page; salon-grade not medical.
- **Read:** Benchmark for *frictionless online booking & new-client acquisition*, not clinical.

**5. Zenoti** — *enterprise all-in-one*
- **Strengths:** Complete operating platform; **HIPAA charting, before/after with comparison overlays, digital intake/consent, e-prescribe, injectable & controlled-substance tracking, treatment-protocol management**; memberships (recurring billing, series, auto-benefits at checkout, churn-risk AI); centralized multi-location inventory (consumables + retail, reorder rules, supplier sync); enterprise reporting + benchmarking vs 30,000+ businesses.
- **Weaknesses:** Custom/opaque pricing, enterprise cost & complexity, steep learning curve; inventory workflows criticized; overkill for single-site.
- **Read:** Best reference for *breadth, memberships, multi-location inventory & controlled-substance tracking* — but heavy.

**6. Timely / 7. Kitomba** — *ANZ salon/spa favourites*
- **Strengths:** Loved in AU/NZ; scheduling, client mgmt, inventory, loyalty, marketing automation, AU GST/financials; Kitomba strong on stock control for retail + treatment supplies.
- **Weaknesses:** Salon-focused, **not medical** — need bolt-on processes for clinical documentation and TGA-compliant injectable tracking.
- **Read:** Proof that ANZ clinics tolerate salon tools — but they leave the compliance gap we'd fill.

### Aesthetic / medical EMR specialists

**8. Aesthetic Record (AR)** — *the photo-first injectable EMR benchmark*
- **Strengths:** Industry-leading **before/after photo documentation** (side-by-side, annotation, patient-phone capture); **chart directly on images — injection points & dosages**, facial mapping, full draw tools; **product traceability — injected product name, expiry, batch ID, lot number, searchable**; **ChartSmart AI / AI Scribe** (dictation/ambient → structured notes, ~80% less charting time); iOS provider app for room-side documentation; consent/questionnaire pre-checks auto-linked to chart; payments & history synced per chart.
- **Weaknesses:** App-stability complaints (lost photos/notes, forced re-login); **charting only in the app, not web**; US/HIPAA-centric.
- **Read:** The clinical gold standard to match on *injectable charting + photos + lot tracking*.

**9. Pabau** — *all-in-one medical aesthetics (UK/EU, used in AU)*
- **Strengths:** Built-in EMR (health info, photos, consent, labs); **form builder + 500+ templates**; **Pabau Scribe** (AI consult transcription → structured notes, real-time safety checks against record); calendar (day/week/month/room views); SMS/email reminders; **Pabau Pay** + terminals, **Klarna BNPL**; real-time inventory with usage-per-treatment + reorder alerts; recalls, segmentation, review requests, gift cards, packages, memberships, loyalty; telehealth; reporting. GDPR + HIPAA, encryption, access controls, audit logs.
- **Weaknesses:** Steep learning curve (feature breadth), occasional performance issues, reporting customization limited. From ~£49/mo solo, priced by team size.
- **Read:** Closest *feature-complete blueprint* for an injectables clinic; 4.6/5 over 600 reviews.

**10. AestheticsPro** — *affordable aesthetics all-in-one (US)*
- **Strengths:** HIPAA cloud EMR + CRM + scheduling + marketing + payments; **AP Focus** photo solution (alignment guides, ghosting, markup); transparent pricing ($150 Solo → $275 Enterprise Plus).
- **Weaknesses:** Fewer third-party integrations / limited API. 4.38/5 over ~398 reviews.

**11. Nextech** — *enterprise EHR (derm/plastics/ophthalmology)*
- **Strengths:** Deep clinical workflows, multi-specialty, advanced photo (markup/annotation/layers), **AI Scribe**, enterprise reporting, broad integration marketplace, ePrescribe/labs.
- **Weaknesses:** Expensive, "charged for everything," confusing for non-traditional-medicine users; built for MD-led practices; custom pricing. 3.99/5.

**12. Symplast** — *mobile-first plastic surgery EMR*
- **Strengths:** Full functionality on phone/tablet, **HIPAA-secure patient texting & photo sharing**, patient-facing galleries, surgical case management (consult→surgery, room allocation, wait-time).
- **Weaknesses:** Surgery-oriented; ~$299/provider/mo.

**13. Moxie** — *modern, aesthetics-specific software + services*
- **Strengths:** Clean UX + workflow automation; charting, scheduling, payments, memberships, engagement; **purpose-built medspa tools — integrated Good-Faith-Exam (GFE), medspa charting templates, online supply ordering (VIP pricing), inventory, payments tied to Alle/Aspire rewards**; bundles coaching/medical-director support; "replaces 5+ systems."
- **Read:** Best reference for *opinionated, compliance-aware medspa workflow* (US GFE ≈ our prescriber-consult requirement).

### AU health / allied-health (data-residency + claiming)

**14. Cliniko** — AU-made (Melbourne), strong AU compliance, online booking, central records, treatment notes, telehealth, invoicing, SMS, Medicare/health-fund claiming, Xero/Stripe/Mailchimp integrations. **No injection plotting / aesthetic consent workflows.**

**15. Power Diary / Halaxy** — affordable allied-health PM; scheduling, billing, online bookings, native claiming; not aesthetic-specific.

**16. Fresh Clinics** — **AU option built around the regulatory environment**: cosmetic clinic management *plus* on-demand doctors for prescribing & professional support. The most direct AU-compliance-aware competitor; worth studying closely (and noting they bundle prescriber access — a service, not just software).

---

## 3. Master feature taxonomy (the "feature list")

The union of capabilities across all platforms, grouped by module. Use this as the menu we'll
cut down via the clarifying questions. **★ = aesthetic/AU-specific differentiator** (where a
generic tool is weak).

### A. Client-facing booking & engagement
- Online booking site (branded), real-time availability, service/provider/room selection
- Booking widgets for own website + Instagram/Facebook/Google integration; optional marketplace listing
- Deposits / prepayment / card-on-file to hold bookings; configurable cancellation & no-show policy + auto-charge
- Waitlist & cancellation backfill; recurring/standing appointments; group/event bookings
- Self-service reschedule/cancel; automated reminders (SMS/email/push) with confirm/decline
- ★ Pre-treatment intake & consent sent ahead of visit, completed on phone, auto-attached to chart
- ★ Pre-care / aftercare instruction sequences (multi-touch, timed per treatment type)
- Client portal & **client mobile app**: bookings, history, documents, photos, memberships, balances, rebook
- Reviews/ratings capture & routing; referral program; loyalty points

### B. Scheduling & front desk
- Multi-resource calendar (provider, room, device/equipment); day/week/month/room views
- Predictive/optimized scheduling; service durations with processing/gap time; buffer & turnaround
- Front-desk dashboard (waiting / running late / in-room / checked-out)
- Multi-location calendars; provider rosters/availability; time-off; double-booking rules
- Check-in (kiosk/QR), arrival status, wait-time tracking

### C. Clinical / EMR ★ (the biggest gap in horizontal tools)
- Structured client medical record: history, medications, **allergies**, conditions, contraindications, flags
- ★ **Injectable charting**: draw/annotate on facial maps & uploaded photos; mark injection sites, product, units/volume, depth, technique per site
- ★ **Before/after photography**: standardized capture (alignment/ghosting overlays), side-by-side compare over time, annotation, secure storage, patient-phone capture
- SOAP / treatment notes; customizable templates per treatment; predictive snippets/phrases
- ★ **AI scribe** (ambient/dictation → structured note); real-time safety checks vs record
- ★ **Consent management**: per-treatment digital consent, versioned, e-signature, expiry/renewal, ★ AHPRA-aligned risk disclosure, ★ under-18 cooling-off enforcement
- ★ **Treatment plans & protocols**; treatment history timeline; outcome tracking & review-date recall
- ★ **Product/dose traceability**: batch/lot number, expiry, brand, volume used per client/visit (TGA + adverse-event recall) — searchable by lot
- Document storage (labs, letters, photos); chart locking/immutability + amendment audit trail
- Adverse-event / complication logging & reporting
- Telehealth video (★ for the consult-before-prescribe requirement)

### D. ★ Prescribing & medicines governance (AU/QLD-specific — see §4)
- ★ Prescriber consult workflow (in-person or video, **per script**, no async/batch)
- ★ e-Prescribe / script capture tied to individual client + consult record
- ★ S4 medicine register: custody/control, receipt, storage, administration, disposal logging
- ★ Two operating models supported: (i) on-site doctor/NP holds stock; (ii) pharmacy-dispensed per-patient (nurse-led)
- ★ Role gating: who can prescribe vs administer vs assess (RN/NP/EN/doctor scope rules)
- ★ Drug stock reconciliation, expiry alerts, wastage logging, audit-ready medicine ledger

### E. Payments & finance
- Integrated POS (in-person terminal + online + mobile/room-side); card-on-file; tap/EMV
- ★ AU payment rails (Tyro / Square AU / Stripe / Worldline); surcharging rules
- BNPL (Afterpay/Zip/Klarna); gift cards; deposits & partial payments; tipping
- Invoicing, receipts, refunds, voids; split payments; package/series redemption at checkout
- ★ Memberships & recurring billing (autopay, dunning, failed-card recovery, expirations) — central to this clinic's model
- Packages / series / pre-paid visit tracking ("visits remaining", outstanding series)
- Commission & payroll calc; tips; daily closeout/reconciliation; cash drawer
- ★ Accounting integration — **Xero** (already in use here), QuickBooks; GST handling
- Accounts receivable, client credit/account balances, debt ageing (already modeled in the analytics layer)

### F. Inventory & retail
- Consumables (injectables, needles) + retail stock; per-treatment usage deduction
- ★ Lot/batch/expiry tracking (links to clinical traceability + TGA)
- Reorder points & alerts; supplier management/sync; purchase orders; cost of goods (COGS)
- Stock counts, transfers between locations, shrinkage/wastage; inventory valuation/age

### G. CRM, marketing & retention
- Unified client profile (360°): bookings, spend, notes, comms, memberships, photos
- Segmentation; campaigns (email/SMS); automated flows (recall, win-back, birthday, post-treatment)
- ★ Recall/recare by treatment interval (e.g., toxin ~3–4 months); rebooking prompts
- Unified inbox / two-way SMS; missed-call text-back; web chat; ★ AI front-desk assistant
- Reputation/reviews; referrals; loyalty; promotions/offers (★ within TGA advertising limits)
- Lead/prospect pipeline & conversion tracking (already modeled here)

### H. Reporting & analytics (this repo is already a strong head-start)
- Revenue (service/product/membership), payroll/commission, sales forecast
- Client: acquisition, retention, churn, LTV, big spenders, at-risk, no-return
- Operations: utilization, no-shows, cancellations, throughput, conversion funnel
- Per-practitioner performance & treatment mix; membership MRR/churn
- ★ Compliance/audit reports (consent coverage, S4 ledger, lot recall lookup)
- Data-quality / anomaly detection (already implemented)

### I. Staff / back office & platform
- Roles & permissions (RBAC); ★ scope-of-practice gating; staff profiles, rosters, payroll, commissions, time-off
- ★ Audit logs (who saw/changed what — required for medicines + privacy)
- Multi-location / multi-entity; tenant settings; service & price catalog; tax config
- ★ Data residency (AU hosting), encryption, backups, access controls, breach handling
- Integrations/API: calendar (Google/Outlook), accounting (Xero), SMS (Twilio/MessageMedia), payments, e-sign, identity, reviews; webhooks
- ★ Migration tooling — **import the existing Mindbody exports** (this repo already parses them)

### J. Mobile apps
- **Client app**: book/rebook, intake/consent, before/after photos, memberships, balances, reminders, loyalty
- **Provider app**: room-side charting, photo capture, schedule, notes, AI scribe (AR & Symplast prove the demand)
- **Front-desk/manager**: check-in, POS, daily numbers
- Native vs PWA decision (see questions)

---

## 4. ★ Regulatory & compliance — the AU/QLD differentiator

This is where a purpose-built product earns its keep. Two layers apply: **federal (TGA/AHPRA)**
and **Queensland state (S4 medicines law)**. The platform should make compliant operation the
*default* and produce audit-ready evidence.

### 4.1 Federal — TGA (advertising) & AHPRA (practice), national, effective **2 Sept 2025**
- **In-person or video consult required *each time* a cosmetic injectable is prescribed.** Async prescribing by text/email/online is **not acceptable**. → *the platform must tie every script to a documented synchronous consult.*
- **No bulk/batch prescribing** — every patient needs an individual prescription. → *per-client script records, no template-script shortcuts.*
- **Holistic, evidence-based patient assessment** before any procedure, incl. **psychological screening (e.g. body dysmorphic disorder / BDD)**. Only **RNs or NPs** may undertake the assessment. → *structured assessment + BDD screening tool in intake.*
- **RN experience:** min **1 year FT** in an area other than non-surgical cosmetics before expanding scope; specialised training. → *credential/scope fields on staff profiles, gating who can do what.*
- **Enrolled Nurses (EN):** stricter supervision; **cannot** inject dermal filler to very-high-risk areas (glabella, nose, forehead); laser only under direct RN supervision. → *scope rules per role + per body region.*
- **Informed consent:** verbal discussion **plus** written plain-language info; must not minimise complexity or overstate outcomes; provide complaints info incl. right to complain to AHPRA even under an NDA. → *consent templates with mandated content + acknowledgement.*
- **Under-18:** mandatory **7-day cooling-off** between consent and procedure; **no payment** accepted until after cooling-off (except initial consult). → *enforce cooling-off timer + payment block for minors.*
- **Advertising (TGA + AHPRA):** **no S4 advertising**, **no influencer testimonials**, no advertising to under-18s, higher-risk procedures flagged as adult content; non-specific terms like "wrinkle-reducing injections" banned. → *marketing module guardrails; brand-name suppression.*

**TGA — beyond advertising (federal therapeutic-goods law):**
- ★ **Approved products + lawful supply:** use **ARTG-registered** products; S4 ordered by an **authorised prescriber** from **TGA-approved wholesalers**. Importing/using unapproved or counterfeit injectables is a 2026–27 TGA enforcement focus (infringements already issued; penalties up to **$1.65M/breach** individuals, **$16.5M** corporations).
- ★ **Adverse-event reporting (DAEN):** report to **DAEN-medicines** (botulinum toxin) or **DAEN-medical devices** (device-class fillers). *Voluntary but strongly encouraged* for injectors; **mandatory** for unapproved goods under authority and (from **21 Mar 2026**) serious device events at hospital/day-hospital *facilities* (not general/cosmetic practices).
- ★ **Storage / cold chain:** botulinum toxin stored **2–8°C** per product information; keep storage + temperature records.
- **Off-label use:** allowed, but the prescriber then assumes TGA-equivalent responsibility for safety/efficacy + must cover it in informed consent.
- **Advertising depth:** the crackdown bans **direct *and indirect*** references to the S4 — brands/nicknames/blurred logos, generic terms ("anti-wrinkle injections", "dermal fillers"), price promotions, banned hashtags (#botox), and promotional before/after or syringe imagery; **the public booking page / service list is itself advertising**; historical social posts must comply; mandatory health warnings apply to permitted ads.
- **Background (fillers as devices):** some fillers are ARTG **medical devices** (Class IIa/IIb); a substance/biological-device reclassification has a **1 Jul 2026** application deadline — matters when filler is added (Phase 2): the product model must handle **medicine vs device**.
- **Reform context:** AU tightening runs across three regulators (TGA advertising/enforcement · AHPRA practice standards · state S4 poisons controls) Sept-2025 → late-2026; TGA listed cosmetic-procedure goods as a formal enforcement focus for 2026–27.

### 4.2 Queensland — S4 medicines (Medicines & Poisons Act 2019 + MPMR 2021)
- Cosmetic injectables (botulinum toxin, dermal fillers) are **Schedule 4 prescription-only**. The law governs **prescribing, administering, buying, supplying, possessing and storing**.
- **Two lawful business models** the platform must support:
  1. **On-site doctor/NP** holds exclusive/joint custody & control of S4 stock, can buy stock, and after consult prescribes for an authorised person to administer/dispense.
  2. **Nurse-led**: RNs **cannot buy/hold S4 stock** for clinic use; may only hold **individually dispensed** medicines for a specific client. Off-site dispensing must go through a **pharmacy** (script → pharmacy dispense → administer). **Standing orders are not permitted** for RN administration of S4 cosmetics.
- **Enforcement:** Queensland Health inspections/audits; referrals to TGA/AHPRA/OHO; max penalty currently **$32,260** for unlawful buying/possession/prescribing/administration.
- **Implication for the build:** a configurable **medicines-governance module** — custody ledger, per-client dispensing, prescriber linkage, storage/expiry/disposal logs, and audit exports — that can be set to "on-site prescriber" or "nurse-led + pharmacy" mode. This is the single biggest thing no incumbent does for QLD.

### 4.3 Privacy / data
- **Australian Privacy Principles**; health data is sensitive info. Strong preference (and client expectation) for **data stored in Australia**, encryption, access controls, audit trails, breach response. (Several AU buyer-guides explicitly warn against offshore storage of medical data.)

---

## 5. Where incumbents fall short → our wedge

1. **No one does AU/QLD medicines governance.** Every clinical EMR is US-HIPAA-framed; AU salon tools have no clinical layer at all. A native **S4 custody + AHPRA-consult-gating** engine is unique.
2. **Clinical depth vs UX is a forced trade-off today.** AR/Pabau have depth but dated/buggy UX; Mangomint/Boulevard have UX but charting is shallow/add-on. **Do both.**
3. **Compliance-as-default.** Make the compliant path the easy path (consult-before-script, cooling-off timers, lot capture at point of injection, consent coverage dashboards) rather than a manual checklist.
4. **Migration from Mindbody is already half-built here** — the export parser + analytics give a credible "switch off Mindbody" story and a data head-start.
5. **Unified comms + automation** (Mangomint Connect-style) tuned to aesthetic recall intervals.

---

## 6. Open questions (to narrow the feature set) — answered in the next step

Grouped by theme; the most foundational are asked first via the structured prompt. Later rounds
drill into each module.

- **Scope & ambition** — internal single-clinic tool, multi-site group, or commercial SaaS to sell to other clinics?
- **Deployment & data residency** — AU-hosted cloud SaaS, local/on-prem (like today), or hybrid?
- **v1 beachhead** — which module ships first (booking, clinical EMR, payments, client app)?
- **Operating model** — on-site prescriber, nurse-led + pharmacy, or both (config)? (drives the medicines module)
- **Clinical depth** — injection mapping, photo standardization, AI scribe, consent versioning — how deep for v1?
- **Payments** — processor (Tyro/Square/Stripe), BNPL, memberships/autopay priority, deposits.
- **Booking** — own-site only vs marketplace; deposits/cancellation policy; waitlist.
- **Mobile** — client app + provider app? native vs PWA?
- **Integrations** — Xero (in use), Google/Outlook calendar, SMS provider, e-sign, identity.
- **Memberships/packages** — how central; replicate current VIP/autopay model exactly?
- **Migration** — lift current Mindbody history in at launch?
- **Team/roles & compliance gating** — RBAC + scope-of-practice rules from day one?
- **Budget / timeline / team** — build capacity and target go-live.

---

## Sources

- Mindbody — [Medical Spa Software](https://www.mindbodyonline.com/business/wellness/medical-spa-software); reviews/critiques: [Pabau](https://pabau.com/blog/mindbody-alternatives/), [PortraitCare](https://www.portraitcare.com/post/alternatives-mindbody), [Egma](https://egma.ai/blog/patient-management-software-for-med-spas/), [Cherry](https://withcherry.com/blog/med-spa-software)
- Aesthetic Record — [Complete EMR](https://www.aestheticrecord.com/complete-emr/), [site](https://www.aestheticrecord.com/)
- Pabau — [features](https://pabau.com/features/), [med spa](https://pabau.com/industry/medi-aesthetic/), [Capterra](https://www.capterra.com/p/140062/Pabau-CRM/)
- Boulevard — [medspas](https://get.joinblvd.com/medspas/), [advanced charting launch](https://www.businesswire.com/news/home/20231024906249/en/), [G2](https://www.g2.com/products/boulevard-labs-inc-boulevard/reviews)
- Zenoti — [medical spa software](https://www.zenoti.com/medical-spa-software)
- AestheticsPro / Nextech / Symplast — [Software Advice comparison](https://www.softwareadvice.com/medical/aesthetics-pro-profile/vs/nextech/), [PortraitCare EMR roundup](https://www.portraitcare.com/post/best-emr-for-aesthetic-practices)
- Jane App — [features](https://jane.app/us/features), [charting](https://jane.app/landing/charting)
- Fresha — [for business](https://www.fresha.com/for-business)
- Mangomint — [medspa features](https://www.mangomint.com/blog/medical-spa-software-features/), [solution](https://www.mangomint.com/solutions/medical-spa-software/)
- Moxie — [site](https://www.joinmoxie.com/), [medspa software](https://www.joinmoxie.com/medspa-software)
- AU landscape — [Consentz AU roundup](https://www.consentz.com/aesthetic-clinic-software-in-australia/), [Cliniko], [Fresh Clinics](https://www.freshclinics.com/en-au/cosmetic-clinic-management)
- **QLD S4** — [Queensland Health: Medicines in cosmetic injectable businesses](https://www.health.qld.gov.au/system-governance/licences/medicines-poisons/medicines/cosmetic-injectables), [fact sheet PDF](https://www.health.qld.gov.au/__data/assets/pdf_file/0038/1393994/fs-cosmetic-injectables.pdf), [Medical Republic](https://www.medicalrepublic.com.au/queensland-just-flipped-the-rules-on-cosmetic-injectables/116117), [Clayton Utz (TGA advertising)](https://www.claytonutz.com/insights/2025/june/tga-injecting-new-life-into-renewed-cosmetics-guidance)
- **AHPRA 2025** — [New guidelines for cosmetic procedures](https://www.ahpra.gov.au/News/2025-09-02-New-guidelines-for-cosmetic-procedures.aspx), [Cosmetic procedure guidelines hub](https://www.ahpra.gov.au/Resources/Cosmetic-surgery-hub/Cosmetic-procedure-guidelines.aspx), [Clayton Utz analysis](https://www.claytonutz.com/insights/2025/june/navigating-the-2025-ahpra-guidelines-on-cosmetic-procedures-heres-what-you-need-to-know)
