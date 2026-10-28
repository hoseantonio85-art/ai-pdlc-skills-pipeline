# Воспроизводимый Visual QA

## Сравниваемая область
Зафиксировать reference revision, aspect/state, viewport/DPR/zoom, fonts, fixtures и region selectors. Native event viewport1728×934; adaptation1440×900 и compact390×844 отдельно. Reference export не responsive; нельзя использовать clipped1440 как целевой layout. Mask только заранее заявленные dynamic IDs/time/content; не маскировать geometry failures.

## Четыре независимых результата
C: одинаковые controls/card shells/tokens. P: repeated zones/order/alignment/density. U: новая UX-composition (смысл, hierarchy, new-vs-reused rationale) — qualitative review и task outcomes, не pixel similarity. F: happy path, filter draft/apply/cancel, search, empty/error/loading, destination/return, stack, retry new history.

## Операционализация 95%
До генерации выбрать comparable regions и требования. Каждому requirement вес, test, expected, tolerance. C geometry вес40, C colors/borders/radii20, P geometry/order30, repeated interaction states10. Coverage — список eligible/excluded regions и reasons. Score=100×Σweight×pass/Σweight, только при complete eligible coverage. Pass critical order/overlap/focus/context tests обязателен независимо от score. Для C и P отдельно ≥95; U и F должны пройти свой gate. Не выдавать geometry-only score за этот полный score.

Tolerances: toolbar/order обязательны; anchor/alignment ≤2px; control height/radius/padding ≤1px; card zone/gaps ≤2px; same viewport widths ≤2px; solid RGB ≤2 на канал. Текст: baseline/layout ≤2px после одинаковых real fonts. При отсутствии fonts typography/pixel область помечается excluded, полный 95% не аттестуется. Anti-alias pixels допускают documented threshold, но не заменяют geometry.

## Измерения
Browser getBoundingClientRect/computedStyle → JSON with reference node IDs/actual selectors; screenshot same viewport. Pixel diff per ROI: RGBA abs-diff threshold16, changed pixel fraction, mean absolute RGB; это различие пикселей, не «процент продуктовой точности». SSIM допустим как дополнительная perceptual метрика, не final score. В этой поставке QA script пишет geometry pass rate отдельно и pixel diagnostic для event ROI; недостающие fonts/icons/новые UI states перечислены.

## Процедура
Снять source и prototype screenshots; прогнать F сценарии и comparable measurements; визуально изучить screenshots выбранных mandatory states; исправить и повторить affected checks. Записать evidence files, commands/tool versions, failures и exclusions. Если browser недоступен: READY_WITHOUT_VISUAL_REVIEW. Если дефекты: NEEDS_VISUAL_FIX. PASS означает весь фактически выполненный gate, не target95. Отдельная техническая готовность не заменяет human/design validation новых hypotheses.
