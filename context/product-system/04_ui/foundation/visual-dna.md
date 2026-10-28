# NORM Visual DNA: измеренный слой

Срез 08.10.2026. Geometry evidence: экспорт НОРМ + локальные repos. Это prototype aliases, не production token API. Для native event/measure scene viewport 1728 × 934, DPR 1, zoom 100%.

| Роль | Значение | Источник |
|---|---|---|
| Shell menu | #f7f8f9 в design scene; #f0f2f5 для secondary controls | event-list #100_62568; UI Kit background.module.scss |
| Workspace | #fff; radius 24 | event-list #100_42285 |
| Sidebar | 288 expanded, 88 collapsed variant | event-list; Assistant Knowledge exports |
| Content | max 1240; x388 при sidebar288 и canvas1728; y40 | event-list #2395_46928 |
| Heading | line40; title28/32; 24 до toolbar | event-list #2395_46931 |
| Toolbar | h40; left scope; right search40 + gap8 + filter≈104 | event-list #2395_81161 |
| Scope | radius100; outer padding4, inner h32, padding6px 16px | event-list; RadioChips/styles.module.scss |
| Quick chip | h40, pad8 16, border1, counter2 8, gap8 | measure-list; CheckboxChips/styles.module.scss |
| Expanded search | h48 radius16; 16 от toolbar; 24 до списка | event-list y160–208; FieldSearch M |
| Event card | pad24, radius16, h160 при эталонном тексте; gap8 | event-list first card y232–392 |
| Risk card | pad24 radius16; gap16; metrics width160 gap64 в repo | RiskCard/styles.module.scss |
| Card hover | 0 0 1px rgba(36,41,46,.32), 0 4px 8px rgba(36,41,46,.12) | RiskCard/styles.module.scss |
| Neutral border | quiet 1px; #dce0e5 в export; token #09203721 в kit | export + UI Kit border/control |
| Body / metadata | 16/20 и 12/16; title weight600; muted #6a737d | export Text roles; UI Kit text.module.scss |
| Primary | green gradient #32d5a7→#32d583; hover #11ad81 | UI Kit styles/button.module.scss |
| Focus | #11ad81 | UI Kit control.module.scss |
| Status | height20, radius99, pad2 8; danger #fee4e2, info #d1e9ff | event-list status nodes; UI Kit background |
| Active advanced filters | red dot6 at top8 right8 | Risks/Measures Filters/styles.module.scss |
| Object modal | max1320; outer margin24; radius24; one scrim | components ModalLayout/styles.module.scss |
| Meta rail | 320 target export incl padding; old starter280 is fallback | universal-object-modal right panel |
| Drawer | subordinate right; radius24 0 0 24; header40; content40; footer40 | components Drawer/styles.module.scss |
| Dock | width600 height88 radius32 pad24 gap16 bottom16 | event-list #410_111558 |

Ритм page/registry/inside-card различается. Не фиксировать высоту карточки при длинных названиях: min geometry для сравнимого fixture; содержимое может увеличить высоту. Не прятать важный результат ради совпадения.

Адаптация: при ширине1001–1400 sidebar220 и insets32 — документированная гипотеза прототипа, не извлечённый breakpoint продукта. При ≤1000 nav скрывается, рабочие зоны сохраняются; при ≤700 двухзонная карточка становится последовательной. Exact production breakpoints подтвердить отдельно.

Шрифты экспортов ссылаются на font/undefinedundefined и имеют некорректные font-weight: Regular/Semibold. Geometry есть, эталонная типографика неполна. Демонстрации используют Arial; pixel-level typography не аттестована. Иконки лёгкие SVG, semantic sizes20/16/12; точные glyphs — отдельный backlog, не emoji-система.

Иерархия: основная смысловая зона слева; статус/date внутри её верхнего ряда допустим. Secondary ID/author/description справа. Статус не становится универсальной ведущей колонкой. Цвет применяют по роли, фон связывает блоки, тень — hover/overlay. Аналитика только для вопроса и перехода к выдаче.
