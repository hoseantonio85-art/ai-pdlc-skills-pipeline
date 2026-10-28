# Tests, checks and severity

## Тесты

Покрывай новую/изменённую business logic:
- store actions и computed views;
- request builders, sample productalizers, domain transformations;
- navigation/formatting/file-validation helpers;
- race-sensitive async behavior.

Type-only, re-export и простая wiring-правка не требуют искусственного теста. Component test нужен, когда в компоненте есть нетривиальное поведение, которое нельзя надёжно проверить ниже. Отсутствие snapshot/render test само по себе не нарушение.

Следуй фактическому test stack target repo, часто Vitest. Generated code не меняется ради coverage.

## Статические проверки

Всегда начни с разрешений `AGENTS.md`. Минимальный аудит:
- `git diff --name-only`, полный просмотр изменённых файлов, `git diff --check`;
- hardcoded colors и запрещённые imports/re-exports;
- empty/unimported style modules;
- component/hook/model size и overloaded Props;
- `any`, `unknown`, unsafe casts, suppressed TypeScript errors;
- новые пользовательские strings, localized guards, CSS strings в domain config;
- toolchain baseline;
- dead/generated changes;
- тесты для затронутой business logic.

Install/dev/build/lint/tests запускаются только если разрешены environment/repo/task. Незапущенную runtime verification помечай `skipped`, не выдавай её за passed.

## Severity

### Blocker

- нарушение architecture layer или Single-SPA/runtime contract;
- запрещённая dependency или adapter/barrel disguise;
- hardcoded color/local palette;
- новый user-facing text вне i18n;
- localized label как business id/guard;
- новый/изменённый business helper/store/sample productalizer без релевантного теста;
- отсутствующий обязательный target TypeScript/Biome baseline;
- необоснованный `any/unknown`, unsafe cast, suppressed type error;
- overloaded новый component API без обоснования;
- недоступное ключевое действие;
- повторный submit/action во время pending;
- пустой/неиспользуемый style module;
- route-level business logic/mock config;
- ручное изменение generated OpenAPI;
- очевидный dead code, отключение unused checks, повреждённая кодировка;
- несовместимое изменение public API/routes/MFE integration;
- расхождение с обязательным observable behavior из approved SDD.

### Major

Локально обязательная правка без системного blocker: пропущенный `observer`, необоснованная memoization, prop drilling, смешение ответственности, недостающее вторичное состояние, нарушение утверждённого frontend plan без продуктового эффекта.

### Recommendation

Legacy вне scope, stylistic consistency и улучшения без доказанного риска. Спорное замечание подкрепляй target-repo example; без доказательства не повышай severity, кроме перечисленных blockers.

## Review verdict

- `PASS`: blockers=0, majors=0; skipped checks явно перечислены.
- `FIX_REQUIRED`: есть blocker/major, которые можно исправить в существующем scope.
- `BLOCKED`: нельзя достоверно завершить review из-за отсутствующего SDD/plan/repo/contract или конфликтующих authoritative sources.
