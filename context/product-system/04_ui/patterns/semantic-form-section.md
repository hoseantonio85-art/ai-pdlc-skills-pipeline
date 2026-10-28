---
id: semantic-form-section
title: Смысловая секция формы
status: draft
maturity: reference-backed
category: form
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
owners:
  design: needs-review
  frontend: needs-review
last_reviewed: 2026-09-30
---

# Смысловая секция формы

## Назначение

Организовать сложную форму как последовательность понятных пользователю вопросов/смыслов, а не как равнозначный перечень полей.

## Anatomy

1. `meaning` — короткий вопрос или смысл секции.
2. `helper` — optional объяснение, зачем нужны данные или как их заполнить.
3. `controls` — связанные поля/controls текущей смысловой задачи.
4. optional local feedback / nested helper intent.

## Preferred desktop variant

`meaning + helper` слева, `controls` справа. Между смысловыми секциями больше вертикальный интервал, чем между полями внутри одной секции.

На узкой ширине: `meaning → helper → controls` последовательно.

## Rules

- Секция отвечает одному пользовательскому вопросу.
- Helper не повторяет label поля.
- Field schema/validation остаётся у form-field/modal-form.
- Binary Switch используется только для boolean on/off; named choices используют подходящий selection control.
- Repeatable groups допустимы внутри controls, но их lifecycle не определяется этим pattern.
