# UI organisms

Этот слой описывает повторяемые композиции из нескольких базовых UI/UX patterns. Organism не заменяет UI Kit component и не является обязательным единым React-компонентом.

## Правило загрузки

1. Сначала прочитать `../patterns/pattern-registry.yaml`.
2. Затем `organism-registry.yaml`.
3. Открывать только organism, реально выбранный для текущей surface.
4. Не читать organisms другого product profile без необходимости.

## Текущий набор

- `registry-page-controls.md` — composition для section/quick filters, Search и Advanced Filter.
- `object-action-meta-zone.md` — единая правая meta/action зона Object View.

## Product profiles

NORM подтверждён production repositories и screenshots. ORM будет добавлен отдельным profile поверх shared pattern/organism contracts, без копирования всей системы.
