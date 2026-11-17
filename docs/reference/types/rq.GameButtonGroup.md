# rq.GameButtonGroup

A group, from `rq.gamebutton.groups`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | "system-menu", "skill-window", "status" or "map". |
| `open` | `boolean` | The group is on the screen now. "map": the map panel exists (a quest's map, also while it hides for a dialog or a fight). |
| `row` *(optional)* | `boolean` | "system-menu": the loader's row is in it (some entry exists). |
| `entries` | [`rq.GameButtonInfo`](rq.GameButtonInfo.md) `[]` | The entries, in the order they were added. |
| `list` *(optional)* | [`rq.GameButtonList`](rq.GameButtonList.md) | "status": the MODS button and its list. Since 2.59.0. |

## Used by

[`rq.gamebutton.groups`](../api/rq.gamebutton.md#rqgamebuttongroups)
