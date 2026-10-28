> **Пакетная политика 7.0.3 precise clean:** внешние технические OpenSpec, код UI Kit, фото и репозитории не входят в поставку. Исторические описания и каталоги — локально, реальные источники проверяются через `~/.gigacode/product-evidence.yaml`.

# UI Kit loading

1. Прочитайте `component-index.yaml`.
2. Составьте mapping элементов prototype к выбранным components.
3. Откройте только соответствующие sections в `ui_base.md`.
4. Если API неоднозначен, проверьте exact type declaration в package `локально установленный UI Kit из product-evidence.yaml`.
5. Не загружайте весь package или весь `ui_base.md` в context window.
