# Back-office / bench tablet surface (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/BACKOFFICE-TABLET`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-11/OPENCLOSE`, `PRD-07/FOLLOWUPS`

## Background

As a clinic staff, I want a bench-tablet hub showing the day's operational attention items, so that I can see at a glance what the back room needs, on a shared device.
Plainly: a back-room bench tablet at its core — a 'Good morning' hub that pulls the day's attention items into one glance, on a shared device that attributes each action to whoever's using it. Where it fits: a late surface that composes existing module views (PRD-04 medicines, PRD-11 operations, PRD-07 jobs) rather than re-implementing them; this basic slice is the shell + hub + shared-device sessions, and the open/close+cold-chain, stock+S4+waste, and tasks+handover panels are its follow-ups. A focused operations view for the back room.

## How it works

A bench tablet for behind-the-scenes work, opening on a 'Good morning' hub that shows the morning's attention items (open/close progress, cold-chain status, expiring stock, last handover) with a left rail (Today · Open & close · Cold chain · Stock · S4 register · Waste log · Tasks & handover). This basic slice stands up the shell, the hub and shared-device sessions; it composes existing module views rather than duplicating data.
Role/financial gating applies (owner-only money stays gated via .fin); actions are audited; shared-device session handling attributes actions to the acting staff member. The open/close + cold-chain, stock + S4-register + waste, and tasks + handover panels are added by the follow-ups (BACKOFFICE-OPENCOLD, BACKOFFICE-STOCK, BACKOFFICE-TASKS).

## Requirements

- A bench-tablet hub showing the day's operational attention items.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A back-office tablet surface opens on a 'Good morning' hub pulling the morning's attention items (open/close progress, cold-chain status, expiring stock, last handover) into one glance.
- [ ] It composes existing module views (does NOT re-implement them).
- [ ] Shared-device session handling attributes every action to the acting staff member; all actions audited.
- [ ] Role/financial gating applies — owner-only money stays behind the .fin capability.

## UI designs / screenshots

_Prototype screen: backroom.html._

- Prototype: backroom — 'Good morning, Tessa' hub with morning attention items; left rail Today · Open & close · Cold chain · Stock · S4 register · Waste log · Tasks & handover.
- Shared-device session handling; financial figures stay owner-only (gated). Panels are filled by the follow-ups.

![backroom — prototype screen](../screens/backroom.png)

## Suggested data model

- **(reuses) hub read-model** — morning attention items: open/close progress, cold-chain status, expiring stock, last handover
  - _Composes existing module reads (PRD-04/07/11); no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Bench-tablet shell + 'Good morning' hub + shared-device sessions**
  Behaviour: a back-office web/tablet surface with a left rail (Today · Open & close · Cold chain · Stock · S4 register · Waste log · Tasks & handover) opening on a 'Good morning' hub that pulls the morning's attention items (open/close progress, cold-chain status, expiring stock, last handover) into one glance. Requirements: composes existing module views (does NOT re-implement them); shared-device session handling attributes every action to the acting staff member; role/financial gating applies (owner-only money stays behind the .fin capability); all actions audited.
