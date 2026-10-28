---
name: 03-build-visual-html-prototype
description: >-
  Третий этап продуктового pipeline: создаёт быстрый интерактивный HTML/CSS/JavaScript-прототип по Business Intent, Product Brief и утверждённому UX Solution, обязательно начиная с визуальных правил и HTML-starter выбранного продукта. Используй для проверки UX-концепции и визуальной композиции. Прототип не является production contract: production-архитектура, настоящий UI Kit, API, i18n и строгая типизация здесь не требуются.
---

# Build Visual HTML Prototype

## Input gate

Начинай, если доступны:

- Product Task Brief со статусом `READY_FOR_UX`;
- Business Intent со статусом `READY_FOR_UX`;
- UX Solution со статусом `READY_FOR_PROTOTYPE`;
- выбранный product context (явно либо default NORM через registry по протоколу ниже);
- visual context и хотя бы базовый HTML starter.

Если UX Solution не определяет основной сценарий, surfaces или информационный приоритет, верни `BLOCKED_BY_UX_HANDOFF`.

## Context loading

Сначала возьми разрешённый контекст и список источников из UX Solution. Если trace неполон, повтори штатный протокол:

1. прочитай `context_id` из `<project>/.gigacode/product-context.yaml`;
2. открой `~/.gigacode/product-contexts.yaml`;
3. найди `contexts[context_id]`;
4. возьми `provider.root` и `provider.manifest`;
5. открой `<provider.root>/<provider.manifest>` и проверь совпадение `context_id`.

Не подменяй этот протокол поиском соседней папки.

Открой manifest, прочитай `loading.always` и профиль `for_visual_html_prototype`. Прочитай все файлы, явно перечисленные в этом профиле. Если manifest содержит `prototype.routing`, используй его как index-first router:

- `visual_profile` — product-specific visual DNA;
- `pattern_registry` — список доступных patterns и runtime overlays;
- `organism_registry` — повторяемые composition contracts.

После чтения registry выбери только patterns/organisms, которые нужны surfaces из UX Solution. Не bulk-load весь каталог. По умолчанию соблюдай бюджеты из registry; если бюджет отсутствует, ориентир: до 4 runtime patterns, до 3 organisms и до 2 HTML references на одну задачу. Полные authoring specs и audit открывай только для разрешения противоречия или спорного решения.

Для NORM прочитай `04_ui/references/reference-registry.yaml` как compact aspect-level index. Он нормализует owner-provided HTML/Pixso evidence: выбирай reference **по аспекту**, а не по сходству whole screen. Raw external exports не являются runtime requirement. Внешние HTML scenes не входят в этот пакет; открывай их через `~/.gigacode/product-evidence.yaml` только при реальном доступе и необходимости. Если источник не подключён — `NEEDS_SOURCE`, не выдумывай evidence.

Patterns не являются жёсткими screen templates. Перед сборкой классифицируй выбранные источники: `invariant` (обязательный contract), `strong-default` (проверенная композиция) или `reference` (визуальный ориентир). Strong defaults разрешено адаптировать. Если существующая композиция не решает задачу, предложи `composition-adaptation` / `new-pattern-candidate`, сохрани invariants и Visual DNA и зафиксируй rationale в handoff.

Если выбран product context, но manifest или профиль не открыты, верни `BLOCKED_BY_CONTEXT`; не создавай generic prototype под видом продукта. Не загружай документацию всего UI Kit. На этом этапе не подключай настоящий UI Kit, если пользователь явно не попросил иначе.

Для NORM дополнительно:

- При проектировании Drawer сверяйся с `patterns/runtime/drawer.md`: Escape по умолчанию выключен, в ORM внешний Close допустим, нет жёсткого максимума в два Drawer; не заменяй эти решения старым поведением HTML-starter.

- `norm-visual-dna.md` и runtime overlay pattern registry являются product-likeness guardrails;
- `object-modal-view` использует единую правую action/meta zone и не имеет общего Footer;
- полный `modal-and-drawer.md` и shell specs открывай только при соответствующих surfaces или конфликте правил.

## Visual Foundation and composition preflight

В этом пакете NORM — default context, если пользователь не выбрал другой. Сохраняй selector/provider protocol: default не разрешает угадывать provider.root. Если project selector отсутствует, используй norm только через запись contexts.norm в registry; при отсутствии registry сохраняется BLOCKED_BY_CONTEXT. Чужой product context не загружает NORM Foundation.

