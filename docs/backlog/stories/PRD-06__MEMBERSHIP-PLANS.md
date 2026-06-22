# Membership plans & tiers admin

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-PLANS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP`

## Background

As a owner / manager, I want to define and manage the membership plans, their tiers, prices and benefits, so that the right plans are sold and the right benefits apply at checkout.
Plainly: the owner's screen for defining the membership products themselves — what tiers exist (e.g. Glow Club / Radiance / Platinum), what each costs per month, and what perks each includes — so that selling, autopay and benefit auto-apply all read one definition. Where it fits: it sits in the Payments/commerce layer after the clinical core, and is the catalogue half of the membership story (PRD-06/MEMBERSHIP) — MEMBERSHIP runs the recurring billing and the member list against the plans this story defines. The per-plan benefit set this screen curates is what auto-applies as deductions at the till (PRD-06/POS). A membership benefit may never reward an S4 (Schedule 4 prescription-only medicine) item, so the benefit editor is constrained to non-S4. Plan pricing is owner-only (.fin); price changes here are the live-pricing counterpart to the owner's read-only Pricing & what-if planner (PRD-06/PRICING-WHATIF).

## How it works

A MembershipPlan defines name/tier, monthly price, billing period and a curated benefit list (e.g. '10% off non-S4 retail & facials', 'priority booking', '1 facial / month', 'dedicated nurse'). The Plans tab renders each tier as a card with its price, active-member count and per-tier MRR (monthly recurring revenue), with '+ New plan' to add one and edit/archive per card. This is the definition the rest of the membership machinery reads: MEMBERSHIP charges and lists members against these plans, and the benefits auto-apply at checkout (PRD-06/POS).
The benefit editor is constrained to non-S4: a plan benefit can discount or reward non-S4 services/retail and account/gift credit, but never an S4 (Schedule 4 prescription-only medicine) item — the same C9 invariant the rewards engine enforces, re-checked server-side at config time. The screen states 'Autopay is card-on-file recurring (added online/in-app, never in person). Member rewards apply to non-S4 only.'
Plan pricing and the MRR figures are owner-only (.fin) and stripped for non-owner roles. Admin is capability-gated and every change is audited; a price change applies to new sign-ups, while existing members keep their terms until explicitly migrated (no silent re-pricing). This is the live-pricing counterpart to the read-only projections in PRD-06/PRICING-WHATIF.

## Requirements

- To define and manage the membership plans, their tiers, prices and benefits.

## Acceptance Criteria

- [ ] Plans/tiers are defined with name, monthly price, billing period and a benefit list; '+ New plan' creates one.
- [ ] Each plan's benefits are constrained to non-S4 items (a benefit can never reward an S4 item, C9).
- [ ] Plan price + member counts + per-tier MRR (monthly recurring revenue) are shown; money figures are owner-only (.fin).
- [ ] Editing a plan is capability-gated and audited; existing members keep their terms until migrated.

## UI designs / screenshots

- Prototype: Memberships -> Plans & packages (memb-plans.png) — tier cards (Glow Club $89/mo, Radiance $149/mo, Platinum $249/mo) each listing benefits (e.g. '10% off non-S4 retail & facials', 'priority booking', 'birthday treat'), active-member count and per-tier MRR (e.g. '412 active · $36,668/mo'); '+ New plan'; footer 'Autopay is card-on-file recurring (added online/in-app, never in person). Member rewards apply to non-S4 only.'
- Per-card Edit/Archive; the benefit editor offers only non-S4 items; owner-only (.fin) on price + MRR figures.
- Packages (pre-paid series) products are defined alongside plans on this tab; selling/redeeming a package happens at checkout (PRD-06/PACKAGES-GIFT).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **MembershipPlan** — id, tenant_id, name, tier, price, period, benefits[]{kind(discount|addon|credit), eligible_items(non-S4), value}, active(bool)
  - _Owner-defined; benefits constrained to non-S4 (C9); consumed by MEMBERSHIP autopay + POS benefit auto-apply._
- **AuditEvent (ref)** — actor, plan_id, change, at
  - _Plan changes audited; admin capability-gated; existing members keep terms until migrated._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **MembershipPlan / tier model + benefit list**
  Behaviour: model MembershipPlan with name/tier, monthly price, billing period and a curated benefit list (kind discount|addon|credit, eligible_items, value). Requirements: tenant-scoped with RLS (row-level security); a plan can be archived (not hard-deleted) to preserve history on existing memberships; this is the single definition MEMBERSHIP (autopay/member list) and POS (benefit auto-apply) read.
- [ ] **Non-S4 benefit constraint (C9) at config time**
  Behaviour: the benefit editor only offers non-S4 items, and any attempt to add an S4 (Schedule 4 prescription-only medicine) item to a plan benefit is rejected with a clear blocked-action reason. Requirements: enforce server-side against the catalogue schedule flag (PRD-04/ADR-0014) — the same invariant the rewards engine uses — so a benefit can never reward/discount an S4 item; audit the block.
- [ ] **Capability-gated plan admin + audit + member-term preservation**
  Behaviour: add/edit/archive a plan is gated to owner/manager capability and every change writes an AuditEvent; a price change applies to new sign-ups while existing members keep their terms until explicitly migrated. Requirements: no silent re-pricing of active members; price + MRR (monthly recurring revenue) figures are owner-only (.fin); 'Apply' here is the live-pricing path that PRD-06/PRICING-WHATIF proposes into.
- [ ] **Plans & packages tab UI (tier cards + per-tier MRR)**
  Behaviour: the Plans tab renders tier cards (name, monthly price, benefit list, active-member count, per-tier MRR) with '+ New plan' and per-card Edit/Archive; packages (pre-paid series products) are defined alongside. Requirements: owner-only (.fin) gate on price/MRR; the 'autopay is card-on-file recurring... member rewards apply to non-S4 only' note is shown; loading/empty/error states.
