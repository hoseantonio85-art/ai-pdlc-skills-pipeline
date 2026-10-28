# UI context

Раздел содержит стабильный UI/visual context для Stage 03 и engineering-reference layer для Stages 05–07.

- `ui_context_status.md` — доступность и ограничения;
- `prototype_ui_rules.md` — compact UX/UI rules Stage 03;
- `frontend_prototype_rules.md` — compact React/frontend rule source для engineering profile;
- `ui_sources.yaml` — маршруты к exact evidence;
- `ui-kit/component-index.yaml` — быстрый индекс UI Kit API;
- `ui-kit/ui_base.md` — документация, читаемая фрагментами;
- `patterns/` — optional registry UI patterns.

Полные packages не bulk-load. Full frontend normative sources в `product-system/05_engineering/` намеренно доступны Stages 05–07 через manifest до завершения rule-by-rule normalization.

## Runtime routing layer

- `visual/norm-visual-dna.md` — compact NORM visual profile;
- `visual/composition-adaptation.md` — граница между invariants, strong defaults и свободой новой композиции;
- `patterns/pattern-registry.yaml` — authoring patterns + runtime overlay router;
- `patterns/runtime/` — короткие task-time pattern contracts;
- `patterns/specs/` — полные Modal/Drawer shell specs для authoring/reconciliation;
- `organisms/` — composition contracts и отдельный registry;
- `references/html/starter/` — product-scoped HTML starter;
- `references/html/norm-vertical-slice/` — visual reference scene;
- `references/html/situational-overview/` — on-demand reference интерактивной аналитики + detailed registry;

Принцип: index-first → selected runtime patterns/organisms → HTML reference только при необходимости. Existing authoring pattern files сохраняются на прежних путях для обратной совместимости.

Patterns являются strong defaults, а не жёсткими шаблонами. Canonical surface semantics и product invariants обязательны; optional composition можно адаптировать с rationale.
