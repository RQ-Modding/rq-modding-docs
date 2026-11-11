# rq.UiItemWindowEntry

`since 2.32.0`

An entry of `rq.uikit.item_window`'s list, when a tile needs more than the item.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `item` | `integer\|` [`rq.UiItemRow`](rq.UiItemRow.md) | The tile's item: an instance or row data, as `rq.uikit.item_icon` takes. |
| `judged` *(optional)* | `boolean` | false: the tip is the game's UNIDENTIFIED card. Default true. |
| `tip` *(optional)* | `string\|false` | The tile's tip instead of the item card, or false for none. |
| `disabled` *(optional)* | `boolean` | The tile darkened; it cannot be clicked. |

## Used by

[`rq.uikit.item_window`](../api/rq.uikit.md#rquikititem_window)
