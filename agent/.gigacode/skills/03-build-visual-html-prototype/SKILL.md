---
name: 03-build-visual-html-prototype
description: Собирает быстрый интерактивный HTML/CSS/JS-прототип по утверждённым Intent, Product Brief и UX Solution, используя выбранный локальный продуктовый контекст и реально доступные UI-источники.
---

# Stage 03 — HTML prototype

## Preflight

1. Проверь `00_intent.md`, `01_product_brief.md`, `02_ux_solution.md` и их согласованные статусы. Не угадывай поведение из графических примеров.
2. Разреши `<project>/.gigacode/product-context.yaml` → `~/.gigacode/product-contexts.yaml` → `context-manifest.yaml`. Явный выбор пользователя имеет приоритет. Отсутствующий контекст или источник — `BLOCKED_BY_CONTEXT`/`NEEDS_SOURCE`.
3. Прочитай `for_visual_html_prototype` и релевантный UX/UI pattern. Профиль demo-контекста `sample_product` — **пример**, а не источник бизнес-истины.
4. При необходимости проверь UI Kit или реальный продуктовый репозиторий через `~/.gigacode/product-evidence.yaml`; не придумывай UI Kit API без источника. Не публикуй конфиденциальный код/токены.

## Output

- Скопируй `assets/sample-html-starter/` или используй `context/product-system/04_ui/starter/` как нейтральную стартовую основу.
- Создай запускаемый HTML/CSS/JS прототип (для проектной гипотезы, не production код). Реализуй все утверждённые пользовательские сценарии, состояния, фильтры, переходы и ошибочные случаи, если они определены.
- Допускаются композиционная адаптация и новая визуализация, если они не нарушают UX-инварианты.
- Проверь размер, прокрутку, действия, keyboard focus, responsive и loading/empty/error/success; при доступном браузере проверь визуально.
- Подготовь `03_visual_prototype.md` с source evidence, assumptions, UX deviations и оставшимися вопросами. Для непроверенных гипотез не утверждай production fidelity.

## Ограничения

Не копируй закрытые фирменные логотипы, внутренние UI-сцены, секреты, API keys или реальные данные пользователей в публичный starter. Не считать этот neutral demo эталоном любого продукта. Стандарты frontend-инженерии применяются на последующих стадиях.
