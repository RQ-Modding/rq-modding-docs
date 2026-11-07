# rq.uikit

`since 1.7.0`

Widgets in the look of the game's Config screen.

They are drawn with `rq.hud` from the game's own pictures: Config draws its labels into its
pictures, so the kit cuts out the parts that carry no text and writes its own text on them. The kit
is Lua on the public `rq.hud` calls.

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
| `themes` | `{config:` [`rq.UiTheme`](../types/rq.UiTheme.md) `}` | The built-in themes. |

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

`since 1.7.0`

Draws a Config button with text.

The button is at least 150 wide (or the text's width) and 40 high. When hovered, the game's cover
pulses over it every 2 seconds. A click counts when the button is let go over the same button it
went down on.

```lua
if rq.uikit.button("Reset", { id = "reset" }) then reset() end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) `\|{disabled?: boolean}` | Place, and `disabled` to grey it out. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the update it is clicked. |

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

`since 1.7.0`

Draws Config's tabs side by side: normal, hovered and current.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `string[]` | The tab texts. |
| `index` | `integer` | The current tab. |
| `opts` *(optional)* | [`rq.UiPlace`](../types/rq.UiPlace.md) | Place; `w` is each tab's width (default 120). |

| Returns | Type | Description |
| --- | --- | --- |
| `index` | `integer` | The current tab. |
| `changed` | `boolean` | true on the update it changed. |

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

`since 1.7.0`

Draws rows on a dark block that scroll by the wheel.

A bar shows when the rows do not fit. A list's clip replaces a clip of your own.

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
