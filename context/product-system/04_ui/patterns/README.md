# UI patterns

Каталог содержит два уровня описания и не должен bulk-load целиком.

## Authoring patterns

Файлы в корне `patterns/` — подробные reference-backed композиционные паттерны. Они сохраняют evidence, rationale, delegated patterns и открытые вопросы.

## Runtime patterns

`runtime/` — короткие task-time contracts для Stage 03 и engineering handoff. Агент сначала читает `pattern-registry.yaml`, затем открывает только выбранные runtime-файлы.

## Shared shell specs

`specs/modal.md` и `specs/drawer.md` — полные canonical-draft shell contracts. Их не читать по умолчанию; использовать при authoring/reconciliation или когда задача действительно требует детальных правил surface.

## Правило совместимости

Существующие authoring pattern paths не переименованы. Если старый pattern конфликтует с runtime overlay/canonical shell spec, приоритет имеет явный `canonical_overrides`/runtime mapping в `pattern-registry.yaml`. Исторический источник сохраняется в audit при замене нормативного решения.

## Flexibility

Pattern не равен готовому screen template. `pattern-registry.yaml` задаёт adaptation policy: invariants сохраняются, strong defaults адаптируются по задаче, visual references используются как evidence. Новая композиция допустима как `composition-adaptation` / `new-pattern-candidate` при явном rationale.
