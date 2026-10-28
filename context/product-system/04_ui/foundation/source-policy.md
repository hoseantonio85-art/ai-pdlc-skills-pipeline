# NORM: приоритет источников по аспекту

1. Явное принятое решение продукта/утверждённый UX Solution определяет flow и target pattern. Оно не доказывает production currentness.
2. Зафиксированный продуктовый repo — evidence поведения и группировки для своего сервиса/revision.
3. Предоставленный HTML export — evidence геометрии конкретного design scene/state; не production DOM. Геометрия снимается в native viewport, идентификатор узла сохраняется.
4. UI Kit 0.307.0 и components 0.269.0 — evidence primitives/tokens, не замена page composition. Пакеты новее локально поставляемых 0.283.0/0.253.0; совместимость с repo runtime не доказана.
5. Нормализованные contracts согласуют эти аспекты и перечисляют конфликты. Starter реализует их, не является отдельным авторитетом.
6. Универсальные UI-рекомендации разрешают только оставшиеся пробелы.

Не объявляй весь исторический export current автоматически. Состояния экспортов датируются содержимым/предоставлением; release registry отсутствует. В object view правая action/meta зона — принятое target-решение, подтвержденное universal-object-modal; старые кнопки edit в tabs не переносятся. Create/Edit имеют нижние действия. Нормализация не переносит production requirements в прототип.

Raw export/repo не загружать массово. Индекс → выбранный contract → evidence fragment по спорному аспекту. В экспериментальном архиве raw exports и снимки лежат вне runtime context в evidence/. В переносимом context достаточно contracts, metrics и reusable primitives. Exact API/types UI Kit остаются закрыты на stage 03; нормализованные visual facts разрешены.

Если другой продукт выбран, применяй его manifest/starter. Если продукт norm и selector отсутствует, разрешён default norm через registry, но не поиск соседней папки. Внешние absolute D: paths принадлежат аудиту и не требуются при установке.
