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

[`rq.uikit.button`](../api/rq.uikit.md#rquikitbutton), [`rq.uikit.castle_row`](../api/rq.uikit.md#rquikitcastle_row), [`rq.uikit.checkbox`](../api/rq.uikit.md#rquikitcheckbox), [`rq.uikit.choice`](../api/rq.uikit.md#rquikitchoice), [`rq.uikit.close`](../api/rq.uikit.md#rquikitclose), [`rq.uikit.filters`](../api/rq.uikit.md#rquikitfilters), [`rq.uikit.item_list`](../api/rq.uikit.md#rquikititem_list), [`rq.uikit.item_picker`](../api/rq.uikit.md#rquikititem_picker), [`rq.uikit.item_row`](../api/rq.uikit.md#rquikititem_row), [`rq.uikit.item_storage`](../api/rq.uikit.md#rquikititem_storage), [`rq.uikit.label`](../api/rq.uikit.md#rquikitlabel), [`rq.uikit.list`](../api/rq.uikit.md#rquikitlist), [`rq.uikit.menu`](../api/rq.uikit.md#rquikitmenu), [`rq.uikit.number`](../api/rq.uikit.md#rquikitnumber), [`rq.uikit.options`](../api/rq.uikit.md#rquikitoptions), [`rq.uikit.page`](../api/rq.uikit.md#rquikitpage), [`rq.uikit.panel`](../api/rq.uikit.md#rquikitpanel), [`rq.uikit.quest_list`](../api/rq.uikit.md#rquikitquest_list), [`rq.uikit.quest_row`](../api/rq.uikit.md#rquikitquest_row), [`rq.uikit.rack`](../api/rq.uikit.md#rquikitrack), [`rq.uikit.scrollbar`](../api/rq.uikit.md#rquikitscrollbar), [`rq.uikit.slider`](../api/rq.uikit.md#rquikitslider), [`rq.uikit.sort`](../api/rq.uikit.md#rquikitsort), [`rq.uikit.tabs`](../api/rq.uikit.md#rquikittabs)
