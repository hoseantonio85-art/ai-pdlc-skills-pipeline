---
id: workflow-footer
title: Подвал действий workflow
status: draft
maturity: reference-backed
category: actions
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
owners:
  design: needs-review
  frontend: needs-review
last_reviewed: 2026-09-30
---

# Подвал действий workflow

## Назначение

Дать устойчивое место для действий, которые завершают текущую form/workflow task, с понятным primary/secondary/destructive приоритетом и pending behavior.

## Use when

- create/edit modal требует Save/Continue/Cancel;
- текущая workflow task должна завершиться явным решением;
- действия должны оставаться достижимыми при прокрутке form/content.

## Anatomy

- secondary/cancel region;
- optional destructive/reject intent с соответствующим consequence contract;
- primary commit/continue action;
- optional compact state/feedback, если это не дублирует body feedback.

## Rules

- Primary action находится в одном устойчивом месте и не дублируется в header/rail.
- Pending блокирует повтор только затронутого действия; draft/context сохраняются.
- Disabled имеет объяснимую permission/dependency причину.
- Create/edit commit actions используют stable footer.
- Read-only Object View может иметь current footer в существующих implementations, но target composition может переносить object-level contextual actions в right Object Action / Meta Zone при явном UX Solution. Не создавать одновременно дублирующие action regions.

## Responsive behavior

Actions остаются достижимыми и не перекрывают последнее поле/ошибку. На узкой ширине ordering сохраняет primary decision и безопасный cancel/close path.

## Evidence

Risk/Event/Measure forms and views подтверждают footer family; Universal Object Modal и `object-action-meta-zone` задают target direction для read-only actions.
