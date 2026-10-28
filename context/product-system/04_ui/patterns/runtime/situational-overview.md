# Runtime pattern: Situational overview / interactive analytics

## Purpose

Помочь пользователю понять состояние выборки до чтения длинного списка: где проблема, как распределяются объекты, что изменилось и куда смотреть дальше.

Это не обязательный dashboard. Это situational layer, который может состоять из одного вывода, нескольких агрегатов, распределения, интерактивного графика или их компактной комбинации.

## Explicit decision rule

На каждой registry/monitoring page агент обязан явно проверить вопрос:

> Может ли пользователь понять ситуацию быстрее через агрегат, распределение, динамику или визуальную зону внимания, чем только через список карточек?

- если да — добавь situational overview;
- если нет — не создавай декоративную аналитику.

Bare card list не является автоматическим default, если данные содержат полезный aggregate story.

## Placement

Выбери один из двух базовых вариантов.

### Filter-coupled

```txt
Page header
→ Registry controls / filters
→ Situational overview
→ Entity list
```

Используй, если analytics и list должны реагировать на один query/filter state.

### Overview-first

```txt
Page header
→ Situational overview
→ Registry controls / list filters
→ Entity list
```

Используй, если overview описывает всю область, а фильтры ниже относятся только к detailed list.

Не фиксируй placement механически. Связь состояния важнее шаблона.

## Content options

Выбирай только данные, которые помогают принять решение:

- distribution по статусу/уровню/категории;
- trend во времени;
- concentration / top contributors;
- share / coverage;
- матрица или heatmap, если важны две оси;
- compact KPI только как часть объясняемой ситуации;
- AI summary, если он добавляет интерпретацию, а не повторяет числа.

## Interaction

Если visualization позволяет естественный drill-down:

- click/selection фильтрует или подсвечивает detailed list;
- active analytical selection явно виден;
- list count и applied filters согласованы;
- reset возвращает общий scope;
- chart не должен создавать скрытый фильтр без видимого состояния;
- пользователь может перейти от aggregate к конкретным объектам.

Интерактивность не обязательна, если она не улучшает сценарий.

## Visual choice

Тип графика выбирай по вопросу, а не по привычке:

- сравнение категорий → bar;
- динамика → line/area;
- небольшое part-to-whole → donut/pie;
- две смысловые оси → matrix/heatmap;
- сложная композиция → только если она реально упрощает чтение.

Не использовать dashboard wall из равнозначных KPI cards.

## Relationship to registry

Situational overview не заменяет entity list, если пользователю нужно работать с отдельными объектами. Он задаёт контекст, помогает выбрать фокус и ведёт к детальному слою.

## NORM evidence

Подтверждённый visual direction:

- контрагентский registry: компактные risk/debt summary blocks + distribution ring + detailed debtor list;
- существующий UX context: dashboard/analytics должны вести к filter/drill-down/action.

Screenshot evidence не определяет точный chart API и не требует копировать конкретную диаграмму.
