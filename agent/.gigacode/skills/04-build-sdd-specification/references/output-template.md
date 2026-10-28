# Product SDD / Delta Specification — шаблон

## Metadata and status

## 1. Intent trace

- Intent:
- Why Now:
- Expected improvement:
- Success criteria covered:

Не копировать весь Intent; дать ссылки и краткую traceability.

## 2. Scope and actors

## 3. States and transitions

Только предметные/user-visible состояния и переходы. Не использовать DTO/DB/API naming как нормативный язык.

## 4. User stories and scenarios

Каждый сценарий должен быть самостоятельным и понятным без прототипа.

### SCN-01 — <название через пользовательский результат>

- Actor and preconditions:
- Trigger:
- Main flow:
- Alternatives:
- Result:
- Sources:

## 5. Business rules and permissions

| ID | Rule | Source | Status |
|---|---|---|---|
| BR-01 | | | confirmed / TBD |

Использовать business vocabulary. Permission фиксировать только если он меняет доступное поведение.

## 6. Acceptance criteria

### AC-01 — <результат>

```gherkin
Given <подтверждённое состояние>
When <действие или событие>
Then <наблюдаемый результат системы>
And <наблюдаемый результат для пользователя>
```

## 7. Error and edge-case matrix

| ID | Condition / error | System reaction | User-visible result | Recovery / next step | Source/status |
|---|---|---|---|---|---|
| ERR-01 | | | | | |

## 8. Consistency and invariants

Только наблюдаемое поведение: что должно сохраняться, не теряться, не дублироваться и не перезаписываться молча. Не описывать storage/concurrency mechanism.

## 9. Constraints, dependencies and assumptions

Технические вопросы, не влияющие на продуктовую семантику, помечать как `engineering dependency/reference`, а не проектировать внутри SDD.

## 10. Non-functional product requirements

Только подтверждённые и наблюдаемые требования (например, доступность ключевого действия, timeout/recovery expectation, аудит как бизнес-требование). Не выбирать технический механизм.

## 11. Traceability

| Requirement | Intent/Brief | UX decision | Prototype evidence | Domain/analytical evidence | Status |
|---|---|---|---|---|---|

## 12. Open questions and owners

Разделять `product/domain question` и `engineering dependency`.

## 13. Review and approval
