# rq.UiTabsStyle

`since 2.6.0`

A tabs style of the hub theme.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `normal` | [`rq.UiPiece`](rq.UiPiece.md) | A tab. |
| `current` | [`rq.UiPiece`](rq.UiPiece.md) | The current tab. |
| `w` | `integer` | Each tab's width, in pixels, when `opts.w` is not given. |
| `h` | `integer` | The height, in pixels. |
| `gap` | `integer` | Pixels between tabs. |
| `pad` | `integer` | Pixels kept free at each side of the text. |
| `cover` | `boolean` | The pulsing cover over a tab under the mouse. |
| `text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | The text. |
| `fit` *(optional)* | `number[]` | As in `rq.UiButtonStyle`. |

## Used by

[`rq.UiTheme`](rq.UiTheme.md)
