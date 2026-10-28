# Pattern Selection

## Flexibility contract

Patterns define proven semantics and strong defaults, not a frozen screen template. Preserve hard product invariants, but adapt optional slots, order and visualization to the user task. HTML references and screenshots are visual evidence, not mandatory DOM/layout copies.

If an existing pattern does not solve the task well enough, propose a `composition-adaptation` or `new-pattern-candidate`: name the closest existing patterns, explain the mismatch, preserve product Visual DNA/surface semantics, and document the benefit.

See `composition-adaptation.md`.

## Card registry

Use for the primary collection of risks, measures, incidents and similar objects. Do not use a classic table as the main surface.

A row-card should expose:

- status or attention signal;
- object title and short meaning;
- two to four decision-relevant attributes;
- consequence, amount, owner or source when relevant;
- available action or clear click affordance.

Column-like alignment is allowed. The result must still behave as a meaningful card, not a raw database row. A compact table is allowed locally for field-change history or direct comparison of homogeneous values.

## Dashboard / situational overview

Use when the primary task is overview, monitoring, comparison or discovery of attention zones. Also consider a compact analytical layer on registry pages when distribution/trend/concentration lets the user understand the situation before reading items. Every aggregate must lead to filtering, investigation or action. Combine summary with a registry or drill-down. Avoid decorative KPI walls.

When analytics and registry share filter state, a valid composition is `controls → situational overview → detailed list`. When overview represents the whole domain and list filters are local, `overview → controls → detailed list` may be better. Do not hard-code one order. See `../patterns/runtime/situational-overview.md`.

## Filters

- Put frequent, comprehensible choices in quick filters/chips.
- Show counts or semantic states when they help choose a focus.
- Reveal search on demand when it is secondary.
- Open the full filter form in a drawer.
- Mark an active advanced filter with a compact visual signal.

## Object modal

Use for a standalone object opened from a collection when the user should retain collection context. NORM object modal may be near-fullscreen, up to about 1320px.

- Keep close/back actions stable.
- Allow previous/next navigation only for sequential review.
- Use a main content area and right action/meta rail for Object View.
- In read-only Object View all object-level actions belong to the right action/meta zone; a common Footer is not used.
- In create/edit mode keep commit actions in a stable footer.
- See `../patterns/runtime/object-modal-view.md` and `../organisms/object-action-meta-zone.md` for the compact runtime contract.
- Scroll the body, not the entire header/footer shell.

## Drawer

Use for a subordinate task: advanced filters, selection, settings, contextual explanation or work inside an object modal. Preserve the parent surface and return state. Do not open a full independent object in a drawer.

## Summary and AI

Use summary when it reduces interpretation work, not as mandatory decoration. Show the situation, significance and next action before evidence. Label AI-generated conclusions and provide a useful fallback when they are unavailable.
