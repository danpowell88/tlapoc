# Business dashboards: FINANCE band tiles

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-FINANCE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a FINANCE band of revenue (+ month-on-month), prepaid liability, to-reactivate value and autopay success, so that I can see the clinic's money metrics in one band.
Plainly: the FINANCE band of the business dashboard — Revenue last month (+ month-on-month), Prepaid liability, To-reactivate value and Autopay success — the money metrics for running the clinic. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that adds the financial band over the core's projection and tiles. Every dollar figure here is owner-only behind the owner-only financial (.fin) capability; only the autopay-success rate may show to a payments role.

## How it works

The FINANCE band renders the money metrics: Revenue last month with its month-on-month (MoM) change, Prepaid liability (outstanding prepaid package/membership value), To-reactivate value, and Autopay success. It reads several projections — revenue/MoM from the payments projection, prepaid liability from the package/membership projection, autopay success from the dunning signal (PRD-06).
Every dollar figure here is gated behind the owner-only financial (.fin) capability and stripped server-side for non-owner roles. The one nuance: the autopay-success rate (a percentage, not a dollar) may show to a payments role per the gating rule, while the dollar figures stay owner-only.

## Requirements

- A FINANCE band of revenue (+ month-on-month), prepaid liability, to-reactivate value and autopay success.

## Acceptance Criteria

- [ ] The FINANCE band renders Revenue last month (+ month-on-month), Prepaid liability, To-reactivate value and Autopay success.
- [ ] Every dollar figure is owner-only (.fin) and stripped for non-owner roles.
- [ ] Revenue/MoM read the payments projection, prepaid liability the package/membership projection, autopay success the dunning signal (PRD-06).
- [ ] The autopay-success rate may show to a payments role per the gating rule while the dollar figures stay owner-only.

## UI designs / screenshots

- Prototype: Reports — the FINANCE band: Revenue last month (+MoM), Prepaid liability, To reactivate, Autopay success.
- Every dollar figure .fin-gated (owner-only); the autopay-success rate may show to a payments role; revenue/MoM, prepaid liability and autopay read their respective projections (PRD-06 for dunning).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics (FINANCE slice, extends PRD-08/BUSINESS-DASH)** — revenue (+ mom), prepaid_liability, reactivation_value, autopay_success
  - _Extends the BusinessMetrics projection; all dollar fields owner-financial; autopay-success rate may show to a payments role._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **FINANCE band tiles (revenue + MoM, prepaid liability, to-reactivate, autopay success)**
  Behaviour: the FINANCE band renders Revenue last month (+ month-on-month), Prepaid liability, To-reactivate value and Autopay success. Requirements: every dollar figure here is owner-only (.fin) and stripped for non-owner roles; revenue/MoM read the payments projection, prepaid liability the package/membership projection, autopay success the dunning signal (PRD-06); the autopay-success rate may show to a payments role per the gating rule while the dollar figures stay owner-only.
