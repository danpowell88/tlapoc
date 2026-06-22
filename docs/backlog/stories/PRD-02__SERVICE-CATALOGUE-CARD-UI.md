# Service catalogue: treatment-menu card UI & status filter

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE-CARD-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/SERVICE-CATALOGUE`

## Background

As a owner / manager, I want treatment cards that show what each service drives, with an Active/Archived/All filter and add/edit, so that I can read and manage the menu at a glance.
Plainly: the treatment-menu card UI — each service card showing its details and a 'Charting & compliance this drives' summary — plus the Active/Archived/All filter and add/edit affordances. Where it fits: a follow-up to the services & treatment menu basic catalogue (PRD-02/SERVICE-CATALOGUE) that adds the rich card presentation and status filtering on top of the basic list. It surfaces the schedule flag's downstream effects (PRD-02/SERVICE-CATALOGUE-WIRING) per card. It sits in Reception (PRD-02).

## How it works

The basic catalogue shows a minimal list; this follow-up adds the rich treatment-menu card UI. Each card shows category, schedule + regulatory class, unit, performed-by roles, price, duration, linked stock, adverse-event route, and a 'Charting & compliance this drives' summary (synchronous consult · individual S4 script · batch-lot select · standard consent · rewards-eligible vs S4 'not rewards-eligible').
S4 (Schedule 4 prescription-only medicine) cards are visibly tagged and their reward/discount controls disabled, surfacing the catalogue-driven enforcement to the owner.
A status filter (Active / Archived / All), a '+ Add treatment' action and per-card Edit/Archive complete the management surface; filtering reflects each service's archived state and archive retires a service without breaking historical bookings.

## Requirements

- Treatment cards that show what each service drives, with an Active/Archived/All filter and add/edit.

## Acceptance Criteria

- [ ] Cards per service show category, schedule + reg class, unit, performed-by roles, price, duration, linked stock, adverse-event route, and a 'Charting & compliance this drives' summary.
- [ ] S4 cards are visibly tagged and their reward/discount controls disabled.
- [ ] A status filter (Active / Archived / All), a '+ Add treatment' action and per-card Edit/Archive are present.
- [ ] Filtering reflects each service's archived state; archive retires a service without breaking historical bookings.

## UI designs / screenshots

- Prototype: Clinical → Treatment menu (clinical-menu.png) — each card shows category, schedule (S4/non-S4) + regulatory class, unit, performed-by roles, price, duration, linked stock, AE route, and 'Charting & compliance this drives'.
- Active/Archived/All filter; '+ Add treatment'; Edit/Archive per card; the S4 tag marks services and disables reward/discount controls.
- (Compounded GLP-1 blocked banner illustrates catalogue-driven enforcement.)

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reads SERVICE-CATALOGUE)** — no new entities; renders Service fields + the 'requires'/rewards_eligible derivation as a card; status(Active|Archived) filter
  - _Presentation over the basic catalogue; S4 cards visibly tagged and reward controls disabled._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Treatment-menu card UI ('Charting & compliance this drives')**
  Behaviour: cards per service showing category, schedule + reg class, unit, performed-by roles, price, duration, linked stock, adverse-event route, and a 'Charting & compliance this drives' summary (synchronous consult · individual S4 script · batch-lot select · standard consent · rewards-eligible vs S4 'not rewards-eligible'). Requirements: visibly tag S4 cards and disable their reward/discount controls; capability-gate the admin actions.
- [ ] **Active / Archived / All filter + add/edit affordances**
  Behaviour: a status filter (Active / Archived / All), a '+ Add treatment' action and per-card Edit/Archive. Requirements: filtering reflects each service's archived state; archive retires a service without breaking historical bookings; add/edit open the capability-gated admin form.
