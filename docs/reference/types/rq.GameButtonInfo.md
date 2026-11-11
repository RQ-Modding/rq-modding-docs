# rq.GameButtonInfo

An entry, as `rq.gamebutton.groups` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | `<mod id>.<id>`. |
| `mod` | `string` | The mod that added it. |
| `label` | `string` | Its text. |
| `enabled` | `boolean` | "system-menu": it is in the list now. "skill-window", "status" and "map": it is not greyed now. |
| `placed` *(optional)* | `boolean` | "skill-window", "status" and "map": it has a cell on the last build or draw (in "map": a tab on the map now). Since 2.17.0. |
| `shown` *(optional)* | `boolean` | "status" and "map": `shown` said yes on the last draw or ask. Since 2.20.0. |
| `button` *(optional)* | `integer` | "skill-window": its `T_Button` id on the window now, 200101 to 200104; "status": on the page now, 100101 or 100102; "map": on the map panel now, 700101 to 700104. Since 2.17.0. |
| `x` *(optional)* | `integer` | "skill-window", "status" and "map": its cell's left edge, in game pixels. Since 2.17.0. |
| `y` *(optional)* | `integer` | "skill-window", "status" and "map": its cell's top edge, in game pixels. Since 2.17.0. |

## Used by

[`rq.GameButtonGroup`](rq.GameButtonGroup.md)
