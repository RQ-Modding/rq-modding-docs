# rq.GameButtonList

The status page's MODS button and its list, as `rq.gamebutton.groups` gives them.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `shown` | `boolean` | MODS is on the page (on its last draw). |
| `open` | `boolean` | The list is open under it. |
| `button` *(optional)* | `integer` | MODS's `T_Button` id, 100105, while it shows. |
| `x` *(optional)* | `integer` | MODS's left edge, 436, while it shows. |
| `y` *(optional)* | `integer` | MODS's top edge, 62, while it shows. |
| `width` *(optional)* | `integer` | The rows' width, 68 to 320, while it shows; they end at x 504. |
| `rows` | `string[]` | The rows' entries (`<mod id>.<id>`), top to bottom; empty while MODS is not shown. |

## Used by

[`rq.GameButtonGroup`](rq.GameButtonGroup.md)
