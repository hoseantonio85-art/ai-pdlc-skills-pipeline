# Подробная установка контекста в GigaCode

Это инструкции для `product-contexts.yaml`, `product-context.yaml` и `context-manifest.yaml` из более подробного варианта исходной 7.0.3. Полный состав пронумерованных скиллов и порядок их установки — в [README](../README.md).

В этой сборке внешний UI Kit, технические спецификации, репозитории и изображения не упакованы; их локальные пути и разрешённые URL задаются в `~/.gigacode/product-evidence.yaml` после установки. Наличие YAML не свидетельствует, что агент прочитал источник.

### 2. Размести папку контекста NORM

`context/` можно оставить прямо в клонированном репозитории, например:

- Windows: `D:/Projects/skills-pipeline/context`
- macOS/Linux: `/home/user/projects/skills-pipeline/context`

Можно хранить контекст отдельно, например `D:/AI/contexts/norm`. Важно, чтобы внутри выбранной папки существовал файл **`product-system/context-manifest.yaml`**.

**Не копируй весь `context/` в каждый frontend-проект**: путь к нему настраивается один раз через реестр. Скиллы и субагенты могут находиться в пользовательском `~/.gigacode/`, а контекст — где удобно.

### 3. Настрой `product-contexts.yaml`: где лежит контекст

Это **реестр доступных продуктовых контекстов**, а не файл запуска pipeline. Это **контракт скиллов и субагентов нашего Skills Pipeline v7.0.3**, а не универсальная встроенная настройка GigaCode: агент должен выполнить описанный в скиллах *context preflight* и реально прочитать нужные файлы. Само наличие YAML ещё не доказывает, что контекст загружен.

Реестр хранится в домашней папке пользователя:

| ОС | Точный путь к файлу |
|---|---|
| Windows | `C:/Users/<имя_пользователя>/.gigacode/product-contexts.yaml` (`$HOME\.gigacode\product-contexts.yaml` в PowerShell) |
| macOS / Linux | `~/.gigacode/product-contexts.yaml` |

В репозитории находится **шаблон**, а не активная настройка:

`agent/.gigacode/product-contexts.yaml.example`

1. Найди пользовательскую папку `.gigacode` (если её нет — создай).
2. Если `product-contexts.yaml` уже существует — **открой его и сохрани остальные записи**. Не замещай файл целиком шаблоном.
3. Если файла нет — скопируй шаблон, убрав суффикс `.example`.
4. В `provider.root` вставь **абсолютный путь именно к папке `context`**, которая существует на твоём компьютере.

**Пример Windows** (если репозиторий находится в `D:/Projects/skills-pipeline`):

```yaml
contexts:
  norm:
    status: ready
    provider:
      type: local_repository
      root: "D:/Projects/skills-pipeline/context"
      manifest: "product-system/context-manifest.yaml"
```

**Пример macOS/Linux**:

```yaml
contexts:
  norm:
    status: ready
    provider:
      type: local_repository
      root: "/home/user/projects/skills-pipeline/context"
      manifest: "product-system/context-manifest.yaml"
```

Что означают параметры:

- `contexts` — словарь доступных продуктовых контекстов.
- `norm` — уникальный идентификатор контекста; он должен совпадать с `context_id` в selector и manifest.
- `status: ready` — контекст объявлен готовым к выбору (это не проверка корректности пути).
- `type: local_repository` — документы читаются из локальной директории.
- `root` — физический абсолютный путь к **корню provider `context/`**; это не ссылка на GitHub, не путь до `product-system/` и не путь к самому manifest.
- `manifest` — путь **относительно `root`**. Для NORM оставь `product-system/context-manifest.yaml` без изменений.

Для Windows используй в YAML прямые слеши (`D:/Projects/...`) — так не возникнут проблемы с экранированием обратных слешей. Не вставляй путь с `<...>` буквально. Не используй табы для отступов YAML.

**Если контекстов несколько**, добавляй новую запись в том же реестре; второй файл `product-contexts.yaml` не нужен:

```yaml
contexts:
  norm:
    status: ready
    provider:
      type: local_repository
      root: "D:/Projects/skills-pipeline/context"
      manifest: "product-system/context-manifest.yaml"
  orm:
    status: ready
    provider:
      type: local_repository
      root: "D:/AI/contexts/orm"
      manifest: "product-system/context-manifest.yaml"
```

Здесь `orm` — **только пример формата**. Указывай его лишь после создания и установки настоящего контекста ORM с собственным manifest. Не копируй эту запись, если второго контекста у тебя нет.

### 4. Настрой `product-context.yaml`: какой контекст выбран для проекта

`product-contexts.yaml` регистрирует контексты, но **не выбирает автоматически NORM для каждой задачи**. Для конкретного frontend-/продуктового проекта создай:

