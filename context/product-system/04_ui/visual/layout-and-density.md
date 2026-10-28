# Layout and Density

## Shell

Use a stable product shell with navigation outside a rounded light work surface. The prototype may simplify global navigation, but it must still feel embedded in NORM rather than displayed on a blank page.

Recommended desktop values:

```css
--norm-content-max: 1240px;
--norm-content-laptop: 875px;
--norm-content-min: 640px;
--norm-surface-radius: 24px;
--norm-card-radius: 16px;
--norm-space-1: 8px;
--norm-space-2: 16px;
--norm-space-3: 24px;
--norm-space-4: 32px;
```

Use these as MVP HTML tokens, not as claims about the production design-token API.

## Page anatomy

1. Page title and meaningful count.
2. Optional contextual action or AI entry point.
3. Quick filters or attention zones.
4. Optional search and advanced filter control.
5. Main registry/dashboard/content.
6. Floating action dock when the scenario has a persistent next action.

## Registry controls

- На desktop держи segmented scope, quick-filter chips и trailing search/filter actions в одной toolbar-строке, если ширина позволяет.
- Segmented и chips образуют левый cluster; search, advanced filter и вторичные filtering actions — правый cluster.
- Expanded search может раскрыться отдельной строкой ниже, не меняя семантику основного toolbar.
- Перенос controls — responsive/task-specific adaptation, а не default desktop layout.

## Density

- Default to compact but readable business density.
- Use 24px card padding on desktop and 16px on compact/mobile layouts.
- Choose the service variant: Event uses 8px between cards; Risk uses 16px. Do not apply one gap to every registry. Compact layouts may adapt the gap with explicit rationale.
- Keep card metadata in aligned groups so a registry can be scanned vertically.
- Hide or collapse secondary fields on small screens instead of shrinking everything.

## Floating action dock

The bottom action dock is a signature NORM pattern. Use it when a primary action or AI/chat must remain available while the user explores a long surface.

- Float above content near the lower edge.
- Combine one primary contextual action with optional assistant/chat access.
- Use a rounded surface and restrained elevation.
- Do not cover important content; reserve bottom space.
- On narrow screens reduce the dock to essential actions.
- Do not use it when no persistent action exists.


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.

В action dock текстовые кнопки занимают всю свободную внутреннюю ширину и делят её поровну (`flex: 1; min-width: 0`). Компактная иконочная AI-кнопка не растягивается.
