# rq.uikit

`since 1.7.0` `changed 2.12.0` `changed 2.13.0`

Widgets in the look of the game's Config screen and, since 2.6.0, of its hub.

They are drawn with `rq.hud` from the game's own pictures: Config draws its labels into its
pictures, so the kit cuts out the parts that carry no text and writes its own text on them. The kit
is Lua on the public `rq.hud` calls. The hub's widgets write in the game's own font: grey buttons
in four sizes, Rance Castle's room rows, quest rows and the quest list, the town tabs, Frostbuy's
rack tiles, the sort column, the game's scroll bar and close button, a page that covers the
hub, and (2.7.0) the choice menu's look. They take their pieces from the theme in use, else from
`themes.hub`.

It works in immediate mode: call the widgets from `rq.on_frame` on every update they show, keep the
values yourself, and pass them back in. Each widget returns the new value and whether it changed on
this update. While the mouse is over a widget the game sees no mouse. Hover and click play the
game's own sounds (1001 and 1002). The widgets are listed for `rqmod-ctl ui` in the section `"kit"`.

The keys (2.12.0): the arrow keys move one cursor between the widgets that take a click, and Enter
clicks the one under it, as the game's own screens do. The mouse and the keys share it: moving the
mouse over a widget puts the cursor there, and an arrow then goes on from it; the mouse is never
moved. An arrow goes to the nearest widget that way, one whose center is past the edge of the
cursor's widget (the gap along the arrow plus twice the offset across it); with none, it wraps to
the widget the other way that lines up best, the farthest of those, as a row of tabs wraps. With no
cursor, Down and Right go to the first widget drawn, Up and Left to the last. A widget's `nav`
changes where its arrows go. In a list (`list`, `quest_list`, `options`, `item_list`) Up and Down
go through its rows, also those scrolled out of sight, and the list scrolls to follow; at the end
of a list that does not wrap they go on to the nearest widget outside it. A focused slider moves
by Page Up and Page Down. A held key moves again after 250 ms, then every 50 ms, as the game's.
The kit takes the keys only on an update where `rq.uikit.keys` is called: inside `page`, on
Config's Mods tab, and where a mod calls it. Elsewhere its widgets over the game's screens are
for the mouse, and the arrows stay the game's.

Tips (2.13.0): every widget that takes a click has `tip`, the game's comment window
(`rq.uikit.comment`) shown when the mouse or the keys' cursor has stayed on it 500 ms, with the
game's sound 5001. Under the mouse it goes at the mouse, as the game's; from the keys, at the
widget's right edge (left of it when it does not fit). It goes when the cursor leaves. A disabled
widget shows its tip under the mouse too. `tabs`, `choice` and `sort` take `tips`, one for each
entry; `list` and `quest_list` rows take `tip`.

