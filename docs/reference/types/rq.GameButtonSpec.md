# rq.GameButtonSpec

An entry for `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The mod's own name for the entry; one per mod. |
| `label` | `string` | The text of its row in the list. |
| `on_click` *(optional)* | `fun(entry:` [`rq.GameButtonHandle`](rq.GameButtonHandle.md) `)` | Runs when the player picks it: in "system-menu" after the menus close; in "skill-window", "status" and "map" with the window, page or map still there, after the game's click sound. Needed everywhere but in "status"'s `spot = "left"`, whose icons take no click (an error there). |
| `group` *(optional)* | `"system-menu"\|"skill-window"\|"status"\|"map"` | The game's group. Default "system-menu". "map" since 2.32.0. |
| `spot` *(optional)* | `"title"\|"left"` | "status" only: `"title"` (the default), a button in the title row by the X; `"left"`, an icon that is not a button at the left end of the LV row, under the class icon (see `rq.gamebutton`). Since 2.58.0. |
| `enabled` *(optional)* | `boolean\|fun(chara?: integer): boolean` | "system-menu": false leaves it out of the list. "skill-window", "status" and "map": false greys the button (a click plays the deny sound and runs nothing). A function is asked each time the list or the window's skill list is built, in "status" on every draw of the card, with the character shown, and in "map" every 200 ms while the map shows, with no argument. Default true. |
| `tip` *(optional)* | `string\|fun(chara: integer): string` | The game's comment while the entry is under the mouse or the keys: beside the list ("system-menu"), under the button with the label as its title ("skill-window"), or beside the icon with the label as its title ("status", also on a greyed one; "map", left of the tab). A function only in "status" and "map", asked when the tip opens (in "status" with the character shown); nil or "" shows none. In "status" and "map", `\n` starts a line. |
| `icon` *(optional)* | `integer\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): integer` | "status" and "map" only, and needed there: the CG drawn as the button, such as one from `rq.image.add` or `rq.image.compose`. The cell is 32 × 29 in "status"'s title row, 32 × 26 in its left spot, and 32 × 34 inside the 40 × 44 tab in "map": a smaller icon is centered, a larger one shrunk to fit. In "status" it may be a function, asked on every draw of the card with the character shown and how the page was opened (since 2.58.0); an answer that is not a CG number leaves the entry out of that draw, and the log says so once. Since 2.20.0. |
| `shown` *(optional)* | `boolean\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): boolean` | "status" and "map" only: false leaves the button out, and the next entry takes its cell. A function is asked on every draw of the card in "status", and every 200 ms while the map shows in "map" (with no argument). Default true. Since 2.20.0. |

## Used by

[`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
