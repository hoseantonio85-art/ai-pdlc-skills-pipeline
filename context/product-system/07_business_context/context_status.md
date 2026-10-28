# Статус продуктового контекста NORM

| Поле | Значение |
|---|---|
| Context ID | `norm` |
| Context version | `7` (сохранён manifest/API пайплайна) |
| Package version | `7.0.3` (актуализирован единый бизнес-контекст; код пайплайна не изменён) |
| Business specification snapshot | `norm-specs-develop@[редакция исходника удалена]` |
| Business context sync | 2026-10-14 |
| Канонические OpenSpec | 90 документов, backend + frontend |
| Состояние синхронизации | `synced_to_norm_openspec_snapshot` |
| Production release | отдельно не аттестован |

Уточнены сервисы, capabilities, role mappings, доменные constraints и source authority. Версии скиллов, agents, UI, frontend-стандартов, schema manifest и API профилей не изменены. Известные gaps: release registry, полная permissions matrix, аналитика и фактический runtime.

## Точечная актуализация описания «Мер» (срез кода 23.10.2026)

- В `02_services/measures.md` расположена одна полная анкета PO (13 разделов); старая короткая карточка заменена.
- `07_business_context/measures_questions.md` хранит отдельный реестр пробелов/решений и не дублирует описание сервиса.
- Для `measures` AS IS — проверенные FE/BE-снимки, не production; для остальных сервисов сохраняется authority OpenSpec `[редакция исходника удалена]`.
- Контракты stage/manifest, скиллы, агенты, UI-паттерны и версия дистрибутива 7.0.3 не изменены.
