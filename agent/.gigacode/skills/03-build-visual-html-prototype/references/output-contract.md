# Prototype Output Contract

## 03_visual_prototype.md

```markdown
# Visual HTML Prototype

## Context trace
- Context ID / provider.root / provider.manifest / manifest revision

## Sources
Перечисли только реально открытые файлы. Наличие пути в manifest не считается чтением.

## Product UI routing
- product starter path
- selected runtime patterns
- selected organisms
- reference scenes actually opened

## Visual plan
## Implemented journey and states
## Pattern decisions
- selected invariants
- strong defaults applied/adapted
- situational overview decision for registry/monitoring surfaces
- `composition-adaptation` / `new-pattern-candidate`, if any, with rationale
## Differences from UX Solution
## Quality gate results
- Semantics and scenario
- States and interactions
- Composition and technical integrity
## Runtime and viewport checks
## Limitations
## Status
```

Use `PASS`, `READY_WITHOUT_VISUAL_REVIEW`, `NEEDS_VISUAL_FIX`, `BLOCKED_BY_CONTEXT`, `BLOCKED_BY_UX_HANDOFF`, or `BLOCKED_BY_VISUAL_CONTEXT`.

Use `PASS` only after actual visual review of every required state and surface. If the environment or model cannot visually inspect the render, use `READY_WITHOUT_VISUAL_REVIEW` and list what still needs a human visual check.

## Foundation evidence extension
В существующий handoff добавь Fidelity mode; Preflight zone→variant→source→reused/new→QA region; Comparable scope/coverage; C/P measurements; U review; F journeys; screenshots paths; source revisions/conflicts; limitations. Existing statuses and downstream artifact contracts are unchanged. 95% target must never be claimed without full comparable coverage.
