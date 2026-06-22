# Inspection-readiness pack & governance hub

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/INSPECTION-PACK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

As a owner, I want a one-click pack that assembles the evidence an inspector would ask for, so that we're always inspection-ready.
This story is the 'one-click, we're ready for the inspector' feature: it assembles, into a single dated bundle, the evidence an AHPRA (Australian Health Practitioner Regulation Agency), TGA (Therapeutic Goods Administration) or state-Health inspector asks for — pulled live from across the app rather than re-typed. It sits in the Reporting/Governance layer (step 6 of the clinic-first build): it draws on the compliance dashboards and register exports (COMPLIANCE-DASH), so it depends on those, and the policies sign-off story (POLICIES) hangs off it. The hub is also where the privacy actions (DSAR (Data Subject Access Request), breach drill) are launched. No money figures appear in the pack. A one-click inspection-readiness pack and the cross-case Governance hub (policies sign-off, waste manifests/IPC, DSAR + breach drill) (REQ-RPT-7, ADR-0030, REQ-SEC-8/9).

## How it works

A one-click inspection-readiness pack that assembles, into one dated PDF/bundle, the evidence an AHPRA/TGA/state-Health inspector asks for — pulling the current evidence from across the app rather than re-keying it (REQ-RPT-7, ADR-0030). The owner ticks the categories to include (Registration currency, Consent coverage, Policies & procedures sign-off, Records retention/destruction log, S4 register + reconciliation, Cold-chain & destruction records, Breach & complaints registers) and builds a fresh pack before an inspection or on a regular cadence.
Each category pulls live from its source projection/register at build time, so the pack is always current; the build is itself audited (who built what, when) as an InspectionPack row referencing the included register exports. The Governance hub is the home for the wider cross-case governance work this pack draws on: policies sign-off (POLICIES), waste manifests/IPC logs (PRD-11), and the privacy actions — DSAR/access-and-correction (APP 12/13) and a notifiable-data-breach drill (REQ-SEC-8/9) — are runnable from the hub.
The Overview tile shows inspection-readiness state (Review / Ready) derived from whether the underlying categories are complete (e.g. unsigned policies or lapsed registrations make it 'Review'). No money figures appear in the pack.

## Requirements

- A one-click pack that assembles the evidence an inspector would ask for.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The pack assembles, into one dated bundle, the ticked categories: registration currency, consent coverage, policies sign-off, retention/destruction log, S4 register + reconciliation, cold-chain & destruction records, breach & complaints registers.
- [ ] Each category pulls current evidence from its source at build time.
- [ ] Policies & procedures sign-off is tracked in the hub and included in the pack.
- [ ] DSAR (APP 12/13) and a notifiable-data-breach drill are runnable from the hub.
- [ ] Pack generation is audited (InspectionPack row + AuditEvent, referencing the included exports).

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Governance → Audit pack (gov-audit.png). Intro: inspectors ask to see evidence — current registrations, S4 register, consent records, cold-chain logs, signed policies — 'bundles all of it into one dated PDF'.
- 'Inspection-readiness pack' card: checklist (Registration currency, Consent coverage, Policies & procedures sign-off, Records retention/destruction log, S4 register + reconciliation, Cold-chain & destruction records, Breach & complaints registers) + 'Build pack'.
- Build (buildAuditPack) → result line 'Pack ready: inspection-pack-2026-06-20.pdf · N evidence categories bundled' + toast.
- Overview Inspection-ready tile (Review/Ready) reflects completeness; hub also links Policies, DSAR and breach-drill.

![gov-audit — prototype screen](../screens/gov-audit.png)

## Suggested data model

- **InspectionPack** — id, tenant_id, generated_at, categories[], contents[](register_export_refs + log refs + status snapshots), actor_id, artifact_ref
  - _Audited; one-click bundle; references RegisterExport + cold-chain/waste logs + policy sign-off status._
- **(read) InspectionReadiness** — tenant_id, state(ready|review), gaps[](unsigned_policies|lapsed_registration|…)
  - _Drives the Overview tile._

## Technical notes (high level)

- Architecture decisions: [ADR-0030](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Category checklist + dated pack assembly**
  Behaviour: the owner ticks the categories to include (Registration currency, Consent coverage, Policies & procedures sign-off, Records retention/destruction log, S4 register + reconciliation, Cold-chain & destruction records, Breach & complaints registers) and 'Build pack' assembles them into one dated bundle. Requirements: each ticked category pulls CURRENT evidence from its source at build time (registrations from PRD-01, consent coverage + S4 (Schedule 4 prescription-only medicine) register + breach/complaints from COMPLIANCE-DASH RegisterExport, retention/destruction + cold-chain from PRD-04/PRD-11, policy sign-off from POLICIES); persist an InspectionPack row referencing the included exports; the build produces the dated result line ('inspection-pack-YYYY-MM-DD.pdf · N evidence categories bundled') + toast; no money figures.
- [ ] **Inspection-readiness state (Review / Ready) on the Overview tile**
  Behaviour: compute InspectionReadiness (ready / review) from category completeness and drive the Governance Overview 'Inspection-ready' tile. Requirements: unsigned policies or a lapsed registration make it 'Review'; the tile reflects readiness live as the underlying categories change; reads the same sources the pack assembles from so the tile and a freshly-built pack agree.
- [ ] **Append-only audit on pack generation**
  Behaviour: pack generation is itself governance evidence — every build writes an AuditEvent (actor, timestamp, ticked categories, referenced exports). Requirements: append-only (ADR-0010); capability-gate to the compliance concern; the audit entry references the included RegisterExport artefacts so the pack is reproducible and traceable.
- [ ] **Hub launchers: DSAR (APP 12/13) + notifiable-breach drill**
  Behaviour: wire the cross-case governance launchers into the hub — a DSAR (Data Subject Access Request) / access-and-correction action (APP 12/13, REQ-SEC-8, ties to PRD-01 PRIVACY-RIGHTS) and a notifiable-data-breach drill (REQ-SEC-9, ties to PRD-01 BREACH). Requirements: the hub LAUNCHES the existing flows and projects their state — it does not relocate the guardrails (ADR-0030); both are capability-gated to compliance/owner; no money figures.