Основной режим NORM — **Product Fidelity**. По явному запросу UX-концепции используй **Concept Exploration**: новые композиции допустимы, Visual DNA и семантика контролов остаются обязательными. Это внутренняя настройка из UX Solution/промпта, не новое публичное API.

Для NORM профиль теперь явно загружает foundation/visual-dna.md, composition-index.json и source-policy.md. При конфликте геометрии/цветов применяй измеренный Foundation contract выбранного варианта; semantic invariants runtime patterns сохраняются. Historical HTML scenes показывают только отношения зон, их tokens/geometry/interactions не заменяют Foundation. При конфликте UX flow с invariant остановись на согласовании UX, не выбирай молча. После index прочитай только contracts выбранных surfaces и компонентную реализацию из starter. Не считай индекс фактически прочитанным contract.

До записи HTML составь внутренний preflight без дополнительного подтверждения пользователя: UX zone → intent → ближайший product variant → evidence/revision → reused component/slots → new/adapted zone → invariant/variation → QA region. Отдельно объясни решение об аналитике. Не копируй весь экран. Фиксируй неизвестные geometry/состояния как hypotheses, а не current product truth. Добавляй preflight в 03_visual_prototype.md.

Для registry выбери event-two-zone / measure-status-chips / risk-attention по смыслу; нельзя автоматически выравнивать их внутренние карточки. Если controls не помещаются, сохраняй левую/правую группы при достаточной ширине; затем адаптируй overflow/wrap по contract. Нельзя сжимать target design canvas для получения ложного сходства.

## Обязательный starter gate

Не начинай HTML с пустого файла, если выбранный product context объявляет starter.

1. Найди `prototype.starter.path` в manifest выбранного продукта.
2. Открой starter-файлы, чтобы понять shell, tokens, layout, demo controls и базовые interactions. Для NORM прочитай `04_ui/foundation/starter-contract.md`: границы реализации вариантов, порядок assets и общий lifecycle поверхностей.
3. Скопируй весь starter в целевую директорию прототипа без изменения структуры файлов, включая assets/icon_logo.svg и assets/gradient-logo.svg. Используй настоящие SVG через Norm.brand(), не рисуй их заменители.
4. Только после копирования адаптируй starter под UX Solution. Сохраняй исходное разделение файлов starter, если manifest не задаёт другое.
5. Используй существующие CSS variables, shell и композиционные primitives starter. Для NORM копируй также norm-components.css и norm-components.js; CSS подключай после styles.css, JS перед prototype.js. Компоненты лёгкие и не подменяют production UI Kit. Существенные отклонения перечисляй в handoff.

Backward compatibility: если `context_id: norm`, а `prototype.starter.path` отсутствует в старом manifest, разрешён fallback на `assets/norm-html-starter` внутри активного skill. Этот fallback не является новой архитектурой и сохраняется только для совместимости с предыдущими NORM context packages.

Если manifest содержит `prototype.reference_scenes`, открывай только доступную scene, связанный с выбранной surface и действительно нужный для product likeness. HTML reference — visual/composition evidence, а не источник production DOM/API.

После адаптации проверь происхождение каждого brand/action token. Для NORM не объявляй синий новым основным цветом: базовые действия должны наследовать зелёный, тёмный нейтральный и мягкие нейтральные стили product starter. Для другого продукта используй его собственный visual profile/starter, не NORM fallback.

Если обязательный product starter отсутствует, не читается или не может быть скопирован, верни `BLOCKED_BY_VISUAL_CONTEXT`. Не заменяй его самодельным generic HTML.

## Priorities

1. UX clarity.
2. Product likeness.
3. Visual hierarchy and composition.
4. Scenario completeness.
5. Plausible content.
6. Sufficient prototype code quality.

## Workflow

