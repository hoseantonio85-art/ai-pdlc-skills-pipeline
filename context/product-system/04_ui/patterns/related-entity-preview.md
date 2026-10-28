---
id: related-entity-preview
title: Превью связанной сущности
status: draft
maturity: reference-backed
category: relationship
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
owners:
  design: needs-review
  frontend: needs-review
last_reviewed: 2026-09-30
---

# Превью связанной сущности

## Назначение

Показать достаточно контекста о связанном объекте, чтобы понять роль связи и решить, нужно ли открыть полный объект, не копируя весь Object View.

## Anatomy

- linked entity identity / name;
- optional stable ID/type;
- один короткий status/signal;
- минимальный meaningful relationship context;
- explicit `open full object` intent, если доступно.

## Behavior

- Preview не становится самостоятельным полным объектом внутри parent surface.
- Переход к полному объекту использует approved entity navigation/Object Modal contract и сохраняет ожидаемый parent context.
- Несколько related entities могут образовать компактную collection с тем же minimal anatomy.

## Do not use when

- связи достаточно одной ссылки/ID без дополнительного смысла;
- preview начинает показывать все domain fields;
- full object открывается в Drawer вместо approved Object Modal без отдельного UX rationale.
