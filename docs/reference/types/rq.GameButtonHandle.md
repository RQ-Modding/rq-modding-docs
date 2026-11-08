# rq.GameButtonHandle

An entry, from `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `fun(): string` | `<mod id>.<id>`. |
| `set` | `fun(opts: {label?: string, enabled?: boolean\|fun(): boolean, tip?: string})` | Changes it; `tip = ""` removes the tip. In "skill-window" a new label or `enabled` shows from the next build of the skill list (`rq.skilllist.refresh` builds it at once). |
| `remove` | `fun()` | Takes it out. "system-menu": with no entry left, the MODS row goes as well. "skill-window": the button goes at once; the others move up on the next build. |

## Used by

[`rq.GameButtonSpec`](rq.GameButtonSpec.md), [`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
