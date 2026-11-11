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
| `nav` *(optional)* | `false\|{up?: any, down?: any, left?: any, right?: any}\|fun(dir: "up"\|"down"\|"left"\|"right"): any` | Where the arrow keys go from this widget, by the other widget's `id`, in place of the nearest one that way; a function returns the id or nil. false: the keys' cursor skips it. Since 2.12.0. |
| `tip` *(optional)* | `string\|` [`rq.UiTip`](rq.UiTip.md) | On a widget that takes a click: the game's comment window after the mouse or the keys' cursor stays on it `tip_wait` ms (see `rq.uikit.comment`). A text, or a table with a header and more; false for none where a widget has a tip of its own (`skill_button`). Since 2.13.0. |
| `tip_wait` *(optional)* | `integer` | How long the cursor stays on the widget before its tip shows, in ms. Default 500, as the game's. Since 2.13.0. |

## Used by

[`rq.uikit.balloon`](../api/rq.uikit.md#rquikitballoon), [`rq.uikit.button`](../api/rq.uikit.md#rquikitbutton), [`rq.uikit.castle_row`](../api/rq.uikit.md#rquikitcastle_row), [`rq.uikit.checkbox`](../api/rq.uikit.md#rquikitcheckbox), [`rq.uikit.choice`](../api/rq.uikit.md#rquikitchoice), [`rq.uikit.close`](../api/rq.uikit.md#rquikitclose), [`rq.uikit.filters`](../api/rq.uikit.md#rquikitfilters), [`rq.uikit.item_list`](../api/rq.uikit.md#rquikititem_list), [`rq.uikit.item_picker`](../api/rq.uikit.md#rquikititem_picker), [`rq.uikit.item_row`](../api/rq.uikit.md#rquikititem_row), [`rq.uikit.item_storage`](../api/rq.uikit.md#rquikititem_storage), [`rq.uikit.label`](../api/rq.uikit.md#rquikitlabel), [`rq.uikit.list`](../api/rq.uikit.md#rquikitlist), [`rq.uikit.menu`](../api/rq.uikit.md#rquikitmenu), [`rq.uikit.number`](../api/rq.uikit.md#rquikitnumber), [`rq.uikit.options`](../api/rq.uikit.md#rquikitoptions), [`rq.uikit.page`](../api/rq.uikit.md#rquikitpage), [`rq.uikit.panel`](../api/rq.uikit.md#rquikitpanel), [`rq.uikit.quest_list`](../api/rq.uikit.md#rquikitquest_list), [`rq.uikit.quest_row`](../api/rq.uikit.md#rquikitquest_row), [`rq.uikit.rack`](../api/rq.uikit.md#rquikitrack), [`rq.uikit.scrollbar`](../api/rq.uikit.md#rquikitscrollbar), [`rq.uikit.section`](../api/rq.uikit.md#rquikitsection), [`rq.uikit.slider`](../api/rq.uikit.md#rquikitslider), [`rq.uikit.sort`](../api/rq.uikit.md#rquikitsort), [`rq.uikit.tabs`](../api/rq.uikit.md#rquikittabs)
