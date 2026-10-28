# Статус UI-контекста

```yaml
status: ready_for_visual_html_and_engineering_reference
supported_stages:
  - 03-build-visual-html-prototype
  - frontend-planner
  - frontend-implementer
  - frontend-reviewer
supported_modes:
  - standalone_concept
  - standalone_engineering
  - product_like_increment
visual_context_available: true
html_starter_available: true
product_scoped_starter_available: true
runtime_pattern_router_available: true
organism_registry_available: true
composition_adaptation_policy_available: true
situational_overview_runtime_available: true
verified_product_repositories:
  - external-product-frontend@[редакция исходника удалена]
  - external-product-frontend@[редакция исходника удалена]
ui_kit:
  package: "@example/ui-kit"
  version: "0.283.0"
  package_available: true
  docs_available: true
```

## Доступно

- продуктовые UX-принципы;
- правила выбора surfaces;
- visual language NORM;
- подтверждённые frontend-repository patterns layout/composition;
- card registry, dashboard, filters, Object Modal, drawer и floating action patterns;
- product-scoped HTML starter для Stage 03 + legacy skill fallback;
- compact runtime pattern/organism routing для Stage 02/03 и engineering handoff;
- explicit composition adaptation policy: invariants vs strong defaults vs visual references;
- situational overview / interactive analytics runtime pattern + on-demand HTML reference;
- screenshot evidence queue для contextual AI guidance, assistant modal и assistant entry in object rail;
- NORM Visual DNA из production repos/screenshots + explicit TO-BE reconciliation;
- UI Kit docs/index/package как exact evidence для engineering stages и будущего усиления visual quality;
- full frontend rules evidence layer для stages 05–07.

## Граница Stage 03

HTML starter не имитирует production UI Kit API. Stage 03 не должен bulk-load package или frontend engineering rules и не превращает prototype в production contract.

## Граница Stages 05–07

Engineering выбирает профиль. В `TARGET_REPO` actual target repo — высший implementation source. В `STANDALONE_ENGINEERING` для greenfield используются verified reference repos/product rules + фактический доступный UI Kit package/API; bundled UI Kit 0.283.0 может быть exact sandbox evidence, но не доказывает production runtime integration.

## Ограничения

- visual context является MVP-аппроксимацией, а не полной дизайн-системой;
- screenshots/task visuals остаются task-specific evidence;
- baseline и отчёты visual QA поставляются отдельно от runtime context; 95% fidelity не аттестованы;
- ORM profile в registries зарезервирован архитектурно, но ещё не наполнен ORM evidence;
- bundled UI Kit package нельзя bulk-load в model context; читать только exact exports/types по необходимости.
