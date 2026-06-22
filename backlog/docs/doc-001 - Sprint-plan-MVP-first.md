---
id: doc-001
title: Sprint plan (MVP-first)
type: guide
created_date: '2026-06-22 11:03'
---

# Sprint plan — MVP first

> **How to read this.** The backlog is **15 epics** (`TLA-001` … `TLA-015`), each a parent task
> whose **stories** are subtasks (`TLA-004.03`). Every story carries a **stage label** (`milestone:M0` …
> `milestone:M8`) that encodes dependency order, and an **`mvp`** or **`later`** label. Sprints below
> are **work-sized, not calendar-boxed** — one AI-assisted developer, a side project, so elapsed time
> is not the constraint. A sprint maps cleanly to one epic (occasionally split) so the plan stays easy
> to reason about; split a sprint further if a slice is too big to land in one reviewable increment.

## The shape of it

**Two tiers.** Sprints **1–7 deliver the MVP** — a working end-to-end clinic platform: a client can be
**booked → screened/consented → consulted/prescribed → treated/charted → checked out**. Only once that
loop works do sprints **8–14** layer on the **enhancements and later surfaces** (memberships, comms,
reporting, the apps, integrations, facility ops, scale). Within each tier the order is
**dependency-first** — a story never precedes something it depends on.

**The golden thread.** The compliance moat is not a late add-on: scope-of-practice (`canInject`), the
intake/consent gate, the consult→prescription→administration invariants and the immutable medicine
register are all **inside the MVP** (sprints 2–6). That is the product's whole reason to exist.

---

## MVP — the basics (sprints 1–7)

| # | Sprint | Epic(s) | Goal / definition of done |
|---|--------|---------|---------------------------|
| 1 | **Foundations & rails** | `TLA-001` | Repo, CI/CD, AU-hosted env, tenant-isolated data, audit infra, staff+client identity, web shell, design system, observability/security, platform services, de-risk spikes. *A trivial change ships to a secure AU environment automatically.* |
| 2 | **Shell, access & core records** | `TLA-002`, `TLA-003` (mvp) | Nav + role-aware Today + clinic context + **financial gating**; RBAC, the **`canInject`** gate, credentials, **roster**, core client record, audit viewer. *A scoped user signs in and an unqualified practitioner is unbookable.* |
| 3 | **Booking & clients** | `TLA-004` (mvp) | Multi-resource calendar, service catalogue, booking wizard, online self-booking, client directory + 360, visit lifecycle, consult-gate, reschedule/cancel, waitlist, walk-ins, basic reminder. *Staff book a client end-to-end at the desk and online.* |
| 4 | **Intake, consent & gating** | `TLA-005` (mvp) | Intake/medical history, BDD screen, consent + e-sign + versioned templates, image-use consent, cooling-off + under-18 block, guardian co-consent, **server-enforced treatment gate**. *Treatment is blocked until required intake/consent is complete.* |
| 5 | **Consult, prescribing & S4** | `TLA-006` (mvp) | Consult, individual prescription, **administration gate + immutable register**, product catalogue, S4 stock ledger + custody, cold-chain, vial reconciliation, recall lookup, POs, stocktake, destruction. *No S4 administration without a valid script, consent and an in-date lot.* |
| 6 | **Clinical charting** | `TLA-007` (mvp) | Pre-treatment review, toxin note, **lot-first injection mapping**, before/after photos, finalise + close-out + immutable amendments, adverse-event/complication logging, non-S4 skin note, treatment plans. *A treatment is charted and locked, every unit tied to its batch.* |
| 7 | **Checkout & payments** | `TLA-008` (mvp) | Itemised invoice (per-line GST, S4 non-discountable), payment-provider seam (Square, tokens only), in-person card/cash tender + receipts, refunds/voids, daily closeout, checkout assist. *Staff check a client out and balance the day.* |

> **End of MVP:** the full clinic loop runs on one platform. Everything after this is additive.

## Enhancements & later surfaces (sprints 8–14)

| # | Sprint | Epic(s) | Goal |
|---|--------|---------|------|
| 8 | **Memberships & rewards** | `TLA-009`, + `TLA-004.13` deposits, `TLA-005.09` form-builder | Plans/tiers, card-on-file **autopay** + dunning, lifecycle/MRR, packages, gift cards, **non-S4 rewards engine**, pricing what-if. |
| 9 | **Comms, reminders & recall** | `TLA-010` | Channels/templates, full reminders, pre/aftercare sequences, **recall worklist**, Spam-Act consent, public S4 naming, unified follow-up queue. |
| 10 | **Reporting & Governance hub** | `TLA-011` | Business dashboards (owner-only money), compliance dashboards, S4 register export + recall execution, DAEN submission, policy sign-off, inspection pack. |
| 11 | **Client & provider apps** | `TLA-012`, + `TLA-007.06` offline sync, `TLA-007.10` modalities | Flutter client app (book/intake/consent, account, concerns) and provider app (room-side charting/mapping/camera, consult/Rx), offline-tolerant. |
| 12 | **Integrations & compliance hardening** | `TLA-013`, + `TLA-003.10–.13` | Xero invoice/payment sync, two-way calendar, adapter/residency posture; privacy rights, retention/destruction, breach workflow, custom role builder. |
| 13 | **Facility, IPC & complaints** | `TLA-014` | Accreditation register, infection-control/sterilisation/waste logs, emergency kit + continuity contact, complaints register (AHPRA pathway). |
| 14 | **Scale / Phase 2** | `TLA-015`, + `TLA-010.08` growth | Multi-location, public API/webhooks, white-label, SaaS onboarding, native POS/kiosk, deferred roadmap (online checkout, e-prescribing), growth surfaces. |

---

## Working the plan

- **Pick the next story** from the lowest-numbered open sprint, respecting `Dependencies` in the task
  frontmatter. `backlog sequence list --plain` computes a dependency-ordered execution order if you
  want the tool to choose.
- **Priorities within a sprint:** `high` = needed for the sprint's goal; `medium`/`low` = can trail or
  drop to the next sprint without breaking the loop.
- **`later`-tagged stories inside an MVP epic** (e.g. booking deposits, intake form-builder) are parked
  to sprint 8+; they are not required for the MVP loop.
- **Re-slice freely.** If a story is too big for one reviewable PR, split it into subtasks
  (`backlog task create -p TLA-00X.0Y "..."`) — the build steps inside each story already mark the seams.
