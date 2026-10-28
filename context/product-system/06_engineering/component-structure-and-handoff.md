# Component structure, data, public API, UI Kit and handoff

Статус: **canonical extension for engineering stages 05–07**. Восстановлены 11 разделов из прежнего подробного компонентного стандарта; примеры намеренно нейтральные. Для `TARGET_REPO` сначала проверяй conventions, затем применяй эту норму там, где она согласована с фактическим API и архитектурой. Обоснованные исключения фиксируй, а не переписывай чужой production без причины.

## 1. Target-first структура

Типичная продуктовая структура, если она подтверждена target/reference:

```text
src/
├── @types/                    # domain contracts
├── components/                # общие UI-компоненты
├── data/                      # fixtures/mock content
├── helpers/                   # чистые функции
├── i18n/                      # translation resources
├── pages/<Page>/components/   # screen-specific UI
├── providers/                 # router/auth/store wiring
├── services/                  # typed external boundary, если принят
├── stores/                    # состояние, actions, derived values
└── <entrypoint>.tsx           # согласно фактическому runtime
```

Не копируй структуру буквально, когда target использует другой принятый pattern. Не создавай пустые директории. Компоненты, используемые только одной страницей, не помещай в глобальный `src/components` без оснований.

## 2. `data` — runtime/fixture, не UI-конфигурация

Крупные демонстрационные списки (объекты, сотрудники, контракты, даты, тарифы, сценарии) находятся в `src/data` или принятом fixture layer, не внутри JSX. Используй синтетические данные в примерах.

Допустимо: stable identifiers, типизированный runtime content, status enums, mock timestamps. Недопустимо: CSS classes, JSX, handlers, colors, переводимые UI-labels. Пример:

```ts
export const sampleRecord = { id: 'rec-001', roleId: 'reviewer', status: 'active' } as const;
```

`status: 'active'` — доменное значение; текст «Активен» — перевод. Не используйте видимый перевод как id/guard.

## 3. `index.ts` как публичная граница компонента

Если **принят target convention** компонентных папок с barrel, каждая самостоятельная публичная папка имеет `index.ts`:

```text
components/RecordList/
├── RecordList.tsx
├── styles.module.scss   # только если реально нужны собственные стили
└── index.ts
```

```ts
// index.ts
export { RecordList } from './RecordList';
// consumer
import { RecordList } from '@/components/RecordList';
```

Не импортируй через глубокий implementation path, если у папки есть public API. Самостоятельный `index.ts` **не** считается бессмысленным re-export: он документирует component boundary. При этом не создавай промежуточных баррелей или facade, скрывающих внешние зависимости или обходящих target public exports. Если target сознательно не применяет barrels, не устраивай глобальную миграцию без engineering decision.

## 4. UI Kit без скрывающих адаптеров

Импортируй выбранный UI Kit напрямую из **фактически разрешённого package**. Имя пакета и версия не зашиты в распространяемый контекст: проверяй installed exports/types/props/icons/enums в target или `products.<id>.ui_kit` evidence. Не создавай `vendor/` с копией UI Kit, вторую базовую библиотеку или re-export `Button/Modal/...` через локальную оболочку.

Узкий adapter допустим для доказанного несовпадения конкретного API, с причиной и typed surface; не маскируй им запрет. UI Kit controls предпочтительны при наличии подходящего API. Native controls допустимы при отсутствии аналога и с доступной семантикой; технические `div`/wrapper/divider допустимы. Интерактивная карточка — button/link либо keyboard/focus/role/accessible-name contract согласно целевому паттерну, не `div onClick` без доступности.

## 5. Layout, типографика, стили

Если target использует `Row/Col`, `Text/Title`, предпочитай их когда подходит API. CSS Modules размещаются рядом с компонентом (`styles.module.scss`), **только при наличии собственных стилей**: файл непустой и импортируется. Стиль не хранится в data/config, глобальные стили — только theme/reset/providers. Inline style допустим для вычисляемой геометрии, но не для назначения палитры.

Цвета: semantic UI Kit props или текущие theme CSS variables; `transparent/currentColor/inherit` при необходимости. Запрещены hardcoded hex/rgb/hsl/oklch/named palette, локальные палитры и `var(--token, #fff)`. Для charts/SVG применяй существующие semantic tokens, а не «примерно похожие» цвета.

