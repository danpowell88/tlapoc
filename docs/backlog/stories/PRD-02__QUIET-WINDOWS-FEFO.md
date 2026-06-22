# Quiet windows: stock-expiry / FEFO tie-in

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/QUIET-WINDOWS-FEFO`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/QUIET-WINDOWS`

## Background

As a front-of-house lead, I want quiet windows to flag where soon-to-expire stock could be used, so that we book treatments that consume that stock before it must be written off.
Plainly: matching lots of injectable stock that are nearing expiry to nearby quiet windows that could absorb them. Where it fits: a follow-up to the quiet-windows basic detection (PRD-02/QUIET-WINDOWS) that cross-references inventory against the window list. It reads expiring lots from injectables inventory (PRD-04) ordered first-expiry-first-out (FEFO — the rule that the earliest-expiring batch is used first). It sits in the Reception schedule (PRD-02).

## How it works

The basic panel lists quiet windows; this follow-up cross-references inventory so the clinic can fill those windows with treatments that consume soon-to-expire stock. Lots nearing expiry are matched to nearby quiet windows that could absorb the stock before it must be written off.
Expiring lots are pulled from injectables inventory (PRD-04) ordered first-expiry-first-out (FEFO — the earliest-expiring batch is consumed first), so the windows surfaced are the ones that would genuinely use the at-risk stock.
Each match flags the write-off it would avoid and links through to the underlying stock item, turning a quiet window into a concrete reason to fill it.

## Requirements

- Quiet windows to flag where soon-to-expire stock could be used.

## Acceptance Criteria

- [ ] Lots nearing expiry are surfaced against quiet windows that could absorb them.
- [ ] Expiring lots are pulled from injectables inventory (PRD-04) ordered first-expiry-first-out (FEFO).
- [ ] Each match flags the write-off avoided and links through to the stock item.

## UI designs / screenshots

- An inline stock-expiry hint on cards where an expiring lot could be absorbed (e.g. 'Lot expiring ~6 wks — 3 quiet windows could absorb it').
- The hint names the lot and links through to the stock item; it shows the write-off that filling the windows would avoid.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends QUIET-WINDOWS)** — no new entities; reads expiring Lot/batch records from PRD-04 inventory (FEFO-ordered) and matches them to QuietWindows
  - _Read-only cross-reference; the lot/batch entity is owned by injectables inventory (PRD-04)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Match FEFO-expiring lots to quiet windows**
  Behaviour: surface lots nearing expiry and match them to quiet windows that could absorb the stock. Requirements: pull expiring lots from injectables inventory (PRD-04) ordered first-expiry-first-out (FEFO — earliest-expiring batch first); flag the write-off avoided; link through to the stock item.
