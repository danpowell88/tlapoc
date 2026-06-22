# Business dashboards: GROWTH band tiles

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-GROWTH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a GROWTH band of MRR, active members, net member change and new members MTD, so that I can see membership growth at a glance with variance against target.
Plainly: the GROWTH band of the business dashboard — Monthly Recurring Revenue (MRR), Active members, Net member change and New members this month — each tile showing value, target and a coloured variance. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that adds the growth-metric band over the core's BusinessMetrics projection and headline tiles. MRR is money and owner-only (.fin); the member counts stay visible to managers without the money.

## How it works

The GROWTH band renders the membership-growth metrics: MRR (Monthly Recurring Revenue), Active members, Net member change and New members MTD (month-to-date), each tile showing value, target and a coloured variance against that target. It reads the core BusinessMetrics projection (PRD-08/BUSINESS-DASH) sliced for these fields.
MRR is money and owner-gated behind the owner-only financial (.fin) capability — stripped server-side for non-owner roles, who still see the member counts (active / net change / new) as operational figures. Variance colouring is driven by the owner targets (ClinicTarget, from the Targets editor follow-up), and each tile drills into the underlying members/appointments so a number is never a dead end.

## Requirements

- A GROWTH band of MRR, active members, net member change and new members MTD.

## Acceptance Criteria

- [ ] The GROWTH band renders MRR, Active members, Net member change and New members MTD, each with value, target and a coloured variance.
- [ ] MRR is owner-gated (.fin) — stripped server-side for non-owner roles, who still see the member counts.
- [ ] Variance colouring is driven by the owner targets (ClinicTarget).
- [ ] Each tile drills into the underlying members/appointments.

## UI designs / screenshots

- Prototype: Reports — the GROWTH band: MRR, Active members, Net member change, New members MTD; each tile shows value, target and variance.
- MRR tile hidden for non-owner roles (.fin); the member-count tiles stay visible; variance colouring from ClinicTarget; tiles drill into members/appointments.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics (GROWTH slice, extends PRD-08/BUSINESS-DASH)** — mrr (owner-gated), active_members, net_member_change, new_members_mtd
  - _Extends the BusinessMetrics projection; MRR money field owner-financial; member counts operational._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **GROWTH band tiles (MRR, active members, net change, new members MTD)**
  Behaviour: the GROWTH band renders MRR (monthly recurring revenue), Active members, Net member change and New members MTD, each tile showing value, target and a coloured variance. Requirements: MRR is money and owner-gated (.fin) — stripped server-side for non-owner roles, who still see the member counts; variance colouring is driven by ClinicTarget; each tile drills into the underlying members/appointments.
