# NORM Visual DNA — runtime

Использовать только после определения `product: norm`.

## Perception

NORM — светлый enterprise workspace с большим количеством воздуха на уровне page и более плотными entity/object surfaces. Интерфейс должен выглядеть спокойным и системным, а не «маркетинговым SaaS».

## Geometry

- App/page: много свободного белого/very-light пространства.
- Entity cards: radius `16px`, padding около `24px`, тонкая border/elevation.
- Secondary blocks: radius `16px`, soft secondary background.
- Large Object Modal: NORM profile `max-width: 1320px`, radius `24px`, viewport margin/padding около `24px`.
- Object View rail: desktop target около `320px`; при узком container rail переносится ниже main content.
- UI Kit Modal baseline: header `32px 40px`, close top/right `32/40`, title около `28/40`.

## Density rhythm

- Page header и верхние controls — воздушные.
- Cards — компактнее и информативнее страницы.
- Modal sections — плотные белые blocks на very-light modal workspace.
- Meta labels и technical IDs — secondary/quiet.
- В registry identity/name является левым anchor; status/signal не превращается в обязательную первую колонку перед названием.

## Color behavior

Не использовать decorative palette. Цвет — преимущественно semantic:

- primary action: фирменный зелёный UI Kit;
- danger/warning/info — только по смыслу;
- status chips — мягкие tinted backgrounds;
- secondary surfaces — neutral gray;
- borders — тонкие neutral tokens.

В production-коде использовать только реальные UI Kit / theme tokens. HTML reference может имитировать их локальными CSS variables, но не является источником production token names.

## Typography

- Заголовки страницы/объекта — сильные, но не oversized.
- Body и metadata компактные.
- Technical IDs, dates, compact labels могут использовать code/secondary styling.
- Иерархия строится weight + spacing, а не постоянным увеличением font-size.

## Controls

- Registry toolbar на desktop по умолчанию — одна строка: `segmented scope` + optional quick-filter chips слева, Search / Filter / filtering utilities справа.
- Segmented scope (`Все / Мои` и аналогичные named choices) — нейтрально-серый общий container с белым selected segment; это не binary Switch.
- Quick filters — отдельные compact pill chips сразу после segmented control; active state soft, без тяжёлой colored outline.
- Binary Switch — только boolean on/off внутри form/content controls.
- Search — tertiary icon trigger → раскрываемое full-width field, если поиск не является главным инструментом страницы.
- Filter — tertiary button с icon + label; active filters обозначаются компактным indicator.
- Status tag — semantic display marker, не интерактивный filter control.
- Primary action заметен, но не заполняет экран цветом.

## Collection variability

- Decision-oriented registry → row/entity cards.
- Navigation/category collection → card/grid entry points.
- Documents/content → compact content/file list.
- Выбор presentation определяется пользовательским решением, а не привычкой использовать один вид карточки.

## Situational analytics

NORM может сочетать registry с compact situational overview, если aggregate view помогает понять ситуацию до чтения объектов. Характерный подход: несколько semantic summary blocks + одна понятная distribution/trend visualization + переход к detailed list.

- analytics должна отвечать на конкретный вопрос;
- chart/segment может фильтровать или подсвечивать list, если это естественно;
- визуализация остаётся спокойной и встроенной в workspace, без отдельного «BI dashboard» языка;
- точный chart type, количество metrics и placement не являются частью Visual DNA.

## Product signature

NORM узнаётся не обязательным набором блоков на каждом экране, а согласованным языком. Используй только элементы, релевантные текущей surface:

1. характерная светлая sidebar/navigation shell — когда показан app context;
2. просторный registry/workspace canvas — для page surfaces;
3. компактные chips и тихие controls — для фильтрации/локальной навигации;
4. плотные bordered entity cards — когда есть object registry;
5. bottom floating create/chat surface — только когда требуется постоянно доступное следующее действие;
6. крупная 1320 Object Modal — только для самостоятельного объекта поверх списка;
7. узкая secondary action/meta rail с блоками radius 24 в выбранном universal-object профиле — внутри Object View.

Не вставляй весь набор ради product likeness. Узнаваемость должна сохраняться и в новой композиции за счёт geometry, density, typography, tokens и interaction semantics.

## Anti-patterns

- generic dashboard с десятком разноцветных KPI cards;
- glassmorphism / gradients ради декора;
- огромные hero-заголовки;
- тёмные массивные borders;
- одинаковая плотность страницы, карточки и Modal;
- Footer actions в Object View;
- произвольная правая панель, не связанная с metadata/actions объекта.


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.
