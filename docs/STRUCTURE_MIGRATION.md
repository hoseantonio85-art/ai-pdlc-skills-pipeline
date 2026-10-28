# Структурный патч 7.0.3

Миграция выполняет только перенос документов, обновление путей, README и инструментов; предметные правила и сценарии не перерабатываются.

Перенос: `01_product_foundation` → `01_foundation`; `02_services` и `07_business_context` → `02_domain/services`, `02_domain/registry`; `context/sources/frontend-rules` → `context/product-system/05_engineering`; `context/tools` → `tools`; `AUDIT_REBUILD.md` → `docs/AUDIT_REBUILD.md`.

Ссылки в README, реестрах, manifest, скриптах и документации адаптированы к новым путям.