```lua
local ui = rq.uikit
local vol, mute = 0.8, false
rq.on_frame(function()
  ui.panel({ x = 12, y = 85, w = 1000, h = 595 })
  ui.col({ x = 62, y = 105, gap = 20 }, function()
    ui.row({ h = 30, align = "center" }, function()
      ui.label("Master", { w = 218 })
      vol = ui.slider(vol, { low = "Low", high = "High", id = "vol" })
      mute = ui.checkbox(mute, "Mute", { x = 640, id = "mute" })
    end)
  end)
end)
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `theme` | [`rq.UiTheme`](../types/rq.UiTheme.md) | The theme in use. |
| `themes` | `{config:` [`rq.UiTheme`](../types/rq.UiTheme.md) `, hub:` [`rq.UiTheme`](../types/rq.UiTheme.md) `}` | The built-in themes. `hub` came in 2.6.0. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.uikit.label`](#rquikitlabel) | Draws a line of text, white with a dark edge. |
| [`rq.uikit.button`](#rquikitbutton) | Draws a Config button with text. |
| [`rq.uikit.checkbox`](#rquikitcheckbox) | Draws a checkbox with its text. |
| [`rq.uikit.choice`](#rquikitchoice) | Draws one of several checkboxes, as the 3D tab's quality. |
| [`rq.uikit.slider`](#rquikitslider) | Draws the Sound tab's slider. |
| [`rq.uikit.stepper`](#rquikitstepper) | Draws a number field: the number in a framed box between - and +, and returns the new number. |
| [`rq.uikit.typing`](#rquikittyping) | Returns the number field typing on this update, by its `opts.id`, or nil. |
| [`rq.uikit.tabs`](#rquikittabs) | Draws Config's tabs side by side: normal, hovered and current. |
| [`rq.uikit.panel`](#rquikitpanel) | Draws a Config page or the 3D tab's dark block, and runs `fn` in a column inside it. |
| [`rq.uikit.list`](#rquikitlist) | Draws rows on a dark block that scroll by the wheel. |
| [`rq.uikit.menu`](#rquikitmenu) | Draws a menu with levels: lists side by side, where an entry with `items` opens the next list. |
| [`rq.uikit.row`](#rquikitrow) | Places the widgets called in `fn` side by side. |
| [`rq.uikit.col`](#rquikitcol) | Places the widgets called in `fn` one under the other. |
| [`rq.uikit.space`](#rquikitspace) | Leaves empty space in a row or column. |
| [`rq.uikit.last`](#rquikitlast) | Returns where the last widget went, as for a tooltip beside it. |
| [`rq.uikit.hovered`](#rquikithovered) | Returns whether the mouse was over a kit widget on this update so far. |
| [`rq.uikit.comment`](#rquikitcomment) | Draws the game's comment window, its tooltip, on this update. |
| [`rq.uikit.comment_size`](#rquikitcomment_size) | Returns the size the comment window would have, without drawing it. |
| [`rq.uikit.bar`](#rquikitbar) | Draws one of the game's bars, a gauge: its CG cut to `value / max` of its width, as the game's `T_Bar`. |
| [`rq.uikit.skill_button`](#rquikitskill_button) | Draws a skill's tile, as the game's status page draws it, and returns whether it was clicked. |
| [`rq.uikit.top`](#rquikittop) | Runs a function now and draws what it draws on top of every widget, as `rq.hud.top` does. |
| [`rq.uikit.keys`](#rquikitkeys) | Lets the kit take the arrow keys, Enter, Page Up and Page Down on this update. |
| [`rq.uikit.focused`](#rquikitfocused) | Returns the widget under the keys' cursor. |
| [`rq.uikit.focus`](#rquikitfocus) | Puts the keys' cursor on a widget, as an arrow would, or takes it away. |
| [`rq.uikit.state`](#rquikitstate) | Returns what the kit keeps for a widget. |
| [`rq.uikit.draw`](#rquikitdraw) | Draws a piece of the theme at any size. |
| [`rq.uikit.copy_theme`](#rquikitcopy_theme) | Returns a deep copy of a theme, to change and pass to `rq.uikit.use`. |
| [`rq.uikit.use`](#rquikituse) | Uses a theme from now on, for every mod. |
| [`rq.uikit.layers`](#rquikitlayers) | Returns a piece as layers for `rq.image.compose`, to make a CG of it. |
| [`rq.uikit.close`](#rquikitclose) | Draws the close button of the hub's windows (24 by 20). |
| [`rq.uikit.castle_row`](#rquikitcastle_row) | Draws a room row of Rance Castle: the grey button with the room's name, the face beside it, and the NEW and heart marks. |
| [`rq.uikit.quest_row`](#rquikitquest_row) | Draws a quest row: the number, the yellow name, and the clear count in its box on the left. |
| [`rq.uikit.quest_list`](#rquikitquest_list) | Draws the quest list: rows 34 apart and the game's scroll bar 15 pixels right of them. |
| [`rq.uikit.scrollbar`](#rquikitscrollbar) | Draws the game's scroll bar, up and down: two arrows, the track and the bar. |
| [`rq.uikit.rack`](#rquikitrack) | Draws a Frostbuy rack tile: a dark see-through square in the shop's black and yellow lines, with yellow text. |
| [`rq.uikit.sort`](#rquikitsort) | Draws the sort column: "SORT" over up to 16 buttons, 30 apart, the current one framed in yellow. |
| [`rq.uikit.page`](#rquikitpage) | Draws a page of a mod's own over the hub and runs `fn` in a column inside it. |
| [`rq.uikit.options`](#rquikitoptions) | Draws the game's choice menu as a widget: its green base, grey rows, separators and a text panel at the top, laid out as the game lays out the menu. It is not modal and does not wait: it returns the picked row's id on the update it is clicked. Use it inside a page; `rq.ui.choose` opens the game's own menu instead. |
| [`rq.uikit.item_data`](#rquikititem_data) | Reads an item instance's row data from the game: its name, level line, stats line, icon, rank, kind, lock, price, place, the classes that may equip it, and whether the game lets it go. |
| [`rq.uikit.item_refresh`](#rquikititem_refresh) | Makes item rows and lists read an instance again on their next update. |
| [`rq.uikit.item_row`](#rquikititem_row) | Draws a vault item row, 381 by 128, as the game draws it: the name, the icon with its rank badge, the red level bar, the stats line in the game's yellow and white, the icons of the classes that may equip it, LOCKED, and the row's buttons. |
| [`rq.uikit.item_icon`](#rquikititem_icon) | Draws an item's tile, as the status page's equip slots draw it, and returns whether it was clicked. |
| [`rq.uikit.item_card`](#rquikititem_card) | Draws the game's item card now, on the top layer, and returns its box. |
| [`rq.uikit.item_card_size`](#rquikititem_card_size) | Returns the item card's size, to place it beside a widget as the game's screens do. |
| [`rq.uikit.item_list`](#rquikititem_list) | Draws the vault's item list: rows 128 apart and the game's scroll bar beside them. |
| [`rq.uikit.item_dropped`](#rquikititem_dropped) | Returns the row dropped on this update on another list of a drag group (`item_list`'s `drag`). |
| [`rq.uikit.item_storage`](#rquikititem_storage) | Draws the game's storage screen: the storage's red list on the left and the vault's list right of it (437 pixels apart, as the game places them), each with its scroll bar, the vault's count and the storage's in their boxes, and the vault's filter column and SORT. Drag a row from one list to the other to move the item (`rq.item.store`). |
| [`rq.uikit.number`](#rquikitnumber) | Draws a number as the game does: the vault's counters (`font = "count"`: the game's font, 20 pixels, bold, white), or one of the game's digit fonts. |
| [`rq.uikit.filters`](#rquikitfilters) | Draws the vault's filter column and returns what is picked: the categories (Special, Weapon, Armor, Item / Other), the classes, and Locked / Unlocked, on the column's grey with its "[FILTERING]" heads; and, while a category with sub-filters is picked, its panel of sub-filters over the list's first row. |
| [`rq.uikit.item_filter`](#rquikititem_filter) | Returns the items of a list that pass a filter state, tested as the vault tests them (`アイテム倉庫_一覧_種類確認`, `_職業確認`, `_装備タイプ確認`, `_ＬＯＣＫタイプ確認`). |
| [`rq.uikit.item_sort`](#rquikititem_sort) | Sorts a list of items in place as the vault sorts it, with the game's own comparers (`compItem_*`). |
| [`rq.uikit.item_sorts`](#rquikititem_sorts) | Lists the vault's sort modes 11 to 28 with the game's names (`アイテム倉庫_ソート名`), for a menu. |
| [`rq.uikit.item_picker`](#rquikititem_picker) | Draws an item picker over the player's items, laid out as the vault: the list with its scroll bar, the filter column 407 pixels right and 154 down, the count of items listed in the column's box, and the store's SORT under the column (405 right and 682 down, as at 943, 682 in the game). |

### rq.uikit.label

```lua
rq.uikit.label(text, opts) -> integer, integer, integer, integer
```

`since 1.7.0`

Draws a line of text, white with a dark edge.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{size?: number, color?: integer[], dim?: boolean, align?: string, valign?: string}` | `size` (default the theme's, 17), `color` `{r, g, b}`, `dim` for the theme's dim color, `align`, `valign` (default "center"). |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | Width. |
| `h` | `integer` | Height. |

### rq.uikit.button

```lua
rq.uikit.button(text, opts) -> boolean
```

`since 1.7.0` `changed 2.6.0`

Draws a Config button with text.

The button is at least 150 wide (or the text's width) and 40 high. When hovered, the game's cover
pulses over it every 2 seconds. A click counts when the button is let go over the same button it
went down on.

With `opts.style`, or a theme with `button_style`, it is one of the hub's grey buttons instead:
"large" (Rance Castle's rooms, 206x30), "choice" (the choice menu's, 340x27), "choice_tall"
(340x60) or "short" (the footer's Vault and Trivia, 98x26). Its size is the style's unless
`opts.w` or `h` is given, and a long text gets smaller until it fits, as the game's labels do.

Raises an error for a style no theme has.

```lua
if rq.uikit.button("Reset", { id = "reset" }) then reset() end
if rq.uikit.button("Open the shop", { style = "large", x = 120, y = 300 }) then open = true end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{disabled?: boolean, style?: "large"\|"choice"\|"choice_tall"\|"short"\|string}` | Place, `disabled` to grey it out, and `style`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

> Changed in 2.6.0: Added `opts.style` and the theme's `button_style`.

### rq.uikit.checkbox

```lua
rq.uikit.checkbox(value, text, opts) -> boolean, boolean
```

`since 1.7.0`

Draws a checkbox with its text.

The text is 42 pixels right of the box, and the game's yellow bar covers the row when hovered.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `boolean` | Whether it is checked. |
| `text` *(optional)* | `string` | The text beside it. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{disabled?: boolean}` | Place (`w` is the bar's width), and `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `boolean` | The new value. |
| `changed` | `boolean` | true on the update it was clicked. |

### rq.uikit.choice

```lua
rq.uikit.choice(list, index, opts) -> integer|nil, boolean
```

`since 1.7.0`

Draws one of several checkboxes, as the 3D tab's quality.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `string[]` | The texts. |
| `index` *(optional)* | `integer` | The checked one; nil for none. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{dir?: "col"\|"row", gap?: integer, disabled?: boolean, tips?: (string\|` [`rq.UiTip`](../types/rq.UiTip.md) `)[]}` | `dir` (default "col"), `gap` in pixels (default 20), `disabled`, `tips` (2.13.0: one for each checkbox). |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The checked one. |
| `changed` | `boolean` | true on the update it changed. |

### rq.uikit.slider

```lua
rq.uikit.slider(value, opts) -> number, boolean
```

`since 1.7.0` `changed 1.8.0` `changed 2.12.0`

Draws the Sound tab's slider.

Drag the knob or click the track; the drag goes on while the button is down, also off the track.
The wheel over it moves it by `step`, or by a twentieth, and the game does not get that wheel step.
Under the keys' cursor, Page Down raises it and Page Up lowers it by `step`, or a twentieth (5%),
as Config's sliders: on the press, then on every update after 250 ms.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | The value. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{min?: number, max?: number, step?: number, low?: string, high?: string, label?: string, disabled?: boolean}` | `w`: the track's width (default 200). `min` (default 0), `max` (default 1), `step`, `low` and `high` (texts at the ends), `label` (its name in `rqmod-ctl ui`), `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `number` | The new value. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 1.8.0: Added `opts.label`.

> Changed in 2.12.0: Page Up and Page Down.

### rq.uikit.stepper

```lua
rq.uikit.stepper(value, opts) -> integer, boolean
```

`since 2.22.0`

Draws a number field: the number in a framed box between - and +, and returns the new number.

- **- and +** change it by `step`, by `big` with Shift held. Held, they repeat: 400 ms after the
  press, then every 80 ms.
- **The wheel** over the field changes it by `step`, and the game does not get that wheel step.
- **Under the keys' cursor**, Page Up raises it and Page Down lowers it by `step`.
- **Typing.** A click on the number, or Enter under the keys' cursor, types into it. The digits are
  read from the keys, 0 to 9 and the keypad's (with the keypad's minus while `min` is below 0), not
  from the system's text input, so `rqmod-ctl type` and `key` can type it. Backspace takes the last
  digit. Enter keeps the number, put inside `min` and `max`; so does a click elsewhere or the keys'
  cursor moving on. Esc puts the old number back. While it types, these keys are hidden from the
  game, and Enter, Esc and Backspace stay hidden until let go: Esc there does not close Config or
  `rq.uikit.page`.

A typed number counts as one change, when it is kept. The field is listed for `rqmod-ctl ui` as
`stepper-<id>` with the number as `value` and `selected` true while it types; its buttons are
`button-<id>-dec` and `button-<id>-inc`.

Raises an error for a `value`, `min`, `max`, `step` or `big` that is not a whole number, a `max` below
`min`, a `step` or `big` below 1, or a `w` that is not a whole number.

```lua
rq.config.page{
  id = "my-mod",
  title = "My Mod",
  draw = function(ui)
    local n, changed = ui.stepper(count, { id = "count", label = "Count", min = 1, max = 99 })
    if changed then
      count = n
      rq.store.global.set("count", n)
    end
  end,
}
```

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `integer` | The number shown; it is put inside `min` and `max`. |
| `opts` *(optional)* | [`rq.UiStepperOpts`](../types/rq.UiStepperOpts.md) | `min`, `max`, `step`, `big`, `label`, `disabled`; place (`w`: the box's width, default to fit `max`), `id`, `tip`, `nav`. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `integer` | The new number. |
| `changed` | `boolean` | true on the update it changed. |

### rq.uikit.typing

```lua
rq.uikit.typing() -> string|nil
```

`since 2.22.0`

Returns the number field typing on this update, by its `opts.id`, or nil.

While one types, the keys it reads are its own; a page of a mod's own that reads Esc or digits
itself can leave them alone while this is not nil.

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The field's `opts.id` (else the kit's id), or nil. |

### rq.uikit.tabs

```lua
rq.uikit.tabs(list, index, opts) -> integer, boolean
```

`since 1.7.0` `changed 2.6.0`

Draws Config's tabs side by side: normal, hovered and current.

With `opts.style = "town"` (or a theme's `tabs_style`) they are the hub's town tabs instead, 248
by 45 and 8 apart, the current one orange.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `string[]` | The tab texts. |
| `index` | `integer` | The current tab. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{style?: "town"\|string, gap?: integer, tips?: (string\|` [`rq.UiTip`](../types/rq.UiTip.md) `)[]}` | Place; `w` is each tab's width (default 120, or the style's). `style`, and `gap` between styled tabs. `tips` (2.13.0): one for each tab. |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer` | The current tab. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 2.6.0: Added `opts.style`.

### rq.uikit.panel

```lua
rq.uikit.panel(opts, fn) -> integer, integer, integer, integer
```

`since 1.7.0`

Draws a Config page or the 3D tab's dark block, and runs `fn` in a column inside it.

A page lower than the game's keeps its top colors; it is not squashed.

Raises an error without `w` and `h`.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{style?: "page"\|"block", pad?: integer, gap?: integer, title?: string}` | `w` and `h` are needed. `style` (default "page"), `pad` (default 12), `gap`, `title`. |
| `fn` *(optional)* | `fun(x: integer, y: integer, w: integer, h: integer)` | The widgets inside. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | Width. |
| `h` | `integer` | Height. |

### rq.uikit.list

```lua
rq.uikit.list(items, index, opts) -> integer|nil, boolean
```

`since 1.7.0` `changed 2.5.0` `changed 2.6.0`

Draws rows on a dark block that scroll by the wheel.

A bar shows when the rows do not fit. The list stays inside a clip of your own (`rq.hud.clip_push`).
With a theme that has `scroll` (the hub theme), the bar is the game's scroll bar, with arrows, when
the list is at least 100 high.

Raises an error without `w` and `h`.

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `(string\|{text: string, disabled?: boolean, tip?: string\|` [`rq.UiTip`](../types/rq.UiTip.md) `})[]` | The rows; `tip` since 2.13.0. |
| `index` *(optional)* | `integer` | The chosen row; nil for none. |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{row_h?: integer, block?: boolean}` | `w` and `h` are needed. `row_h` (default 30), `block = false` leaves out the dark block. |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The chosen row. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 2.5.0: Stays inside a clip of your own; before, its clip replaced yours.

> Changed in 2.6.0: The game's scroll bar with a theme that has `scroll`.

### rq.uikit.menu

```lua
rq.uikit.menu(tree, path, opts) -> integer[], boolean, string|rq.UiMenuItem|nil
```

`since 1.7.0`

Draws a menu with levels: lists side by side, where an entry with `items` opens the next list.

A new pick on a level drops the levels after it.

Raises an error without `h`.

| Parameter | Type | Description |
| --- | --- | --- |
| `tree` | [`rq.UiMenuItem`](../types/rq.UiMenuItem.md) `[]` | The first level. |
| `path` *(optional)* | `integer[]` | The index picked at each level. |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{gap?: integer}` | `h` is needed. `w` is each list's width (default 200), `gap` (default 10). |

| Returns | Type | Description |
| --- | --- | --- |
| `path` | `integer[]` | The path; a new table when it changed. |
| `changed` | `boolean` | true on the update it changed. |
| `item` | `string\|` [`rq.UiMenuItem`](../types/rq.UiMenuItem.md) `\|nil` | The entry at the path's end. |

### rq.uikit.row

```lua
rq.uikit.row(opts, fn) -> integer, integer, integer, integer
```

`since 1.7.0`

Places the widgets called in `fn` side by side.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.UiBox`](../types/rq.UiBox.md) `\|fun()` | The box, or `fn` itself. |
| `fn` *(optional)* | `fun(x: integer, y: integer, w?: integer, h?: integer)` | The widgets. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | The width the widgets cover. |
| `h` | `integer` | The height they cover. |

### rq.uikit.col

```lua
rq.uikit.col(opts, fn) -> integer, integer, integer, integer
```

`since 1.7.0`

Places the widgets called in `fn` one under the other.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.UiBox`](../types/rq.UiBox.md) `\|fun()` | The box, or `fn` itself. |
| `fn` *(optional)* | `fun(x: integer, y: integer, w?: integer, h?: integer)` | The widgets. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | The width the widgets cover. |
| `h` | `integer` | The height they cover. |

### rq.uikit.space

```lua
rq.uikit.space(w, h)
```

`since 1.7.0`

Leaves empty space in a row or column.

| Parameter | Type | Description |
| --- | --- | --- |
| `w` | `integer` | Width, in pixels. |
| `h` | `integer` | Height, in pixels. |

### rq.uikit.last

```lua
rq.uikit.last() -> integer, integer, integer, integer
```

`since 1.7.0`

Returns where the last widget went, as for a tooltip beside it.

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge. |
| `y` | `integer` | Top edge. |
| `w` | `integer` | Width. |
| `h` | `integer` | Height. |

### rq.uikit.hovered

```lua
rq.uikit.hovered() -> boolean
```

`since 1.7.0`

Returns whether the mouse was over a kit widget on this update so far.

| Returns | Type | Description |
| --- | --- | --- |
| `hovered` | `boolean` | true when a widget drawn so far is under the mouse. |

### rq.uikit.comment

```lua
rq.uikit.comment(text, opts) -> integer|nil, integer|nil, integer|nil, integer|nil
```

`since 2.13.0`

Draws the game's comment window, its tooltip, on this update.

It is the game's own look (`T_Comment`): a paper window with three thin borders, a shadow, a
header, the text in the game's font and red `sub` lines under it, laid out as the game lays its
own out, to the pixel. The text wraps at 520 pixels, as the game's, and shows 20 lines at most.
It is drawn on the top layer (`rq.uikit.top`), over every widget. Call it on every update it
should show; it does not wait. For a tip that waits for the mouse, give a widget `tip`.

Without `x` and `y` it goes at the mouse, 11 right and 20 under it; past the screen's right edge it
goes left of the mouse, and past the bottom it ends at 736, as the game's. A given `x` past the
right edge ends at 1024. It takes no clicks and covers no game control: `rqmod-ctl` lists it in
the section "kit" with the type "comment" and its text as `value`.

Raises an error when the text, `header` or `sub` is not a string, `style` is unknown or `opts` is
not a table.

```lua
rq.on_frame(function()
  if hovering_my_icon then
    rq.uikit.comment("Doubles the gold from quests.", { header = "Golden Touch", sub = "Not in the tutorial." })
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string\|nil` | The text. `\n` breaks a line. |
| `opts` *(optional)* | [`rq.UiCommentOpts`](../types/rq.UiCommentOpts.md) | `header`, `sub`, `style`, `x`, `y`, `game`, `id`. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer\|nil` | The window's left edge, or nil when there is nothing to show (no text, header or sub). |
| `y` | `integer\|nil` | Its top edge. |
| `w` | `integer\|nil` | Its width, without the 5-pixel shadow. |
| `h` | `integer\|nil` | Its height, without the shadow. |

See also: [`rq.uikit.comment_size`](rq.uikit.md#rquikitcomment_size)

### rq.uikit.comment_size

```lua
rq.uikit.comment_size(text, opts) -> integer|nil, integer|nil
```

`since 2.13.0`

Returns the size the comment window would have, without drawing it.

Raises an error as `comment` does.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string\|nil` | The text. |
| `opts` *(optional)* | [`rq.UiCommentOpts`](../types/rq.UiCommentOpts.md) | `header`, `sub`, `style`, `game`. |

| Returns | Type | Description |
| --- | --- | --- |
| `w` | `integer\|nil` | The width without the 5-pixel shadow; nil when there is nothing to show. |
| `h` | `integer\|nil` | The height without the shadow. |

### rq.uikit.bar

```lua
rq.uikit.bar(value, max, opts) -> number
```

`since 2.14.0`

Draws one of the game's bars, a gauge: its CG cut to `value / max` of its width, as the game's
`T_Bar`.

With `dir = "up"` it is cut to that part of its height and fills from the bottom. A value above 0
shows at least 1 pixel. A value is kept between 0 and `max`; a `max` under 1 draws nothing. With
`anim` the value shown moves from the old value to a new one over that many ms.

Only the bar: the frames round the game's bars are parts of each screen's background. It takes no
click and is not on the keys' cursor; `tip` shows under the mouse. It is listed for `rqmod-ctl
ui` with the type "bar" and the value it shows, and never covers a game control.

Raises an error for a `value` or `max` that is not a number, an unknown `style` or `dir`, a CG that
is not there, no `style`, `cg` or `color`, or an `anim` that is not a whole number of 0 or more.

```lua
rq.on_frame(function()
  local c = rq.chara.get(1)
  rq.uikit.bar(c.hp, c.hp_max, { style = "hp", x = 74, y = 394, id = "hp", anim = 250 })
  rq.uikit.bar(fuel, 100, { color = { 255, 200, 0 }, x = 400, y = 600, w = 120, h = 6, tip = "Fuel" })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | The value. |
| `max` | `number` | The value of a full bar. |
| `opts` *(optional)* | [`rq.UiBarOpts`](../types/rq.UiBarOpts.md) | `style`, `cg` or `color`; `dir`, `anim`; place, `id`, `tip`. |

| Returns | Type | Description |
| --- | --- | --- |
| `shown` | `number` | The value the bar shows on this update (moving with `anim`). |

### rq.uikit.skill_button

```lua
rq.uikit.skill_button(skill, opts) -> boolean
```

`since 2.15.0`

Draws a skill's tile, as the game's status page draws it, and returns whether it was clicked.

The tile is the CG of the skill's panel color, the game's own pick (`スキルボタン_ＣＧ番号`), 142 by
24. The name is in the game's font, fitted as the game fits it: 18 pixels, else 16, 14 or 12 until
the name and the rank marks fit, then squeezed. Under the mouse it shows the CG's hovered look
and the game's yellow frame; Enter and the keys' cursor work as on every widget.

Its `tip` is the game's comment for the skill, its name and `スキル_説明文１`, right of the tile as
the status page shows it; give a `tip` of your own, or false for none. With `skill` nil and `slot`
it draws the empty slot (CG 10121) with its number.

It is listed for `rqmod-ctl ui` with the type "skill" and the skill number as `value`; an empty
slot with the type "slot", which takes no click.

Raises an error for a skill that is not a whole number above 0 or has no tile (no long tile, with
`long`), no `slot` without a skill, or a `rank`, `chara`, `count` or `count_max` that is not a whole
number.

```lua
rq.on_frame(function()
  if not open then return end
  open = rq.uikit.page({ id = "skills", title = "Skills" }, function(x, y)
    for i, skill in ipairs(my_skills) do
      if rq.uikit.skill_button(skill, { x = x + 20, y = y + i * 26, chara = chara, id = skill }) then
        pick(skill)
      end
    end
    rq.uikit.skill_button(nil, { x = x + 200, y = y + 26, slot = 1 })
  end)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` | `integer\|nil` | A skill number, or nil for an empty slot. |
| `opts` *(optional)* | [`rq.UiSkillOpts`](../types/rq.UiSkillOpts.md) | `rank` or `chara`, `long`, `count`, `count_max`, `disabled`, `slot`; place, `id`, `tip`, `nav`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

### rq.uikit.top

```lua
rq.uikit.top(fn) -> any
```

`since 2.11.0`

Runs a function now and draws what it draws on top of every widget, as `rq.hud.top` does.

For a widget's floating part: its tooltip, its comment, an icon it drags. Widgets inside `fn` draw
as usual, but clicks are still decided in call order.

Raises an error when `fn` is not a function, and the error `fn` raises.

```lua
if rq.uikit.hovered() then
  rq.uikit.top(function() rq.uikit.label("Sells for 120 G", { x = mx + 16, y = my }) end)
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | The widgets and draws for the top layer. |

| Returns | Type | Description |
| --- | --- | --- |
|  | `any` | ... What `fn` returns. |

See also: [`rq.hud.top`](rq.hud.md#rqhudtop)

### rq.uikit.keys

```lua
rq.uikit.keys(opts)
```

`since 2.12.0`

Lets the kit take the arrow keys, Enter, Page Up and Page Down on this update.

They move the keys' cursor between widgets (see `rq.uikit`) and are hidden from the game
(`rq.hud.block_keys`); other keys still reach it. Call it on every update the keys should be the
kit's; `page` calls it, and so do Config's Mods tab, `options` and `item_list` with `keys`.

With `edge`, an arrow that finds no widget that way calls `edge(dir)` and the cursor does not
wrap: a mod hands the cursor to something else there, as Config's Mods tab gives it back to the
game's tab row on Up.

Raises an error when `opts` is not a table or `edge` not a function.

```lua
rq.on_frame(function()
  if not open then return end
  rq.uikit.keys()
  if rq.uikit.button("One", { id = "one", x = 100, y = 200 }) then pick(1) end
  if rq.uikit.button("Two", { id = "two", x = 300, y = 200 }) then pick(2) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | `{edge?: fun(dir: "up"\|"down"\|"left"\|"right")}` | `edge`: called when an arrow finds nothing that way. |

See also: [`rq.uikit.focus`](rq.uikit.md#rquikitfocus)

### rq.uikit.focused

```lua
rq.uikit.focused() -> any|nil
```

`since 2.12.0`

Returns the widget under the keys' cursor.

It is the widget the arrows reached or the mouse last moved over. A list row is its list's `id`
with the row's number, such as "pages.3" for row 3 of a list with `id = "pages"`.

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The widget's `id` (or the kit's own id for one without), or nil for no cursor. |

### rq.uikit.focus

```lua
rq.uikit.focus(id)
```

`since 2.12.0`

Puts the keys' cursor on a widget, as an arrow would, or takes it away.

It also calls `rq.uikit.keys` for this update. A widget not drawn on the last update gets the
cursor when it shows.

```lua
rq.uikit.focus("start")  -- the page opens with the cursor on its Start button
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The widget's `id`, or a list row's (see `focused`); nil takes the cursor away. |

### rq.uikit.state

```lua
rq.uikit.state(id) -> table
```

`since 1.7.0`

Returns what the kit keeps for a widget.

```lua
local top = rq.uikit.state("list:options").top  -- the list's scroll, in pixels
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The widget's kind and id, such as "list:options". |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `table` | The kept state, made empty on first use. |

### rq.uikit.draw

```lua
rq.uikit.draw(piece, x, y, w, h, opts)
```

`since 1.7.0`

Draws a piece of the theme at any size.

Raises an error for a name the theme has no piece for.

| Parameter | Type | Description |
| --- | --- | --- |
| `piece` | `string\|` [`rq.UiPiece`](../types/rq.UiPiece.md) | A piece name in the theme, or a piece. |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` *(optional)* | `integer` | Width. Default: the piece's own. |
| `h` *(optional)* | `integer` | Height. Default: the piece's own. |
| `opts` *(optional)* | [`rq.HudCgOpts`](../types/rq.HudCgOpts.md) | `alpha` and `tint`, as in `rq.hud.cg`. |

### rq.uikit.copy_theme

```lua
rq.uikit.copy_theme(theme) -> rq.UiTheme
```

`since 1.7.0`

Returns a deep copy of a theme, to change and pass to `rq.uikit.use`.

A piece in the copy may point at a CG from `rq.image.add`.

| Parameter | Type | Description |
| --- | --- | --- |
| `theme` *(optional)* | [`rq.UiTheme`](../types/rq.UiTheme.md) | The theme to copy. Default: Config's. |

| Returns | Type | Description |
| --- | --- | --- |
| `copy` | [`rq.UiTheme`](../types/rq.UiTheme.md) | The copy. |

### rq.uikit.use

```lua
rq.uikit.use(theme)
```

`since 1.7.0`

Uses a theme from now on, for every mod.

Set it back when your HUD closes.

Raises an error when `theme` is not a table.

| Parameter | Type | Description |
| --- | --- | --- |
| `theme` | [`rq.UiTheme`](../types/rq.UiTheme.md) | The theme. |

### rq.uikit.layers

```lua
rq.uikit.layers(piece, x, y, w, h) -> rq.ImageLayer[]
```

`since 1.8.0`

Returns a piece as layers for `rq.image.compose`, to make a CG of it.

The Mods tab of Config is made this way: Other 2's tab with its label cut away and new text on it.

| Parameter | Type | Description |
| --- | --- | --- |
| `piece` | `string\|` [`rq.UiPiece`](../types/rq.UiPiece.md) | A piece name in the theme, or a piece. |
| `x` *(optional)* | `integer` | Left edge in the new CG. Default 0. |
| `y` *(optional)* | `integer` | Top edge in the new CG. Default 0. |
| `w` *(optional)* | `integer` | Width. Default: the piece's own. |
| `h` *(optional)* | `integer` | Height. Default: the piece's own. |

| Returns | Type | Description |
| --- | --- | --- |
| `layers` | [`rq.ImageLayer`](../types/rq.ImageLayer.md) `[]` | The layers. |

### rq.uikit.close

```lua
rq.uikit.close(opts) -> boolean
```

`since 2.6.0`

Draws the close button of the hub's windows (24 by 20).

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{disabled?: boolean}` | Place, and `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

### rq.uikit.castle_row

```lua
rq.uikit.castle_row(opts) -> boolean
```

`since 2.6.0`

Draws a room row of Rance Castle: the grey button with the room's name, the face beside it, and
the NEW and heart marks.

The row is 270 by 36; the button is at +3,+3 and 206 by 30, and a long name gets smaller until it
fits. The face is any CG, drawn at 24 by 29 in its frame; without one the frame is black.

Raises an error for a mark that is not "heart" or "run".

```lua
if rq.uikit.castle_row({ x = 145, y = 82, text = "Lab", face = 12345, new = true, id = "lab" }) then
  page_open = true
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{text?: string, face?: integer, new?: boolean, mark?: "heart"\|"run", disabled?: boolean}` | `text`, `face` (a CG number), `new`, `mark` ("heart", or "run" for MORU RUN), `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update its button is clicked. |

### rq.uikit.quest_row

```lua
rq.uikit.quest_row(opts) -> boolean
```

`since 2.6.0`

Draws a quest row: the number, the yellow name, and the clear count in its box on the left.

The row is 228 by 30. A number is written with three digits ("077"); a long name gets smaller until
it fits. `mark` past 9 shows "★", as the game does; 0 shows nothing. The box for the count is
38 pixels left of the row; `box = false` leaves it out.

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{no?: integer\|string, name?: string, mark?: integer\|string, box?: boolean, current?: boolean, disabled?: boolean}` | `no`, `name`, `mark` (the clear count, or a text), `box`, `current` (covered in see-through cyan, as the game marks a quest it locks), `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

### rq.uikit.quest_list

```lua
rq.uikit.quest_list(rows, index, opts) -> integer|nil, boolean
```

`since 2.6.0`

Draws the quest list: rows 34 apart and the game's scroll bar 15 pixels right of them.

13 rows show by default, as on the Quests screen. The wheel over the rows scrolls a row at a time;
the bar's arrows, its track and a drag of the bar scroll it too. A click on a row makes it the
current one. The scroll is kept by `opts.id` (`rq.uikit.state("questlist:<id>").top`).

```lua
local rows, pick = {}, nil
for i, q in ipairs(my_quests) do rows[i] = { no = q.no, name = q.name, mark = q.clears } end
rq.on_frame(function()
  pick = rq.uikit.quest_list(rows, pick, { x = 330, y = 130, id = "mine" })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `rows` | `{no?: integer\|string, name?: string, mark?: integer\|string, disabled?: boolean, tip?: string\|` [`rq.UiTip`](../types/rq.UiTip.md) `}[]` | The rows; `tip` since 2.13.0. |
| `index` *(optional)* | `integer` | The current row; nil for none. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{shown?: integer}` | Place, `id`, and `shown` (rows at once, default 13). |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The current row. |
| `changed` | `boolean` | true on the update it changed. |

### rq.uikit.scrollbar

```lua
rq.uikit.scrollbar(top, count, shown, opts) -> integer, boolean
```

`since 2.6.0` `changed 2.10.0`

Draws the game's scroll bar, up and down: two arrows, the track and the bar.

`top`, `count` and `shown` are in any unit: rows, or pixels with `opts.step`. The bar is
`shown / count` of the track, at least 10 pixels, as the game sizes it. The arrows move by `step`,
a click on the track by `shown` toward the click, and a drag of the bar goes where the bar goes. The
wheel over the bar, or over `opts.wheel`, moves by `step`, and the game does not get it.

As the game's bar (`T_ScrollBar`), an arrow or the track moves on the press. Held, it waits 250 ms
and then moves again on every update while the button stays down, wherever the mouse goes; the
track stops once the bar reaches the mouse.

Raises an error without `h`, or with an `h` that leaves no room between the arrows.

| Parameter | Type | Description |
| --- | --- | --- |
| `top` | `integer` | The first shown. |
| `count` | `integer` | How many there are. |
| `shown` | `integer` | How many show at once. |
| `opts` | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{step?: integer, wheel?: integer[], label?: string, disabled?: boolean}` | `h` is needed (with the two 40 high arrows). `step` (default 1), `wheel = {x, y, w, h}`, `label`, `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `top` | `integer` | The new first shown. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 2.10.0: Moves on the press, and again while held.

### rq.uikit.rack

```lua
rq.uikit.rack(text, opts) -> boolean
```

`since 2.6.0`

Draws a Frostbuy rack tile: a dark see-through square in the shop's black and yellow lines, with
yellow text.

The shop's own racks are painted into its picture, so the tile is drawn from shapes and the game's
font; its lettering is close to the painted one, not the same. "\n" starts a new line, and all
lines take the size that fits the widest. Under the mouse the game's cover pulses over it.

```lua
if rq.uikit.rack("MOD\nRACK", { x = 560, y = 123 }) then shop_open = true end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{disabled?: boolean}` | Place (`w` and `h` default 104 by 106), and `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

### rq.uikit.sort

```lua
rq.uikit.sort(list, index, opts) -> integer|nil, boolean, integer|nil
```

`since 2.6.0` `changed 2.10.0`

Draws the sort column: "SORT" over up to 16 buttons, 30 apart, the current one framed in yellow.

The game's column is see-through, on the Quests screen's parchment; the kit puts that parchment
under it unless `opts.back = false`. A long label gets smaller until it fits. The current button
cannot be clicked, unless `again` names it: a store's SORT is this column with two buttons, and
its second one opens the sort menu each time.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `string[]` | The labels. |
| `index` *(optional)* | `integer` | The current one; nil for none. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{back?: boolean, again?: boolean\|integer, disabled?: boolean, tips?: (string\|` [`rq.UiTip`](../types/rq.UiTip.md) `)[]}` | Place, `back`, `again` (true, or the index of the button that can be clicked while current), `disabled`, `tips` (2.13.0: one for each button). |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The current one. |
| `changed` | `boolean` | true on the update it changed. |
| `clicked` | `integer\|nil` | The index of the button clicked on this update, current or not. |

> Changed in 2.10.0: `again`, and the button clicked.

### rq.uikit.page

```lua
rq.uikit.page(opts, fn) -> boolean
```

`since 2.6.0` `changed 2.7.0` `changed 2.12.0` `changed 2.22.0`

Draws a page of a mod's own over the hub and runs `fn` in a column inside it.

The page covers the hub under the town tabs and above the footer (0, 56, 1024 by 536). The game
shows dimmed under it and gets no mouse and no keys (`rq.hud.capture_mouse`, `rq.hud.block_keys`),
so it is modal. With `title` the title sits on the current town tab's piece at the top left. The
page closes by its close button at the top right, a right click, or Esc; the right click and Esc
close when let go, so the game does not get them. Keep the page's state yourself: draw it while
it is open, and stop when it returns false. It does not open by itself; open it from a button of
your own or a key.

A choice menu from `rq.ui.choose` shows over the page. While it does, the page leaves the mouse and
the keys to the menu, and the right click, Space or Esc that ends the menu does not close the page.

The arrow keys and Enter move the keys' cursor between the page's widgets (`rq.uikit.keys`).
Esc while a number field types (`rq.uikit.stepper`) puts the field's number back and does not
close the page.

```lua
local open = false
rq.on_frame(function()
  if not open then return end
  open = rq.uikit.page({ id = "mine", title = "My Page" }, function(x, y, w, h)
    rq.uikit.button("Do it", { style = "large" })
  end)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{title?: string, pad?: integer, gap?: integer}` | `x`, `y`, `w`, `h` (the hub's area by default), `id` (keeps its state), `title`, `pad` (default 16), `gap` between widgets. |
| `fn` *(optional)* | `fun(x: integer, y: integer, w: integer, h: integer)` | The widgets inside, in a column at the box under the title, clipped to it. |

| Returns | Type | Description |
| --- | --- | --- |
| `open` | `boolean` | false on the update it closes. |

> Changed in 2.7.0: Stays open, under it, while the game's choice menu shows over it.

> Changed in 2.12.0: The arrow keys and Enter move between its widgets.

> Changed in 2.22.0: Esc that ends a number field's typing does not close it.

### rq.uikit.options

```lua
rq.uikit.options(items, opts) -> any|nil
```

`since 2.7.0` `changed 2.9.0` `changed 2.10.0` `changed 2.11.0` `changed 2.12.0` `changed 2.13.0`

Draws the game's choice menu as a widget: its green base, grey rows, separators and a text panel
at the top, laid out as the game lays out the menu. It is not modal and does not wait: it returns
the picked row's id on the update it is clicked. Use it inside a page; `rq.ui.choose` opens the
game's own menu instead.

The list is 380 wide. With fewer than 3 rows to pick it draws the tall buttons, as the game does.
`message` goes in the text panel at the top, in up to 3 lines of 346 pixels. A long row text gets
smaller until it fits.

Its rows are on the kit's keys cursor (see `rq.uikit`): Up and Down go through the rows that can be
picked, wrapping round as the game's menu does, and Enter picks the cursor's row, framed in yellow
as under the mouse. With `keys` the widget takes the keys itself (`rq.uikit.keys`), and Esc picks
Return; the arrows, Enter and Esc are hidden from the game while it shows.

The list grows to `h` (default and at most 762 pixels, the game's base). Past it, the rows under
the message scroll inside the base, with the game's scroll bar right of it (22 pixels more): the
wheel over the list and the bar move them a row at a time, and the keys' cursor stays in sight.
The message stays at the top. Only the rows wholly in sight are listed for `rqmod-ctl`.

Raises an error without a list, with a row without text, or with an `h` that is not a whole
number.

```lua
local pick = rq.uikit.options({ "Attack", "Defense", "-", { id = "hp", text = "HP" } },
  { id = "sortby", message = "Sort by", back = true })
if pick == 0 then open = false elseif pick then sort_by(pick) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `(string\|` [`rq.UiOptionRow`](../types/rq.UiOptionRow.md) `)[]` | The rows: a text, `"-"` for a separator, or a table. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{message?: string, back?: string\|boolean, keys?: boolean, h?: integer}` | Place and `id` (keeps the scroll); `message` (the text panel at the top); `back` (a Return row, true or its text; picking it gives 0); `keys` (the arrow keys, Enter and Esc); `h` (the most height, default 762). |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The picked row's id on the update it is clicked or Enter picks it (0 for Return); nil otherwise. |

> Changed in 2.9.0: `keys`.

> Changed in 2.10.0: `h`, and rows past it scroll.

> Changed in 2.11.0: A row's `comment` box is drawn on the top layer, over widgets drawn later.

> Changed in 2.12.0: The rows are on the kit's keys cursor; Left and Right leave the list.

> Changed in 2.13.0: A row's `comment` is the game's comment window, after 500 ms, as the game's menu shows it.

See also: [`rq.ui.choose`](rq.ui.md#rquichoose)

### rq.uikit.item_data

```lua
rq.uikit.item_data(ii) -> rq.UiItemRow|nil
```

`since 2.8.0` `changed 2.9.0`

Reads an item instance's row data from the game: its name, level line, stats line, icon, rank,
kind, lock, price, place, the classes that may equip it, and whether the game lets it go.

The vault's widgets read it for you; call it to read an item once, or to change a field before
drawing the row.

Raises an error when `ii` is not a whole number.

```lua
local row = rq.uikit.item_data(ii)
if row then rq.log(row.name, row.place) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `row` | [`rq.UiItemRow`](../types/rq.UiItemRow.md) `\|nil` | The row data; nil when there is no such instance. |

> Changed in 2.9.0: `discard`.

### rq.uikit.item_refresh

```lua
rq.uikit.item_refresh(ii)
```

`since 2.8.0` `changed 2.9.0`

Makes item rows and lists read an instance again on their next update.

Lists keep each instance's data for a second, so a change, such as a lock, shows within a second
by itself. Call this after your own change to show it at once. `rq.item.lock`, `sell`, `donate`
and `store` call it for you, and pickers list their items again.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` *(optional)* | `integer` | The instance; nil for all of them. |

> Changed in 2.9.0: Pickers and `item_storage` list again too.

### rq.uikit.item_row

```lua
rq.uikit.item_row(row, opts) -> boolean, "lock"|"unlock"|"sell"|"donate"|nil
```

`since 2.8.0` `changed 2.9.0`

Draws a vault item row, 381 by 128, as the game draws it: the name, the icon with its rank badge,
the red level bar, the stats line in the game's yellow and white, the icons of the classes that
may equip it, LOCKED, and the row's buttons.

The background is cut from the vault's panel (`style = "vault"`), the storage's red one
(`"storage"`), the shop's green one with the price in its GOLD box (`"shop"`), or a character's
brown equip list (`"equip"`). The name is centered and gets smaller until it fits, down to 12
pixels; past that it wraps in two lines of 12 pixels, as the game's does. The stats line wraps at
264 pixels as the game's does, in 3 lines under a level bar and 4 without.

`buttons` adds the vault's LOCK (UNDO LOCK on a locked item), SELL and DONATE buttons at their
places; a click on one is not a click on the row. A locked row has no SELL or DONATE, as in the
vault. With `keys` on the current row, L, S and D press its LOCK, SELL and DONATE, as in the vault.
The buttons only say which was clicked: call `rq.item.lock`, `sell` or `donate` to do it. The row
is listed for `rqmod-ctl` as `row-<id>`, its buttons as `button-<id>-lock`, `-unlock`, `-sell`,
`-donate`.

Raises an error without a row, for an `ii` with no instance, or with another style.

```lua
local clicked, button = rq.uikit.item_row(ii, { x = 538, y = 0, id = "mine", buttons = { lock = true } })
if button == "lock" then rq.item.lock(ii) elseif button == "unlock" then rq.item.lock(ii, false) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `row` | `integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) | An instance, or row data (from `item_data`, or made up). |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{style?: "vault"\|"storage"\|"shop"\|"equip", buttons?: {lock?: boolean, sell?: boolean, donate?: boolean}, current?: boolean, disabled?: boolean, keys?: boolean}` | Place and `id`; `style` (default "vault"); `buttons`; `current` (covered in see-through cyan, as the game marks the row it works on); `disabled` (greyed out, no buttons, no clicks); `keys` (L, S and D press the buttons while the row is current). |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update the row is clicked. |
| `button` | `"lock"\|"unlock"\|"sell"\|"donate"\|nil` | The button clicked on this update. |

> Changed in 2.9.0: The shop and equip styles, two-line names, `keys`, no SELL or DONATE on a locked row.

### rq.uikit.item_icon

```lua
rq.uikit.item_icon(item, opts) -> boolean, "remove"|nil
```

`since 2.21.0`

Draws an item's tile, as the status page's equip slots draw it, and returns whether it was clicked.

The tile is the item's icon, 100 by 100, with its rank badge (CG 11420 + rank) at its bottom left
(`T_ItemIcon`). Under the mouse or the keys' cursor, and while `current`, it gets the game's frame
(216, 255, 0) at 102. With `item` nil it draws nothing, as the game leaves an empty slot to its
page's picture, but it still takes the frame, the click and a tip.

Its `tip` is the game's item card (`rq.uikit.item_card`), left of the tile at its y (right of it
when there is no room), after 500 ms from the mouse and at once from the keys, as the status page
shows it. Give a `tip` of your own (the comment window), or false for none.

With `remove`, REMOVE shows beside the tile; a click on it, or D on the tile from the keys, returns
`"remove"`. The tile only says so: take the item off yourself.

For an item the player must not see yet, pass a row table with the icon you want shown (as
`rq.loot.list`'s `cg`, the game's "?") and `judged = false`: the tile and the card draw the row's
`icon`, never the instance's.

It is listed for `rqmod-ctl ui` with the type "item", the name as label and the ii as `value`
(`item-<id>`), REMOVE as `button-<id>-remove`, and its card as the type "card", which takes no
click.

Raises an error for an `ii` with no instance, an item that is not an ii, a table or nil, or a `size`
that is not a whole number above 0.

```lua
local SLOTS = { 1, 11, 17 } -- weapon, armor, held item
rq.on_frame(function()
  if not open then return end
  open = rq.uikit.page({ id = "gear", title = "Gear" }, function(x, y)
    for i, kind in ipairs(SLOTS) do
      local ii = rq.ain.call("キャラ_装備取得", chara, kind)
      local _, act = rq.uikit.item_icon(ii > 0 and ii or nil, { x = x + 20, y = y + (i - 1) * 116, id = "slot" .. i, remove = true })
      if act == "remove" then take_off(chara, kind) end
    end
  end)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `item` | `integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) `\|nil` | An instance, row data, or nil for an empty slot. |
| `opts` *(optional)* | [`rq.UiItemIconOpts`](../types/rq.UiItemIconOpts.md) | `size`, `current`, `disabled`, `remove`, `judged`; place, `id`, `tip`, `nav`. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update the tile is clicked. |
| `action` | `"remove"\|nil` | `"remove"` on the update REMOVE is pressed. |

### rq.uikit.item_card

```lua
rq.uikit.item_card(item, opts) -> integer, integer, integer, integer
```

`since 2.21.0`

Draws the game's item card now, on the top layer, and returns its box.

The card is the game's `T_ItemComment`: CG 10402, 393 by 139, with the item's row on it (the name,
the icon with its rank, the kind, the stats line, the level bar, LOCKED, the classes), as the
status page shows it beside an equip slot. With `judged = false` it is the game's card for an
item not identified: CG 10403 (UNIDENTIFIED) over it and the icon alone.

It goes at the mouse + 11, + 20 unless `x` and `y` are given. Past the screen's right edge it goes
to the left of the mouse, and past y 736 it goes up to end at 736, as the game keeps its card on
the screen. Call it on every update it should show; `rq.uikit.item_icon` shows it as its tip.

It is listed for `rqmod-ctl ui` with the type "card", which takes no click.

Raises an error for an `ii` with no instance, or an item that is not an ii or a table.

```lua
rq.on_frame(function()
  if hovered_ii then rq.uikit.item_card(hovered_ii) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `item` | `integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) | An instance, or row data. |
| `opts` *(optional)* | `{x?: integer, y?: integer, judged?: boolean, id?: string\|integer}` | `x` and `y` (default at the mouse); `judged` (default true); `id` for `rqmod-ctl ui`. |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` |  |
| `y` | `integer` |  |
| `w` | `integer` | 393. |
| `h` | `integer` | 139. |

### rq.uikit.item_card_size

```lua
rq.uikit.item_card_size() -> integer, integer
```

`since 2.21.0`

Returns the item card's size, to place it beside a widget as the game's screens do.

| Returns | Type | Description |
| --- | --- | --- |
| `w` | `integer` | 393. |
| `h` | `integer` | 139. |

### rq.uikit.item_list

```lua
rq.uikit.item_list(rows, index, opts) -> integer|nil, boolean, "lock"|"unlock"|"sell"|"donate"|nil, integer|nil, boolean
```

`since 2.8.0` `changed 2.9.0` `changed 2.11.0` `changed 2.12.0`

Draws the vault's item list: rows 128 apart and the game's scroll bar beside them.

6 rows show by default, as in the vault. The wheel over the rows scrolls a row at a time; the bar's
arrows, its track and a drag of the bar scroll it too. A click on a row makes it the current one
and chooses it. Rows given as instances are read from the game and kept for a second
(`item_refresh`). The scroll is kept by `opts.id` (`rq.uikit.state("itemlist:<id>").top`).

With `keys`, the list takes the keys (`rq.uikit.keys`) and its rows are the kit's keys cursor: Up
and Down move the current row, also on to a widget outside at the list's ends; Page Up and Page
Down move six rows, Home and End to the first and last, scrolling to keep it shown; a held key
repeats after 250 ms, every 50 ms. Enter chooses the current row, and L, S and D press its
buttons. Those keys are hidden from the game while the list shows (`rq.hud.block_keys`).

With `drag`, a row pressed and moved more than 6 pixels is dragged: its icon follows the mouse on
the top layer (`rq.hud.top`), over every widget and clip, and a list of the same group under it
lights up. Let go over another list of the group and
`rq.uikit.item_dropped(group)` returns the row on that update; nothing moves by itself.
`item_storage` is the game's storage screen built on this.

Raises an error without a list, or when `drag` is not a name.

```lua
local list = rq.uikit.item_sort(rq.uikit.item_filter(my_iis, { type = 1 }), 11)
rq.on_frame(function()
  pick = rq.uikit.item_list(list, pick, { x = 538, y = 0, id = "weapons" })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `rows` | `(integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) `)[]` | The rows: instances or row data. |
| `index` *(optional)* | `integer` | The current row; nil for none. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{shown?: integer, style?: "vault"\|"storage"\|"shop"\|"equip", buttons?: {lock?: boolean, sell?: boolean, donate?: boolean}, bar?: {y: integer, h: integer}, keys?: boolean, drag?: string}` | Place and `id`; `shown` (rows at once, default 6); `style` and `buttons` for each row; `bar` (where the scroll bar runs, default beside the rows); `keys` (the keys above); `drag` (a group name: rows can be dragged to another list of the group). |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The current row. |
| `changed` | `boolean` | true on the update it changed. |
| `button` | `"lock"\|"unlock"\|"sell"\|"donate"\|nil` | A row button clicked on this update. |
| `at` | `integer\|nil` | The index of that button's row. |
| `chosen` | `boolean` | true on the update a row is clicked or Enter is pressed (2.9.0). |

> Changed in 2.9.0: `keys`, `drag`, and the fifth return.

> Changed in 2.11.0: The dragged icon is drawn once, on the top layer.

> Changed in 2.12.0: `keys` uses the kit's keys cursor; it repeats after 250 ms, every 50 ms (was 400 and 80).

### rq.uikit.item_dropped

```lua
rq.uikit.item_dropped(group) -> integer|rq.UiItemRow|nil, string|nil, string|nil, integer|nil
```

`since 2.9.0`

Returns the row dropped on this update on another list of a drag group (`item_list`'s `drag`).

Raises an error when `group` is not a name.

```lua
rq.on_frame(function()
  a_pick = rq.uikit.item_list(a, a_pick, { x = 101, y = 0, id = "a", drag = "mine" })
  b_pick = rq.uikit.item_list(b, b_pick, { x = 538, y = 0, id = "b", drag = "mine" })
  local row, from, to = rq.uikit.item_dropped("mine")
  if row then move(row, from, to) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `group` *(optional)* | `string` | The group; nil for any. |

| Returns | Type | Description |
| --- | --- | --- |
| `row` | `integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) `\|nil` | The row as its list holds it; nil when nothing was dropped. |
| `from` | `string\|nil` | The `id` of the list it came from. |
| `to` | `string\|nil` | The `id` of the list it was dropped on. |
| `index` | `integer\|nil` | Its index in the list it came from. |

### rq.uikit.item_storage

```lua
rq.uikit.item_storage(opts) -> integer|nil, "vault"|"storage"|nil
```

`since 2.9.0` `changed 2.10.0`

Draws the game's storage screen: the storage's red list on the left and the vault's list right of
it (437 pixels apart, as the game places them), each with its scroll bar, the vault's count and
the storage's in their boxes, and the vault's filter column and SORT. Drag a row from one list to
the other to move the item (`rq.item.store`).

As on the game's screen, the filters and the sort apply to both lists, and each count is of its
list as filtered. While a category's sub-filters show over the vault list's first row, that list
starts a row lower. The sort starts at the stores' saved mode, as `item_picker`'s. The lists are
read again after a move, a filter or a sort, and every 2 seconds. The lists are listed for
`rqmod-ctl` as `row-<id>-storage-<n>` and `row-<id>-vault-<n>`; the filters and SORT as in
`item_picker`. `rq.uikit.state("storage:<id>")` has `filter` and `sort`.

```lua
rq.on_frame(function()
  if not open then return end
  rq.hud.capture_mouse()
  local ii, where = rq.uikit.item_storage({ id = "mine" })
  if ii then rq.log("moved", ii, "to the", where) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{shown?: integer}` | Place (the storage list's top left, default 101, 0) and `id`; `shown` (rows, default 6). |

| Returns | Type | Description |
| --- | --- | --- |
| `ii` | `integer\|nil` | The instance moved on this update. |
| `where` | `"vault"\|"storage"\|nil` | Where it went. |

> Changed in 2.10.0: The filter column and SORT, for both lists.

### rq.uikit.number

```lua
rq.uikit.number(value, opts) -> integer, integer, integer, integer
```

`since 2.8.0` `changed 2.9.0` `changed 2.14.0` `changed 2.15.0`

Draws a number as the game does: the vault's counters (`font = "count"`: the game's font, 20
pixels, bold, white), or one of the game's digit fonts.

A digit font is a CG cut across into 10 equal cells, 0 to 9, as the game's `T_NumberCg`. By name:

| `font` | CG | Where the game uses it |
| --- | --- | --- |
| `"gold"` | 11103 | The vault's and the shop's gold, 16 by 23 |
| `"hp"` | 10096 | HP in battle, skill uses on the mini cards |
| `"level"` | 10122 | Levels and maximums on the cards, skill uses on the status page |
| `"level_max"` | 10124 | A level at its maximum, on the cards (red) |
| `"status"` | 10321 | The status page's points, EXP and gold; the level up; the results |
| `"small"` | 10210 | Skill uses on the mini-mini cards |
| `"world"` | 10507 | The world level on the title |
| `"gallery"` | 12252 | The CG mode's page numbers |

Any other CG number works as a font too, a mod image from `rq.image.add` included. With `hyphen` its
CG has an 11th cell, a "-", and a negative number gets it; without, a negative number draws as 0,
as the game's.

Raises an error for a number that is not whole, an unknown font name, a CG that is not there, or
another `align`.

```lua
rq.uikit.number(#list, { x = 957, y = 31, w = 39 })
rq.uikit.number(price, { x = 758, y = 2, font = "gold", w = 118, align = "right", gap = 1 }) -- the shop's
rq.uikit.number(level, { x = 300, y = 200, font = level >= max and "level_max" or "level" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `integer` | The number. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{font?: "count"\|"gold"\|"hp"\|"level"\|"level_max"\|"status"\|"small"\|"world"\|"gallery"\|integer, digits?: integer, align?: "left"\|"center"\|"right", gap?: integer, hyphen?: boolean, tint?: integer[]}` | Place (`w` with `align` places it in that width, default centered); `font` (default "count"; a name or a CG number); `digits` (pads with zeros to that many); `gap` (pixels between digits, default 0); `hyphen` (the CG has an 11th cell, "-"); `tint` (2.15.0: multiplies a digit font's colors, as `rq.hud.cg`'s). |

| Returns | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The left edge of what was drawn. |
| `y` | `integer` | Its top edge. |
| `w` | `integer` | Its width, in pixels. |
| `h` | `integer` | Its height. |

> Changed in 2.9.0: `align` and `gap`.

> Changed in 2.14.0: The game's digit fonts by name or CG number, `hyphen`, and it returns its place.

> Changed in 2.15.0: `tint`.

### rq.uikit.filters

```lua
rq.uikit.filters(state, opts) -> rq.UiFilterState, boolean
```

`since 2.8.0` `changed 2.9.0`

Draws the vault's filter column and returns what is picked: the categories (Special, Weapon,
Armor, Item / Other), the classes, and Locked / Unlocked, on the column's grey with its
"[FILTERING]" heads; and, while a category with sub-filters is picked, its panel of sub-filters
over the list's first row.

`style` picks the column as each screen paints it: the vault's (`"vault"`), the shop's without
Locked / Unlocked (`"shop"`), or a character's equip list with Equippable / Unequippable under
Locked / Unlocked (`"equip"`; put the character in `state.chara`).

Each group works as the vault's: a click picks one, a second click on it clears it; with none
picked all are lit, with one picked only it is. Picking another category clears the sub-filter.
The state table is changed in place. The buttons are listed for `rqmod-ctl` as
`filter-<id>-special`, `-weapon`, `-armor`, `-item`, `-class-1` to `-class-8`, `-locked`,
`-unlocked`, `-equippable`, `-unequippable`, and the sub-filters by their names
(`filter-<id>-swords`, `-rank-a`, `-others`).

Raises an error when the state is not a table of whole numbers, or with another style.

```lua
local state = {}
rq.on_frame(function()
  local _, changed = rq.uikit.filters(state, { x = 945, y = 154, id = "mine" })
  if changed then list = rq.uikit.item_filter(all, state) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `state` *(optional)* | [`rq.UiFilterState`](../types/rq.UiFilterState.md) | The state; a new one when nil. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{style?: "vault"\|"shop"\|"equip", back?: boolean, classes?: boolean, lock?: boolean, equip?: boolean, sub?: false\|{x: integer, y: integer}}` | Place (the categories' top left, 945, 154 in the vault, the shop and the equip list) and `id`; `style` (default "vault"); `back` (the column's grey, default true); `classes`, `lock` and `equip` (false leaves them out); `sub` (where the sub-filters' panel goes, default 407 left and 153 up, over the list's first row; false leaves it out). |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | [`rq.UiFilterState`](../types/rq.UiFilterState.md) | The state. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 2.9.0: `style`, and Equippable / Unequippable.

### rq.uikit.item_filter

```lua
rq.uikit.item_filter(list, state) -> table
```

`since 2.8.0` `changed 2.9.0`

Returns the items of a list that pass a filter state, tested as the vault tests them
(`アイテム倉庫_一覧_種類確認`, `_職業確認`, `_装備タイプ確認`, `_ＬＯＣＫタイプ確認`).

Raises an error without a list, or when the state is not a table of whole numbers.

```lua
local swords = rq.uikit.item_filter(rq.items(), { type = 1, sub = 2 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `(integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) `\|` [`rq.Item`](../types/rq.Item.md) `)[]` | Instances, row data or `rq.items()` entries. |
| `state` *(optional)* | [`rq.UiFilterState`](../types/rq.UiFilterState.md) | The filter; nil keeps all. |

| Returns | Type | Description |
| --- | --- | --- |
| `list` | `table` | A new list of the entries that pass, in their order. |

> Changed in 2.9.0: `equip` and `chara`.

### rq.uikit.item_sort

```lua
rq.uikit.item_sort(list, mode) -> table
```

`since 2.8.0`

Sorts a list of items in place as the vault sorts it, with the game's own comparers
(`compItem_*`).

Mode 1 is the vault's default, by item number. Modes 11 to 28 are its "Default Sort" menu: 11
Attack, 12 Magic, 13 Accuracy, 14 Critical, 15 Stun, 16 Speed, 17 Defense, 18 Resistance, 19
Evasion, 20 Resilience, 21 HP, 22 to 26 the five damage reductions (fire, ice, electric, light,
darkness), 27 low and 28 high enhancement rank. Ties keep the item-number order. It calls the game
for each pair, so sort when the list changes, not on every update.

Raises an error without a list or with another mode.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `(integer\|` [`rq.UiItemRow`](../types/rq.UiItemRow.md) `\|` [`rq.Item`](../types/rq.Item.md) `)[]` | Instances, row data or `rq.items()` entries. |
| `mode` *(optional)* | `integer` | The mode; default 1. |

| Returns | Type | Description |
| --- | --- | --- |
| `list` | `table` | The same list. |

See also: [`rq.uikit.item_sorts`](rq.uikit.md#rquikititem_sorts)

### rq.uikit.item_sorts

```lua
rq.uikit.item_sorts() -> {mode: integer, name: string}[]
```

`since 2.8.0`

Lists the vault's sort modes 11 to 28 with the game's names (`アイテム倉庫_ソート名`), for a menu.

```lua
local rows = {}
for _, s in ipairs(rq.uikit.item_sorts()) do rows[#rows + 1] = { id = s.mode, text = s.name } end
rq.ui.choose(rows, function(mode) if mode ~= 0 then sort_by(mode) end end)
```

| Returns | Type | Description |
| --- | --- | --- |
| `modes` | `{mode: integer, name: string}[]` | The modes, in the menu's order. |

### rq.uikit.item_picker

```lua
rq.uikit.item_picker(opts) -> integer|nil, integer|nil
```

`since 2.8.0` `changed 2.9.0` `changed 2.10.0`

Draws an item picker over the player's items, laid out as the vault: the list with its scroll
bar, the filter column 407 pixels right and 154 down, the count of items listed in the column's
box, and the store's SORT under the column (405 right and 682 down, as at 943, 682 in the game).

SORT is the game's: "Default Sort" sorts by item number, and the second button, which shows the
mode's short name, opens the game's sort menu (`rq.ui.choose`, modes 11 to 28) each time it is
clicked. The mode in use is framed. The sort starts at the stores' saved mode
(`アイテムソートモード`), and a new one is saved, as the game's stores do, so the vault opens
sorted the same way. A new sort goes back to the top of the list.

It lists the items in the vault, the storage, both, the shop's stock or the quest storage,
filtered and sorted, and reads them again when the filters or the sort change, after an
`rq.item` change, and every 2 seconds. The rows and the filter column take the look of the place:
the shop's green rows with their prices and its column without Locked, the storage's red rows.
With `chara` the rows are a character's equip list and the column gets Equippable /
Unequippable for them. The quest storage keeps the game's order unless a sort is picked. While a
category's sub-filters show, the list starts a row lower, as the vault's does. Clicking a row (or
Enter, with `keys`) returns its instance; the picker moves nothing. The filters, the sort, the
scroll and the pick are kept by `opts.id` (`rq.uikit.state("picker:<id>")` has `filter`, `sort`,
`list` and `ii`).

Raises an error with another place, or when `chara` is not a whole number.

(`button-<id>-sort` is now `tab-<id>-sort-default-sort` and the mode's tab); the saved sort mode.

```lua
local picking = true
rq.on_frame(function()
  if not picking then return end
  rq.hud.capture_mouse() -- the game under it gets no clicks
  local ii = rq.uikit.item_picker({ x = 538, y = 0, id = "gift" }) -- where the vault's list is
  if ii then
    picking = false
    give(ii)
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{where?: "vault"\|"storage"\|"both"\|"shop"\|"quest", chara?: integer, shown?: integer, style?: "vault"\|"storage"\|"shop"\|"equip", sort?: integer, keys?: boolean}` | Place and `id`; `where` (default "vault"); `chara` (a character's roster slot: their equip list); `shown` (rows, default 6); `style` of the rows (default from `where`); `sort` (the first sort mode, default the stores' saved one; a mode under 10 is 1, as in the game); `keys` (the list's keys). |

| Returns | Type | Description |
| --- | --- | --- |
| `picked` | `integer\|nil` | The instance picked on this update. |
| `current` | `integer\|nil` | The instance picked last. |

> Changed in 2.9.0: The shop and quest places, `chara`, `keys`; a click on the current row picks it again.

> Changed in 2.10.0: The game's SORT at the bottom right, in place of the sort button under the column
