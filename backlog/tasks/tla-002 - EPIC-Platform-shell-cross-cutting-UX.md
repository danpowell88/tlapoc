---
id: TLA-002
title: 'EPIC: Platform shell & cross-cutting UX'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - mvp
  - 'milestone:M1'
dependencies: []
references:
  - docs/prds/PRD-01-foundations-tenancy.md
priority: high
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The frame every staff screen lives in: global navigation, the role-aware 'Today' dashboard the clinic opens on, the current-clinic context, financial gating (money figures owner-only), global search, and in-app notifications. Cross-cutting concerns that no single feature owns but every feature depends on.

Derived from the PLATFORM area of the prototype and PRD-01/PRD-08. Financial gating is a hard rule: revenue/MRR/pricing stay behind the owner-only capability; Reception sees memberships but no money.

**MVP:** yes — the shell that hosts booking and checkout. **Surface:** web (staff).
<!-- SECTION:DESCRIPTION:END -->
