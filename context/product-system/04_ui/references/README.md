# UI reference registry

Этот слой связывает реальные/целевые UI references с конкретными аспектами продуктовой системы.

## Правило

Не считать whole-screen reference универсальным шаблоном. Читай `reference-registry.yaml`, выбери 1–3 references только по нужному aspect и применяй их вместе с UX/visual/pattern rules. Unrelated parts экрана не копируются автоматически.

Authority: `canonical | preferred | allowed | specialized | reference_only`.
Lifecycle: `current | target | legacy`.

Raw Pixso/HTML exports являются evidence-only и не должны автоматически загружаться в model context. Registry хранит нормализованное назначение references.
