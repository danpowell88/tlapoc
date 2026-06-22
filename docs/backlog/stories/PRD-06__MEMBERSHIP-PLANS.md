# Membership plans & tiers — define plans + non-S4 benefit constraint (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-PLANS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a owner / manager, I want to define the membership plans, their tiers, prices and a non-S4 benefit list, so that the right plans exist for selling, autopay and benefit auto-apply to read.
Plainly: the core for defining the membership products themselves — what tiers exist (e.g. Glow Club / Radiance / Platinum), what each costs per month, and what non-S4 perks each includes — so that selling, autopay and benefit auto-apply all read one definition. This is the minimal end-to-end core; the capability-gated/audited admin with member-term preservation, and the full Plans & packages tab UI, are added as their own follow-ups. Where it fits: it sits in the Payments/commerce layer after the clinical core, and is the catalogue half of the membership story (PRD-06/MEMBERSHIP). A membership benefit may never reward an S4 (Schedule 4 prescription-only medicine) item, so the benefit editor is constrained to non-S4 from the start (C9). Plan pricing is owner-only (.fin).

## How it works

A MembershipPlan defines name/tier, monthly price, billing period and a curated benefit list (e.g. '10% off non-S4 retail & facials', 'priority booking', '1 facial / month', 'dedicated nurse'). This is the definition the rest of the membership machinery reads: MEMBERSHIP charges and lists members against these plans, and the benefits auto-apply at checkout (PRD-06/MEMBERSHIP-BENEFITS / POS-DEDUCTIONS).
The benefit editor is constrained to non-S4: a plan benefit can discount or reward non-S4 services/retail and account/gift credit, but never an S4 (Schedule 4 prescription-only medicine) item — the same C9 invariant the rewards engine enforces, re-checked server-side at config time. A plan can be archived (not hard-deleted) to preserve history.
Plan pricing is owner-only (.fin) and stripped for non-owner roles. The capability-gated/audited admin with member-term preservation, and the full Plans & packages tab UI with per-tier MRR, are follow-ups.

## Requirements

- To define the membership plans, their tiers, prices and a non-S4 benefit list.

## Acceptance Criteria

- [ ] Plans/tiers are defined with name, monthly price, billing period and a benefit list; a plan can be created.
- [ ] Each plan's benefits are constrained to non-S4 items (a benefit can never reward an S4 item, C9), re-checked server-side at config time.
- [ ] A plan can be archived (not hard-deleted) to preserve history on existing memberships.
- [ ] Plan price figures are owner-only (.fin); the plan is the single definition MEMBERSHIP autopay/member list and POS benefit auto-apply read.

## UI designs / screenshots

- Prototype: Memberships -> Plans & packages (memb-plans.png) — tier cards (Glow Club $89/mo, Radiance $149/mo, Platinum $249/mo) each listing benefits (e.g. '10% off non-S4 retail & facials', 'priority booking', 'birthday treat'); a basic create/define form; the benefit editor offers only non-S4 items; owner-only (.fin) on price figures.
- Per-tier MRR, full card Edit/Archive UX and the packages-alongside layout are added by the Plans-tab-UI follow-up.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **MembershipPlan** — id, tenant_id, name, tier, price, period, benefits[]{kind(discount|addon|credit), eligible_items(non-S4), value}, active(bool)
  - _Owner-defined; benefits constrained to non-S4 (C9); consumed by MEMBERSHIP autopay + POS benefit auto-apply._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **MembershipPlan / tier model + benefit list**
  Behaviour: model MembershipPlan with name/tier, monthly price, billing period and a curated benefit list (kind discount|addon|credit, eligible_items, value). Requirements: tenant-scoped with RLS (row-level security); a plan can be archived (not hard-deleted) to preserve history on existing memberships; this is the single definition MEMBERSHIP (autopay/member list) and POS (benefit auto-apply) read.
- [ ] **Non-S4 benefit constraint (C9) at config time**
  Behaviour: the benefit editor only offers non-S4 items, and any attempt to add an S4 (Schedule 4 prescription-only medicine) item to a plan benefit is rejected with a clear blocked-action reason. Requirements: enforce server-side against the catalogue schedule flag (PRD-04/ADR-0014) — the same invariant the rewards engine uses — so a benefit can never reward/discount an S4 item; audit the block.
