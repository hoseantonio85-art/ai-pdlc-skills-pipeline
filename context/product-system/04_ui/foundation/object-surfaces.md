# Composition contract: object, form, drawer

## Когда / зоны
Object view — самостоятельный объект поверх реестра. Header identity/status; scrollable main sections; right meta/action rail. Create/Edit — смысловые секции формы и стабильные нижние действия. Drawer — зависимая задача фильтра/настройки, не замена объекта.

## Геометрия
Object max1320, radius24, viewport inset24; scrim rgba(36,40,43,.56). Header UI Kit32px 40px; main target white sections on #f7f8f9. Rail320 в universal export (280 в историческом starter); main/rail gap32. Значение320 — target-specific default, не универсальная production ширина. Drawer header40/content40/footer40; subordinate scrim rgba(255,255,255,.8), right radius24 0 0 24; width608 в демонстрации выведена из видимой field width528+insets80. Export drawer canvas1728 не является шириной самого runtime drawer.

## Обязательные связи / варианты
Object View все workflow/lifecycle actions в rail, общий Footer отсутствует. Create/Edit actions справа в Footer; labels/helpers слева, fields справа на desktop в risk/event/measure forms (example risk label292, gutter24, controls924). Секции объединяют смысл, не каждый field в отдельной карточке. Ошибка у поля + summary при необходимости, длинная форма прокручивается независимо. Одна декоративная underlay слева только при stack depth>1. Close/Escape закрывает только top; lower query/modal остаётся. Focus возвращается trigger, underlying inert. Details/Edit target rule уточняет старые tabs с кнопкой edit; это не доказанная миграция production.

## Адаптация
На узком container rail ниже main, формы labels над controls; overlay уменьшается по viewport, controls остаются доступны. Новые поля/секции разрешены, footer только по режиму. Максимальная depth не задана; один scrim и одна underlay. Dependent drawer внутри modal должен блокировать только его текущий контекст.

## Эталоны / ошибки
universal-object-modal: right rail/actions; risk-view/event-view/measure-view: hierarchy/domain sections, исторические placements; risk-form/event-form/measure-form: side-label groups; components-0.269.0/src/components/{Drawer,ModalLayout}; existing patterns/specs/modal.md: stack. Запрещены: close всех окон сразу, накопление затемнений, повторение object actions в общем footer, drawer для самостоятельного linked object. Norm.open/close реализует lightweight stack; Norm.drawer поддерживает viewport/container scope, единый Escape и возврат фокуса; demo form простая, не эталон полной доменной формы. Production focus/API/type requirements остаются в поздних этапах.
