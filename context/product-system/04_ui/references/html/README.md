# HTML references

HTML в этом разделе нужен для повышения product likeness Stage 03. Это visual/composition evidence, а не production UI Kit implementation и не React contract.

## `starter/`

Product-scoped starter для новых NORM HTML prototypes. Он продублирован из legacy skill asset для обратной совместимости и расширен без потери сценариев: Object View показывает новую action/meta zone без Footer, а отдельный Standard/Create/Edit Modal сохраняет fixed Footer с secondary + primary actions. Новый runtime должен брать путь из product context manifest; legacy copy внутри skill пока сохраняется как fallback.

## `norm-vertical-slice/`

Reference scene для цепочки:

`Registry page → Search/Filters → Entity Card → Object Modal/View → Action/Meta Zone → Drawer`.

Использовать выборочно. Не bulk-load HTML, если для задачи достаточно runtime pattern/organism descriptions.

## `situational-overview/`

Reference scene для filter-coupled composition: `controls → interactive situational overview → detailed registry`. Показывает принцип, а не обязательный chart type. Использовать только когда aggregate view помогает понять ситуацию.

## Reference flexibility

HTML scenes являются visual/composition evidence. Их не нужно копировать буквально: canonical invariants обязательны, patterns — strong defaults, references — ориентиры. См. `../../visual/composition-adaptation.md`.

## Aspect-level owner references

`../reference-registry.yaml` normalizes additional owner-provided Pixso/HTML evidence by aspect (filter toolbar, collection variability, forms, current vs target Object View). Raw exports are not required at runtime and are never whole-screen templates.
