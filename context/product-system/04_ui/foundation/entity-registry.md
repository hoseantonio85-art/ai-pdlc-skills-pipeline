# Composition contract: entity registry

## Когда
Decision registry объектов. Не применять к knowledge category grid или файлам.

## Зоны / варианты
Event: card pad24, two columns660/484 при content1240, gap48. Left status/date/elapsed → gap16 → title16/20 → gap16 → metrics (label12/16 + value16/20 gap4). Right ID/author → gap16 → description ≤3 lines → gap16 → organisation. Card h160 для reference fixture; list gap8. Measure сохраняет two-zone hierarchy, title может занимать несколько строк, metrics planned/actual dates, дополнительный признак system measure; не копировать event losses. Risk: status + ID in top row, title, losses/strategy, divider, description/recommendations/measures + org. Metrics160 и gap64 в repo; list gap16.

## Обязательные связи
Identity — основной left anchor, не отдельная trailing мелкая колонка. Click opens самостоятельный объект и return сохраняет search/filter/scroll. Если внутри карточки есть independent actions, использовать article + отдельные buttons; не вкладывать button в button. Selection допускается только как отдельная задача, не выдуманный state по умолчанию.

## Геометрия и вариативность
radius16, pad24 desktop/16 compact, inset neutral line1, hover replaces inset with measured shadow. Height определяется содержимым. Не фиксировать одинаковые domain columns для всех сервисов. Статус row над заголовком допустим; не переносить его в обязательную leading column. ID/author secondary. Description truncation допустима в preview, полный текст в details.

## Состояния
Default/loading/filtered empty/error взаимоисключающие; geometry controls остаётся стабильной. Error retry сохраняет query. Registry loading skeleton по выбранной variant height. Hover не двигает соседние карточки. Не подтверждены HTML-export selection/real loading: это UX prototype implementation, не current-product fact.

## Новая задача
AI run = самостоятельная запись: title=document, status/date/time, result, ID/author, explanation/error. Не подменять историю overwrite при retry: новый ID и parent link. Новая аналитика optional above controls если это all-domain overview; если ниже controls, явно пометить scope «Обзор всех запусков», чтобы не выдавать общие числа за filtered counts.

## Эталоны / запреты

## Открытие и независимые действия (7.0.2)

Карточка самостоятельного объекта в реестре целиком кликабельна и открывает объект. Отдельная кнопка «Открыть», «Подробнее» или «Посмотреть» не нужна. Внутри допустимы только независимые действия с прямым результатом (например, повторить запуск, согласовать, скачать). Их активация не должна одновременно открывать карточку. Без внутренних действий использовать одну семантическую кнопку/ссылку карточки; при независимых действиях — article с отдельными sibling controls, доступным входом в объект с клавиатуры и обработкой клика свободной области. Не вкладывать кнопку в кнопку; не перехватывать взаимодействие с action controls и выделение текста.
