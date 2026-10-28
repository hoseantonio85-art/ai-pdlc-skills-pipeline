# Frontend engineering standard — 05/06/07

Статус: **canonical engineering constraints**, не бывший объединённый subagent. Ответственные роли: `frontend-planner` (05), `frontend-implementer` (06), `frontend-reviewer` (07). Применять после `APPROVED_FOR_ENGINEERING`, по approved SDD/plan и изменённому scope. Продуктовые принципы UX/UI дополняют эти правила, но не задают React API.

## 1. Профиль и источник истины

- `TARGET_REPO`: существующий frontend/MFE; прочитай `AGENTS.md`, package/lockfile, tsconfig, lint/Biome, runtime, router/providers, stores, i18n, применимые компоненты и тесты. **Не** создавай параллельную архитектуру или независимый `createRoot` для фичи внутри существующего runtime.
- `STANDALONE_ENGINEERING`: только для реального greenfield без целевого production repo/runtime. Создавай переносимый React/TypeScript sandbox на подтверждённом UI Kit и fixtures. Изолируй local `createRoot`/router/demo shell. Не называй результат проверенным production MFE, не имитируй auth/API/analytics. При отсутствии существующего обязательного repo — `BLOCKED_BY_REPOSITORY`, а не downgrade.
- **Приоритет:** ограничения среды/`AGENTS.md` → явный approved scope, SDD и plan → фактический stack/runtime/exports target (`TARGET_REPO`) или verified approved reference (`STANDALONE_ENGINEERING`) → данные product context → общие нормы этого файла. Нельзя считать устаревший референс production truth. Не выдумывать версии, APIs, data contracts.
- Внешние источники (specs, UI Kit, toolchain rules, репозитории) доступны только если реально разрешены через `product-evidence.yaml` и проверены. При отсутствии нужного evidence — `BLOCKED_BY_SOURCE` или `NEEDS_ENGINEERING_DECISION`, не «прочитано».

## 2. Preflight и reconnaissance

В начале зафиксируй engineering profile, target path, exact diff/scope, approved SDD, user scenarios, boundary, data/API sources, responsive states, UI Kit API и критерии готовности. В `TARGET_REPO` исследуй один аналогичный экран, store-connected component, релевантную form/modal/drawer, helper/store test, public exports и call sites. Для изменяемой зависимости обозначь `reuse | adapt | replace | discard | target-provided | unresolved`. В standalone классифицируй `reuse-reference | adapt | create-portable | sandbox-only | unresolved | integration-later`. Не выполняй объёмную загрузку нерелевантных исходников.

Проверь scope файлов `*.ts`, `*.tsx`, `*.scss`, `package.json`, lockfile, `tsconfig*`, конфигурации lint/formatter и build; просмотрев **полные изменённые файлы**, а не только diff. Generated/build (`src/openapi/**`, `dist/**`, `build/**`, `coverage/**`, `node_modules/**`, сгенерированные i18n-типы, binary assets) не редактировать вручную, отличать `skipped` от проверенного.

## 3. Toolchain и зависимости

- В `TARGET_REPO`: используй фактические версию TypeScript, package manager, `tsconfig`, Biome/другой утверждённый lint/format, test runner и lockfile; не создавай конкурирующий ESLint/Prettier/другой pipeline.
- Если target/reference использует централизованные TS и Biome config-пакеты, **подтверди имена, exports, `extends` и resolution** из доступного `package.json`/workspace/approved toolchain evidence. Проверяй CLI `@biomejs/biome` **только если он принят**. В standalone версию бери из проверенного reference baseline, не `latest` по памяти.
- Root workspace dependency допустима, если toolchain реально резолвится. Запускай `tsc --noEmit` или принятый typecheck; lint/format/build/tests — разрешёнными командами. Не отключай strict/noUnused ради зелёной сборки.
- Lockfile меняется только через разрешённый package manager. Credentials, internal URLs и токены не коммитить; запрет package install не обходить. Невыполненные команды документировать как `skipped` или environment blocker.

## 4. Архитектура и ответственность

- `pages`: route composition/orchestration; `pages/<Page>/components`: только экранные элементы; `components`: используемые несколькими сценариями; `stores`: состояние, actions, derived values; `helpers`: чистая доменная логика; `services`: transport/adapter boundary (если принят); `providers`: runtime; `data`: fixtures; `i18n`: UI-строки; `@types/model`: contracts.
- Не помещать большие mock arrays, вычисления тарификации/прав, network normalization, CSS strings или visual configs в route JSX. Применять существующий импортный alias только когда он задан target; локальные импорты могут быть относительными.
- Generated API types не должны без необходимости протекать в UI; на границе service/store преобразуй в typed domain/view model. Статусы и бизнес-идентификаторы не вычислять из локализованных текстов.
- Не делать god-hook, не универсализировать один компонент на будущее, не создавать пустые files/dirs. Если route file >400 строк — **review границ**; blocker лишь при реально смешанных независимых ответственностях.

