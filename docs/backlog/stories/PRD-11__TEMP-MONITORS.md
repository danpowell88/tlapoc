# Temperature monitor management (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/TEMP-MONITORS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web, integration
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a owner / staff, I want to manage temperature monitors, see their readings and act on breaches, so that cold-chain is continuously evidenced without manual logging.
Plainly: manage the wireless fridge sensors, watch their temperature charts, and act when one reports an out-of-range reading or goes silent. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; this basic slice provisions the monitors, ingests + charts their readings, and runs the excursion/dead-monitor breach pathway (kept in the basic because cold-chain breach is safety-critical), with the manual+device reconciliation added as a follow-up. The prototype's Operations → Temperature monitors (openMonitor/monitorJob) manages wireless cold-chain (the unbroken temperature-controlled storage required for medicines) sensors (the ESP32 (a low-cost Wi-Fi microcontroller) design).

## How it works

Manage wireless cold-chain sensors (the ESP32 design): one monitor per fridge streams readings to this clinic's private API endpoint over WiFi, giving continuous data, instant excursion alerts and a tamper-evident trail. Register/provision monitors per fridge/location (each with a per-device API key); the view shows per-monitor status (online/offline), charted temp, last-seen/signal/firmware/power and summary tiles. Readings chart over time; an excursion raises a breach job and flags affected stock; missing heartbeats surface under Needs attention with 'Raise job' (monitorJob → Lead Nurse).
The excursion/dead-monitor breach pathway stays in this basic because cold-chain breach is safety-critical. The automated feed and the manual fridge log (OPENCLOSE-FRIDGE) reconcile into one cold-chain record in the follow-up (MONITOR-RECONCILE, C13). Continuous, evidenced cold-chain without manual logging.

## Requirements

- To manage temperature monitors, see their readings and act on breaches.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Monitors can be registered/provisioned per fridge/location and authenticate to the per-clinic API.
- [ ] Readings chart over time; a breach raises a job and flags affected stock.
- [ ] Missing heartbeats (dead monitor) are detected and surfaced.
- [ ] The manual+device reconciliation into one cold-chain record is added by the follow-up (MONITOR-RECONCILE).

## UI designs / screenshots

_Prototype screen: prototype.html — Operations → Temperature monitors._

- Prototype: Operations → Temperature monitors (ops-monitors) — tiles Monitors/Online/Last sync/Needs attention; per-monitor cards (name·TM-id·fridge, online/offline, charted temp, Last seen/Signal/Firmware/Power, 'healthy' or 'Raise job', 'Details →').
- Dead-monitor/offline detection ('no recent data'); breach raises a job to Lead Nurse + flags stock (openMonitor/monitorJob). Reconciliation is the follow-up (MONITOR-RECONCILE).

![ops-monitors — prototype screen](../screens/ops-monitors.png)

## Suggested data model

- **Monitor** — id, tenant_id, location_id, fridge_id, label, api_key_ref, last_heartbeat, signal, firmware, power, status
  - _ESP32; missing heartbeat → offline + alert._
- **(reuses) TempLog/Excursion** — PRD-04 COLD-CHAIN — device readings + excursions
  - _Device readings land here; manual+device reconcile in the follow-up (MONITOR-RECONCILE)._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Monitor entity + per-fridge provisioning + per-device auth**
  Behaviour: register/provision one wireless monitor per fridge/location and issue it credentials so it can stream readings. Requirements: model Monitor (tenant_id, location_id, fridge_id, label, api_key_ref, last_heartbeat, signal, firmware, power, status); issue a per-device API key (api_key_ref) so each ESP32 (a low-cost Wi-Fi microcontroller) sensor authenticates to THIS clinic's private endpoint only; tenant-scoped; see the hardware design doc for the ESP32 build.
- [ ] **Ingest readings + chart over time + monitors view**
  Behaviour: ingest streamed readings and chart per-monitor temperature, with a monitors view (summary tiles Monitors / Online / Last sync / Needs attention; per-monitor cards showing online/offline, charted temp, last-seen / signal / firmware / power). Requirements: readings land in the PRD-04 COLD-CHAIN TempLog (not a separate store); the chart is continuous and tamper-evident; cards link to 'Details →' (openMonitor).
- [ ] **Excursion + dead-monitor (heartbeat) detection → breach job**
  Behaviour: a heartbeat watchdog flags monitors with no recent data as offline ('no recent data', '3h 12m ago') under Needs attention; an excursion (or offline / battery-low / firmware condition) raises a breach job. Requirements: monitorJob creates a job to the Lead Nurse carrying the reason and flags the affected stock; 'Raise job' surfaces on the card; the excursion path mirrors the manual breach pathway (OPENCLOSE-FRIDGE).
