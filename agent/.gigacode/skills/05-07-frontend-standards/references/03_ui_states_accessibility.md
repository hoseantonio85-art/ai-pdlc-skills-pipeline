# UI Kit, states and accessibility

## UI Kit hierarchy

Для реализации опирайся на проверенный целевой репозиторий и выбранный внешний UI Kit; внутренние имена и версии в публичном комплекте отсутствуют.
2. Существующий target adapter.
3. Новый узкий adapter только при подтверждённом несовпадении API.

Для реализации опирайся на проверенный целевой репозиторий и выбранный внешний UI Kit; внутренние имена и версии в публичном комплекте отсутствуют.

## Layout/styles/tokens

- `Row/Col` — основной layout pattern, если он принят target; технический `div` допустим.
- `Text/Title` предпочтительны, когда подходят фактическому API.
- Свои стили colocate в непустом импортированном `styles.module.scss`.
- Не создавай style/type/barrel files только ради структуры.
- Global styles — только app/provider theme/reset.
- Inline style допустим для динамической geometry, не для цвета.

Цвета только из:
- semantic props UI Kit;
- существующих CSS variables target theme;
- `transparent`, `currentColor`, `inherit` при семантической необходимости.

Запрещены hardcoded `hex/rgb/hsl/oklch`, named colors, local palettes и fallback `var(--token, #fff)`.

## i18n/domain ids

- весь новый пользовательский текст находится в i18n;
- stable id, enum, API/store value не зависят от localized label;
- presentation boundary мапит id → translation key/tone/icon;
- company names, INN, договоры, даты, comments — runtime/mock data, а не translation resources;
- legacy hardcoded text вне scope — recommendation, не автоматический blocker.

## Сценарии и async

Реализуй только релевантные SDD/UX состояния, но не теряй обязательные:
`default/success`, `loading/refreshing`, `empty`, `recoverable error/retry`, `validation`, `disabled/pending`, modal/drawer lifecycle, optimistic outcome — когда они описаны или следуют из фактического async flow.

- network + NORMalization живут в service/store/domain layer;
- page оркестрирует, presentational component не знает transport details;
- async action имеет явные pending/success/error transitions;
- pending блокирует повторный submit/click, если concurrency не задумана;
- pending сбрасывается в `finally` или одном store transition;
- floating promises и silently swallowed errors запрещены;
- stale-response risk → target pattern cancellation/request id;
- `ErrorBoundary` не заменяет request error state/retry/notification;
- технические ошибки, secrets и персональные данные не выводятся пользователю/в небезопасные logs.

## Accessibility

- используй native `button/a/input/label` или semantic UI Kit component;
- `div/span` не имитируют action без keyboard handling, focus и accessible name;
- icon-only action получает accessible name из i18n;
- ключевые действия доступны с клавиатуры и имеют visible focus;
- modal/drawer использует target focus management + Escape behavior;
- field связан с label/hint/error; ошибка не выражается только цветом;
- pending/disabled state выражен визуально и семантически.

Недоступное новое ключевое действие — blocker.
