> **Пакетная политика 7.0.3 precise clean:** внешние технические OpenSpec, код UI Kit, фото и репозитории не входят в поставку. Исторические описания и каталоги — локально, реальные источники проверяются через `~/.gigacode/product-evidence.yaml`.

# Подключение контекста NORM — Skills Pipeline v7.0.3

Полная инструкция по установке и первому запуску — в корневом [README](../README.md). В этом файле — именно контракт выбора продуктового контекста.

## Где что находится

- `agent/.gigacode/skills/`: 7 скиллов, готовые к копированию в `~/.gigacode/skills/` или `<project>/.gigacode/skills/`.
- `agent/.gigacode/agents/`: 3 субагента, готовые к копированию в `~/.gigacode/agents/` или `<project>/.gigacode/agents/`.
- `context/`: единый NORM product-context provider, который хранится в стабильном месте **вне** обязательной project-level `.gigacode`.

## Связующие файлы

**1. Registry — `~/.gigacode/product-contexts.yaml`** (путь к установленному контексту). Шаблон: `agent/.gigacode/product-contexts.yaml.example`.

```yaml
contexts:
  norm:
    status: ready
    provider:
      type: local_repository
      root: "D:/AI/skills-pipeline/context"
      manifest: "product-system/context-manifest.yaml"
```

Укажи существующий **абсолютный путь** к корню папки `context`, не к `product-system` и не к файлу manifest. При уже существующем реестре объедини запись `norm`, не перезаписывая другие продукты.

**2. Selector — `<target-project>/.gigacode/product-context.yaml`** (какой контекст использовать в данном проекте). Шаблон: `agent/.gigacode/product-context.yaml.example`.

```yaml
version: 1
context_id: norm
```

**3. Manifest — `context/product-system/context-manifest.yaml`** — карта stage-aware загрузки документации. Отдельно в корень repo не переносить: текущие скиллы ожидают именно относительный путь от `provider.root`.

## Проверка

Из корня репозитория: `python -X utf8 tools/validate_context.py` (необходим PyYAML). После обновления установленной `.gigacode` начни новую сессию GigaCode или выполни `/clear`.

Полный сервис «Меры»: `context/product-system/02_domain/services/measures.md`. Открытые вопросы: `context/product-system/02_domain/registry/measures_questions.md`.

Контекст не загружается целиком на каждом шаге. Compact-регистры используются для навигации, а полный документ читается по реальной потребности; для задач о мерах чтение релевантной части полного документа обязательно.
