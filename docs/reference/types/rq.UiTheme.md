# rq.UiTheme

`since 1.7.0`

A look for the kit: pieces, text styles, colors and sounds.

`rq.uikit.themes.config` is the look of the game's Config screen; it holds Config's pieces only.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `label` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | Label text. |
| `dim` | `{r: integer, g: integer, b: integer}` | The grey-green of Config's Low and High. |
| `page` | [`rq.UiPiece`](rq.UiPiece.md) | A Config page. |
| `block` | [`rq.UiPiece`](rq.UiPiece.md) | The 3D tab's dark block. |
| `button` | [`rq.UiPiece`](rq.UiPiece.md) | A button. |
| `button_text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | Button text. |
| `button_cover` | `{r: integer, g: integer, b: integer, a: integer}` | The cover that pulses over a hovered button. |
| `tab` | `{normal:` [`rq.UiPiece`](rq.UiPiece.md) `, hover:` [`rq.UiPiece`](rq.UiPiece.md) `, current:` [`rq.UiPiece`](rq.UiPiece.md) `}` | The tabs. |
| `tab_text` | `{normal:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `, hover:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `, current:` [`rq.HudTextStyle`](rq.HudTextStyle.md) `}` | Tab text. |
| `check_frame` | [`rq.UiPiece`](rq.UiPiece.md) | The checkbox frame. |
| `check_mark` | [`rq.UiPiece`](rq.UiPiece.md) | The checkmark. |
| `hover_bar` | [`rq.UiPiece`](rq.UiPiece.md) | The bar over a hovered row. |
| `track` | [`rq.UiPiece`](rq.UiPiece.md) | The slider track. |
| `knob` | [`rq.UiPiece`](rq.UiPiece.md) | The slider knob. |
| `knob_hot` | [`rq.UiPiece`](rq.UiPiece.md) | The knob while hovered or dragged. |
| `list_text` | [`rq.HudTextStyle`](rq.HudTextStyle.md) | List row text. |
| `list_current` | `{r: integer, g: integer, b: integer}` | The color of the chosen list row. |
| `scrollbar` | `{r: integer, g: integer, b: integer, a: integer}` | A list's scroll bar. |
| `sound` | `{hover?: integer, click?: integer, error?: integer}` | Sound numbers; nil plays none. |

## Used by

[`rq.uikit`](../api/rq.uikit.md), [`rq.uikit.copy_theme`](../api/rq.uikit.md#rquikitcopy_theme), [`rq.uikit.use`](../api/rq.uikit.md#rquikituse)
