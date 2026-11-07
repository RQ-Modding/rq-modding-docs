# rq.UiOptionRow

`since 2.7.0`

One row of `rq.uikit.options`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` *(optional)* | `any` | What `options` returns for this row. Default: its place in the list, counting separators. |
| `text` | `string` | The text. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default: the game's grey. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default: the game's grey. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default: the game's grey. |
| `comment` *(optional)* | `string` | Shown in a box right of the list while the row is under the mouse. |
| `disabled` *(optional)* | `boolean` | Greyed out; it cannot be picked. |

## Used by

[`rq.uikit.options`](../api/rq.uikit.md#rquikitoptions)