1. Прочитай Intent, Brief и UX Solution; Intent используй как outcome guardrail, Brief — как product truth. Не меняй flow молча.
2. По pattern/organism registries выбери минимальный набор runtime contracts для surfaces из UX Solution. Для любой collection сначала определи intent: decision registry, navigation collection или compact content/file list.
3. Выполни обязательный starter gate; не создавай альтернативную заготовку.
4. Составь короткий visual plan: shell, surfaces, hierarchy, density, states, interactions. Для registry/monitoring surface обязательно ответь, нужен ли situational overview/interactive analytics; не делай bare card list механическим default, если aggregate view реально сокращает интерпретацию.
5. Используй product visual profile и только релевантные reference scenes. Для NORM применяй `product-likeness.md` и `norm-visual-dna.md`; не вставляй dock, attention zones, AI gradient, analytics или Object Modal только ради сходства.
6. Создай правдоподобные fixtures на русском языке.
7. Реализуй happy path и критические альтернативные состояния.
8. Добавь только взаимодействия, необходимые для демонстрации решения.
   Если acceptance criteria проверяют переход в другой объект/surface и возврат с сохранением контекста, этот round-trip обязан быть интерактивно прототипирован. Toast/закрытие текущей modal без destination state не считается реализацией навигации. Если полный source service избыточен, сделай lightweight representative destination surface и реальный путь возврата.
9. Открой прототип в доступном browser/preview и проверь desktop layout.
10. Исправь очевидные проблемы композиции после первого render.
11. Сохрани прототип и короткий handoff.

## Implementation rules

- Предпочитай обычные HTML, CSS и JavaScript; React допустим, если уже есть подходящий starter или сложное состояние.
- Используй CSS variables визуального контекста.
- Допускай локальные prototype-компоненты без имитации API настоящего UI Kit.
- Не называй самодельные компоненты внутренним пакетом UI Kit и не создавай ложный alias.
- Не добавляй production layers, stores, API clients, i18n и тесты без необходимости.
- Не превращай имена переменных, mock data, DOM structure или demo behavior прототипа в production contract.
- Отделяй demo scenario controls от продуктовой поверхности.
- Не используй изображения как обязательный вход: GigaCode должен работать по текстовым правилам и assets.
- Создавай и изменяй Markdown, HTML, CSS и JavaScript файловыми инструментами редактирования. Не передавай содержимое документов в shell построчно. Shell используй только для запуска, сборки и проверки.
- Не подключай Google Fonts, CDN и другие внешние runtime-зависимости. Используй системный font stack или локальные assets starter.
- Не объединяй starter в один HTML-файл, если пользователь явно не запросил single-file artifact.
- Наличие одного большого HTML с встроенными CSS/JavaScript при доступном starter считается нарушением starter gate, а не допустимым упрощением.

## NORM rules

- Не используй классические таблицы как основной реестр.
- Используй card registry или row-cards с приоритетом, объяснением и действием. Карточка целиком открывает объект; отдельные «Открыть/Подробнее» не добавлять. Внутренние кнопки допустимы для независимых прямых действий, не запускающих открытие; избегай вложенных interactive controls.
- Dashboard или compact situational overview допустим и желателен для обзора, мониторинга или зон внимания, если aggregate story помогает понять ситуацию и ведёт к drill-down/filter/action. На registry page явно проверь этот вариант вместо автоматической выдачи только карточек.
- Используй floating action dock, когда основное действие или AI/chat должно оставаться доступным при прокрутке. Текстовые кнопки растягиваются на всю свободную ширину dock и делят её поровну; AI-icon сохраняет фиксированный размер.
- Используй emoji точечно, но не вместо системной визуальной семантики целиком.
- Не делай summary обязательной декоративной секцией: добавляй её, когда она сокращает работу интерпретации.
- На desktop registry toolbar соблюдай strong-default `segmented scope + quick chips` слева и `search/filter utilities` справа в одной строке; binary Switch не использовать для `Все / Мои`.
- Identity/name остаётся левым anchor entity row-card; status не делать обязательной leading-колонкой перед названием.

## Required states

Реализуй default и все состояния, критичные для UX acceptance criteria. Обычно это loading, empty, error и один action progress/success. Не создавай пять декоративных сценариев, если они не проверяют решение.

## Evidence-based visual QA

Для NORM прочитай foundation/visual-qa.md после выбора эталонов. Если browser renderer доступен, обязательны одинаковые viewport/DPR, скриншоты default и выбранных interactive states, геометрия зон и проверка сценариев. При дефекте исправь реализацию и повтори затронутые проверки. При недоступном рендеринге сохрани READY_WITHOUT_VISUAL_REVIEW.

