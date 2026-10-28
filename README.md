# AI PDLC Skills Pipeline — NORM

**Полный продуктовый контекст NORM + GigaCode-скиллы и субагенты.** Репозиторий содержит 14 описаний сервисов, 56 capabilities, 7 скиллов, 3 субагента, UX/UI-паттерны и полноценный локальный HTML-starter. Внешние технические источники подключаются через персональные YAML-настройки; история исследования не приравнивается к текущему production.

## Что внутри

```text
ai-pdlc-skills-pipeline/
├── agent/.gigacode/
│   ├── skills/
│   │   ├── 00-capture-product-service-context/  # создание бизнес-описаний сервисов
│   │   ├── 01-formulate-product-intent-and-brief/
│   │   ├── 02-design-ux-solution/
│   │   ├── 03-build-visual-html-prototype/
│   │   ├── 03-5-sync-ux-decisions/
│   │   ├── 04-build-sdd-specification/
│   │   └── 05-07-frontend-standards/
│   ├── agents/                          # 3 frontend-субагента
│   ├── product-contexts.yaml.example
│   ├── product-context.yaml.example
│   └── product-evidence.yaml.example
├── context/
│   ├── product-system/
│   │   ├── 01_foundation/               # цели, философия продукта
│   │   ├── 02_domain/services/         # 14 сервисов + карта
│   │   ├── 02_domain/registry/         # 56 capabilities, 12 ролевых профилей, Q/R
│   │   ├── 03_ux/                     # UX-правила
│   │   ├── 04_ui/                     # foundation, patterns, runtime, visual, organisms, starter
│   │   ├── 05_external/               # политика внешних источников
│   │   ├── 06_engineering/            # полные frontend-нормативы stages 05–07
│   │   └── context-manifest.yaml
│   └── tools/validate_context.py
└── README.md
```

В отличие от демонстрационного публичного кандидата, здесь сохранены **содержательные бизнес-описания** реестра рисков, анализа, лимитной кампании, событий, мер, AI-агентов, продуктов, контрагентов, справочников, документов, мониторинга, ассистента и платформенных областей. Особое внимание — **`measures.md`** (разделы 0–12) и **`measures_questions.md`** (исторические Q/R и противоречия).

**Полный NORM HTML-starter восстановлен.** Теперь в `context/product-system/04_ui/starter/` и в fallback скилла `agent/.gigacode/skills/03-build-visual-html-prototype/assets/norm-html-starter/` лежат одинаковые 7 файлов HTML/CSS/JS/SVG (два сценария: события и история AI-запусков; запусти `index.html` либо `index.html?scenario=ai`). Сохранены логотипы, палитра, компонентные стили, карточки, фильтры, Object Modal, Drawer, action dock, состояния и интерактивное поведение. Личные имена и пример инцидента заменены на синтетические. **Drawer не закрывается по Escape по умолчанию**, Modal/Form — закрываются. Стартер не является реальным UI Kit, внешние API не использует.

В `04_ui/patterns/specs/` сохранены **дизайн-спецификации паттернов** (Drawer/Modal): это рабочие правила интерфейса, **не** внешние OpenSpec. Правила Drawer синхронизированы с поздними решениями: отдельные темы NORM/ORM, отсутствие технического лимита в два Drawer, Escape по умолчанию выключен.

## Установка GigaCode

**1. Скиллы и агенты.** Скопируйте содержимое `agent/.gigacode/skills/` в `~/.gigacode/skills/`, а `.md` из `agent/.gigacode/agents/` — в `~/.gigacode/agents/`. Не удаляйте другие навыки. Старые версии тех же навыков без префикса временно отключите, чтобы не получить два конкурирующих варианта.

**2. Контекст.** Оставьте `context/` в стабильном месте (например, `D:/AI/ai-pdlc-skills-pipeline/context`). Не копируйте всю папку в каждый frontend-проект.

**3. Пользовательский реестр.** Создайте `~/.gigacode/product-contexts.yaml` по шаблону `agent/.gigacode/product-contexts.yaml.example`:

```yaml
contexts:
  norm:
    status: ready
    provider:
      type: local_repository
      root: "D:/AI/ai-pdlc-skills-pipeline/context"  # свой абсолютный путь
      manifest: "product-system/context-manifest.yaml"
```

**4. Селектор проекта.** В рабочем проекте создайте `<project>/.gigacode/product-context.yaml` по одноимённому `.example`:

```yaml
version: 1
context_id: norm
```

**5. Внешние источники — отдельный YAML.** Из `agent/.gigacode/product-evidence.yaml.example` создайте **локально** `~/.gigacode/product-evidence.yaml`. Здесь можно указать как абсолютные пути на компьютере, так и разрешённые ссылки:

```yaml
schema_version: 1
products:
  norm:
    specifications:
      local_root: "D:/WORK/approved-specifications"
      index_url: ""       # опциональный разрешённый URL
    ui_kit:
      package_path: "D:/WORK/approved-ui-kit"
      docs_root: ""
      docs_url: ""        # опциональный разрешённый URL
    repositories:
      frontend_root: ""  # только если доступ разрешён
      backend_root: ""
    design_references:
      local_root: ""     # одобренные визуальные референсы
      index_url: ""
    frontend_rules:
      local_root: ""     # доп. разрешённые engineering-правила
      index_url: ""
      toolchain_root: "" # фактические TS/Biome baseline
```

