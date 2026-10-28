# Контекст: как загружать по стадиям

1. Явный продуктовый контекст пользователя имеет приоритет. Иначе project selector → user-level registry → provider manifest. Не угадывать соседние каталоги.
2. Сначала читать `loading.always` и профиль текущей стадии из `context-manifest.yaml`.
3. По сервисам использовать `service_registry.yaml`, затем **полный документ затронутого сервиса** по `primary_document`; для «Мер» обязательно сверяться с `measures_questions.md`.
4. По UI сначала `patterns/pattern-registry.yaml` → выбранный `runtime/*.md` → при необходимости `specs/*.md`, organisms и composition index.
5. Внешние specs/UI Kit/frontend/backend и визуальные evidence — только через user-level `~/.gigacode/product-evidence.yaml`. Если доступа нет, `NEEDS_SOURCE` или `BLOCKED_BY_SOURCE`; не симулировать чтение.
6. Для Stage 01 исключить UI Kit и code evidence без необходимости; Stage 02 фокус UX; Stage 03 использовать локальный HTML-starter; Stage 04 — продуктовая SDD без генерации API; Stage 05–07 — approved artifacts и реальный target repo.
7. Не bulk-load весь provider: компактные реестры — навигация, а не замена полных документов.
