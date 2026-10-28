---
id: collection-presentation
title: Представление множества
status: draft
maturity: reference-backed
category: collection
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
owners:
  design: needs-review
  frontend: needs-review
last_reviewed: 2026-09-30
---

# Представление множества

## Назначение

Выбрать форму показа множества по пользовательскому решению, а не автоматически по типу данных или привычке использовать Entity Card.

## Use when

Перед проектированием любого списка, коллекции, каталога или набора категорий.

## Decision model

### Decision registry

Используй row/entity cards, когда пользователь сравнивает состояние бизнес-объектов, понимает приоритет и решает, что открыть или обработать первым. Evidence: Risks / Measures / Events lists.

### Navigation collection

Используй navigation cards/grid, когда пользователь выбирает раздел, область или категорию, а сами элементы являются точками входа. Evidence: Assistant Knowledge primary.

### Content/file collection

Используй compact content/file list, когда задача — найти, выбрать или открыть документ/материал, а не оценить состояние бизнес-объекта. Evidence: Assistant Knowledge secondary.

## Rules

- Не превращай любой список в одинаковые row-cards.
- Таблица не является default для decision registry; локально допустима для истории и прямого сравнения однородных значений.
- Collection presentation не определяет domain fields или конкретную grid geometry.
- При смешанном intent выбери dominant user decision и раскрой вторичный слой отдельно.

## Acceptance checklist

- [ ] Ясно, какое решение пользователь принимает по множеству.
- [ ] Выбран decision registry, navigation collection или content/file collection осознанно.
- [ ] Presentation не копирует unrelated reference целиком.
- [ ] Density и interaction соответствуют выбранному intent.
