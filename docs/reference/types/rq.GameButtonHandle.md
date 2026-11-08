# rq.GameButtonHandle

An entry, from `rq.gamebutton.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `fun(): string` | `<mod id>.<id>`. |
| `set` | `fun(opts: {label?: string, enabled?: boolean\|fun(): boolean, tip?: string})` | Changes it; `tip = ""` removes the tip. |
| `remove` | `fun()` | Takes it out. With no entry left, the MODS row goes as well. |

## Used by

[`rq.GameButtonSpec`](rq.GameButtonSpec.md), [`rq.gamebutton.add`](../api/rq.gamebutton.md#rqgamebuttonadd)
