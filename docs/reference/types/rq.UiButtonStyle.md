# rq.UiButtonStyle

`since 2.6.0`

A button style of the hub theme: two states of a grey button and its text.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `normal` | [`rq.UiPiece`](rq.UiPiece.md) | The button. |
| `hover` | [`rq.UiPiece`](rq.UiPiece.md) | The button under the mouse. |
| `w` | `integer` | Its width, in pixels, when `opts.w` is not given. |
| `h` | `integer` | Its height, in pixels. |
| `text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | The text, usually with `font = "game"`. |
| `fit` *(optional)* | `number[]` | `{max size, min size, max spacing, min spacing}`: as the game's `FitText2`, a long text gets smaller, 2 pixels at a time, and tighter until it fits. |
| `pad` *(optional)* | `integer` | Pixels kept free at each side of the text. Default 4. |
| `hover_dy` *(optional)* | `integer` | The text moves down this much under the mouse, as on the footer's buttons. |
| `cover` *(optional)* | `boolean` | The pulsing cover over it under the mouse, as on rect buttons. |

## Used by

[`rq.UiTheme`](rq.UiTheme.md)
