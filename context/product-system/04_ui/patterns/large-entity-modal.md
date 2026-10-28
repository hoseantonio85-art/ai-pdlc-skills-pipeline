---
name: large-entity-modal
title: Большая модалка сущности
status: draft
version: 0.2.0
type: ui-composition-pattern
applies_to:
  - norm
  - orm
related:
  - ./specs/modal.md
  - ./runtime/object-modal-view.md
  - ../organisms/object-action-meta-zone.md
---

# Большая модалка сущности

## Назначение

Object Modal открывает самостоятельный объект поверх текущего рабочего контекста. Она используется для полноценного просмотра, создания или редактирования объекта без перехода со страницы.

Shared shell и поведение определяет `specs/modal.md`. Этот документ фиксирует composition-level правила большой объектной модалки и её связь с product profiles.

## Режимы

### Object View

```txt
Object Modal / View
├─ Topbar / Header
├─ Object Header
├─ Body
│  ├─ Main content
│  └─ Right action/meta zone
└─ Footer отсутствует
```

Правила:

- Main content содержит summary, основные разделы, AI-выводы, связанные данные и локальные действия блоков.
- Right rail является единой action/meta zone: metadata, history/service navigation, related-object transitions, workflow/lifecycle/destructive actions.
- Общий Footer в Object View запрещён.
- Одно object-level действие не дублируется в Header, content и rail.
- Редкие lifecycle/destructive actions допускается размещать в More внутри rail.
- Подчинённая задача открывается Drawer.
- Самостоятельный связанный объект открывается новой Object Modal в stack.

### Object Create / Edit

```txt
Object Modal / Create or Edit
├─ Topbar / Header
├─ Scrollable form workspace
└─ Fixed Footer
```

Правила:

- completion actions `Отмена / Сохранить / Продолжить / Создать` находятся в Footer;
- dirty guard обязателен;
- Right rail может содержать подсказки, metadata и contextual information, но не заменяет Footer как место завершения формы.

## Product profiles

### NORM

- reference width: `1320px`;
- surface radius: `24px`;
- viewport padding: около `24px`;
- desktop view: Main + rail, rail target около `280px`;
- визуально остаётся большой overlay над продуктом.

### ORM

- reference width: `1424px`;
- near-fullscreen workspace perception;
- тот же semantic contract Object View / Create / Edit;
- конкретный visual profile должен приходить из ORM context, а не копироваться из NORM.

## Action / Meta Zone

Подробный composition contract: `../organisms/object-action-meta-zone.md`.

Рекомендуемый порядок:

1. основная metadata;
2. статус, владелец/автор/даты;
3. история и коммуникация;
4. связанные сущности и служебные переходы;
5. primary action;
6. secondary actions;
7. lifecycle/destructive actions.

Visibility и permissions приходят из domain/workflow rules и не определяются визуальным паттерном.

## Scroll и state continuity

- Header/Topbar не прокручиваются вместе с Body.
- Body является основной scroll-зоной.
- Rail остаётся доступным; sticky допустим, если не создаёт конфликтующих nested scroll areas.
- При открытии Drawer или stacked Object Modal состояние текущего слоя сохраняется: section, scroll, раскрытые блоки, ввод и trigger.

## Responsive

- ширина является `max-width`, не жёсткой fixed width;
- при уменьшении container Main и rail перестраиваются без создания нового произвольного размера;
- rail может переноситься под Main content или становиться отдельным внутренним уровнем;
- Object Modal не выходит за viewport.

## Source reconciliation

Production Risks/Measures подтверждают крупный modal shell, main/meta split и sticky information rail. TO-BE `risk-Modals.png` подтверждает объединение metadata и workflow actions справа.
Owner-provided HTML exports Risk/Event/Measure View подтверждают, что current/legacy View может иметь Footer. Это current-state evidence; target/canonical Object View остаётся `Main + Right action/meta zone` без общего Footer, как в Universal Object Modal direction.

Старое правило `Object View → workflow Footer` отменено. Предыдущая версия документа сохранена в `../audit/legacy/large-entity-modal-v0.1.0.md` только как историческое authoring evidence и не является runtime rule.

## Для AI-агента

Перед генерацией:

1. определить product profile;
2. определить mode: `view | create | edit`;
3. для `view` использовать Main + Right action/meta zone и **не создавать Footer**;
4. для `create/edit` использовать fixed Footer;
5. определить Drawer vs stacked Modal по роли следующей задачи;
6. открыть только релевантный runtime pattern/organism и product visual profile.
