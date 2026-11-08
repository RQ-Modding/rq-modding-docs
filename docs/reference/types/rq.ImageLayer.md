# rq.ImageLayer

`since 1.8.0`

One layer of `rq.image.compose`: a part of a CG, a fill, or text.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `cg` *(optional)* | `integer` | A CG number; the CG being composed reads the game's own picture, so a page can be made from itself. |
| `src` *(optional)* | `integer[]` | `{x, y, w, h}` in the CG. Default: all of it. |
| `fill` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer, a?: integer}` | A color. |
| `text` *(optional)* | `string` | Text in the HUD font, placed in the box `w` by `h`. |
| `x` *(optional)* | `integer` | Left edge in the new CG. Default 0. |
| `y` *(optional)* | `integer` | Top edge in the new CG. Default 0. |
| `w` *(optional)* | `integer` | Width; a part is stretched to it. Default: the part's own (a fill: to the right edge). |
| `h` *(optional)* | `integer` | Height. Default: the part's own (a fill: to the bottom edge). |
| `alpha` *(optional)* | `integer` | Opacity, 0 to 255. Default 255. |
| `mode` *(optional)* | `"over"\|"copy"` | "copy" replaces what is under it, alpha and all. Default "over". |
| `size` *(optional)* | `number` | Text size. Default 16. |
| `color` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer}` | Text color. Default white. |
| `align` *(optional)* | `"start"\|"center"\|"end"` | Text placement in `w`. |
| `valign` *(optional)* | `"top"\|"center"\|"bottom"` | Text placement in `h`. |
| `edge` *(optional)* | `boolean` | false leaves out the text's dark edge. |
| `bold` *(optional)* | `boolean` | Bold text. |
| `font` *(optional)* | `"hud"\|"game"` | "game": the text in the game's own font, as `rq.hud.text` draws it; `face`, `outline`, `shadow`, `space` and `spacing` work as there, `color` gives the color. Since 2.5.0. |
| `face` *(optional)* | `256\|257\|258` | With `font = "game"`: the game's font number. Default 258. Since 2.5.0. |
| `outline` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer, w?: integer}` | With `font = "game"`: an outline. Since 2.5.0. |
| `shadow` *(optional)* | `integer[]\|{x?: integer, y?: integer, r: integer, g: integer, b: integer, a?: integer}` | With `font = "game"`: a shadow under the text, `a` its opacity (default 255). Since 2.5.0; `a` since 2.11.0. |
| `space` *(optional)* | `integer` | With `font = "game"`: the game's fixed spacing. Default -4. Since 2.5.0. |
| `spacing` *(optional)* | `number` | With `font = "game"`: the game's letter spacing. Default 1. Since 2.5.0. |

## Used by

[`rq.image.compose`](../api/rq.image.md#rqimagecompose), [`rq.uikit.layers`](../api/rq.uikit.md#rquikitlayers)
