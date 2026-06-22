# Compliance: breach & complaints registers

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH-REGISTERS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

As a compliance officer, I want to view and export the breach and complaints registers, so that I can evidence our breach and complaint handling in an inspection.
Plainly: the notifiable-data-breach register and the complaints register, presented as viewable and exportable lists on the compliance dashboard. Where it fits: a follow-up to the compliance dashboards core (PRD-08/COMPLIANCE-DASH) that surfaces two more register exports. The dashboard composes these from their source modules (the breach workflow PRD-01/BREACH and the complaints records) rather than owning the records; each export is recorded against the audit trail. Capability-gated to the compliance concern; no money figures.

## How it works

This follow-up surfaces two further registers on the compliance dashboard: the notifiable-data-breach register (C22, sourced from the breach workflow PRD-01/BREACH) and the complaints register (C24, including the right to complain to AHPRA — Australian Health Practitioner Regulation Agency), each as a viewable, exportable list.
The dashboard composes these from their source modules — it reads the breach and complaint records, it does not own them. Each export is a RegisterExport artefact recorded against the audit trail (a point-in-time evidence file, like the S4 register). The surface is capability-gated to the compliance concern; no money figures appear.

## Requirements

- To view and export the breach and complaints registers.

## Acceptance Criteria

- [ ] The notifiable-data-breach register (C22, sourced from PRD-01 BREACH) and the complaints register (C24, including the right to complain to AHPRA) are viewable, exportable lists.
- [ ] Each export is a RegisterExport artefact recorded against the audit trail.
- [ ] The registers read their source modules — the dashboard composes, it does not own the breach/complaint records.
- [ ] Capability-gated to the compliance concern; no money figures.

## UI designs / screenshots

- Prototype: Governance → Overview register exports — the breach register and complaints register download/export actions.
- Each export records a RegisterExport artefact against the audit trail; the registers read their source modules (PRD-01 BREACH + complaints); capability-gated to the compliance concern; no money figures.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **RegisterExport (extends PRD-08/COMPLIANCE-DASH)** — type(breach|complaints), params(date_range?), generated_at, actor_id, artifact_ref
  - _Composes the breach (PRD-01/BREACH) + complaints source records; immutable; recorded against the audit trail (C22/C24)._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Breach & complaints registers (viewable + exportable)**
  Behaviour: present the notifiable-data-breach register (C22, sourced from PRD-01 BREACH) and the complaints register (C24, including the right to complain to AHPRA) as viewable, exportable lists. Requirements: each export is a RegisterExport artefact recorded against the audit trail; the registers read their source modules (the dashboard composes, it does not own the breach/complaint records); capability-gated to the compliance concern; no money figures.
