---
id: TLA-001
title: 'EPIC: Platform foundations & setup'
status: To Do
assignee: []
created_date: '2026-06-22 10:40'
labels:
  - 'type:epic'
  - 'area:infra'
  - mvp
  - 'milestone:M0'
dependencies: []
references:
  - docs/prds/PRD-01-foundations-tenancy.md
priority: high
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Everything that must exist before clinic features can be built safely: the repository and solution structure, CI/CD, an Australia-hosted cloud environment, the multi-tenant data baseline with row-level isolation, staff and client identity wiring, the web and app shells, a shared design system, plus observability and a security baseline.

This epic ships no clinical value on its own — it makes every later epic possible and safe. Stories are scoped to outcomes ("engineers can deploy to a secure AU environment") rather than prescribing the technical how. Derived from PRD-01 §infrastructure and the docs index 'de-risk spikes' note.

**MVP:** yes — blocks all feature work. **Surface:** infra · web shell · provider/client app shells.
<!-- SECTION:DESCRIPTION:END -->
