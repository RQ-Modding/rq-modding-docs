# rq.UiPiece

`since 1.7.0`

A part of a CG drawn at any size: the edges stay as they are, the middle stretches.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `cg` | `integer` | The CG number; one from `rq.image.add` works. |
| `src` *(optional)* | `integer[]` | `{x, y, w, h}` in the CG. Default: all of it. |
| `edge` *(optional)* | `integer[]` | `{left, top, right, bottom}`: the edges kept as they are, in pixels. |
| `mid` *(optional)* | `integer[]` | `{x, w}`: the middle columns, from `x` in `src`, such as one empty column between a frame and the text the game drew on it. Default: what the edges leave. |
| `vmid` *(optional)* | `integer[]` | `{y, h}`: the middle rows, from `y` in `src`. |
| `vfit` *(optional)* | `"crop"` | Takes the top rows of the middle instead of squashing them. |

## Used by

[`rq.UiButtonStyle`](rq.UiButtonStyle.md), [`rq.UiScrollPieces`](rq.UiScrollPieces.md), [`rq.UiTabsStyle`](rq.UiTabsStyle.md), [`rq.UiTheme`](rq.UiTheme.md), [`rq.uikit.draw`](../api/rq.uikit.md#rquikitdraw), [`rq.uikit.layers`](../api/rq.uikit.md#rquikitlayers)