## 5. TypeScript и React

- Используй explicit domain/API typing, union, generics, `Pick/Omit`, `Awaited`, `ReturnType`, `ComponentProps`, `satisfies`. Не скрывать проблемы через `as any`, `as unknown as`, `Record<string, any>`, `@ts-ignore`, `@ts-nocheck`, ослабление strict.
- `unknown` допустим на недоверенной внешней границе (raw JSON, caught error, third-party), но локализуется в parser/guard/adapter и сужается **до** store/component. `as`/non-null `!` только при доказанном инварианте.
- Взаимоисключающие состояния и режимы — discriminated unions + exhaustive `never`, а не мешок optional props или набор boolean flags.
- `observer` для читающего observable store компонента, если target использует MobX/MST. `useMemo`, `useCallback`, `memo` — для доказанного referential contract/дорогих вычислений, не автоматически на каждый inline handler.
- API компонента выражает предметные понятия: именованные `item/model/viewModel`, осмысленные `state/actions`, явные небольшие callbacks, composition/slots; не пропускай неизменённые props сквозь несколько компонентов. **8+ собственных props** — API review; **>12** в новом/существенно изменённом компоненте — blocker без обоснования; **3+ boolean flags** — проверить boolean explosion; **2+ промежуточных forwarding layers** — проверить state ownership.

## 6. UX, UI Kit и accessibility

- Перед использованием компонента UI Kit подтверждай **реальные** exports/props/types/icons/enums выбранной версии. Импортируй напрямую, не vendoring, не маскируя библиотеку re-export/facade. Узкий adapter только при реальном несовпадении подтверждённого API.
- Используй имеющиеся UI Kit semantic controls и theme tokens; не создавать вторую base UI library. Hardcoded палитры (hex/rgb/hsl/oklch/named colors), локальные color fallback и CSS colors в domain config запрещены. Layout/Typography следуют доступным target patterns.
- Новый пользовательский текст — i18n, идентификаторы/flags — стабильные domain values. Не передавай в опасные логи персональные данные, secrets или technical errors. Ключевые действия: native/semantic controls, accessible name, keyboard/focus, ассоциированные label/error, семантическое pending/disabled. Недоступное новое ключевое действие — blocker.
- Drawer/Modal следуют подтверждённым product UX behavior и target focus-management; **не** навязывать Escape как универсальный контракт (NORM Drawer по умолчанию без Escape, если выбран этот product pattern).

## 7. Асинхронность, состояния, тесты

Сначала scenario matrix: `default/success`, `loading/refreshing`, `empty`, `recoverable error/retry`, `validation`, `disabled/pending`, relevant modal/drawer lifecycle и optimistic states, если применимы. Async action имеет pending/success/error transitions, блокирует повторное действие при pending (если нет разрешённой конкурентности), сбрасывает pending в `finally`/едином store transition. Race → cancellation/request id/target pattern. Не допускать floating promises и swallowed errors; ErrorBoundary ≠ request retry.

Тестировать новую/изменённую бизнес-логику: stores/actions/computed, normalizers, request builders, filters, file validators, navigation/formatting helpers и race-sensitive transitions. Type-only/re-export/wiring не требуют искусственного теста. Component test — для нетривиального поведения. Фактический runner берётся из target/reference.

## 8. Review, severity, safe auto-fix

- **Blocker / FAIL** для новых или затронутых: поломанный runtime/public API, обязательный behavior SDD, запрещённый dependency/facade, unsafe TS, hardcoded color, user-facing text вне i18n, localized business ID, нет теста новой доменной логики, ручной generated edit, недоступное ключевое действие, дублированный submit, route-level domain logic, небезопасное логирование, нарушенный обязательный toolchain.
- **Major** для доказанных локальных проблем: пропущенный `observer`, пропущенное вторичное state, лишние layers/prop drilling, неоправданная memoization или нарушение утверждённого frontend plan без product effect.
- **Recommendation** для legacy вне scope, стилистической консистентности и необязательных улучшений. Severity подкрепляй evidence и line references; legacy не повышать до blocker просто потому, что он неидеален.
- Локальные очевидно безопасные исправления (import, observer, key, token, тест, удаление нового dead code) допустимы в рамках scope; broad API/routing/dependency/behavior change требует решения.
- Проверки: полный changed scope + call sites, `git diff --check`, типы, недопустимые цвета/imports, запрещённые зависимости, i18n, style modules, handler/state, tests и разрешённые команды. Не утверждай о runtime/visual verification без запуска.

В конце: scope/profile, verdict `PASS | FIX_REQUIRED | BLOCKED`, findings с severity/evidence, что исправлено, какие проверки `passed/failed/skipped`, integration gaps, допущения. Для standalone указывай `Integration verification: NOT_PERFORMED`, пока не было интеграции с production target.