Разделяй C (компоненты), P (повторяемая композиция), U (новая UX-композиция), F (функциональность). Цель 95% относится только к определённому comparable C/P coverage с измерениями, не к новой странице в целом. Не переводить субъективное сходство или успешную загрузку в процент. Отдельно сообщать geometry pass rate, pixel differences и ограничения источника. Минимум native design viewport и адаптированный laptop viewport; формы, drawer, empty/error и stack проверяются по scenario acceptance.

## Visual quality gate

Перед статусом пройди чек-лист. Не ставь PASS только потому, что страница открылась.

### Семантика и сценарий

- основной сценарий можно пройти от входа до результата;
- активный пункт навигации соответствует странице и заявленной архитектуре;
- объекты, события и состояния не подменяют друг друга;
- повторный запуск или новая версия создаёт новую запись и связь с исходной, а не переписывает историю;
- числа, подписи, счётчики, фильтры и fixtures согласованы между экранами;
- входы в ассистента не дублируются без разных и понятных задач.

### Состояния и взаимодействия

- default, loading, empty и error взаимоисключающие;
- empty state соответствует активным фильтрам и предлагает релевантный следующий шаг;
- карточка открывается по клику и с клавиатуры без отдельной кнопки открытия; independent action не открывает карточку;
- demo controls визуально отделены от продуктовой поверхности;
- modal/drawer открывается и закрывается ожидаемо, сохраняет контекст и выдерживает длинный контент;
- navigation acceptance criteria проверены реальным destination/return state, а не toast-имитацией;
- размер surface соответствует UX Solution: большая Object Modal действительно использует доступное пространство;
- floating dock не перекрывает последний контент и действия; текстовые кнопки заполняют свободную внутреннюю ширину, icon не растягивается.
- одинаковый primary CTA не дублируется в header, строках и floating dock без разных задач;

### Композиция и техническая целостность

- первый экран объясняет приоритет и следующий шаг;
- для registry/monitoring page проверено, нужен ли situational overview; если analytics добавлена, она отвечает на конкретный вопрос и связана с detailed layer, а не является KPI-декором;
- интерфейс использует shell, tokens и primitives starter, а не пересобран по памяти;
- узнаваемые shell, card hover, modal и dock-параметры сверены с `product-likeness.md`, но применены только по сценарию;
- primary, secondary, text и destructive actions визуально различаются; заполненный primary не повторяется в каждой строке реестра;
- NORM не получил самодельный синий brand: action tokens сверены со starter и `visual-language.md`;
- card registry быстро сканируется, строки не избыточно высокие;
- нет наложений, обрезанного текста, прыгающих блоков и недоступных действий на проверенных viewport;
- внешние CDN и подмена UI Kit отсутствуют;
- HTML, CSS и JavaScript загружаются без явных ошибок.
- сохранены отдельные `index.html`, `styles.css` и `prototype.js`, а для текущего NORM starter также `norm-components.css` и `norm-components.js`; single-file без прямого запроса получает `NEEDS_VISUAL_FIX`.

Если доступен browser/preview, проверь минимум desktop viewport, каждое обязательное состояние и открытые modal/drawer. Если модель не может визуально оценить render, честно используй `READY_WITHOUT_VISUAL_REVIEW`. `PASS` допустим только после фактической визуальной проверки всего чек-листа. При найденных дефектах используй `NEEDS_VISUAL_FIX`, исправь их и повтори проверку.

## Output

Сохрани запускаемый проект и обязательный `03_visual_prototype.md` с разделами: Context trace, реально прочитанные visual sources, путь использованного product starter, выбранные runtime patterns/organisms, использованные reference scenes, сохранённые starter-файлы, visual plan, реализованные сценарии, режим fidelity, composition preflight, reused/new inventory, QA evidence и comparable coverage, отклонения от UX Solution и starter, результаты чек-листа по группам, проверенные viewport, ограничения и статус. Не заявляй проверки, которые фактически не выполнялись. Без этого файла этап не завершён.

## Внешние источники и ограничения поставки

Встроены только product rules и starter. Репозитории, OpenSpec, UI Kit и внешние HTML-референсы подключаются через `~/.gigacode/product-evidence.yaml` на рабочем компьютере. Не генерируй фиктивные пути/URL и не утверждай, что недоступные источники были прочитаны. Сначала делай доступные UX/visual действия; точные API и реализационные ограничения требующие evidence — `NEEDS_SOURCE`.
