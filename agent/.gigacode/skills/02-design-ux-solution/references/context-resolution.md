# Разрешение контекста для UX-решения

## 1. Общий принцип

Skill универсален. Продуктовые знания находятся вне skill.

Используй:

```text
~/.gigacode/product-contexts.yaml
```

и manifest выбранного контекста.

## 2. Порядок выбора

1. Явный context ID пользователя.
2. Контекст, уже выбранный в текущей задаче.
3. `.gigacode/product-context.yaml`.
4. User registry.
5. Вопрос пользователю.

Вопрос:

```text
Какой продуктовый контекст использовать для UX-решения?

1. norm
2. orm
3. без контекста
```

## 3. Проверка local repository

Проверь:

- `provider.root`;
- существование директории;
- manifest;
- совпадение context ID;
- status;
- обязательные документы;
- git branch и revision, если доступны.

## 4. UX loading profile

Если manifest содержит:

```yaml
loading:
  for_ux_solution:
```

используй этот профиль.

Ожидаемые логические группы:

- context status;
- source authority;
- product foundation;
- service map;
- relevant service documents;
- roles;
- business rules;
- known capabilities;
- released features;
- constraints;
- UX principles;
- UX patterns;
- compact UI pattern registry, если доступен;
- current product state;
- current product sources.

Если группы отсутствуют, используй доступные эквиваленты и зафиксируй пробел.

## 5. Что читать всегда

- status и ограничения контекста;
- source authority;
- Product Task Brief;
- foundation;
- service map;
- UX principles;
- UX patterns.

## 6. Что читать по необходимости

- описание затронутого сервиса;
- связанные сервисы;
- роли;
- бизнес-правила;
- capabilities;
- релизы;
- текущий продукт;
- full UI pattern authoring specs при спорном выборе surface;
- аналитика;
- codebase;
- screenshots.

Не загружай все сервисы и весь код без необходимости.

## 7. Что не читать на UX-этапе по умолчанию

- UI Kit documentation;
- Storybook;
- design tokens;
- UI component props;
- Lovable prompt template;
- frontend implementation rules.

Исключение: только если источник нужен для проверки реального текущего поведения,
а не для UI mapping.

## 8. Confluence в будущем

Для `confluence_mcp` получи:

- каноническую корневую страницу;
- UX principles;
- service pages;
- current behavior pages;
- page IDs;
- version или last updated.

Не считай страницу актуальной только по названию.

## 8.5. Явный режим без контекста

Если пользователь явно выбрал `none`, не пытайся подменять его NORM или соседним repository. Для автономной/greenfield инициативы UX может продолжаться по Intent/Brief при owner approval. Для изменения существующего продукта отсутствие обязательного product evidence остаётся `BLOCKED_BY_CONTEXT`.

## 9. Если контекст частичный

Продолжай, если можно построить логически безопасный flow.

Обязательно:

- указать `context_status: partial`;
- разделить подтверждённое и предполагаемое;
- вынести пробелы;
- ограничить финальный статус.

## 10. Фиксация в результате

Запиши:

```text
context_id
context_provider
context_status
context_manifest
context_revision
context_checked_at
current_product_evidence_status
```
