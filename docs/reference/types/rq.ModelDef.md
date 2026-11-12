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

## Used by

[`rq.monster.model`](../api/rq.monster.md#rqmonstermodel)
