# rq.GameButtonSpec

An entry for `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The mod's own name for the entry; one per mod. |
| `label` | `string` | The text of its row in the list. |
| `on_click` | `fun(entry:` [`rq.GameButtonHandle`](rq.GameButtonHandle.md) `)` | Runs when the player picks it, after the menus close. |
| `group` *(optional)* | `"system-menu"` | The game's group. Default "system-menu", the only one for now. |
| `enabled` *(optional)* | `boolean\|fun(): boolean` | false leaves it out of the list; a function is asked each time. Default true. |
| `tip` *(optional)* | `string` | The game's comment beside the list while the row is under the mouse. |

## Used by

[`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
