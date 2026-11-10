# rq.UiAskRow

One row of `rq.ui.ask`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `any` | What `ask` returns for this row: any value but nil. Default: its place in the list, counting separators. |
| `text` | `string` | The text. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default: the game's grey. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default: the game's grey. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default: the game's grey. |
| `comment` *(optional)* | `string` | Shown in the game's comment box beside the dialog while the row is under the mouse. |
| `sound` *(optional)* | `integer` | A sound number the row plays when picked; default the game's. |

## Used by

[`rq.ui.ask`](../api/rq.ui.md#rquiask)
