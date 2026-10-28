# Organism: Object Action / Meta Zone

Status: canonical target for Object View

## Purpose

Единая правая зона объединяет сведения об объекте, history/service navigation и все object-level actions. Устраняет разнос действий между aside и нижним Footer.

## Anatomy

```txt
ActionMetaZone
├─ Metadata block
│  ├─ object ID
│  ├─ created / updated
│  ├─ author / source
│  └─ product-specific context (assessment object, owner, etc.)
├─ Context block?, optional
├─ History / service navigation
├─ Related-object action?, optional
└─ Decision/actions block
   ├─ Primary action
   ├─ Secondary action(s)
   └─ More actions
      ├─ lifecycle
      └─ destructive
```

## Placement

- desktop: right rail, NORM target width около `320px`;
- sticky внутри object workspace;
- visual blocks отделяются небольшим gap и secondary surfaces;
- responsive: rail может перейти под main content; смысловой порядок сохраняется.

## Rules

- В `view` Footer отсутствует.
- `Согласовать`, `Отклонить`, `Редактировать`, `Архив`, `Удалить` и другие object-level actions не распределяются между несколькими зонами.
- Rare/destructive actions допустимо свернуть в More.
- Action visibility приходит из permissions/workflow model, не определяется визуальным компонентом.
- History и подчинённые задачи открывают Drawer. Самостоятельный linked object открывается новой Object Modal; контекст родителя сохраняется.
- Metadata не смешивается с business content main column.

## NORM evidence

Production Risks/Measures уже имеют sticky Info + History + related action. TO-BE добавляет туда workflow actions. Это evolutionary normalization, а не новый arbitrary sidebar.
Current Risk/Event/Measure View exports могут содержать Footer; это evidence текущего состояния и не отменяет target-normalization для новых Object View.
