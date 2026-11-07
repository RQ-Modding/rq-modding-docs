# rq.AgentWidget

A control a mod drew on this update, for `rqmod-ctl ui`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | ASCII, no spaces, under 40 characters. |
| `label` *(optional)* | `string` | The text the dump shows. |
| `type` *(optional)* | `string` | The kind of control. Default "button"; `rq.uikit` uses text, button, check, slider, tab and row. |
| `value` *(optional)* | `string\|number\|boolean` | The control's value, such as "on" for a checkbox. |
| `selected` *(optional)* | `boolean` | The control is the chosen one (a tab, a list row, a checked box). |
| `disabled` *(optional)* | `boolean` | The control does not take input. |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` | `integer` | Width, in game pixels. |
| `h` | `integer` | Height, in game pixels. |

## Used by

[`rq.agent.widgets`](../api/rq.agent.md#rqagentwidgets)
