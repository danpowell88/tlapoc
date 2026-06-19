# Aesthetic Clinic Platform — Documentation Index

A purpose-built, compliance-native operating platform for aesthetic injectable & cosmetic
clinics (the modern replacement for Mindbody). This folder holds the full planning set.

## Reading order

| # | Doc | What it is |
|---|-----|------------|
| 1 | [01-market-research.md](01-market-research.md) | Competitor deep-dives, feature taxonomy, AU/QLD regulatory landscape |
| 2 | [02-requirements.md](02-requirements.md) | Locked decisions, modules (`REQ-*`), 24 compliance criteria (`C1–C24`), phasing |
| 3 | [adr/decision-log.md](adr/decision-log.md) | Architecture Decision Records (`ADR-0001…`) — the "how" |
| 4 | [prds/](prds/) | Product Requirement Docs (`PRD-01…11`) — per-feature detail, → backlog |
| 5 | [ux/README.md](ux/README.md) | UX principles, screen inventory & end-to-end flows |

## The PRD set

| PRD | Title | Phase | Key REQ / C IDs | ADRs |
|-----|-------|:-----:|-----------------|------|
| [PRD-01](prds/PRD-01-foundations-tenancy.md) | Foundations & tenancy (auth, RBAC, audit, data model) | 0 | TEN, SEC, C10/C19/C21/C22 | 1,2,3,4,5,8,10,16,**17** |
| [PRD-02](prds/PRD-02-booking-scheduling.md) | Booking & scheduling (+ client/CRM basics) | 1 | BOOK, CLI | 5,8 |
| [PRD-03](prds/PRD-03-intake-consent-gating.md) | Intake, consent & compliance gating | 1 | CONS, C3/C5/C6/C14 | 8 |
| [PRD-04](prds/PRD-04-consult-prescribing-s4.md) | Consult, prescribing & S4 medicines governance — *the moat* | 1 | RX, MED, C1/C2/C7/C8/C11/C13/C15–C17 | 8,11,**21** |
| [PRD-05](prds/PRD-05-clinical-charting.md) | Clinical charting: injection mapping & before/after | 1 | CLIN, C8/C12/C14 | 9,10,15,**20** |
| [PRD-06](prds/PRD-06-payments-memberships-rewards.md) | Payments (in-person POS + autopay), memberships & non-S4 rewards | 1 | PAY, MEMB, C9/C23 | 7,14,**22** |
| [PRD-07](prds/PRD-07-comms-reminders-recall.md) | Comms, reminders & recall | 1 | NOTIF, C9/C23 | 12,**18,19** |
| [PRD-08](prds/PRD-08-reporting-compliance.md) | Reporting & compliance dashboards | 1 | RPT, C10 + all | 13 |
| [PRD-09](prds/PRD-09-apps-client-provider.md) | Apps (Flutter): client & provider | 1 | APP | 6,9,15 |
| [PRD-10](prds/PRD-10-integrations.md) | Integrations: Xero & calendar | 1 | INT | 12 |
| [PRD-11](prds/PRD-11-facility-complaints.md) | Facility, infection-control, emergency & complaints | 1–2 | FAC, CLI, C20/C24 | 8 |

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

> Status: DRAFT, **rev 3 (2026-06-19)** — aligned to the **Option A** prototype: new **ADR-0017…0022**, requirements **§12** (alignment & feasibility register) and an "Option A alignment" note on every PRD. Items needing validation are flagged 🔬 (chiefly Meta messaging, injection auto-detect). Working title only — no product name chosen.