## 6. i18n: JSON UI resources

Новые системные UI-строки (actions, statuses, filters, errors, notifications, labels) храни в JSON-ресурсах, когда это принятый проектом формат; пример:

```json
{"toolbar":{"all":"Все","active":"Активные"},"errors":{"load":"Не удалось загрузить данные"}}
```

TypeScript допускается для wiring ресурсов, namespaces и type inference, но не как второе хранилище user-facing strings. ФИО, названия организаций, даты, договоры и сообщения пользователей — **runtime data**, не JSON translation; для примеров только синтетические значения. Если target использует иной авторитетный i18n-resource format, следуй ему, а конфликт отметь.

## 7. UI и бизнес-логика — разные слои

Страница компонует, store владеет state/actions/derived, helper содержит чистые вычисления, service — network/normalization boundary, `data` — fixtures. Нельзя строить в JSX логику лимитов/прав/валидации/фильтрации и переносить её в CSS/class config.

```text
src/
├── data/recordFixtures.ts
├── helpers/recordStatus.ts
├── helpers/recordStatus.test.ts
├── stores/RecordStore.ts
├── stores/RecordStore.test.ts
└── pages/RecordRegistry/
```

Не создавать store для тривиального локального UI-state, если target использует state hooks. Новая бизнес-логика тестируется, маппинги status/id остаются типизированными и независимыми от UI-переводов.

## 8. Handlers и observable state

Используй именованные handlers, когда их поведение нетривиально, они участвуют в dependencies или должны иметь стабильную identity для memoized child. `useCallback` **не обязателен** на каждый inline handler; назначай его по фактическому referential contract/complexity. Компонент с observable store в MobX/MST оборачивается в `observer`, если это target convention.

## 9. Microfrontend runtime

Не встраивай самостоятельный Router/`createRoot` и не создавай собственную product shell для фичи внутри существующего MFE. Если target работает через Single-SPA, сохрани предоставленные entrypoints, providers, externals, auth, analytics и host routing. Конкретные exports/runtime registration берутся только из target evidence, не из этого документа.

Для `STANDALONE_ENGINEERING` локальные `createRoot`, router и preview shell допустимы как **изолированный sandbox harness**; typed mock adapter не равен production API. Не объявляй эту сборку production-ready MFE. Если нужен перенос, укажи список незавершённой интеграции.

## 10. Разделение preview и handoff

При недоступном runtime/dependencies могут существовать:

- **Preview:** локальная оболочка, demo-state controls, fixtures и инструменты визуальной проверки; никогда не считается production integration.
- **Handoff:** чистый переносимый React/TypeScript product increment с imports/dependencies target, но без demo shell, vendored UI Kit, временных assets, генератов `dist/`, `*.tsbuildinfo` и workaround dependencies.

Для handoff перечисли: реальные dependencies и что target должен предоставить; точные версии, которые ещё требуется подтвердить; fixtures для замены API; query/debug/demo сценарии для удаления; contracts, auth/analytics integration gaps; тесты/build/typecheck после интеграции. Preview и handoff не должны расходиться в согласованных business rules.

## 11. Pre-handoff checklist

- [ ] Все component public imports проходят через принятые `index.ts`/exports; нет facade UI Kit.
- [ ] Нет ненужных `src/components` для screen-only components, больших fixtures в JSX и domain logic на странице.
- [ ] Нет hardcoded colors или неиспользуемых/пустых style modules; визуальные tokens из реального UI Kit.
- [ ] Все новые UI-строки в approved i18n resources; ids не привязаны к переводам.
- [ ] Нетривиальные handlers/state не теряют keyboard/focus/pending/error behavior.
- [ ] Components >400 lines и Props 8+/12+ рассмотрены; решение и исключения задокументированы.
- [ ] Новая/изменённая helpers/stores business logic покрыта релевантными тестами.
- [ ] Нет запрещённых imports/dependencies, manually edited generated OpenAPI, dead code или debug-only assets в handoff.
- [ ] `git diff --check`, TS, format/lint/tests/build выполнены **если разрешено**, иначе `skipped` с причиной.
- [ ] Для standalone записано `Integration verification: NOT_PERFORMED` до реальной интеграции.
