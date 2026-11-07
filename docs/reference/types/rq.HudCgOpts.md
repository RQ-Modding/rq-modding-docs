# rq.HudCgOpts

`since 1.6.0`

How `rq.hud.cg` draws a CG.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `src` *(optional)* | `integer[]\|{x: integer, y: integer, w: integer, h: integer}` | The part of the CG to draw, `{x, y, w, h}` in the CG's pixels; cut at the CG's edge. |
| `w` *(optional)* | `integer` | Stretch what is drawn to this width, in pixels. |
| `h` *(optional)* | `integer` | Stretch what is drawn to this height, in pixels. |
| `alpha` *(optional)* | `integer` | Opacity, 0 to 255. Default 255. |
| `tint` *(optional)* | `integer[]\|{r: integer, g: integer, b: integer}` | Multiplies the colors: `{128, 128, 128}` is half as bright. |

## Used by

[`rq.hud.cg`](../api/rq.hud.md#rqhudcg), [`rq.uikit.draw`](../api/rq.uikit.md#rquikitdraw)
