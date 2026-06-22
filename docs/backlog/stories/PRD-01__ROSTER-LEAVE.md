# Roster: time-off / leave list with approval

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/ROSTER-LEAVE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/ROSTER`

## Background

As a manager, I want to record staff time-off and approve or decline it, so that an approved day off automatically removes that practitioner from the bookable diary.
Plainly: the leave list under the roster grid where staff time-off is recorded and Owner/Lead approve or decline it — and where approved leave then carves a practitioner out of the bookable diary. Where it fits: a follow-up to the roster core (PRD-01/ROSTER) that adds the time-off side of availability. The roster core ships the shift grid and the availability query (roster ∩ canInject); this story adds the 'minus approved leave' term and the approval workflow that drives it.

## How it works

Below the weekly grid sits the Leave list: entries per staff member with a kind (annual / personal / other) and dates, each carrying a status chip (Pending / Approved / Declined). The prototype shows the worked examples ('Dr Lena Park · Annual leave · Thu 26 – Fri 27 Jun · Pending', 'Chloe Adams · Personal · Mon 23 Jun · Approved'). Owner/Lead approve or decline; Reception sees it read-only.
Approved leave is the 'minus approved leave' term in the roster core's availability derivation (PRD-01/ROSTER) — an approved day off carves the practitioner out of the bookable diary (PRD-02) so they can't be booked while away; a pending request is visible but does not yet block. Approve / decline is gated to team:manage and audited so leave decisions are on the record.

## Requirements

- To record staff time-off and approve or decline it.

## Acceptance Criteria

- [ ] A leave list under the roster grid records time-off per staff member with kind (annual / personal / other) and dates.
- [ ] Each entry has a status chip (Pending / Approved / Declined); Owner/Lead can approve or decline.
- [ ] Approved leave blocks bookable availability (subtracted in the ROSTER availability derivation); pending does not yet block but is visible.
- [ ] Approve / decline is gated to team:manage and audited.

## UI designs / screenshots

- Prototype: Team → Roster & leave (team-roster.png) — the Leave list below the grid (e.g. 'Dr Lena Park · Annual leave · Thu 26 – Fri 27 Jun · Pending', 'Chloe Adams · Personal · Mon 23 Jun · Approved') with status chips.
- Owner/Lead approve/decline; Reception sees it read-only; approved leave blocks availability, pending does not yet block but is visible.

## Suggested data model

- **TimeOff** — id, tenant_id, staff_id, kind(annual|personal|other), start, end, status(pending|approved|declined), approved_by
  - _Approved leave blocks availability (feeds the ROSTER availability derivation); pending does not yet block but is visible._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Leave list + approve/decline workflow**
  Behaviour: the Leave list below the grid — entries with kind (annual/personal/other), dates and a status chip (Pending/Approved/Declined), with approve/decline actions for Owner/Lead and a read-only view for Reception. Requirements: model TimeOff with the approval status; approve/decline is gated to team:manage and audited.
- [ ] **Approved leave subtracted from bookable availability**
  Behaviour: approved leave is subtracted in the roster core's availability derivation (PRD-01/ROSTER) so an approved day off removes the practitioner from the bookable diary (PRD-02); pending leave is visible but does not yet block. Requirements: this only supplies the 'minus approved leave' term — the availability query itself lives in ROSTER.
