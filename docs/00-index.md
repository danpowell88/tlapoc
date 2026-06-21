# Aesthetic Clinic Platform — Documentation Index

A purpose-built, compliance-native operating platform for aesthetic injectable & cosmetic
clinics (the modern replacement for Mindbody). This folder holds the full planning set.

> **Not technical? Start with the [Plain-language review](review/00-start-here.md).** It's a
> jargon-free, chaptered walk-through of *everything* the platform does — what each feature is, why it
> exists and who it's for — with a glossary and a coverage checklist, written so a clinic operator can
> judge whether anything needed to run a clinic is missing.

## Reading order

| # | Doc | What it is |
|---|-----|------------|
| 1 | [01-market-research.md](01-market-research.md) | Competitor deep-dives, feature taxonomy, AU/QLD regulatory landscape |
| 2 | [02-requirements.md](02-requirements.md) | Locked decisions, modules (`REQ-*`), 24 compliance criteria (`C1–C24`), phasing |
| 3 | [03-commercial-model.md](03-commercial-model.md) | **Pricing structure, QLD market size (TAM/SAM/SOM), revenue projection & operating costs** |
| 4 | [adr/decision-log.md](adr/decision-log.md) | Architecture Decision Records (`ADR-0001…`) — the "how" |
| 5 | [prds/](prds/) | Product Requirement Docs (`PRD-01…11`) — per-feature detail, → backlog |
| 6 | [ux/README.md](ux/README.md) | UX principles, screen inventory & end-to-end flows |

## Function tours (plain-language review)

The per-area function tours — what each feature does, who it's for, and the workflows — now live in the
**[Plain-language review](review/00-start-here.md)**, a jargon-free, chaptered walk-through written so a
non-technical clinic operator can read every area and assess coverage. (This folds in and replaces the
old "Area overviews".)

## Hardware

- [ESP32 fridge temperature monitor](hardware/esp32-temp-monitor.md) — reference design for the clinic's own wireless cold-chain monitor (USB power + WiFi → private per-clinic/fridge API with auth): BOM, wiring, firmware sketch, API contract, security & provisioning, and how the app charts it / raises breach jobs.
- [ESP32 S4 cabinet access & tamper monitor](hardware/esp32-cabinet-sensor.md) — sealed-inside, somewhat tamper-resistant DIY monitor for a locked S4 cabinet: solves the metal-box RF problem with an external antenna, fuses door/light/motion sensors to resist magnet-spoofing, and makes silent defeat detectable via a dead-man heartbeat. BOM, wiring, firmware sketch, signed-event API, provisioning, and the access log + tamper jobs it drives (`REQ-MED-8`/`C15`).

## The PRD set

| PRD | Title | Phase | Key REQ / C IDs | ADRs |
|-----|-------|:-----:|-----------------|------|
| [PRD-01](prds/PRD-01-foundations-tenancy.md) | Foundations & tenancy (auth, RBAC, audit, data model) | 0 | TEN, SEC, C10/C19/C21/C22 | 1,2,3,4,5,8,10,16,**17**,**28** |
| [PRD-02](prds/PRD-02-booking-scheduling.md) | Booking & scheduling (+ client/CRM basics) | 1 | BOOK, CLI | 5,8,**24**,**26,29** |
| [PRD-03](prds/PRD-03-intake-consent-gating.md) | Intake, consent & compliance gating | 1 | CONS, C3/C5/C6/C14 | 8 |
| [PRD-04](prds/PRD-04-consult-prescribing-s4.md) | Consult, prescribing & S4 medicines governance — *the moat* | 1 | RX, MED, C1/C2/C7/C8/C11/C13/C15–C17 | 8,11,**21**,**25,27,31** |
| [PRD-05](prds/PRD-05-clinical-charting.md) | Clinical charting: injection mapping & before/after | 1 | CLIN, C8/C12/C14 | 9,10,15,**20**,**25** |
| [PRD-06](prds/PRD-06-payments-memberships-rewards.md) | Payments (in-person POS + autopay), memberships & non-S4 rewards | 1 | PAY, MEMB, C9/C23 | 7,14,**22**,**27,32,33,34,36** |
| [PRD-07](prds/PRD-07-comms-reminders-recall.md) | Comms, reminders & recall | 1 | NOTIF, C9/C23 | 12,**18,19,23**,**32,33,34** |
| [PRD-08](prds/PRD-08-reporting-compliance.md) | Reporting & compliance dashboards | 1 | RPT, C10 + all | 13,**30,31** |
| [PRD-09](prds/PRD-09-apps-client-provider.md) | Apps (Flutter): client & provider | 1 | APP | 6,9,15 |
| [PRD-10](prds/PRD-10-integrations.md) | Integrations: Xero & calendar | 1 | INT | 12,**35,36** |
| [PRD-11](prds/PRD-11-facility-complaints.md) | Facility, infection-control, emergency & complaints | 1–2 | FAC, CLI, C20/C24 | 8,**26,30,31** |

## Recommended build order

1. **PRD-01** (foundations — unblocks all) → **PRD-04** (the compliance moat, highest risk).
2. **PRD-02 → PRD-03 → PRD-05** (the clinical loop).
3. **PRD-06 → PRD-07 → PRD-10** (commerce + comms + integrations).
4. **PRD-08 → PRD-09** (reporting + ship the apps).
5. **PRD-11** (facility/complaints — lighter, can trail).

Run a few **de-risk spikes** alongside PRD-01 (see ADR notes): Square AU card-on-file recurring,
Entra External ID ↔ Flutter ↔ .NET auth, the Flutter injection-mapping canvas, Postgres RLS.
Book a **compliance/legal review** of `02-requirements.md` before building PRD-03/04.

## From PRDs → backlog (next step)

Each PRD's **§4 user stories** and **§6 functional scope** are written to slice directly into
epics/stories. The `REQ-*`/`C*` tags make every backlog item traceable to a requirement and a
compliance criterion. Acceptance criteria (§8) become the story's definition of done.

> Status: DRAFT, **rev 4 (2026-06-20)** — the **gap-area build**: six research/design passes added POC flows for treatments & clinical depth, front desk & operations, money & retail, staff & HR, compliance & governance, and growth & integrations (client app excluded). New **ADR-0025…0036** (decision log), requirements **§12.3** (gap-area additions + register F9–F18), and rev-4 "Prototype alignment" notes on the affected PRDs. Builds on rev 3 (ADR-0017…0024, §12). Items needing validation are flagged 🔬 (Meta messaging, injection auto-detect, AHPRA PIE, reg-system submission APIs, e-prescribing, two-way calendar). Working title only — no product name chosen.
>
> **rev 4.2 (2026-06-20) — QLD/national regulatory re-review.** Fresh re-read of the live standards (AHPRA 2025 guidelines, QLD S4 custody clarification, TGA advertising, ASDER, designated RN prescriber) against C1–C24 → see **[requirements §6.1](02-requirements.md#61-qld--national-regulatory-re-review--gaps--corrections-2026-06-20)** and refreshed **[market research §4](01-market-research.md)**. Headlines: **new role — *designated RN prescriber*** (QLD, Sept 2025); **C6 correction** (no mandatory adult cooling-off); **C7** exclusive-custody precision; **C12/C20** scoped (ASDER + NSQHS apply to hospitals/day-hospitals & cosmetic *surgery*, not a non-surgical clinic). *Recommended follow-up:* an ADR for the designated-RN-prescriber capability.
