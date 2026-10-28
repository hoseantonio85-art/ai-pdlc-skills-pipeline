---
id: situational-overview
title: Ситуационный обзор и интерактивная аналитика
status: draft
maturity: screenshot-and-ux-backed
category: analytics
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
normative_scope:
  - decision whether aggregate visualization is useful
  - relationship between overview, filters and detailed results
  - drill-down and cross-filter semantics
  - information hierarchy for situation understanding
---

# Ситуационный обзор и интерактивная аналитика

## Назначение

Паттерн помогает не сводить сложную рабочую область к выдаче карточек. Если данные позволяют показать распределение, динамику, концентрацию, покрытие или зоны внимания, пользователь получает сначала понятную картину ситуации, а затем detailed registry.

## Основной принцип

Analytics существует ради ответа на пользовательский вопрос и следующего действия. Она не декоративна и не обязательна на каждом экране.

Подробный компактный runtime contract: `runtime/situational-overview.md`.

## Evidence

- `03_ux/ux_patterns.md` — Dashboard: обзор, мониторинг, comparison, attention zones, обязательный drill-down/action;
- NORM контрагенты — summary + распределение задолженности + detailed list;
- продуктовые UX-принципы требуют дать первичное понимание ситуации без чтения всех деталей.

## Не фиксирует

- конкретный chart type;
- число KPI;
- точную позицию относительно filters;
- production component API;
- обязательное наличие AI summary.
