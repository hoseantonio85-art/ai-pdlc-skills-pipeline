# Compact UI rules for prototype stage

## 1. Не перепроектировать UX молча, но не копировать шаблон механически

`02_ux_solution.md` определяет flow, surfaces, information hierarchy, actions и states. Этап 03 выбирает визуальную композицию и может адаптировать existing pattern, если это улучшает утверждённый сценарий и не меняет business semantics.

Patterns — strong defaults. Canonical surface behavior и product invariants — constraints. HTML references/screenshots — visual evidence. Если нужна новая композиция, зафиксируй rationale и класс `composition-adaptation` / `new-pattern-candidate` в handoff.

## 2. Управлять вниманием

- сначала главный вопрос, сигнал и summary;
- затем причины, связи и детали;
- приоритет важнее полноты;
- сложное раскрывается прогрессивно;
- интерфейс должен вести к следующему действию.

## 3. Surface roles

- page — обзор, список и продолжительная работа;
- object modal — полный просмотр объекта, фокус и решение;
- drawer — короткий вспомогательный шаг без потери контекста;
- action modal — подтверждение или критическое действие.

Не открывайте полный объект в drawer и не делайте drawer обязательной остановкой перед object modal.

## 4. Действия

- page-level primary actions следуют утверждённому page pattern;
- Object View: object-level actions находятся в единой правой action/meta zone, общий footer отсутствует;
- Object Create/Edit: completion actions находятся в fixed footer;
- primary action не дублируется без причины;
- destructive action визуально и смыслово отделяется;
- результат значимого действия всегда имеет feedback.

## 5. Состояния

Для применимых surfaces реализуйте default/success, loading, empty, recoverable error, disabled/pending, validation и action success/failure. Empty и error states должны объяснять следующий шаг.

## 6. Situational overview / analytics

На registry и monitoring surfaces не ограничивайся карточками автоматически. Явно проверь, можно ли быстрее объяснить ситуацию через aggregate, distribution, trend, concentration, coverage, matrix/heatmap или другой meaningful visual. Если да — добавь компактный analytical layer и свяжи его с detailed list через понятный drill-down/filter/highlight. Если нет — оставь список без декоративного dashboard.

Placement зависит от scope фильтров: analytics может быть после controls, если делит с list один query state, либо до list controls, если показывает общий domain overview.

## 6. AI blocks

AI объясняет ситуацию, основания и рекомендуемое действие. Он не является декоративным баннером и не дублирует данные без новой ценности.

## 7. Visual language

Используйте продуктовый UI Kit и tokens. Не создавайте новую палитру, новую типографику или случайный dashboard-style. Минимализм достигается иерархией, spacing и точностью, а не отсутствием содержания.

Подробные основания находятся в `product-system/03_ux/ux_principles.md` и `ux_patterns.md`; stage 03 читает только релевантные разделы при споре.
