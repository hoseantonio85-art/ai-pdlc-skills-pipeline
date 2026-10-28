# Единый бизнес-контекст NORM

Эта папка — **раздел действующего product context**, не новый источник фактов. Исторически описанные сервисы и их связи сохраняются как отправная модель для AI PDLC; текущую реализацию и production необходимо проверять по доступным утверждённым источникам.

## Где что находится

- `services/services_map.md` — карта 14 сервисов и сквозных сценариев.
- `services/*.md` — 14 отдельных описаний сервисов (для `measures.md` — подробное описание по 13 разделам).
- `registry/service_registry.yaml` — путь к полному описанию, роли и переходы между сервисами.
- `registry/capability_registry.yaml` — 56 capabilities; наличие записи не доказывает релиз.
- `registry/role_registry.yaml`, `registry/common_business_rules.md`, `registry/glossary.md` — роль, терминология, правила.
- `registry/measures_questions.md` — 28 исторических вопросов к модели «Мер» и решений.
- `registry/current_product_sources.yaml` — какие внешние свидетельства могут быть подключены локально, но **не входят** в пакет.
- `registry/source_authority.md`, `registry/source_registry.yaml`, `registry/current_product_state.md`, `registry/released_features.md` — достоверность и границы AS IS.

## Изменение предметной модели

Изменяя сервис, синхронизируй полный документ, карту сервисов, registry, capability/role links и документы вопросов. Затем запусти `python -X utf8 context/tools/validate_context.py`. Не утверждай, что в контекст автоматически попали новые версии внешних спецификаций или актуальный runtime: источник должен быть подключён через разрешённый `~/.gigacode/product-evidence.yaml`, открыт и проверен.

## Порядок загрузки

1. Читать manifest и профиль нужной стадии.
2. Для локальной задачи найти сервис в `service_registry.yaml`.
3. Открыть соответствующий **полный** `services/<service>.md`; для «Мер» при необходимости прочитать `measures_questions.md`.
4. При точных требованиях и поведении кода читать только релевантный внешний первоисточник; если недоступен — `NEEDS_SOURCE`.
