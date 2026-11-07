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

## Used by

[`rq.image.compose`](../api/rq.image.md#rqimagecompose), [`rq.uikit.layers`](../api/rq.uikit.md#rquikitlayers)
