# rq.UiPlace

Where a widget goes.

Without `x` and `y` it goes where its row or column puts it. A widget given both `x` and `y` stands
where it says and does not move the row on.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` *(optional)* | `integer` | Left edge, in game pixels. |
| `y` *(optional)* | `integer` | Top edge, in game pixels. |
| `w` *(optional)* | `integer\|"fill"` | Width in pixels, or "fill": the width left in the row, or the column's width less its pad. "fill" needs a row or column with a `w`. |
| `h` *(optional)* | `integer` | Height in pixels. |
| `id` *(optional)* | `any` | Keeps the widget's state across updates (a drag, a list's scroll). Without one a widget is known by the order of the calls, so give one to widgets that show or hide. |

## Used by

[`rq.uikit.button`](../api/rq.uikit.md#rquikitbutton), [`rq.uikit.checkbox`](../api/rq.uikit.md#rquikitcheckbox), [`rq.uikit.choice`](../api/rq.uikit.md#rquikitchoice), [`rq.uikit.label`](../api/rq.uikit.md#rquikitlabel), [`rq.uikit.list`](../api/rq.uikit.md#rquikitlist), [`rq.uikit.menu`](../api/rq.uikit.md#rquikitmenu), [`rq.uikit.panel`](../api/rq.uikit.md#rquikitpanel), [`rq.uikit.slider`](../api/rq.uikit.md#rquikitslider), [`rq.uikit.tabs`](../api/rq.uikit.md#rquikittabs)
