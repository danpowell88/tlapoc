# Leads: conversion KPIs + Follow-ups queue projection

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/LEADS-KPI-FOLLOWUPS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/LEADS-CRM`

## Background

As a front desk / owner, I want conversion KPIs and lead follow-ups surfaced in the unified queue, so that I can see pipeline health and work lead follow-ups in one place.
Plainly: show the pipeline's health — open leads, consults booked, conversion %, average days — and surface lead follow-ups in the unified queue so they get worked. Where it fits: a follow-up to the leads core (PRD-07/LEADS-CRM), which tracks and converts leads; this adds the conversion read-model and the projection of lead follow-ups into the Follow-ups queue (PRD-07/FOLLOWUPS). KPI figures are computed server-side from stage transitions.

## How it works

A conversion KPI read-model powers the cards (Open leads, Consults booked, Conversion %, Avg days), computed server-side from the stage transitions tracked by the leads core (PRD-07/LEADS-CRM). Lead follow-ups surface in the unified Follow-ups queue (e.g. 'Reply & book — Friday consult').
Lead Jobs project into PRD-07/FOLLOWUPS rather than a duplicate table. This extends the leads core (PRD-07/LEADS-CRM). Front-desk/owner gated; loading/empty/error states handled.

## Requirements

- Conversion KPIs and lead follow-ups surfaced in the unified queue.

## Acceptance Criteria

- [ ] A conversion KPI read-model powers the cards (Open leads, Consults booked, Conversion %, Avg days), computed server-side from stage transitions.
- [ ] Lead follow-ups surface in the unified Follow-ups queue (e.g. 'Reply & book — Friday consult').
- [ ] Lead Jobs project into PRD-07/FOLLOWUPS (no duplicate table).
- [ ] Front-desk/owner gated; loading/empty/error states.

## UI designs / screenshots

- Prototype: Growth -> Leads (CRM) — KPI cards (Open leads, Consults booked, Conversion %, Avg days); lead follow-ups appear in the Follow-ups queue.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **(conversion read-model over PRD-07/LEADS-CRM) + Job projection** — open leads, consults booked, conversion %, avg days; lead Jobs → PRD-07/FOLLOWUPS
  - _No new entity; KPIs from stage transitions; lead follow-ups project as Jobs._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Conversion KPIs + lead follow-ups -> Follow-ups queue**
  Behaviour: a conversion KPI read-model powers the cards (Open leads, Consults booked, Conversion %, Avg days); lead follow-ups surface in the unified Follow-ups queue (PRD-07/FOLLOWUPS). Requirements: KPI (key performance indicator) figures computed server-side from stage transitions; lead Jobs project into PRD-07/FOLLOWUPS (no duplicate table); front-desk/owner gated.
