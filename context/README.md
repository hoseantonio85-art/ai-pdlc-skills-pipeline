> **Пакетная политика 7.0.3 precise clean:** внешние технические OpenSpec, код UI Kit, фото и репозитории не входят в поставку. Исторические описания и каталоги — локально, реальные источники проверяются через `~/.gigacode/product-evidence.yaml`.

# NORM Product Context v4

Рабочий product-context provider для Skills Pipeline v7.

## Точка входа

`product-system/context-manifest.yaml`

Manifest определяет stage-aware загрузку. Ранние продуктовые этапы используют compact registries и не bulk-load полный service map. Подробные service documents, analytical specs, UI runtime patterns и package evidence читаются on demand.

## Состав

- `product-system/01_product_foundation` — миссия и продуктовая философия;
- `product-system/02_services` — подробная сервисная модель;
- `product-system/03_ux` — UX principles/patterns;
- `product-system/04_ui` — visual rules, patterns, organisms, starter и UI Kit index;
- `product-system/07_business_context` — compact business layer v4;
- `sources` — on-demand evidence (analytical specs, UI Kit package, frontend rules);
- `tools` — validation/packaging utilities.

Исторические patch notes, migration reports, authoring audits и screenshots не входят в runtime distribution v4. Их нормализованные выводы уже зафиксированы в рабочих правилах.

**Актуализация бизнес-истины:** исходные OpenSpec не входят в архив; исторически нормализованные сведения сохранены в предметной модели. Их требования встроены в существующие `02_services/` и `07_business_context/`, без добавления конкурирующего overlay.
