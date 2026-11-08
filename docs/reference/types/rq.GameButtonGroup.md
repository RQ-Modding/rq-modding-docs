# rq.GameButtonGroup

A group, from `rq.gamebutton.groups`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | "system-menu" or "skill-window". |
| `open` | `boolean` | The group is on the screen now. |
| `row` *(optional)* | `boolean` | "system-menu": the loader's row is in it (some entry exists). |
| `entries` | [`rq.GameButtonInfo`](rq.GameButtonInfo.md) `[]` | The entries, in the order they were added. |

## Used by

[`rq.gamebutton.groups`](../api/rq.gamebutton.md#rqgamebuttongroups)
