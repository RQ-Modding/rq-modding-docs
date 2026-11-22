# rq.TextureColors

`since 2.64.0`

Colors by numbers on a texture, as `rq.image.texture` takes them. At least one field.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `hue` *(optional)* | `number` | Degrees added to each point's hue, -360 to 360. Default 0. |
| `saturation` *(optional)* | `number` | A factor on each point's saturation, 0 (grey) to 4. Default 1. |
| `lightness` *(optional)* | `number` | A factor on each point's lightness, 0 (black) to 4. Default 1. |

## Used by

[`rq.ModelDef`](rq.ModelDef.md), [`rq.ModelInfo`](rq.ModelInfo.md), [`rq.TextureInfo`](rq.TextureInfo.md), [`rq.image.texture`](../api/rq.image.md#rqimagetexture)
