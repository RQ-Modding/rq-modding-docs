# rq.GameButtonSpec

An entry for `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The mod's own name for the entry; one per mod. |
| `label` | `string` | The text of its row in the list. |
| `on_click` | `fun(entry:` [`rq.GameButtonHandle`](rq.GameButtonHandle.md) `)` | Runs when the player picks it: in "system-menu" after the menus close; in "skill-window" with the window still open, after the game's click sound. |
| `group` *(optional)* | `"system-menu"\|"skill-window"` | The game's group. Default "system-menu". |
| `enabled` *(optional)* | `boolean\|fun(): boolean` | "system-menu": false leaves it out of the list. "skill-window": false greys the button (a click plays the deny sound and runs nothing). A function is asked each time the list or the window's skill list is built. Default true. |
| `tip` *(optional)* | `string` | The game's comment while the entry is under the mouse or the keys: beside the list ("system-menu"), or under the button with the label as its title ("skill-window"). |

## Used by

[`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
