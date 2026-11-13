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
| `comment` *(optional)* | `string` | Shown in the game's comment window right of the list, at the row, while the mouse or the keys' cursor stays on the row (as the game's menu shows it). Before 2.13.0, a plain box at once. Its lines are cut as `rq.UiChoice.comment`'s, at most 28 half-width letters, since 2.45.1. |
| `disabled` *(optional)* | `boolean` | Greyed out; it cannot be picked. |

## Used by

[`rq.uikit.options`](../api/rq.uikit.md#rquikitoptions)
