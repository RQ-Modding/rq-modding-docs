# rq.hud

`since 0.2.0`

Draws text, boxes and CGs over the game, and reads clicks on them.

The HUD is immediate mode: draw everything again on every `rq.on_frame`, and it shows for that
frame. It is drawn on the game's own picture, after the game's scene, in game pixels. Every frame
can hold up to 480 draw calls; past that, a call draws nothing.

```lua
local function button(x, y, w, h, label)
  if rq.hud.hit(x, y, w, h) then
    rq.hud.rect(x, y, w, h, 80, 100, 160, 235)
  else
    rq.hud.rect(x, y, w, h, 28, 36, 64, 225)
  end
  rq.hud.text(x + 14, y + 6, label, { size = 18 })
  return rq.hud.clicked(x, y, w, h)
end
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.hud.screen`](#rqhudscreen) | Returns the size of the game screen. |
| [`rq.hud.rect`](#rqhudrect) | Draws a filled box. |
| [`rq.hud.text`](#rqhudtext) | Draws a line of UTF-8 text. |
| [`rq.hud.text_width`](#rqhudtext_width) | Returns how wide `rq.hud.text` draws a text. |
| [`rq.hud.wrap`](#rqhudwrap) | Breaks a text into lines that fit a width. |
| [`rq.hud.cg`](#rqhudcg) | Draws a game CG, or a mod image. |
| [`rq.hud.cg_size`](#rqhudcg_size) | Returns a CG's size without drawing it. |
| [`rq.hud.clip`](#rqhudclip) | Shows what is drawn next only inside a box, as for a list that scrolls. |
| [`rq.hud.hit`](#rqhudhit) | Returns whether the mouse is inside a box on this update. |
| [`rq.hud.clicked`](#rqhudclicked) | Returns whether the left button went down inside a box on this update. |
| [`rq.hud.block_game_input`](#rqhudblock_game_input) | Hides the mouse buttons from the game, so a click on the HUD does not also click the game. |
| [`rq.hud.block_keys`](#rqhudblock_keys) | Hides the keyboard from the game for this update. |
| [`rq.hud.text_begin`](#rqhudtext_begin) | Starts reading typed text. |
| [`rq.hud.text_value`](#rqhudtext_value) | Returns the typed text and whether reading is on. |
| [`rq.hud.text_end`](#rqhudtext_end) | Stops reading typed text. |

### rq.hud.screen

```lua
rq.hud.screen() -> integer, integer
```

`since 0.2.0`

Returns the size of the game screen.

| Returns | Type | Description |
| --- | --- | --- |
| `w` | `integer` | Width in pixels, usually 1024. |
| `h` | `integer` | Height in pixels, usually 768. |

### rq.hud.rect

```lua
rq.hud.rect(x, y, w, h, r, g, b, a)
```

`since 0.2.0`

Draws a filled box.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` | `integer` | Width, in pixels. |
| `h` | `integer` | Height, in pixels. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default 20. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default 20. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default 30. |
| `a` *(optional)* | `integer` | Opacity, 0 to 255. Default 220. |

### rq.hud.text

```lua
rq.hud.text(x, y, str, style)
```

`since 0.2.0` `changed 1.8.0`

Draws a line of UTF-8 text.

The text is white with a dark edge unless the style says otherwise. The font is VL PGothic, from
the game's `xsystem4\fonts` folder, each letter at its own width. Only characters the game's font
can draw show. With `w` and `align` the text is placed in the box `w` wide from `x`, and with `h`
and `valign` in the box `h` high from `y`; text wider than the box goes past it on both sides.

Raises an error for an unknown `align` or `valign`.

```lua
rq.hud.text(0, 40, "Centered", { size = 20, w = 1024, align = "center" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge, or of the box with `style.w`, in game pixels. |
| `y` | `integer` | Top edge, or of the box with `style.h`, in game pixels. |
| `str` | `string` | The text. |
| `style` *(optional)* | [`rq.HudTextStyle`](../types/rq.HudTextStyle.md) | Size, color and placement. |

> Changed in 1.8.0: The font is VL PGothic with letters at their own width (before, VL Gothic with half-width Latin letters).

See also: [`rq.hud.text_width`](rq.hud.md#rqhudtext_width)

### rq.hud.text_width

```lua
rq.hud.text_width(str, size_or_style) -> integer
```

`since 0.2.0`

Returns how wide `rq.hud.text` draws a text.

Only `size` and `bold` of a style count.

| Parameter | Type | Description |
| --- | --- | --- |
| `str` | `string` | The text. |
| `size_or_style` *(optional)* | `number\|` [`rq.HudTextStyle`](../types/rq.HudTextStyle.md) | A font size, or a style. Default size 16. |

| Returns | Type | Description |
| --- | --- | --- |
| `px` | `integer` | Width in pixels; 0 for an empty text. |

### rq.hud.wrap

```lua
rq.hud.wrap(str, max_px, size) -> string[]
```

`since 0.2.0`

Breaks a text into lines that fit a width.

Lines break at spaces when they can, else inside a word, and also at each line break in the text.

```lua
for i, line in ipairs(rq.hud.wrap(desc, 300, 16)) do
  rq.hud.text(20, 100 + (i - 1) * 20, line, { size = 16 })
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `str` | `string` | The text. |
| `max_px` | `integer` | The widest a line may be, in pixels (at least 8). |
| `size` *(optional)* | `number` | The font size to measure with. Default 14. |

| Returns | Type | Description |
| --- | --- | --- |
| `lines` | `string[]` | The lines in order; empty for an empty text. |

### rq.hud.cg

```lua
rq.hud.cg(x, y, cg_no, opts) -> integer, integer
```

`since 0.2.0` `changed 1.6.0`

Draws a game CG, or a mod image.

`cg_no` is a game CG number (item icons and the like) or a number from `rq.image.add`. Up to 160
different CGs are kept for drawing; past that, a new one draws nothing.

Raises an error for a `src` whose `w` or `h` is under 1.

```lua
rq.hud.cg(100, 100, icon, { w = 32, h = 32, alpha = 180 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `cg_no` | `integer` | A CG number. |
| `opts` *(optional)* | [`rq.HudCgOpts`](../types/rq.HudCgOpts.md) | The part, size, opacity and tint. |

| Returns | Type | Description |
| --- | --- | --- |
| `w` | `integer` | The CG's own width, whatever is drawn; 0 when there is no such CG. |
| `h` | `integer` | The CG's own height; 0 when there is no such CG. |

> Changed in 1.6.0: Added `opts`.

See also: [`rq.hud.cg_size`](rq.hud.md#rqhudcg_size)

### rq.hud.cg_size

```lua
rq.hud.cg_size(cg_no) -> integer|nil, integer
```

`since 1.6.0`

Returns a CG's size without drawing it.

| Parameter | Type | Description |
| --- | --- | --- |
| `cg_no` | `integer` | A CG number. |

| Returns | Type | Description |
| --- | --- | --- |
| `w` | `integer\|nil` | Width in pixels, or nil when there is no such CG. |
| `h` | `integer` | Height in pixels. |

### rq.hud.clip

```lua
rq.hud.clip(x, y, w, h)
```

`since 1.6.0`

Shows what is drawn next only inside a box, as for a list that scrolls.

The clip lasts until `rq.hud.clip()` with no arguments. A new clip replaces the box; it does not
narrow it. Every frame starts with no clip.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` *(optional)* | `integer` | Left edge, in game pixels. Leave all four out to end the clip. |
| `y` *(optional)* | `integer` | Top edge, in game pixels. |
| `w` *(optional)* | `integer` | Width, in pixels. |
| `h` *(optional)* | `integer` | Height, in pixels. |

### rq.hud.hit

```lua
rq.hud.hit(x, y, w, h) -> boolean
```

`since 0.2.0`

Returns whether the mouse is inside a box on this update.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` | `integer` | Width, in pixels. |
| `h` | `integer` | Height, in pixels. |

| Returns | Type | Description |
| --- | --- | --- |
| `inside` | `boolean` | true while the cursor is in the box. |

### rq.hud.clicked

```lua
rq.hud.clicked(x, y, w, h) -> boolean
```

`since 0.2.0`

Returns whether the left button went down inside a box on this update.

| Parameter | Type | Description |
| --- | --- | --- |
| `x` | `integer` | Left edge, in game pixels. |
| `y` | `integer` | Top edge, in game pixels. |
| `w` | `integer` | Width, in pixels. |
| `h` | `integer` | Height, in pixels. |

| Returns | Type | Description |
| --- | --- | --- |
| `clicked` | `boolean` | true on the one update the button went down in the box. |

See also: [`rq.hud.block_game_input`](rq.hud.md#rqhudblock_game_input)

### rq.hud.block_game_input

```lua
rq.hud.block_game_input()
```

`since 0.2.0`

Hides the mouse buttons from the game, so a click on the HUD does not also click the game.

It lasts for this update and until the buttons come up. `rq.input.mouse` and the HUD calls still
see the clicks.

### rq.hud.block_keys

```lua
rq.hud.block_keys()
```

`since 0.3.0`

Hides the keyboard from the game for this update.

Call it on every update while a modal HUD is open. The mouse buttons are not affected (use
`rq.hud.block_game_input`), and `rq.input.key` still reads the real keys.

### rq.hud.text_begin

```lua
rq.hud.text_begin(initial, max_bytes)
```

`since 0.3.0`

Starts reading typed text.

It uses the system's text input, so input methods and keyboard layouts work. Only characters the
game's font can draw are kept, and Backspace removes the last character. Read the text with
`rq.hud.text_value` and end with `rq.hud.text_end`. Calling it again restarts with the new text.

```lua
rq.hud.text_begin("Rance", 20)
rq.on_frame(function()
  local text, on = rq.hud.text_value()
  if on then rq.hud.text(20, 20, text .. "_") end
  if on and rq.input.key(rq.input.code("enter")) then rq.hud.text_end() end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `initial` *(optional)* | `string` | The starting text, in UTF-8. Default "". |
| `max_bytes` *(optional)* | `integer` | The longest the text may be, in bytes, 1 to 255. Default 40. |

See also: [`rq.hud.text_value`](rq.hud.md#rqhudtext_value)

### rq.hud.text_value

```lua
rq.hud.text_value() -> string, boolean
```

`since 0.3.0`

Returns the typed text and whether reading is on.

| Returns | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text so far, in UTF-8. |
| `active` | `boolean` | true between `text_begin` and `text_end`. |

### rq.hud.text_end

```lua
rq.hud.text_end()
```

`since 0.3.0`

Stops reading typed text.

The text stays readable with `rq.hud.text_value` until the next `text_begin`.
