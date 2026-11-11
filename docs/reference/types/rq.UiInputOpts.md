# rq.UiInputOpts

`since 2.29.0`

What `rq.uikit.input` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `w` *(optional)* | `integer` | The box's width in pixels (not "fill"). Default 240. |
| `max` *(optional)* | `integer` | The longest the text may be, in bytes, 1 to 255. Default 40. |
| `label` *(optional)* | `string` | Text left of the box, in the theme's label font. Also its label in `rqmod-ctl ui`. |
| `placeholder` *(optional)* | `string` | Dim text in the box while the text is empty and it does not type. |
| `focus` *(optional)* | `boolean` | Types from the update the field first shows (again after it was not drawn for an update), as a name prompt does. |
| `disabled` *(optional)* | `boolean` | Greyed: no typing. A field that types stops, with its old text back. |

## Used by

[`rq.uikit.input`](../api/rq.uikit.md#rquikitinput)
