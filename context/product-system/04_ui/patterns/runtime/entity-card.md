# Entity Card — runtime pattern

## Intent

Сканируемый preview сущности в registry. Это shell, а не универсальная схема полей.

## Shared shell

```txt
EntityCard
├─ status/meta row
├─ title / identity
├─ key metrics / attributes
├─ optional divider
└─ secondary description / ownership / related info
```

## Geometry

NORM evidence:

- radius `16px`;
- padding около `24px`;
- neutral 1px border / inset border;
- hover — мягкая elevation/background change;
- карточка самостоятельного объекта целиком кликабельна; открытие не дублируется отдельной кнопкой. Independent actions не запускают открытие.

## Rules

- Не пытаться уравнять Risk, Measure и Event card по внутренним колонкам.
- Сохранять общий shell, hierarchy и density; service profile определяет content slots.
- Самый важный смысл — в верхней половине карточки.
- Technical ID вторичен.
- Не превращать карточку в мини-детальную страницу.

## Service profile examples

- Risk: risk level/status → title → losses/strategy → related recommendations/measures → owner path.
- Measure: status/date → title → planned/actual dates and feature → ID/description/responsible unit.
- Event: использовать отдельный profile по screenshots/repo evidence; не копировать Risk fields.


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.

## Открытие и независимые действия (7.0.2)

Карточка самостоятельного объекта в реестре целиком кликабельна и открывает объект. Отдельная кнопка «Открыть», «Подробнее» или «Посмотреть» не нужна. Внутри допустимы только независимые действия с прямым результатом (например, повторить запуск, согласовать, скачать). Их активация не должна одновременно открывать карточку. Без внутренних действий использовать одну семантическую кнопку/ссылку карточки; при независимых действиях — article с отдельными sibling controls, доступным входом в объект с клавиатуры и обработкой клика свободной области. Не вкладывать кнопку в кнопку; не перехватывать взаимодействие с action controls и выделение текста.
