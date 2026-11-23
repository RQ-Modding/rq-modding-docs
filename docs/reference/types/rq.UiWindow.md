# rq.UiWindow

`since 2.67.0`

What `rq.ui.window` returns.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `w` | `integer` | The window's inside width, in points (pixels on a monitor at 100%). |
| `h` | `integer` | The window's inside height, in points. |
| `pixels_w` | `integer` | Its width in pixels: `w` times the monitor's scale. |
| `pixels_h` | `integer` | Its height in pixels. |
| `view` | `{x: integer, y: integer, w: integer, h: integer}` | Where the game's picture is drawn, in the window's pixels: all of it, or between bars when the window's shape is not 4 by 3. |
| `scale` | `number` | The picture's enlargement: `view.w` over 1024. |
| `fullscreen` | `boolean` | The window fills the screen. |
| `sharp_3d` | `boolean` | The setting "3D at the window's size" is on (and works on this computer). |
| `sharp_3d_shown` | `boolean` | The last frame showed the 3D at the window's size. |
| `sharp_3d_w` *(optional)* | `integer` | The 3D's picture's width then, in pixels; nil when not shown. |
| `sharp_3d_h` *(optional)* | `integer` | Its height. |

## Used by

[`rq.ui.window`](../api/rq.ui.md#rquiwindow)
