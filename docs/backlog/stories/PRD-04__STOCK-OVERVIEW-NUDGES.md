# Stock overview: reduce-waste & lift-margin nudges (FEFO, non-S4)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-OVERVIEW-NUDGES`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/STOCK-OVERVIEW`

## Background

As a owner, I want nudges to consume near-expiry lots first-expiry-first-out and clear slow-moving retail using only non-S4 incentives, so that I avoid write-offs and lift margin without breaking S4 advertising rules.
Plainly: the action panel that turns near-expiry stock into a prompt to use it before it must be written off — nudging first-expiry-first-out use and clearing slow-moving retail, using only lawful non-S4 incentives. Where it fits: a follow-up to PRD-04/STOCK-OVERVIEW that adds the 'so-what, do-this' layer on top of the read-only tiles. It reads the expiry-alert query the basic exposes and coordinates with the schedule's quiet windows (PRD-02/QUIET-WINDOWS) so a near-expiry lot can be absorbed.

## How it works

This follow-up turns the overview data into action. A 'Reduce waste & lift margin' panel frames a near-expiry lot as a write-off to avoid ('Lot B2188 expiring ~6 wks · 40u — avoid a ~$440 write-off'), nudges first-expiry-first-out (FEFO) use, and links to the schedule's quiet windows that could absorb it (PRD-02/QUIET-WINDOWS). It also nudges clearing slow-moving retail.
Two hard constraints frame the panel: S4 (Schedule 4 prescription-only medicine) medicines can never be discounted or advertised, so every lever uses non-S4 incentives sent privately to consented clients (TGA, the Therapeutic Goods Administration); and every dollar/margin figure is owner-only and stripped for non-owner roles (the .fin capability) — a non-owner sees the lot-health prompt to act, but no money.
It reads the near-expiry-lot query the basic (PRD-04/STOCK-OVERVIEW) exposes; the write-off value is derived per lot and is owner-only.

## Requirements

- Nudges to consume near-expiry lots first-expiry-first-out and clear slow-moving retail using only non-S4 incentives.

## Acceptance Criteria

- [ ] A 'reduce waste & lift margin' panel frames a near-expiry lot as a write-off to avoid and nudges first-expiry-first-out (FEFO) use.
- [ ] The panel cross-links to the schedule's quiet windows (PRD-02/QUIET-WINDOWS) that could absorb a near-expiry lot.
- [ ] A non-S4 member-offer nudge and a slow-moving-retail bundle nudge are included; every lever uses ONLY non-S4 incentives sent privately to consented clients.
- [ ] Every dollar/margin/write-off figure is owner-only and stripped for non-owner roles (the .fin capability) — a non-owner sees the lot-health prompt to act, but no money.

## UI designs / screenshots

- Prototype screen: Stock & medicines — 'Reduce waste & lift margin' panel (stock.png).
- A near-expiry-lot card ('Lot B2188 expiring (~6 wks · 40u) · avoid a ~$440 write-off · FEFO · 3 quiet windows could absorb it · See quiet windows →'), a 'pull bookings into the window' non-S4 member-offer card and a slow-moving-retail bundle card, with the footnote that S4 medicines can't be discounted/advertised (TGA).
- Owner-only ($) figures rendered only when the .fin capability is present.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **ExpiryAlert (derived)** — lot_id, product_id, expiry, on_hand, weeks_to_expiry, est_writeoff_value(.fin)
  - _Extends the basic's expiry-alert query: adds the owner-only write-off value (.fin) and the FEFO nudge. Ties to PRD-02/QUIET-WINDOWS for absorption._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Near-expiry write-off framing + FEFO nudge + quiet-window link**
  Behaviour: frame a near-expiry lot as a write-off to avoid, nudge first-expiry-first-out (FEFO) use, and link to the schedule's quiet windows that could absorb it (PRD-02/QUIET-WINDOWS). Requirements: read the basic's near-expiry-lot query; the est-write-off dollar value is owner-only and stripped for non-owner roles (.fin).
- [ ] **Non-S4 member-offer & slow-moving-retail nudges**
  Behaviour: a 'pull bookings into the window' non-S4 member-offer nudge and a slow-moving-retail bundle nudge. Requirements: every lever uses ONLY non-S4 incentives sent privately to consented clients — S4 may never be discounted or advertised (TGA); every dollar/margin figure stays owner-only (.fin).
