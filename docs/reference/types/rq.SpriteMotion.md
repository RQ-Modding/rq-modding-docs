# rq.SpriteMotion

`since 1.10.0`

The values `Sprite:to` moves to, and how.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` *(optional)* | `number` | Left edge to move to. |
| `y` *(optional)* | `number` | Top edge to move to. |
| `w` *(optional)* | `number` | Width to move to. |
| `h` *(optional)* | `number` | Height to move to. |
| `scale` *(optional)* | `number` | Scale to move to, both ways. |
| `scale_x` *(optional)* | `number` | Horizontal scale to move to. |
| `scale_y` *(optional)* | `number` | Vertical scale to move to. |
| `rotate` *(optional)* | `number` | Turn to move to, in degrees. |
| `alpha` *(optional)* | `integer` | Opacity to move to. |
| `tint` *(optional)* | `{r: integer, g: integer, b: integer}` | Tint to move to. |
| `add` *(optional)* | `{r: integer, g: integer, b: integer}` | Added color to move to. |
| `ms` *(optional)* | `number` | How long, in ms. Default 0, a jump. |
| `delay` *(optional)* | `number` | Ms before it starts. Default 0. |
| `ease` *(optional)* | `"linear"\|"in"\|"out"\|"in_out"` | "in" starts slow, "out" ends slow. Default "linear". |
| `on_end` *(optional)* | `fun(s:` [`rq.Sprite`](rq.Sprite.md) `)` | Runs once a frame has drawn the last values; it may call `to` again for the next step. |

## Used by

[`rq.Sprite:to`](rq.Sprite.md#rqspriteto)
