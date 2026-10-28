# Registry Page — runtime pattern

## Intent

Рабочая страница со списком однотипных сущностей. Пользователь должен быстро понять scope выдачи, переключить сегмент, найти сущность, уточнить фильтры и открыть объект.

## Canonical composition

```txt
Page
├─ Title + total/context
├─ Optional service-specific insight / situational overview
├─ RegistryPageControls
│  ├─ Section / quick filters
│  ├─ Search trigger
│  ├─ Advanced filter trigger
│  └─ Expandable search
├─ Optional filter-coupled situational overview / interactive analytics
├─ Entity list
│  └─ EntityCard × N
└─ Optional NORM floating create/chat surface
```

## Rules

- Search и Filter находятся в одном control row; search может раскрываться отдельной строкой под ним.
- Quick filters отражают частые срезы; расширенные поля не выносятся все на страницу.
- Filter открывает Drawer.
- Page не оборачивать целиком в большую white card: registry должен сохранять ощущение workspace/canvas.
- Список должен иметь один устойчивый vertical rhythm.
- На каждой registry/monitoring page явно проверь, нужен ли `situational-overview`: распределение, динамика, концентрация или другой aggregate story может дать понимание ситуации быстрее, чем один список.
- Если analytics и list используют общий filter/query state, situational overview можно ставить после controls и перед list. Если overview описывает весь domain, он может быть выше list controls.
- Service-specific insights допустимы между controls/title и list, но не становятся частью universal registry shell; конкретный chart type не фиксируется этим pattern.
- Bare card list не должен быть механическим default, если meaningful analytics реально помогает принять решение.

## States

- loading: skeleton/list loader, controls не прыгают;
- empty: объяснение + следующий шаг;
- filtered empty: отличать от системного empty;
- error: recoverable retry;
- search expanded/collapsed;
- filters active indicator.

## NORM profile

- spacious top area;
- entity cards radius 16 / ~24px padding;
- bottom floating create/chat surface допустим как NORM-specific behavior;
- reference: `../../references/html/starter/index.html` (current implementation); `../../references/html/norm-vertical-slice/index.html#registry` (historical composition only).


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.
