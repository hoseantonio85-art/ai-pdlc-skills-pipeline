# Target/reference reconnaissance

## Сначала выбери engineering profile

- `TARGET_REPO` — существующий frontend/MFE или доступный production target repo.
- `STANDALONE_ENGINEERING` — greenfield/новый сервис без доступного production MFE/runtime, когда нужен локальный React/TypeScript engineering sandbox.

Если существующий repo должен быть доступен, но его нет, standalone не является fallback → `BLOCKED_BY_REPOSITORY`.

## TARGET_REPO: target-first discovery

До архитектурных выводов прочитай применимые `AGENTS.md`, затем в объёме задачи проверь:

- `package.json` и lockfile;
- `tsconfig*.json`, `biome.json/jsonc`, релевантный `vite.config.*`;
- entrypoint, providers, router, store и i18n;
- один реальный пример похожей страницы;
- один store-connected component;
- похожую form/modal/drawer, если релевантно;
- helper/store test и фактический test stack;
- фактические UI Kit imports/exports/types, UI Kit docs и допустимые dependencies;
- дополнительные правила frontend/toolchain из одобренных локальных sources;
- реальные API/OpenAPI contracts, если они доступны.

Для каждой потенциальной зависимости/части прототипа классифицируй:

`reuse | adapt | replace | discard | target-provided | unresolved`

## STANDALONE_ENGINEERING: reference-first discovery

До реализации зафиксируй:

- почему target repo/MFE runtime пока отсутствует и почему standalone профиль допустим;
- 1–2 доступных reference repo/pattern source или selected product engineering context;
- целевой React/TypeScript/toolchain baseline из references, не из памяти;
- actual exports/types и ограничения подключённого UI Kit package;
- разрешённый dependency source: corporate Nexus/registry, existing workspace/cache или локальный package artifact;
- test stack/baseline из reference evidence;
- typed data boundary: known API contract либо `PRODUCTION_CONTRACT_UNKNOWN` + fixture/mock adapter;
- какие части являются portable product code, а какие sandbox-only runtime harness.

Для каждой потенциальной части классифицируй:

`reuse-reference | adapt | create-portable | sandbox-only | unresolved | integration-later`

## Runtime guardrails

### TARGET_REPO
- Не создавай `BrowserRouter`/`createRoot`, если фича живёт внутри существующего Single-SPA runtime.
- Сохраняй entrypoints, routing, externals и public exports target repo.

### STANDALONE_ENGINEERING
- `createRoot` и minimal local router допустимы только как sandbox harness.
- Sandbox shell должен быть изолирован так, чтобы pages/components/stores/helpers можно было перенести в target MFE без зависимости от local shell.
- Не имитируй Single-SPA registration, auth provider, analytics или real API, если их фактические contracts недоступны.
- Явно фиксируй `Integration verification: NOT_PERFORMED`, пока target runtime не подключён.

### Оба профиля
- Не вендорь UI Kit.
- Не маскируй запрещённую библиотеку adapter/barrel re-export.
- Generated/build paths (`src/openapi/**`, `coverage/**`, `dist/**`, `build/**`, `node_modules/**`, generated i18n types, binary assets) не рассматриваются как ручной код; изменения там помечаются separately/skipped, а `src/openapi/**` вручную не редактируется.

## Toolchain baseline

Приоритет: target `package.json`/workspace/lockfile → доступный, одобренный reference/toolchain evidence → этот общий checklist. Публичный pipeline **не** закрепляет внутренние имена config-пакетов.

| Назначение | Что проверить |
|---|---|
| TypeScript config | Где хранится base tsconfig; как резолвится локальный/shared `extends` |
| Formatter/linter config | Как резолвится принятый `biome.json/jsonc`/extends либо фактический target tool |
| CLI | Наличие и версия `@biomejs/biome`, **если** используется Biome; иначе утверждённый CLI target |
| App tsconfig | Цепочка `extends`, strict/noUnused и рабочая команда typecheck |
| Package workflow | Package manager, lockfile, registry и разрешённые команды |

В `TARGET_REPO` версии и реальные названия бери только из repo. В `STANDALONE_ENGINEERING` — из approved reference baseline или локально настроенного `products.<id>.frontend_rules`; никогда не угадывай `latest`.

Root workspace dependency достаточна при доказанном resolution. Параллельный ESLint/Prettier pipeline без причины не добавлять. Dependencies/lockfile меняются только разрешённым package-manager workflow; если install запрещён — skipped/`BLOCKED_BY_ENVIRONMENT` с пояснением, не workaround.
