# rq.UiChoice

`since 2.7.0`

One row of `rq.ui.choose`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `any` | What `fn` gets for this row: any value but nil. Default: its place in the list, counting separators. |
| `text` | `string` | The text. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default: the game's grey. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default: the game's grey. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default: the game's grey. |
| `comment` *(optional)* | `string` | Shown in the game's comment box beside the menu while the row is under the mouse. |
| `sound` *(optional)* | `integer` | A sound number the row plays when picked; default the game's. |

## Used by

[`rq.ui.choose`](../api/rq.ui.md#rquichoose)
