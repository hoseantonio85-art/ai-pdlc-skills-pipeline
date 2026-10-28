# Object Modal / View — runtime pattern

## Intent

Полноценный просмотр самостоятельного объекта без потери родительского registry context.

## Shared composition

```txt
Object Modal / View
├─ Top controls: Back? / Close
├─ Object header
│  ├─ identity/status
│  ├─ title/description
│  └─ local section navigation / Edit, optional
└─ Scroll workspace
   ├─ Main content
   └─ ActionMetaZone
```

## Hard rules

- Object View **не имеет общего Footer**.
- Все object-level workflow, lifecycle и destructive actions просмотра — в `ActionMetaZone` или её More-actions.
- Local actions внутри content остаются рядом со своим блоком.
- Связанный самостоятельный объект открывается новой Object Modal в stack.
- Подчинённая задача открывается Drawer.
- Create/Edit — отдельный mode с fixed Footer.

## NORM profile

- max-width `1320px`;
- radius `24px`;
- viewport padding `24px`;
- main + rail;
- rail desktop target `320px`;
- rail может перестраиваться под main при узком container;
- close/back group расположен внутри верхней области, product evidence `top 32 / right 40`.

## TO-BE reconciliation

`risk-Modals.png` считается canonical evidence для:

- объединения metadata и object actions в правую rail;
- visual grouping rail blocks;
- workflow actions справа.

Нижние `Удалить / В архив` на TO-BE screenshot **не являются canonical**: актуальное правило Object View запрещает общий Footer.
