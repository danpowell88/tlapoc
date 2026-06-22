---
id: TLA-005
title: 'EPIC: Intake, consent & compliance gating'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - 'area:api'
  - mvp
  - compliance
  - 'milestone:M2'
dependencies: []
references:
  - docs/prds/PRD-03-intake-consent-gating.md
priority: high
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Everything that must be true before a needle touches skin. Digital intake and medical history, consent capture against versioned templates, the body-dysmorphia (BDD) screen, image/photo consent, the cooling-off handling, guardian co-consent for under-18s, and the hard gate that blocks treatment until intake + consent + (for injectables) a consult are complete.

Derived from PRD-03. This is what makes the platform compliance-native rather than a generic booking tool — the gate is enforced server-side, not just hinted in the UI.

**MVP:** yes. **Surface:** web (staff) · client (intake/consent links) · API. Compliance: C3, C5, C6, C14.
<!-- SECTION:DESCRIPTION:END -->
