# rq.SettingsRow

`since 2.35.0` `changed 2.44.0`

One row of a settings page, for `rq.config.settings`.

`kind` picks the widget: "checkbox" (true or false), "stepper" (a whole number, `rq.uikit.stepper`),
"slider" (a number, `rq.uikit.slider`), "choice" (one of `options`, `rq.uikit.choice`) and "input"
(a text, `rq.uikit.input`) keep a value under `key`; "label" (a line of text) and "space" (a gap)
keep none. Each value's row checks it: a stored value it cannot take, as a number past `max` after
the mod lowered it, reads as the default.

A slider shows its value beside the track (`format`) and writes it when the knob is let go. A
stepper or a slider with `recommend` draws that range lighter on the track (a slider's), says
"Recommended: a to b" after the control (under the row when the line has no room), and asks with
the game's Yes / No when the player sets a value outside it: the question gives the value, the
range and `warn`; Yes keeps the value, No puts the range's nearest end. Moving further on the same side does not ask again. `Settings.set` and
Reset never ask.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `kind` | `"checkbox"\|"stepper"\|"slider"\|"choice"\|"input"\|"label"\|"space"` | The widget. |
| `key` *(optional)* | `string` | Where the value is kept in the store; each value row needs one, and no two rows share one. A mod that had a page of its own keeps its players' settings by naming the keys it used. |
| `label` *(optional)* | `string` | The text beside the widget. The labels of a page line up in one column. |
| `default` *(optional)* | `boolean\|integer\|number\|string` | The value before the player changes it. Default false, `min`, the first option (or the first of `values`), or "". |
| `note` *(optional)* | `string\|string[]` | Dim lines under the row, at size 15. |
| `tip` *(optional)* | `string\|` [`rq.UiTip`](rq.UiTip.md) | The game's comment window over the widget while the mouse is on it. |
| `disabled` *(optional)* | `boolean\|fun(): boolean` | Greys the row out; a function is asked on every update, as one row that follows another. |
| `id` *(optional)* | `string` | The widget's id in `rqmod-ctl ui` and `rq.ui.get`. Default `key`. |
| `w` *(optional)* | `integer` | The widget's width in pixels: a checkbox's bar, a stepper's box, a slider's track, an input's box. |
| `min` *(optional)* | `number` | A stepper's or a slider's lowest value. Default 0. |
| `max` *(optional)* | `number` | A stepper's or a slider's highest value (default 999999 and 1), or an input's longest text in bytes, 1 to 255 (default 40). |
| `step` *(optional)* | `number` | What a stepper's - and + add, or a slider's step. |
| `big` *(optional)* | `integer` | A stepper's step with Shift held. Default `step` x 10. |
| `low` *(optional)* | `string` | A slider's text at its low end. |
| `high` *(optional)* | `string` | A slider's text at its high end. |
| `format` *(optional)* | `string` | How a slider's value is written beside it, a `string.format` pattern for one number, such as "%.1f". Default "%g". Since 2.44.0. |
| `value` *(optional)* | `boolean` | false hides a slider's value. Default true. Since 2.44.0. |
| `recommend` *(optional)* | `number[]` | A stepper's or a slider's recommended range, {min, max}, inside its `min` and `max`; leaving it asks the player first. Since 2.44.0. |
| `warn` *(optional)* | `string` | What the question says past the recommended range: what goes wrong there. Needs `recommend`. Since 2.44.0. |
| `options` *(optional)* | `string[]` | A choice's texts. |
| `values` *(optional)* | `any[]` | A choice's values, one for each option; without them a choice keeps the option's number, 1 and up. |
| `dir` *(optional)* | `"row"\|"col"` | A choice's options side by side (default) or one under another. |
| `gap` *(optional)* | `integer` | A choice's gap between options, in pixels. |
| `tips` *(optional)* | `(string\|` [`rq.UiTip`](rq.UiTip.md) `)[]` | A choice's tip for each option. |
| `placeholder` *(optional)* | `string` | An input's dim text while it is empty. |
| `text` *(optional)* | `string` | A label row's text. |
| `dim` *(optional)* | `boolean` | A label row in the dim color. |
| `size` *(optional)* | `number` | A label row's text size. |
| `color` *(optional)* | `{r: integer, g: integer, b: integer}` | A label row's text color. |
| `h` *(optional)* | `integer` | A space row's height in pixels. Default 8. |

## Used by

[`rq.SettingsOpts`](rq.SettingsOpts.md)
