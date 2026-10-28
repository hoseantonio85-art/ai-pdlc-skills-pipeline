# Composition contract: registry controls

## Когда / варианты
Поиск и уточнение множества самостоятельных объектов. Event: scope + utilities, expanded search; quick chips отсутствуют. Measures: scope / status chips + utilities; search expanded в export. Risks: section scope + utilities; далее attention summary; search может быть закрыт. AgentRisks: scope без обязательных attention/status chips. Не добавлять чипы ради одинакового вида.

## Зоны / обязательные связи
Title y40–80 → gap24 → toolbar y104–144 → gap16 → expanded search y160–208 → gap24 → list y232. Left cluster: segmented named choices, optional separator '/', optional independent chips. Right cluster: search icon then filter icon+label, gap8, align center. Ширина строки равна ширине выдачи. Search always раскрывается в пределах этого же query context.

## Геометрия / допустимые параметры
Scope h40 padding4 inner32; controls h40; expanded input48 radius16. Named choices меняют число и label, но не тип control. Набор chips — domain dependent; semantics могут быть multi-select OR внутри группы. Между scope/chips8, chips4–8 в зависимости от variant. Новые редкие фильтры идут в drawer; не превращать toolbar в форму.

## Поведение
Quick/search применяются сразу. Advanced draft копируется из applied при открытии. Apply проверяет range и меняет applied; Cancel/Escape сохраняют applied и выдачу. Clear внутри drawer очищает draft; этот эксперимент выбирает Apply для применения сброса. Repo reset у Measures очищает также статусы — отличие service-specific, его нельзя объявлять универсальным. Advanced active = dot6, не перекраска всей панели. Search active определяется заполненным input, chip active — своим pressed state. Счётчик выдачи связан с одним query. Empty объясняет действующие условия, reset сбрасывает scoped query.

## Адаптация / новое UX
В AI-реестре scope Все/Мои + multi-status В работе/Ошибка, период в drawer. Scope AND search AND period AND advanced status; quick statuses OR внутри quick group. Если same-group conditions конфликтуют, объяснить filtered empty. При laptop width допускается горизонтальный overflow chips; при compact wrap left/right clusters; не сжимать controls ниже размера. Responsive решения — hypotheses до подтверждения repo breakpoint.

## Эталоны / запрещённые ошибки
event-list nodes #2395_81086,#2395_81161,#2395_81214; measure-list #2395_99039…#2395_99147; Risks/Measures src/pages/{Risks,Measures}/components/{Filters,QuickFilters}; UI Kit RadioChips/CheckboxChips. Запрещены: binary switch вместо named choices, search/filter слева перед scope без UX-основания, desktop utilities в независимом ряду при достаточной ширине, modal вместо filter drawer, применение draft при cancel, декоративные chips без фильтрации. Реализация: starter norm-components.css + prototype.js query/draft lifecycle.
