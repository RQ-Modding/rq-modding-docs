# rq.UiStepperOpts

`since 2.22.0`

What `rq.uikit.stepper` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `min` *(optional)* | `integer` | The lowest number. Default 0. |
| `max` *(optional)* | `integer` | The highest number. Default 999999. |
| `step` *(optional)* | `integer` | What - and + add or take, the wheel and Page Up / Page Down too. Default 1. |
| `big` *(optional)* | `integer` | The same with Shift held. Default `step` x 10. |
| `label` *(optional)* | `string` | Text left of the field, in the theme's label font. Also its label in `rqmod-ctl ui`. |
| `disabled` *(optional)* | `boolean` | Greyed: no buttons, no typing, no wheel. Its tip still shows. |
| `h` *(optional)* | `integer` | The field's height in pixels, 18 to 30; the buttons are square, their text smaller. Default 30. Since 2.49.0. |
| `ends` *(optional)* | `"max"\|"min"\|true` | A MAX button after +, a MIN button before -, or both. Since 2.49.0. |

## Used by

[`rq.uikit.stepper`](../api/rq.uikit.md#rquikitstepper)
