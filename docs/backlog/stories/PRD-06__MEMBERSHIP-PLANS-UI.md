# Membership plans: Plans & packages tab UI (tier cards + per-tier MRR)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP-PLANS-UI`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/MEMBERSHIP-PLANS`

## Background

As a owner / manager, I want a Plans & packages tab with tier cards showing benefits, member counts and per-tier MRR, so that I can see and manage the membership products at a glance.
Plainly: the polished Plans & packages screen — each tier as a card with its price, benefits, active-member count and per-tier MRR (monthly recurring revenue), with '+ New plan' and per-card edit/archive, and packages defined alongside. Where it fits: a follow-up to the basic plans core (PRD-06/MEMBERSHIP-PLANS) that gives the management surface; it presents what the plan model defines and the admin follow-up governs. Owner-only (.fin) on price/MRR figures.

## How it works

The Plans tab renders each tier as a card with its price, active-member count and per-tier MRR (monthly recurring revenue), with '+ New plan' to add one and edit/archive per card. Packages (pre-paid series products) are defined alongside plans on this tab; selling/redeeming a package happens at checkout (PRD-06/PACKAGES-GIFT).
The screen states 'Autopay is card-on-file recurring (added online/in-app, never in person). Member rewards apply to non-S4 only.' Owner-only (.fin) gate on price/MRR figures. This extends the basic plans core (PRD-06/MEMBERSHIP-PLANS) and surfaces the governance from PRD-06/MEMBERSHIP-PLANS-ADMIN.

## Requirements

- A Plans & packages tab with tier cards showing benefits, member counts and per-tier MRR.

## Acceptance Criteria

- [ ] The Plans tab renders tier cards (name, monthly price, benefit list, active-member count, per-tier MRR) with '+ New plan' and per-card Edit/Archive.
- [ ] Packages (pre-paid series products) are defined alongside plans on this tab; selling/redeeming a package happens at checkout (PRD-06/PACKAGES-GIFT).
- [ ] Owner-only (.fin) gate on price/MRR; the 'autopay is card-on-file recurring... member rewards apply to non-S4 only' note is shown.
- [ ] Loading/empty/error states are handled.

## UI designs / screenshots

- Prototype: Memberships -> Plans & packages (memb-plans.png) — tier cards (Glow Club $89/mo, Radiance $149/mo, Platinum $249/mo) each listing benefits, active-member count and per-tier MRR (e.g. '412 active · $36,668/mo'); '+ New plan'; per-card Edit/Archive; footer 'Autopay is card-on-file recurring (added online/in-app, never in person). Member rewards apply to non-S4 only.'; packages defined alongside.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(read-only over PRD-06/MEMBERSHIP-PLANS + member counts)** — renders tier cards with price, benefits, member count, per-tier MRR
  - _No new entity; per-tier MRR is a read-model; owner-only (.fin)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Plans & packages tab UI (tier cards + per-tier MRR)**
  Behaviour: the Plans tab renders tier cards (name, monthly price, benefit list, active-member count, per-tier MRR) with '+ New plan' and per-card Edit/Archive; packages (pre-paid series products) are defined alongside. Requirements: owner-only (.fin) gate on price/MRR; the 'autopay is card-on-file recurring... member rewards apply to non-S4 only' note is shown; loading/empty/error states.
