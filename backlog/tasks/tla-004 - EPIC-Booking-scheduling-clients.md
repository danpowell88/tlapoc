---
id: TLA-004
title: 'EPIC: Booking & scheduling + clients'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - 'area:api'
  - mvp
  - 'milestone:M2'
dependencies: []
references:
  - docs/prds/PRD-02-booking-scheduling.md
priority: high
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The calendar that runs the front desk and the 360-degree client record everything hangs off. Multi-resource scheduling (practitioner + room/chair/device with real durations and buffers), the staff booking wizard, online self-booking, the client directory and client 360, the visit lifecycle (booked to checked-in to complete to no-show), the service catalogue, walk-ins, waitlist and deposits. Bookings are scope-aware — only cleared RN/NP can be booked for injectables — and an injectable booking is gated so it cannot proceed to treatment without intake/consent and a consult.

Derived from PRD-02. The single largest MVP area and the spine the clinical loop runs on.

**MVP:** yes. **Surface:** web (staff) · public web (online booking) · API. Compliance: C4.
<!-- SECTION:DESCRIPTION:END -->