В настоящем распространяемом пакете **не должно быть заполненных внутренних путей и URL**. Секреты/токены нельзя класть в YAML вообще. Путь не гарантирует доступ: GigaCode должен проверить файл, права, версию и действительно прочитать релевантный источник. При отсутствии источника — `NEEDS_SOURCE` или `BLOCKED_BY_SOURCE`.

## Как использовать

`00-capture-product-service-context` — **дополнительный скилл до Stage 01**, не новый этап создания фичи. Помогает PO описать существующий сервис по 13 разделам (0–12), ведёт отдельный реестр вопросов и решений, не обновляет контекст без отдельного согласованного handoff. Встроенные примеры обезличены.

Основной цикл остался прежним: **01 Intent/Brief → 02 UX Solution → 03 HTML Prototype → 03.5 UX Sync → 04 SDD → 05 Frontend Plan → 06 Implementation → 07 Review**. `05-07-frontend-standards` используется инженерными субагентами на этапах 05–07.

Контекст читается из manifest **избирательно**: `always` + профиль текущего этапа + нужный сервис/UI-паттерн. Для «Мер» обязательны **полное описание** и **реестр вопросов**; `service_registry.yaml` только указывает путь.

## Проверка

Из корня сборки:

```bash
python -X utf8 context/tools/validate_context.py
```

Требуется Python и PyYAML (`python -m pip install pyyaml`). После установки начните новую сессию GigaCode или `/clear`. Проверочный запрос:

> Используй контекст NORM. Назови прочитанный manifest и путь к `product-system/02_domain/services/measures.md`. Открой его и `product-system/02_domain/registry/measures_questions.md`. Покажи основные роли, два этапа согласования и три открытых вопроса. Отдели исторические сведения от новых фактов, подтверждённых внешними источниками.

**Важная граница:** источник может быть упомянут в документе, но не доступен в этой копии. Нельзя автоматически считать ранее изученный код актуальной реализацией и обещать точные права, API, формулы или релиз без новой проверки.

## Что исключено и почему

Нет встроенных исходников, OpenSpec/аналитических спецификаций, корпоративного пакета UI Kit, внешних корпоративных HTML-выгрузок, скриншотов, ZIP/TGZ, `.git`, внутренних адресов и имён репозиториев. **Исключение:** сохранены два SVG-логотипа в составе исходного локального HTML-starter по решению владельца материалов (права на публичное распространение отдельно проверить). Поиск названий организации и технических указателей произведён, но **это не сертификация безопасности**.

**Область публикации:** бизнес-модель и UX/UI-правила включены в открытый репозиторий по решению владельца комплекта. Из состава исключены встроенные исходные репозитории, OpenSpec, аналитические технические спецификации, курсы и корпоративные адреса. Статическая проверка не заменяет формальное согласование ИБ и прав на используемые фирменные SVG.

## Аудит восстановления от 28.10.2026

Дополнительно восстановлены: подробный Stage 03 skill, все 15 aspect-level UI reference entries, семантические роли и связи сервисов в registry, `current_product_sources.yaml`, `ui_sources.yaml`, подробные варианты содержимого Drawer и единая навигация по бизнес-контексту. Внешние исходники не копировались.


Перед переносом восстановлены критически потерянные маршруты: `composition-index.json`, `pattern-registry.yaml` с областью ответственности, `organism-registry.yaml` с составом, `reference-registry.yaml` с флагом внешних источников, stage/skill matrix, status/release/source guards и compact UI/engineering rules. Расширена карта сервисов сквозными сценариями. **Полные внутренние OpenSpec, репозитории, UI Kit и приватные HTML-референсы намеренно не копировались.**

Точность функционального Stage 03 с новым composition index нужно отдельно проверить в GigaCode. `validate_context.py` проверяет локальные маршруты, но не подтверждает готовность внешних источников.

**Один репозиторий — полный контекст и pipeline.** Для рабочего использования подключай разрешённые внешние источники только через локальный `~/.gigacode/product-evidence.yaml`; реальные пути, URL и секреты не коммить.

## Исторический контекст ≠ реальные инциденты клиентов

Термин «исторический» здесь означает описанную по предоставленным материалам модель и результаты технического исследования **снимка на 23.10.2026**, не подтверждённый реальный пользовательский инцидент или факт production. Утверждения `[HISTORICAL-AS-IS]` необходимо повторно сверить с одобренными локальными источниками.

## Дополнительные локальные визуальные сцены

Вернул две **синтетические standalone HTML-иллюстрации** из исходного контекста: `04_ui/references/html/norm-vertical-slice/index.html` и `04_ui/references/html/situational-overview/index.html`. Они дополняют полноценный starter, но не являются исходниками frontend-репозиториев, реальными инцидентами или нормативным HTML/API. Клик/данные в них не должны переопределять актуальную спецификацию Drawer.

## Frontend Standards · восстановление нормы

Скилл `05-07-frontend-standards` и три субагента теперь читают из выбранного context manifest два **встроенных** документа в `context/product-system/06_engineering/`: полный инженерный стандарт и компонентный/preview-handoff стандарт. Эти документы загружаются **только на stages 05–07**, а не при Intent/UX/HTML prototype/SDD. Реальные имена frontend repos, config packages, версии и UI Kit exports не вшиты в репозиторий — должны быть проверены в target repo и при необходимости подключены через опциональный `frontend_rules` в персональном YAML.
