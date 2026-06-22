---
id: TLA-012
title: 'EPIC: Client & provider apps (mobile/tablet)'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:flutter'
  - later
  - 'milestone:M6'
dependencies: []
references:
  - docs/prds/PRD-09-apps-client-provider.md
priority: medium
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The Flutter apps. The client app (booking, intake/consent, pre/post-care, photos, memberships, 'report a concern') and the provider app (chairside charting, injection mapping on a tablet, offline-tolerant capture). Native surfaces that reuse the same API and compliance rules as the web platform.

Derived from PRD-09. Explicitly later than the web platform — the device simulators in the prototype (client-app, treatment-room, check-in) preview these.

**MVP:** no — comes after the web platform is working. **Surface:** Flutter (client + provider) · API. Compliance: inherits all.
<!-- SECTION:DESCRIPTION:END -->
