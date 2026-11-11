# rq.UiItemWindowOpts

`since 2.32.0`

Options for `rq.uikit.item_window`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `string\|integer` | Keeps its state (the page shown) and names its controls. Default "itemwindow". |
| `title` *(optional)* | `string` | Text in the grey band at the top left, in the game's font; cut where it would reach the page arrows. |
| `rows` *(optional)* | `integer` | Rows of five tiles, 1 to 5. Default 3, or 4 with more than 15 items. |
| `x` *(optional)* | `integer` | The left edge, in game pixels. Default 473, the game's. |
| `y` *(optional)* | `integer` | The top edge, in game pixels. Default 165, the game's, or higher for a window that would go past y 607 (the 3D view's bottom). |
| `empty` *(optional)* | `string` | Text in the window's middle when the list is empty. |
| `cell` *(optional)* | `fun(index: integer, x: integer, y: integer, entry: any)` | Called after each tile is drawn, with the item's place in the list, the tile's top left (100 × 100) and the list's value, to draw marks on it. |

## Used by

[`rq.uikit.item_window`](../api/rq.uikit.md#rquikititem_window)
