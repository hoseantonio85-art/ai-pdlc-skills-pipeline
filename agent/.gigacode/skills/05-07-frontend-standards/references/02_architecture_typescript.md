# Architecture and TypeScript

## Базовые слои

Ориентир при наличии соответствующего pattern в target:

- `pages` — route-level composition и orchestration;
- `components` — переиспользуемые/составные UI-блоки;
- `stores` — state, actions, derived values и прикладная логика;
- `helpers` — чистые transformations, formatters, небольшие hooks;
- `services` — transport boundary, если слой принят target repo;
- `providers` — router, stores, auth, lazy integration;
- `i18n`, `openapi`, `assets`, `@types` — инфраструктурные области.

Правила:
- route-specific компоненты держи в `pages/<Page>/components`, если target следует этому pattern;
- не помещай business logic, большие mock arrays и visual configs в route-level JSX;
- generated OpenAPI types преобразуй в domain/view model, если UI иначе начинает зависеть от transport details;
- stable ids и business mappings не зависят от localized labels;
- внутренние импорты из `src` обычно через `@/`, локальные соседние — relative, если это соответствует target.

## Component boundaries

Типичный компонент: `ComponentName.tsx`, локальный `styles.module.scss` при наличии собственных стилей, `index.ts` и только реально нужные `types/helpers/components`.

Route-level компонент остаётся композицией. Файл >400 строк — обязательный review границ; blocker только если новый/изменённый файл реально смешивает независимые сценарии или слои.

### Props contract

- связанные поля сущности: именованная `item/model/viewModel`;
- избыточную API-модель сужай до view model или `Pick`;
- связанные UI state/actions можно группировать в `state/actions`;
- 1–2 callbacks, `className`, `children`, `testId`, mode prop оставляй явными;
- взаимоисключающие режимы — discriminated union, не boolean explosion;
- вариации содержимого — composition/children/slots;
- не пробрасывай props неизменными через несколько слоёв.

Сигналы review:
- 8+ собственных props → обязательный API review;
- >12 props в новом/существенно изменённом компоненте → blocker без обоснования;
- 3+ boolean mode flags → проверить boolean explosion;
- prop через 2+ промежуточных слоя → пересмотреть ownership/composition/context/store.

## React/state

- observable store consumer → `observer`, если это фактический pattern target;
- вычисления/normalization/repeated logic → store/helper;
- `useMemo/useCallback/React.memo` только при реальной причине (referential contract, dependency array, дорогая работа);
- не универсализируй одноразовый компонент «на будущее»;
- независимые user flows не объединяй в god-hook;
- удаляй dead imports/exports/files, созданные изменением.

## TypeScript

- Не используй `any` и `unknown`, если тип можно выразить domain/API type, generic, union, `Pick/Omit`, `Awaited`, `ReturnType`, `ComponentProps` или `satisfies`.
- Запрещены `as any`, `as unknown as T`, `Record<string, any>` и casts, скрывающие несовместимость.
- Не подавляй type errors через `@ts-ignore`, `@ts-nocheck` или ослабление strict/noUnused. `@ts-expect-error` допустим только для намеренного type-test с пояснением.
- Взаимоисключающие состояния моделируй discriminated union + exhaustive `never`.
- Public/exported contracts получают понятные типы; очевидные локальные значения оставляй inference.
- `!` и broad `as T` допустимы только при доказанном инварианте.

`unknown` допустим на реально динамической внешней границе (raw JSON, untyped third-party, `postMessage`, runtime config, caught error), но должен остаться внутри adapter/parser/type guard и быть сужен до конкретной модели до store/component.
