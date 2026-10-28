# UX Quality Checklist

## 1. Input Gate

- [ ] Есть Product Task Brief.
- [ ] Проблема сформулирована без UI-решения.
- [ ] Понятен основной пользователь.
- [ ] Понятен ожидаемый результат.
- [ ] Scope и out of scope зафиксированы.
- [ ] Критичные бизнес-правила известны или вынесены как blocker.
- [ ] Вход имеет допустимый статус.

## 2. Context Gate

### Existing product / selected context

- [ ] Context ID выбран явно или настройкой.
- [ ] Provider проверен.
- [ ] Manifest прочитан.
- [ ] Revision зафиксирована.
- [ ] Foundation прочитан.
- [ ] Service map прочитан.
- [ ] Релевантные service documents прочитаны.
- [ ] UX principles прочитаны.
- [ ] UX patterns прочитаны.
- [ ] Compact pattern registry / adaptation policy прочитаны, если доступны.
- [ ] Known constraints учтены.
- [ ] Ограничения контекста указаны.

### Explicit `context_id: none`

- [ ] Product owner подтвердил автономную/greenfield инициативу.
- [ ] Не утверждаются существующие capabilities, service boundaries или business rules без источника.
- [ ] Отсутствие AS IS/product evidence явно обозначено.
- [ ] UX можно определить по Intent/Brief без выдумывания критичной product/domain semantics.

## 3. Current Product Gate

Для existing-product задачи:

- [ ] AS IS исследован.
- [ ] Evidence текущего продукта указано.
- [ ] Составлена continuity map.
- [ ] Легаси не перенесено автоматически.
- [ ] Неизвестные части отмечены.
- [ ] Решение не дублирует известную capability без объяснения.

Для автономной/greenfield инициативы вместо этого:

- [ ] Зафиксирован режим `target-state-by-choice` / отсутствие существующего AS IS.
- [ ] Не создаётся фиктивная continuity map или production evidence.

## 4. UX Logic

- [ ] UX-задача соответствует brief.
- [ ] Определён центр сценария.
- [ ] Определены сущности и связи.
- [ ] Определены данные для принятия решения.
- [ ] Happy path завершён.
- [ ] Ключевые развилки описаны.
- [ ] Нет лишних промежуточных шагов.
- [ ] Понятна точка завершения.
- [ ] Feedback присутствует после значимых действий.

## 5. Information Architecture

- [ ] Определён главный сигнал.
- [ ] Summary идёт до деталей.
- [ ] Приоритет данных объяснён.
- [ ] Content и meta разделены.
- [ ] Прогрессивное раскрытие обосновано.
- [ ] Пользователь не обязан вручную собирать вывод.
- [ ] Для registry/monitoring page явно решено, нужен ли situational overview/interactive analytics; bare list не выбран механически.
- [ ] Если есть analytics, определены aggregate question и путь к detailed layer / filter / action.
- [ ] Связанные сущности показаны только если влияют на решение.

## 6. Interaction Architecture

- [ ] Каждый surface имеет назначение.
- [ ] Page/modal/drawer выбран по намерению.
- [ ] Drawer не используется для полного просмотра объекта.
- [ ] Modal не используется для лёгкого вспомогательного шага.
- [ ] Переходы и возвраты понятны.
- [ ] Пользователь не теряет контекст без необходимости.
- [ ] Действия расположены логически, не декоративно.

## 7. States and Edge Cases

- [ ] Loading.
- [ ] Empty.
- [ ] Error.
- [ ] Partial/stale data.
- [ ] No access.
- [ ] Action progress/success/failure.
- [ ] Conflict/change by another actor.
- [ ] Terminal state.
- [ ] Критичные edge cases.
- [ ] Нет тупиковых состояний.

## 8. AI Gate

- [ ] AI имеет конкретный контекст.
- [ ] AI добавляет ценность.
- [ ] Входные данные AI понятны.
- [ ] Неопределённость обозначена.
- [ ] Финальное решение остаётся у человека.
- [ ] Есть сценарий несогласия.
- [ ] Есть fallback без AI.
- [ ] AI не дублирует очевидный UI.

## 9. Traceability and Handoff

- [ ] Каждая цель brief связана с UX.
- [ ] Открытые вопросы не скрыты.
- [ ] Assumptions документированы.
- [ ] UX acceptance criteria наблюдаемы.
- [ ] Handoff покрывает surfaces, actions, states и transitions.
- [ ] Следующий этап не должен заново изобретать flow.
- [ ] Adaptation/new pattern candidate явно обозначен и обоснован, если существующего pattern недостаточно.

## 10. UX/UI Boundary

- [ ] Нет макета.
- [ ] Нет wireframe.
- [ ] Нет цветов.
- [ ] Нет точных размеров.
- [ ] Нет визуальных токенов.
- [ ] Нет UI Kit component mapping.
- [ ] Нет HTML/CSS/React-кода.
- [ ] Нет Lovable prompt.
- [ ] Нет готового прототипа.

## Blockers

Результат не может получить `READY_FOR_PROTOTYPE`, если:

- вход не утверждён;
- основной пользователь неизвестен;
- центральное решение неизвестно;
- отсутствует основной flow;
- критичные сущности или данные неизвестны;
- неизвестное бизнес-правило меняет сценарий;
- для existing-product задачи недоступен обязательный product context или AS IS, влияющий на flow;
- есть необработанный критичный edge case;
- нарушена traceability;
- решение подменено макетом или кодом;
- владелец не подтвердил результат.

## Verdict

Используй только статусы Stage 02 из `references/pipeline-status-contracts.md`:

### `READY_FOR_PROTOTYPE`

Все blockers закрыты; UX Solution достаточно определено для Stage 03.

### `NEEDS_UX_DECISION`

Не определена критичная UX/product/object semantics, которую нельзя безопасно оставить следующему этапу.

### `NEEDS_PRODUCT_ALIGNMENT`

Intent и Brief расходятся по outcome, scope или guardrails.

### `BLOCKED_BY_CONTEXT`

Для существующего продукта недоступен обязательный источник/контекст, без которого UX пришлось бы выдумывать.
