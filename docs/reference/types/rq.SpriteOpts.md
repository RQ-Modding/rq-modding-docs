# rq.SpriteOpts

`since 1.9.0`

Options for `rq.sprite.new` and `Sprite:set`.

`new` needs one of `gif`, `flash`, `cg`, `fill` or `text`; `set` changes only the options given. A
CG that `rq.image.replace` or `compose` changes is shown as it is now.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `gif` *(optional)* | `string` | A GIF file in the mod's folder, or an `rq.image.add_gif` key. It plays over and over from the start. Since 1.10.0. |
| `flash` *(optional)* | `string` | An `rq.image.add_flash` key, or a game Flash file's name as in `rq.image.add_gif`. It plays over and over from frame 1, at 30 frames a second, its actions and sounds as in the game; the stage is its size. Since 2.63.0. |
| `sound` *(optional)* | `boolean` | false keeps a Flash file's sounds quiet. Default true. Since 2.63.0. |
| `fps` *(optional)* | `number` | Frames a second for the GIF or the Flash file, 0 to 240; 0 (default) uses the GIF's own delays, and a Flash file's 30. Since 1.10.0; Flash since 2.63.0. |
| `clock` *(optional)* | `"game"\|"real"` | GIFs, Flash files and motion run on the game's clock, which follows `rq.speed` (default), or on real time. Since 1.10.0. |
| `cg` *(optional)* | `integer` | A CG number; `rq.image.add` gives one for a file in the mod. |
| `src` *(optional)* | `{x: integer, y: integer, w: integer, h: integer}\|false` | A part of the CG; false for the whole again. |
| `fill` *(optional)* | `{r: integer, g: integer, b: integer, a?: integer}` | A color; needs `w` and `h`. |
| `text` *(optional)* | `string` | Text in the HUD font. |
| `size` *(optional)* | `number` | Text size, 4 to 200. Default 16. |
| `color` *(optional)* | `{r: integer, g: integer, b: integer}` | Text color. Default white. |
| `edge` *(optional)* | `boolean` | The text's dark edge. Default true. |
| `bold` *(optional)* | `boolean` | Bold text. Default false. |
| `x` *(optional)* | `number` | Left edge before scale and turn, in game pixels. |
| `y` *(optional)* | `number` | Top edge before scale and turn, in game pixels. |
| `w` *(optional)* | `number` | Stretch to this width; 0 for its own. |
| `h` *(optional)* | `number` | Stretch to this height; 0 for its own. |
| `scale` *(optional)* | `number` | Sets both `scale_x` and `scale_y`. |
| `scale_x` *(optional)* | `number` | Horizontal scale, around `origin`. |
| `scale_y` *(optional)* | `number` | Vertical scale, around `origin`. |
| `rotate` *(optional)* | `number` | Degrees, clockwise on screen, around `origin`. |
| `origin` *(optional)* | `{x: number, y: number}\|"center"` | In the sprite's own pixels from its top left. Default `{0, 0}`. |
| `alpha` *(optional)* | `integer` | Opacity, 0 to 255. |
| `tint` *(optional)* | `{r: integer, g: integer, b: integer}` | Multiplies the colors. |
| `add` *(optional)* | `{r: integer, g: integer, b: integer}` | Added to the colors before the tint. |
| `blend` *(optional)* | `"normal"\|"add"` | "add" adds it to what is under it, for light and glow. Default "normal". |
| `show` *(optional)* | `boolean` | Shown. Default true. |
| `z` *(optional)* | `integer\|"back"\|"cards"\|"under_windows"\|"top"` | A number, or "back" (0, behind all of the game's), "cards" (300, over a fight's cards and the dungeon view, under the bottom bar), "under_windows" (1000, the default: under messages, menus, fades and Config) or "top" (20000, over all of the game's). |
| `keep` *(optional)* | `"screen"\|"removed"` | "screen" removes it when `rq.ui.get().screen` is no longer the one it was made on. Default "removed": it stays until the mod, a load or the title removes it. |
| `attach` *(optional)* | [`rq.SpriteAttach`](rq.SpriteAttach.md) `\|false` | Follows a target; `x`, `y` and `z` are added to its (z default 1). false lets it go. Since 1.11.0. |

## Used by

[`rq.Sprite:set`](rq.Sprite.md#rqspriteset), [`rq.sprite.new`](../api/rq.sprite.md#rqspritenew)