```text
<путь к рабочему проекту>/
└── .gigacode/
    └── product-context.yaml
```

Например, если GigaCode работает в `D:/Projects/[обезличено]-cloud-measures-front`, файл будет здесь:

`D:/Projects/[обезличено]-cloud-measures-front/.gigacode/product-context.yaml`

Содержимое:

```yaml
version: 1
context_id: norm
```

Готовый образец: `agent/.gigacode/product-context.yaml.example`. Скопируй его именно **в `.gigacode` рабочего проекта**, убрав `.example`. Не путай с папкой `agent/.gigacode` в репозитории этого pipeline — там лежат установочные шаблоны.

`context_id: norm` должен соответствовать ключу `norm` из пользовательского `product-contexts.yaml` и полю `context_id` в manifest NORM.

**Как работает выбор:** если в задаче прямо сказано «используй контекст ORM» или «без контекста», явный выбор пользователя имеет приоритет; иначе GigaCode обращается к selector текущего рабочего проекта. Если контекст не определён однозначно, skill должен запросить выбор, а не угадывать.

Папки `skills/` и `agents/` можно установить глобально и использовать из разных проектов. `product-context.yaml` тогда отличается от проекта к проекту.

### 5. Не меняй `context-manifest.yaml` ради установки

Файл `context/product-system/context-manifest.yaml` **уже есть** в комплекте. Его не нужно копировать в `.gigacode` или переносить в корень GitHub.

Manifest описывает профили загрузки знаний для стадий AI PDLC и on-demand документы:

- для постановки: business rules, реестры сервисов и ролей;
- для UX: продуктовый контекст и UX-паттерны;
- для прототипирования: UI-паттерны и эталонные HTML-компоненты;
- для инженерных стадий: релевантные frontend-правила и target-repo evidence.

При задачах по «Мерам» агент должен открыть **полный** `product-system/02_domain/services/measures.md`, а не ограничиваться записью в `service_registry.yaml`.

### 6. Проверь установку и начни работу

**Проверка А — существуют ли файлы?**

В Windows PowerShell (пути в примере адаптируй к своей установке):

```powershell
Test-Path "$HOME/.gigacode/product-contexts.yaml"
Test-Path "D:/Projects/skills-pipeline/context/product-system/context-manifest.yaml"
Test-Path "D:/Projects/[обезличено]-cloud-measures-front/.gigacode/product-context.yaml"
```

Для каждого корректно размещённого файла результат должен быть `True`. В Linux/macOS можно проверить аналогично командой `test -f <путь>`.

**Проверка Б — целостность поставляемого контекста.** Из корня `skills-pipeline`:

```bash
python -X utf8 tools/validate_context.py
```

Понадобятся Python и PyYAML (`python -m pip install pyyaml`, если модуль отсутствует). Ожидаемый результат: `"status": "passed"` и пустой массив `errors`. При необходимости `--write-report` создаёт локальный отчёт, который не нужно коммитить.

Важно: **этот валидатор проверяет файлы комплекта, но сам по себе не подтверждает, что GigaCode прочитал пользовательский registry и selector**.

**Проверка В — загрузка внутри GigaCode.** После установки начни новую сессию или выполни `/clear` в рабочем проекте с `product-context.yaml`. Спроси:

> Работаем с продуктом NORM. Проверь выбранный `context_id`, `provider.root`, manifest и открой полное описание сервиса «Меры». Кратко назови его источник истины для AS IS, один подтверждённый маршрут согласования и два открытых вопроса со ссылкой на документы.

Успешная проверка — агент **действительно открыл файлы** по указанному provider и может назвать их пути/разделы. Одной фразы «контекст подключён» недостаточно.

### Частые ошибки

| Симптом | Что проверить |
|---|---|
| `BLOCKED_BY_CONTEXT` или manifest не найден | Существует ли `provider.root`, указывает ли он на **`context/`**, доступен ли `product-system/context-manifest.yaml` внутри него |
| GigaCode не находит NORM | Файл должен называться `product-contexts.yaml` **без** `.example`; ключ `contexts.norm` должен существовать |
| Агент спрашивает контекст каждый раз | Находишься ли ты в нужном рабочем проекте и существует ли там `.gigacode/product-context.yaml` с `context_id: norm` |
| Контекст найден, но документы «Мер» игнорируются | Проверь `measures.primary_document` в `service_registry.yaml` и попроси открыть полный `measures.md` |
| YAML перестал читаться | Проверь отступы пробелами, кавычки у путей и отсутствие буквальных `<примеров>` |
| У разных проектов разные контексты | Это нормально: общий user-level registry хранит **все** providers, а каждый проект выбирает свой `context_id` |

