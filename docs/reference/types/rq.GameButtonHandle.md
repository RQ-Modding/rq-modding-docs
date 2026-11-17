# rq.GameButtonHandle

An entry, from `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `fun(): string` | `<mod id>.<id>`. |
| `set` | `fun(opts: {label?: string, enabled?: boolean\|fun(chara?: integer): boolean, tip?: string\|fun(chara: integer): string?, icon?: integer\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): integer, shown?: boolean\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): boolean, text?: string\|fun(chara: integer, mode:` `rq.StatusPageMode` `?): string?})` | Changes it; `tip = ""` removes the tip, `text = ""` the text (an error for an entry with no icon). In "skill-window" a new label or `enabled` shows from the next build of the skill list (`rq.skilllist.refresh` builds it at once). In "status" it shows at once while the page is open, and in "map" on the next frame; `icon` and `shown` are for "status" (2.20.0) and "map" (2.32.0) only, `icon` a function in "status" only (2.58.0), and `text` for "status"'s title spot only (2.59.0). The `spot` and `list` stay as added. |
| `state` | `fun():` `rq.GameButtonState` `\|nil` | "status": where it is on the page's last draw (`"hidden"` while the page is closed); nil in the other groups. Since 2.59.0. |
| `remove` | `fun()` | Takes it out. "system-menu": with no entry left, the MODS row goes as well. "skill-window": the button goes at once; the others move up on the next build. "status": the button goes at once, and the next entry takes its cell. "map": the tab goes on the next frame, and the tabs under it move up. |

## Used by

[`rq.GameButtonSpec`](rq.GameButtonSpec.md), [`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
