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

## Drawer — актуальная редакция

Тема выбирается продуктом независимо от scope: NORM — Close в Header и отдельная скруглённая поверхность; ORM — внешний Close и правый край scope. Каскад не ограничен двумя слоями, каждый новый Drawer имеет overlay, Escape по умолчанию выключен. По подробностям читать `../patterns/specs/drawer.md` и `../patterns/runtime/drawer.md`, а старые конфликтующие описания не использовать.
