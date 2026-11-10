# rq.GameButtonSpec

An entry for `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The mod's own name for the entry; one per mod. |
| `label` | `string` | The text of its row in the list. |
| `on_click` | `fun(entry:` [`rq.GameButtonHandle`](rq.GameButtonHandle.md) `)` | Runs when the player picks it: in "system-menu" after the menus close; in "skill-window" and "status" with the window or page still open, after the game's click sound. |
| `group` *(optional)* | `"system-menu"\|"skill-window"\|"status"` | The game's group. Default "system-menu". |
| `enabled` *(optional)* | `boolean\|fun(chara?: integer): boolean` | "system-menu": false leaves it out of the list. "skill-window" and "status": false greys the button (a click plays the deny sound and runs nothing). A function is asked each time the list or the window's skill list is built, and in "status" on every draw of the card, with the character shown. Default true. |
| `tip` *(optional)* | `string\|fun(chara: integer): string` | The game's comment while the entry is under the mouse or the keys: beside the list ("system-menu"), under the button with the label as its title ("skill-window"), or beside the icon with the label as its title ("status", also on a greyed one). A function only in "status", asked with the character shown when the tip opens; nil or "" shows none. In "status", `\n` starts a line. |
| `icon` *(optional)* | `integer` | "status" only, and needed there: the CG drawn as the button, such as one from `rq.image.add` or `rq.image.compose`. The cell is 32 × 29: a smaller icon is centered, a larger one shrunk to fit. Since 2.20.0. |
| `shown` *(optional)* | `boolean\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): boolean` | "status" only: false leaves the button out of the title row, and the next entry takes its cell. A function is asked on every draw of the card. Default true. Since 2.20.0. |

## Used by

[`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
