# NORM Visual Language MVP

## Character

NORM is a calm, dense decision-support product. Make complex risk data easy to scan, explain why an object matters, and keep the next action visible. Use marketplace-like discoverability: meaningful cards, filters, counts, grouping and comparison. Take inspiration from Yandex and Ozon in clarity and information density, not in brand imitation.

## Composition

- Use a light application surface with restrained semantic accents.
- Keep the desktop work area at `max-width: 1240px`; use about `875px` on compact laptops and at least `640px` before mobile adaptation.
- Use a 24px radius for the main application/object surface and 16px for entity cards.
- Build rhythm primarily from 8, 16, 24 and 32px.
- Prefer several clear layers over many equal white boxes.
- Keep service/demo controls outside the product composition.

## Palette and action character

NORM is not a blue-brand interface. Use the measured Foundation palette below. These are prototype aliases, not production token names:

```css
--norm-menu: #f7f8f9;
--norm-surface: #ffffff;
--norm-surface-soft: #f0f2f5;
--norm-text: #24292e;
--norm-text-muted: #6a737d;
--norm-border: #dce0e5;
--norm-action: #32d583;
--norm-action-hover: #11ad81;
--norm-action-soft: #d1faef;
--norm-danger: #f04438;
--norm-danger-soft: #fee4e2;
--norm-warning: #c88417;
```

The navigation/menu area uses the light `#f7f8f9` background in the supplied design scene; soft controls use `#f0f2f5`. Product pages and the rounded application work surface remain white. Do not use a dark sidebar as a NORM signature.

- Use green for the single primary or confirming action and for positive status.
- Use dark neutral actions when emphasis is needed without implying confirmation.
- Use soft neutral buttons for secondary actions. Prefer text actions inside repeated registry rows.
- Blue is allowed only as a restrained semantic color for conventional links or an explicitly blue data category. Never invent dark blue as the NORM brand or use it for all primary buttons, active tabs, filters and links.
- Do not turn every row action into a filled primary button. A clickable row with a clear arrow or text affordance is usually enough; reserve the filled action for the page's main next step.
- Active filters and tabs should rely on weight, border, shape and a soft tint. Avoid a page covered with colored outlines.
- Semantic status colors do not define the product brand. Running may use a cool accent, but it must not recolor unrelated controls.

## Control taxonomy

- **Segmented control** — группа 2–нескольких взаимоисключающих устойчивых вариантов (`Все / Мои`, режимы, локальная section navigation). В NORM это общий нейтрально-серый контейнер с белым выбранным сегментом. Не подменять binary Switch.
- **Binary Switch** — только boolean on/off (`включено / выключено`, `реализовано / нет`). Не использовать для именованных вариантов вроде `Все / Мои`.
- **Filter chip** — отдельный компактный pill-control для частого фильтра. Он располагается рядом с segmented control, но не является его сегментом. Active state — soft tint/weight/shape без тяжёлой цветной рамки.
- **Status tag** — неинтерактивный semantic marker состояния. Не использовать его как filter chip и наоборот.

На desktop registry toolbar по умолчанию сохраняет `segmented + chips` слева и search/filter utilities справа в одной строке; expanded search может раскрыться отдельным нижним рядом.

## Attention hierarchy

For each surface answer in this order:

1. What requires attention?
2. Why does it matter?
3. What should the user do?
4. What evidence supports the conclusion?
5. What technical or historical details are available?

Use size, weight, grouping, spacing and position before color. Color is semantic support, never the only carrier of status.

## Content

- Use plausible Russian business content rather than `item-1`, `risk-101` or lorem ipsum.
- Put the object name, status and decisive signal first.
- В decision registry название/identity остаётся главным левым визуальным якорем. Status/signal не должен автоматически становиться постоянной leading-колонкой перед названием; preferred placement — справа/рядом в верхней смысловой зоне либо в отдельной спокойной status/meta области, если это лучше для конкретной карточки.
- Не применять один row-card layout ко всем коллекциям: navigation categories могут быть card grid, документы/контент — compact list.
- Visually weaken timestamps, IDs and technical metadata.
- Keep AI conclusions distinguishable from confirmed facts.
- Emoji may be used sparingly when it communicates a familiar meaning and matches the product tone. Do not use emoji as the default icon system.

## Avoid

- generic admin-dashboard styling without a scenario reason;
- a narrow column floating in excessive empty space;
- a grid of equal decorative KPI cards that does not add interpretation, navigation or drill-down value; meaningful attention-summary cards are allowed;
- raw tables as the main object registry;
- long unstructured modal content;
- arbitrary gradients, shadows, radii or bright colors;
- a generic blue corporate/admin palette;
- repeated filled CTA buttons in every registry row;
- using one accent color simultaneously for navigation, filters, links, statuses and all actions;
- presenting prototype controls as part of NORM.


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.
