# rq.uikit

`since 1.7.0`

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
Keyboard moves between widgets are not there yet.

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
| [`rq.uikit.tabs`](#rquikittabs) | Draws Config's tabs side by side: normal, hovered and current. |
| [`rq.uikit.panel`](#rquikitpanel) | Draws a Config page or the 3D tab's dark block, and runs `fn` in a column inside it. |
| [`rq.uikit.list`](#rquikitlist) | Draws rows on a dark block that scroll by the wheel. |
| [`rq.uikit.menu`](#rquikitmenu) | Draws a menu with levels: lists side by side, where an entry with `items` opens the next list. |
| [`rq.uikit.row`](#rquikitrow) | Places the widgets called in `fn` side by side. |
| [`rq.uikit.col`](#rquikitcol) | Places the widgets called in `fn` one under the other. |
| [`rq.uikit.space`](#rquikitspace) | Leaves empty space in a row or column. |
| [`rq.uikit.last`](#rquikitlast) | Returns where the last widget went, as for a tooltip beside it. |
| [`rq.uikit.hovered`](#rquikithovered) | Returns whether the mouse was over a kit widget on this update so far. |
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
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{dir?: "col"\|"row", gap?: integer, disabled?: boolean}` | `dir` (default "col"), `gap` in pixels (default 20), `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The checked one. |
| `changed` | `boolean` | true on the update it changed. |

### rq.uikit.slider

```lua
rq.uikit.slider(value, opts) -> number, boolean
```

`since 1.7.0` `changed 1.8.0`

Draws the Sound tab's slider.

Drag the knob or click the track; the drag goes on while the button is down, also off the track.
The wheel over it moves it by `step`, or by a twentieth, and the game does not get that wheel step.

| Parameter | Type | Description |
| --- | --- | --- |
| `value` | `number` | The value. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{min?: number, max?: number, step?: number, low?: string, high?: string, label?: string, disabled?: boolean}` | `w`: the track's width (default 200). `min` (default 0), `max` (default 1), `step`, `low` and `high` (texts at the ends), `label` (its name in `rqmod-ctl ui`), `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `number` | The new value. |
| `changed` | `boolean` | true on the update it changed. |

> Changed in 1.8.0: Added `opts.label`.

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
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{style?: "town"\|string, gap?: integer}` | Place; `w` is each tab's width (default 120, or the style's). `style`, and `gap` between styled tabs. |

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
| `items` | `(string\|{text: string, disabled?: boolean})[]` | The rows. |
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
| `rows` | `{no?: integer\|string, name?: string, mark?: integer\|string, disabled?: boolean}[]` | The rows. |
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

`since 2.6.0`

Draws the game's scroll bar, up and down: two arrows, the track and the bar.

`top`, `count` and `shown` are in any unit: rows, or pixels with `opts.step`. The bar is
`shown / count` of the track, at least 10 pixels, as the game sizes it. The arrows move by `step`,
a click on the track by `shown` toward the click, and a drag of the bar goes where the bar goes. The
wheel over the bar, or over `opts.wheel`, moves by `step`, and the game does not get it.

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
rq.uikit.sort(list, index, opts) -> integer|nil, boolean
```

`since 2.6.0`

Draws the sort column: "SORT" over up to 16 buttons, 30 apart, the current one framed in yellow.

The game's column is see-through, on the Quests screen's parchment; the kit puts that parchment
under it unless `opts.back = false`. A long label gets smaller until it fits.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `string[]` | The labels. |
| `index` *(optional)* | `integer` | The current one; nil for none. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{back?: boolean, disabled?: boolean}` | Place, `back`, `disabled`. |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer\|nil` | The current one. |
| `changed` | `boolean` | true on the update it changed. |

### rq.uikit.page

```lua
rq.uikit.page(opts, fn) -> boolean
```

`since 2.6.0` `changed 2.7.0`

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

### rq.uikit.options

```lua
rq.uikit.options(items, opts) -> any|nil
```

`since 2.7.0`

Draws the game's choice menu as a widget: its green base, grey rows, separators and a text panel
at the top, laid out as the game lays out the menu. It is not modal and does not wait: it returns
the picked row's id on the update it is clicked. Use it inside a page; `rq.ui.choose` opens the
game's own menu instead.

The list is 380 wide. With fewer than 3 rows to pick it draws the tall buttons, as the game does.
`message` goes in the text panel at the top, in up to 3 lines of 346 pixels. A long row text gets
smaller until it fits.

Raises an error without a list or with a row without text.

```lua
local pick = rq.uikit.options({ "Attack", "Defense", "-", { id = "hp", text = "HP" } },
  { id = "sortby", message = "Sort by", back = true })
if pick == 0 then open = false elseif pick then sort_by(pick) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `(string\|` [`rq.UiOptionRow`](../types/rq.UiOptionRow.md) `)[]` | The rows: a text, `"-"` for a separator, or a table. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{message?: string, back?: string\|boolean}` | Place and `id`; `message` (the text panel at the top); `back` (a Return row, true or its text; picking it gives 0). |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `any\|nil` | The picked row's id on the update it is clicked (0 for Return); nil otherwise. |

See also: [`rq.ui.choose`](rq.ui.md#rquichoose)
