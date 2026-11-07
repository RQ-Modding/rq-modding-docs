# rq.AgentOpts

How `rq.agent.control` finds a control: a game button, or a rectangle a mod draws.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `label` *(optional)* | `string` | The text `rqmod-ctl ui` shows for the control. |
| `button` *(optional)* | `integer` | The game's `T_Button` id. Leave it out for a HUD rectangle and give `x`, `y`, `w`, `h`. |
| `hoverOnly` *(optional)* | `boolean` | The control exists only while the cursor is already on its parent. |
| `x` *(optional)* | `integer` | Left edge of a HUD rectangle, in game pixels. |
| `y` *(optional)* | `integer` | Top edge of a HUD rectangle, in game pixels. |
| `w` *(optional)* | `integer` | Width of a HUD rectangle, in game pixels. |
| `h` *(optional)* | `integer` | Height of a HUD rectangle, in game pixels. |

## Used by

[`rq.agent.control`](../api/rq.agent.md#rqagentcontrol)
