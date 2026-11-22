# rq.ModelDef

What `rq.monster.model` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The text id, such as "mymod:big_roach". |
| `base` | `integer` | The game model to draw (`rq.Monster.model`, from `rq.monster.models`). |
| `scale` *(optional)* | `number` | The size, above 0 and at most 50. Default: the base's. |
| `x` *(optional)* | `number` | The offset across. Default: the base's. |
| `y` *(optional)* | `number` | The offset up. Default: the base's. |
| `z` *(optional)* | `number` | The offset in depth. Default: the base's. |
| `textures` *(optional)* | `table<string, string\|string[]\|` [`rq.TextureColors`](rq.TextureColors.md) `>` | Textures of its own: a texture's name in the base's folder (as `rq.image.textures(base)` lists it) to a PNG inside the mod's folder, a list of PNGs for a texture with frames, or colors (as `rq.image.texture` takes them). The key "*" takes colors only, for every colour texture of the model; a name given beside it wins. |

## Used by

[`rq.monster.model`](../api/rq.monster.md#rqmonstermodel)
