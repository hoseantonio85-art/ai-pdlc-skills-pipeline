---
name: 03-5-sync-ux-decisions
description: >-
  Синхронизирует UX Solution после проверки HTML-прототипа: финализирует UX-решения, фиксирует подтверждённые deviations и создаёт approval handoff перед SDD. Используй после human UX/UI review stage 03. Не изменяет Business Intent, не превращает prototype implementation в production contract и не пишет SDD.
---

# Sync UX Decisions

## Вход

- `00_intent.md` — только outcome/priority guardrail;
- `01_product_brief.md` — product truth;
- `02_ux_solution.md`;
- `03_visual_prototype.md` и запускаемый прототип;
- feedback/approval владельца UX или продукта.

Без явного результата review разрешён только статус `NEEDS_UX_REVIEW`.

## Процесс

1. Сопоставь финальный UX Solution с фактически проверенными сценариями прототипа.
2. Классифицируй различия как `approved deviation`, `prototype defect`, `unresolved decision` или `implementation-only detail`.
3. Обнови `02_ux_solution.md` только по подтверждённым UX-решениям.
4. Если для capability доступны analytical specs, выборочно проверь approved UX на domain conflicts и пропущенные user-visible states/permissions/errors. Не переносить implementation details.
5. Сохрани `03_5_ux_sync.md` по `references/output-contract.md`.
6. Не меняй `00_intent.md`. Если review выявил изменение outcome, Why Now, успеха или guardrails, верни `REQUIRES_INTENT_REVIEW` и останови handoff.

## Границы

- Prototype — UX evidence, а не production contract.
- Не переносить DOM/CSS/JavaScript structure, mock fields, variable names или demo shortcuts в требования.
- Не добавлять GWT, API, DTO/DB schema или technical design.
- Analytical specs использовать только как consistency check: lifecycle, permissions, business rules, errors и user-visible states. При конфликте возвращать `NEEDS_UX_DECISION` или продуктовый вопрос, а не молча адаптировать UX.
- Не исправлять Product Brief молча; продуктовые расхождения возвращать владельцу.

## Статусы

- `READY_FOR_SDD` — UX Solution финализирован, прототип approved, deviations зафиксированы.
- `NEEDS_UX_REVIEW` — отсутствует явное approval.
- `NEEDS_UX_DECISION` — критичное UX-расхождение не решено.
- `REQUIRES_INTENT_REVIEW` — найдено изменение business Intent.

