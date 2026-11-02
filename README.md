# AI PDLC Skills Pipeline · NORM · v8.0

Это **полный продуктовый контекст, восстановленный напрямую из базовой 7.0.3**, не упрощённая реконструкция. Изменены только номера скиллов, внешний evidence, признаки компании/персональные примеры и актуальные решения Drawer. Добавлен PO-скилл `00-capture-product-service-context`.

**v8.0:** выпуск без изменения stage API и состава пайплайна; добавлены правила не переносить персональные данные из источников в документы описания сервисов. Шаблон описания сервиса по-прежнему содержит 13 разделов (0–12), используется вместе с реестром вопросов/решений. Базовая 7.0.3 сохранена как исторический источник.

## Устройство

- `agent/.gigacode/skills` — семь пронумерованных скиллов (00 / 01 / 02 / 03 / 03-5 / 04 / 05-07); `agent/.gigacode/agents` — Planner, Implementer, Reviewer.
- `context/product-system/01_foundation` — цель и философия; `02_domain/services` — **14 описаний сервисов**, включая подробные Меры; `03_ux` — UX; `04_ui` — поведение, паттерны, словари UI Kit, HTML-starter и сцены; `02_domain/registry` — роли/capabilities/решения/глоссарий/источники.
- `context/product-system/05_engineering` — **оригинальные подробные frontend-нормативы** (до глобальной чистки), доступны только на 05–07.
- `tools/validate_context.py` — исходный строгий валидатор + локальные проверки.
- Картинок, логотипов, OpenSpec, аналитических технических спецификаций, UI Kit code package, исходных репозиториев и истории Git здесь **нет**. Нет внешних действующих URL/адресов.

[Подробная установка для Windows/macOS/Linux и диагностика](docs/INSTALLATION.md)

## Установка в GigaCode

1. Скопируй содержимое `agent/.gigacode/skills/` в `~/.gigacode/skills/`, а `agent/.gigacode/agents/` — в `~/.gigacode/agents/`. Не смешивай со старыми дублями: старые одноимённые скиллы без префиксов лучше удалить/отключить перед новым smoke test.
2. Размести `context/` в постоянном месте вне frontend-проекта.
3. Из `agent/.gigacode/product-contexts.yaml.example` создай `~/.gigacode/product-contexts.yaml` с **абсолютным** `contexts.norm.provider.root` на каталог `context/` и `manifest: product-system/context-manifest.yaml`.
4. Для целевого репозитория создай `<project>/.gigacode/product-context.yaml` из шаблона (`context_id: norm`).
5. Дополнительные OpenSpec, аналитические документы, UI Kit, frontend/backend репозитории и изображения подключаются локально/по разрешённой ссылке **через `~/.gigacode/product-evidence.yaml`**. Пример — `agent/.gigacode/product-evidence.yaml.example`. Не коммитить конфиг с действующими корпоративными путями.
6. Проверка: `python -X utf8 tools/validate_context.py`. Нужен PyYAML: `python -m pip install pyyaml`. Затем новая сессия GigaCode и тест на чтение `context-manifest.yaml`.

## Истина о внешних источниках

Встроенная бизнес-модель сохраняет исторические факты, сценарии и вопросы из исходной 7.0.3. Но удалённые OpenSpec и source репозитории **не доступны автоматически**. Manifest и реестры не должны выдавать ссылку из YAML за прочитанный документ. Указанный source подключается только после проверки доступности и текущей версии. Для frontend-инженерии реальная структура target repo и экспорты установленного UI Kit проверяются по фактической среде.

## AI PDLC

`00` Product service context → `01` Intent/Brief → `02` UX Solution → `03` HTML Prototype → `03.5` UX Sync → `04` Product SDD → `05` Frontend Planning → `06` Implementation → `07` Review.

Stage 01–04 — скиллы и соответствующие контекстные профили, инженерные 05–07 — три субагента с `05-07-frontend-standards` и **полными** `product-system/05_engineering/*` из 7.0.3.

Drawer: исходная большая спецификация сохранена полностью и снабжена актуальным нормативным override NORM/ORM, без потери старых иллюстративных схем.

## Важные ограничения

Это статически проверяемый комплект; проверка действительного чтения агентом и production frontend build производится в GigaCode на рабочем компьютере. Для открытой публикации содержательного контекста организации требуется локальное согласование ИБ/прав, если это предусмотрено политиками.
