# Руководство по загрузке контекста v7

## Общий принцип

Сначала selector/provider manifest и профиль текущего stage. Используйте compact registries для навигации; подробный `services_map.md`, service documents и evidence читайте только по затронутому scope. Не передавайте модели весь repository.

## Stage 01 — Intent + Product Brief

Автоматически: status/authority, mission, constraints, product philosophy, service goal, `service_registry`, `role_registry`, glossary, common rules, `capability_registry`, product decisions и release-evidence status.

По запросу: `services_map.md`, релевантный service document и evidence, влияющее на boundary/feasibility.

Не читать: UX/UI/UI Kit/frontend implementation rules.

## Stage 02 — UX Solution

Автоматически: source authority, current-product status/sources, product philosophy, compact service/role/capability registries, rules/decisions, UX principles/patterns и pattern index.

По запросу: `services_map.md`, релевантные service documents, analytical specs и task-specific AS IS evidence.

Не читать: UI Kit API и frontend implementation rules.

## Stage 03 — Visual HTML Prototype

Автоматически: loading.always, UX principles/patterns, UI context status, visual profile, pattern/organism registries, reference registry и Foundation visual-dna/source-policy/composition-index. По индексу прочитайте только выбранные contracts; визуальный QA contract — при проверке.

По запросу: выбранный UI/runtime pattern, organism и максимум релевантные reference scenes.

Не читать bulk UI Kit packages, все services или engineering rules.

## Stage 03.5 — UX Sync

Главный вход — task artifacts + human review evidence; UX principles/patterns загружаются автоматически. Domain evidence — selective consistency check.

## Stage 04 — Product SDD

Автоматически: source authority, product philosophy, compact service/role/capability registries, glossary, common rules, product decisions и constraints.

По запросу: `services_map.md` и подтверждённые service/domain/analytical sources конкретного requirement.

Не копировать API/DTO/storage/components/stores/backend design или prototype code structure в Product SDD.

## Stage 05 — Frontend Plan

Автоматически: NORM UX/UI engineering profile. Обязательны approved SDD, final UX/Sync и `05-07-frontend-standards`.

- `TARGET_REPO`: target repo обязателен и является implementation truth.
- `STANDALONE_ENGINEERING`: допустим только для greenfield/нового сервиса без доступного product runtime; используются reference repos + actual UI Kit + typed mocks/fixtures. Такой результат не доказывает Single-SPA/DEV/auth/real API integration.

## Stage 06 — Frontend Implementation

Работать только по выбранному increment approved plan и выбранному engineering profile. Prototype = UX evidence, не source code.

## Stage 07 — Independent Frontend Review

Reviewer начинает с actual diff/changed files и проверяет SDD + plan + standards. Для `TARGET_REPO` дополнительно проверяет target runtime contract; для `STANDALONE_ENGINEERING` явно отделяет локальную verification от production integration.

## Длинные задачи

Progress и реально прочитанные sources фиксируются в stage artifact. После `/clear` продолжайте по artifact/checkpoint, а не по памяти сессии.
