# rq.GameButtonInfo

An entry, as `rq.gamebutton.groups` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | `<mod id>.<id>`. |
| `mod` | `string` | The mod that added it. |
| `label` | `string` | Its text. |
| `enabled` | `boolean` | "system-menu": it is in the list now. "skill-window": it is not greyed now. |
| `placed` *(optional)* | `boolean` | "skill-window": it has a cell on the last build. Since 2.17.0. |
| `button` *(optional)* | `integer` | "skill-window": its `T_Button` id on the window now, 200101 to 200104. Since 2.17.0. |
| `x` *(optional)* | `integer` | "skill-window": its cell's left edge, in game pixels. Since 2.17.0. |
| `y` *(optional)* | `integer` | "skill-window": its cell's top edge, in game pixels. Since 2.17.0. |

## Used by

[`rq.GameButtonGroup`](rq.GameButtonGroup.md)
