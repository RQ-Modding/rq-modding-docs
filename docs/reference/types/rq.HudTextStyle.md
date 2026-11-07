# rq.HudTextStyle

How `rq.hud.text` draws text.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `size` *(optional)* | `number` | Font size, in pixels. Default 16. |
| `r` *(optional)* | `integer` | Red, 0 to 255. Default 255. |
| `g` *(optional)* | `integer` | Green, 0 to 255. Default 255. |
| `b` *(optional)* | `integer` | Blue, 0 to 255. Default 255. |
| `a` *(optional)* | `integer` | Opacity, 0 to 255. Default 255. Since 1.6.0. |
| `w` *(optional)* | `integer` | Width of the box `align` places the text in, in pixels. Since 1.6.0. |
| `h` *(optional)* | `integer` | Height of the box `valign` places the text in, in pixels. Since 1.6.0. |
| `align` *(optional)* | `"left"\|"center"\|"right"` | Where the text sits in the box `w` wide. Default "left". Since 1.6.0. |
| `valign` *(optional)* | `"top"\|"center"\|"bottom"` | Where the text sits in the box `h` high. Default "top". Since 1.6.0. |
| `edge` *(optional)* | `boolean` | false leaves out the dark edge, as on Config's tabs. Default true. Since 1.7.0. |
| `bold` *(optional)* | `boolean` | The heavier weight the game's own Config labels look like. Default false. Since 1.8.0. With `font = "game"`: the game's bold. |
| `font` *(optional)* | `"hud"\|"game"` | "game" draws in the game's own font, as its buttons and lists do: no dark edge, and `edge` does not count. Default "hud". Since 2.5.0. |
| `face` *(optional)* | `256\|257\|258` | With `font = "game"`: the game's font number. 258 is on most buttons, lists and the castle; 256 on item names; 257 on big marks. Default 258. Since 2.5.0. |
| `outline` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer, w?: integer}` | With `font = "game"`: an outline in this color, `w` pixels wide (1 to 4, default 1), as the castle's room names. Since 2.5.0. |
| `shadow` *(optional)* | `integer[]\|{x?: integer, y?: integer, r: integer, g: integer, b: integer}` | With `font = "game"`: a copy of the text in this color, `x` and `y` pixels away (default 1 and 1), drawn under it. Since 2.5.0. |
| `space` *(optional)* | `integer` | With `font = "game"`: the game's fixed spacing in pixels, for Japanese letters (`SetFixedWidthSpacing`). Default -4. Since 2.5.0. |
| `spacing` *(optional)* | `number` | With `font = "game"`: the game's letter spacing for English letters, 0 to 4 (`SetSpacing`); the game's lists use 0.95. Default 1. Since 2.5.0. |

## Used by

[`rq.UiTheme`](rq.UiTheme.md), [`rq.hud.text`](../api/rq.hud.md#rqhudtext), [`rq.hud.text_width`](../api/rq.hud.md#rqhudtext_width)
