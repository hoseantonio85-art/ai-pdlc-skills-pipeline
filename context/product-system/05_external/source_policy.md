# Подключение внешних источников

Внешние OpenSpec/БТ, UI Kit и его документация, frontend/backend и визуальные референсы **не вложены в пакет**. Путь/URL задаётся через `~/.gigacode/product-evidence.yaml`, шаблон в `agent/.gigacode/product-evidence.yaml.example`.

- `products.norm.specifications.local_root/index_url`: разрешённые спецификации и их индекс.
- `products.norm.ui_kit.package_path/docs_root/docs_url`: UI Kit, документы и разрешённый URL.
- `products.norm.repositories.frontend_root/backend_root`: локальные исходники при наличии допуска.
- `products.norm.design_references.local_root/index_url`: разрешённые продуктовые макеты/референсы.

Указание пути не означает доступ. Агент обязан проверить наличие, дату, версию, доступность и прочитать релевантный фрагмент. При недоступности — `NEEDS_SOURCE`/`BLOCKED_BY_SOURCE`. Реальные пути, секреты, внутренние URL не коммитить в распространяемый комплект.
