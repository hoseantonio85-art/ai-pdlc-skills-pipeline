# Engineering standards · stages 05–07

Это **встроенные нормативные правила** pipeline, восстановленные из расширенных frontend-источников. Это не пакеты UI Kit, снимки репозиториев, внешние продуктовые спецификации или заменитель target repo.

## Маршрутизация

`context-manifest.yaml` загружает оба документа в `for_frontend_planning`, `for_frontend_implementation`, `for_frontend_review` и **не** загружает на этапах 01–04.

1. [Engineering standards](engineering-standards.md) — профиль, evidence, TS/React, async, тесты, severity.
2. [Component structure & handoff](component-structure-and-handoff.md) — data, barrels, UI Kit, styles, i18n, boundaries, preview/handoff.

Frontend-агент обязан разрешить выбранный context, прочесть документы профиля и skill `05-07-frontend-standards` с references. Если выбранный context недоступен, не утверждать, что локальные product rules прочитаны. `TARGET_REPO` остаётся источником **фактических** версий, runtime, exports и conventions; нормативные ограничения проверяются на применимость к target и конфликтующие требования отражаются в плане/ревью. Чужую архитектуру без доказательств не навязывать.

Источники извне: `~/.gigacode/product-evidence.yaml` (локально, не коммитить). Путь — только указатель, не свидетельство прочтения; проверяй право доступа, версию, путь/URL и содержимое. Не указывай реальные корпоративные адреса здесь.
