---
name: 05-07-frontend-standards
description: Общие frontend-правила для инженерного планирования, реализации и независимого ревью после APPROVED_FOR_ENGINEERING. Поддерживает target frontend repo и standalone engineering sandbox для greenfield, контролирует React/TypeScript, UI Kit, architecture, i18n, accessibility, async, toolchain и tests.
---

# Frontend Standards

## Назначение

Это **общий нормативный skill**, а не самостоятельная роль. Его читают `frontend-planner`, `frontend-implementer` и `frontend-reviewer`.

Skill не должен активироваться на продуктовых стадиях 01–04 и не должен влиять на HTML-прототип. Он становится применим только после `APPROVED_FOR_ENGINEERING`.

## Engineering profiles

### `TARGET_REPO`
Для существующего frontend/MFE или уже созданного production target repo. Работает target-first: фактический repo является implementation truth.

### `STANDALONE_ENGINEERING`
Для greenfield/нового сервиса, когда production target repo/MFE runtime ещё объективно отсутствует или недоступен как инфраструктурный факт. Это React/TypeScript engineering sandbox на реальном UI Kit и mock/fixture data, а не Stage 03 HTML prototype и не production microfrontend.

Standalone нельзя использовать как обход отсутствующего доступа к существующему repo. Если repo должен существовать → `BLOCKED_BY_REPOSITORY`.

## Приоритет источников

Общие приоритеты:

1. Применимые `AGENTS.md` и ограничения среды.
2. Явный запрос и утверждённый engineering scope/profile.
3. `04_sdd_specification.md` для observable product behavior.
4. `05_frontend_plan.md` после его утверждения.
5. Этот skill и его references.

Для `TARGET_REPO` между пунктами 3 и 4 действует фактический target repo: stack, runtime, package versions, APIs и local conventions; он выше generic guidance.

Для реализации опирайся на проверенный целевой репозиторий и выбранный внешний UI Kit; внутренние имена и версии в публичном комплекте отсутствуют.

## Обязательный порядок чтения

Всегда прочитай:
- [Target/reference reconnaissance](references/01_target_first.md)
- [Architecture and TypeScript](references/02_architecture_typescript.md)
- [UI Kit, states and accessibility](references/03_ui_states_accessibility.md)
- [Tests, checks and severity](references/04_tests_review.md)

## Сквозные инварианты

- Не переносить HTML prototype буквально в React implementation.
- Не придумывать props/icons/enums UI Kit по памяти: проверять фактические exports/types доступной версии.
- Не вендорить UI Kit и не скрывать его за универсальным facade.
- Новый пользовательский текст — через i18n.
- Цвета — только semantic UI Kit props или существующие theme tokens; hardcoded palette запрещена.
- Business logic не живёт в route-level JSX.
- Не скрывать несовместимости типами `any`, unsafe casts или подавлением TypeScript errors.
- Async action имеет явные pending/success/error transitions; повторный submit во время pending блокируется, если конкуренция не задумана.
- Новая/изменённая business logic в stores/helpers/NORMalizers покрывается релевантными тестами.
- Недоступное новое ключевое действие — blocker.
- Dependency credentials/tokens не коммитятся; корпоративный Nexus/registry используется только через разрешённую конфигурацию среды.

Дополнительно для `TARGET_REPO`:
- не создавать параллельную архитектуру рядом с принятой в target repo;
- сохранять runtime, routes, providers, public exports и package workflow target repo.

Дополнительно для `STANDALONE_ENGINEERING`:
- local shell (`createRoot`, optional local router, demo controls) отделяется от portable product code;
- production Single-SPA/auth/API/analytics не имитируются как «готовая интеграция»;
- mocks/fixtures живут за typed boundary и не объявляются production contract;
- integration gaps явно фиксируются в 05/06/07 artifacts;
- local package `.tgz` допустим как dependency source, но его source не копируется в приложение и file-path dependency не переносится в production handoff.

## Target/reference family

Основные ориентиры, если они доступны в рабочем окружении:
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.
- Проверяй реальные пути, версии, UI Kit и технические зависимости **в локально подключённых источниках**; они не входят в публичный комплект.

В `TARGET_REPO` фактический target repo остаётся источником истины; ориентиры не используются для насильственной унификации legacy-проектов.
В `STANDALONE_ENGINEERING` ориентиры используются для reference-first reconnaissance и portability, но не дают права заявлять production integration.
