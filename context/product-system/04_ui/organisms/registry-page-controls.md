# Organism: Registry Page Controls

Status: NORM-confirmed, shared-candidate

## Problem

В Risks и Measures фактически повторяется одна композиция управления registry. Организм фиксирует композицию, но не бизнес-набор фильтров.

## Anatomy

```txt
RegistryPageControls
├─ Left cluster
│  ├─ SectionNavigation / RadioChips, optional
│  └─ QuickFilters / CheckboxChips, optional
├─ Right cluster
│  ├─ Search trigger (tertiary icon)
│  └─ Filter trigger (tertiary icon + label + active indicator)
└─ ExpandableSearchRow, optional
```

Filter trigger → `AdvancedFilterDrawer`.

## Canonical desktop composition

`SectionNavigation` — это segmented control: общий neutral/soft container, selected option — white segment. Он предназначен для named mutually-exclusive choices и не заменяется binary Switch.

Если есть QuickFilters, они идут **сразу после segmented control в том же left cluster** как отдельные pill chips. Search, Filter и другие filtering utilities остаются в right cluster той же строки. Expanded search — допустимый второй ряд только после раскрытия или при responsive/task-specific необходимости.

```txt
[ Все | Мои ] [ Чип ] [ Чип ] [ Чип ]              [ Search ] [ Filter ]
```

## Behavior

- Quick filters применяются сразу.
- Search trigger toggles second row; при открытии input получает focus.
- Search может быть debounced; runtime behavior зависит от продукта/API.
- Filter active state обозначается маленьким status indicator, а не полной перекраской toolbar.
- Advanced filters применяются осознанно через Drawer Footer.
- Сброс Drawer возвращает расширенные фильтры; связь с quick filters задаётся service contract.

## Slots / data

```ts
interface RegistryPageControlsModel {
  sections?: ChoiceItem[];
  quickFilters?: ChoiceItem[];
  search?: { value: string; placeholder: string };
  advancedFilters?: FilterSection[];
  hasActiveAdvancedFilters: boolean;
}
```

Это concept contract, не production React API.

## Do not

- не делать отдельный `RiskFilters`/`MeasureFilters` shell при той же композиции;
- не помещать все advanced filters в page toolbar;
- не открывать Filter Modal;
- не фиксировать конкретные названия фильтров в organism.
- не использовать binary Switch для `Все / Мои` или других named mutually-exclusive вариантов.
- не выносить chips/search/filter в отдельные desktop-строки без responsive/task-specific причины.


## Measured Foundation refinement (4.0.1)
For NORM stage 03, read product-system/04_ui/foundation/composition-index.json (path relative to provider context root) and the selected contract. Exact comparable geometry/color roles come from foundation/visual-dna.md and source-policy.md; approximate MVP numbers above remain fallback only. Event export uses 8px card gap; Risk uses 16px. A status row above title is valid; a compulsory status-leading column is not.
