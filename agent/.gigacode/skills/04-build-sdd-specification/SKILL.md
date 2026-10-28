---
name: 04-build-sdd-specification
description: >-
  Создаёт product SDD/delta specification после UX Sync по Business Intent, Product Brief, финальному UX Solution, approved HTML-прототипу и релевантным domain constraints. Используй для формализации проверяемого поведения продукта: scenarios, GWT, states, business rules, permissions, errors, edge cases, constraints и traceability перед engineering. Не проектирует API, DTO, storage, frontend/backend architecture или implementation plan.
---

# Build Product SDD Specification

## Роль этапа

Stage 04 — последний продуктово-поведенческий gate перед engineering. Он отвечает на вопрос **«как система должна вести себя наблюдаемо»**, а не **«как это реализовать технически»**.

Документ должен быть достаточно точным для реализации и тестирования без прототипа, но не должен диктовать frontend/backend architecture, API shape, DTO, storage, concurrency mechanism, component/store decomposition или transport details.

## Обязательный вход

- `00_intent.md` — outcome и priority guardrails;
- `01_product_brief.md` — product truth;
- финальный `02_ux_solution.md`;
- `03_5_ux_sync.md` со статусом `READY_FOR_SDD`;
- approved `03_visual_prototype.md` и прототип как UX evidence;
- product context: стабильный домен, capabilities, constraints;
- analytical specs — только как **on-demand reference/evidence**, если они релевантны capability.

Если UX Sync не завершён, верни `BLOCKED_BY_UX_SYNC`. Если источник противоречив и конфликт влияет на требование, верни `CONFLICTING_SOURCES`.

## Source authority

1. Intent определяет зачем, ожидаемое улучшение, успех и guardrails.
2. Brief определяет продуктовую проблему, scope и подтверждённые business rules.
3. Final UX Solution + UX Sync определяют утверждённые пользовательские сценарии, states и interaction decisions.
4. Approved prototype подтверждает UX behavior и coverage, но не production implementation.
5. Product context подтверждает стабильные domain constraints.
6. Analytical specs подтверждают релевантные domain/system facts: lifecycle, permissions, business invariants, states, transitions, validation, errors и существующие capabilities. Они **не имеют права автоматически превращать implementation details в продуктовые требования**.
7. Repository/contracts могут использоваться engineering-этапом для implementation planning; Stage 04 обращается к ним только чтобы подтвердить существующий факт, если без него нельзя корректно сформулировать observable requirement.

Mock fields, variable names, endpoint names, DTO fields, DB columns, hardcoded limits, DOM structure, client store, internal class names и demo shortcuts не становятся requirements по факту присутствия в источнике.

## Analytical spec resolver

Не загружай все analytical specs.

1. Открой `product-system/05_external/source_policy.md`.
2. Определи 1–3 capability specs, непосредственно связанные со scope.
3. Проверь status. `unknown` — usable evidence with caution; `needs-review` — ненормативный источник без дополнительного подтверждения.
4. Извлекай только факты, влияющие на наблюдаемое поведение:
   - roles / permissions;
   - lifecycle, states и transitions;
   - доступные действия;
   - business validation и invariants;
   - async / error / retry behavior;
   - object relationships;
   - persistence semantics, только если она пользовательски наблюдаема (например, история не должна исчезать).
5. Игнорируй implementation-only details: API/DTO naming, DB/storage mechanics, Java/TS classes, topics, internal IDs, repository patterns, component/store design.
6. Технический факт преобразуй в product behavior. Например, version-field/optimistic locking → «система не должна молча перезаписывать более актуальные изменения».
7. При конфликте не выбирай удобную версию молча; зафиксируй source conflict.

## Процесс

1. Построй traceability от Intent и Brief к сценариям.
2. Опиши самостоятельные user stories/scenarios, понятные без прототипа.
3. Зафиксируй actors/permissions только там, где они меняют доступное пользователю поведение.
4. Сформулируй states и transitions предметными терминами.
5. Сформулируй acceptance criteria в Given/When/Then для observable outcomes и значимых business rules.
6. Создай error/edge-case matrix: `условие → реакция системы → что видит пользователь → восстановление/следующий шаг`.
7. Зафиксируй consistency/invariants только в наблюдаемой форме: что должно сохраниться, не потеряться, не дублироваться или не быть молча перезаписано.
8. Зафиксируй constraints, dependencies и unresolved questions. Технические неизвестные, не меняющие product behavior, передай как `engineering dependency`, не раскрывая implementation design.
9. Проверь непротиворечивость и traceability по `references/quality-checklist.md`.
10. Сохрани `04_sdd_specification.md` по `references/output-template.md`.

## Запрещено в Stage 04

Не проектируй и не нормируй:

- endpoint/method/URL и request-response contracts;
- DTO/schema/DB columns;
- storage technology и persistence implementation;
- React component/store/hook decomposition;
- backend classes/services/repositories;
- Kafka/topics/queues и transport topology;
- caching/locking/concurrency mechanism;
- package/library choices;
- implementation task breakdown.

Если подобная деталь встречается в analytical spec, используй её только для понимания ограничения и переведи в observable behavior либо передай как engineering reference.

## Статусы

- `READY_FOR_SPEC_REVIEW` — product SDD полна и требует review.
- `APPROVED_FOR_ENGINEERING` — продуктово-поведенческие requirements подтверждены; engineering может строить implementation plan.
- `NEEDS_PRODUCT_RULE` — отсутствует продуктовая/domain-семантика, без которой нельзя определить поведение.
- `BLOCKED_BY_UX_SYNC` — нет утверждённого UX handoff.
- `CONFLICTING_SOURCES` — source conflict влияет на requirement.
