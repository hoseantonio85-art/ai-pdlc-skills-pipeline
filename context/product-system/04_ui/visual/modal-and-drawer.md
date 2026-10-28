# Modal and Drawer Rules

## Decision

- Choose Object Modal for a self-contained object opened from a list or another object.
- Choose Drawer for a dependent task that should not replace the parent context.
- Choose a regular modal for short decisions, confirmations or focused forms.
- Choose a page when the work has its own long-lived navigation context.
- An Object Modal may be large. Choose by task and context preservation, not by an arbitrary size limit. If the object contains substantial readable content or several related actions, use a genuinely spacious modal with a stable header; Object View keeps actions in the right action/meta zone, while Create/Edit use a stable footer.

## Modal anatomy

- Small: focused confirmation or short content.
- Medium: ordinary form or structured task.
- Large: complex form or substantial content.
- Object: near-fullscreen object surface; NORM reference width is about 1320px.

Keep header stable, body scrollable and footer stable when it exists. Read-only Object View has no common footer: object-level actions belong to the right action/meta zone. Create/edit actions belong in the footer. Do not invent arbitrary widths for every feature. Shared shell rules live in `../patterns/specs/modal.md`; compact runtime rules live in `../patterns/runtime/object-modal-view.md`.

## Drawer anatomy

Use a stable header, scrollable content and optional fixed footer. A filter drawer commonly uses two actions: reset and apply. A drawer inside Object Modal remains visually subordinate to the object. Shared shell rules live in `../patterns/specs/drawer.md`; compact runtime rules live in `../patterns/runtime/drawer.md`.

## Nested layers

Preserve the state of every underlying layer. Avoid stacking several scrims. Escape and close affect only the top layer. Make the return destination obvious.

These are MVP UX/visual rules. Detailed production focus management and component API belong to the later UI Kit implementation stage.


**Актуальный override Drawer:** для Drawer Escape off by default, Close только верхнего слоя, каждый новый Drawer со своим overlay. Геометрия и два theme-сценария описаны в `../patterns/specs/drawer.md`. Старые общие утверждения о Escape распространяются на Modal в рамках её контракта, но не на Drawer.
