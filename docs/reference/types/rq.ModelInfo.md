# rq.ModelInfo

A model in the game's model table, as `rq.monster.models` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `model` | `integer` | The model number, as `rq.Monster.model` holds it: 100000 + its place in the table. |
| `name` | `string` | The model's name in the table. |
| `poly` | `string` | The 3D file it draws. |
| `scale` | `number` | Its size. |
| `x` | `number` | Its offset across. |
| `y` | `number` | Its offset up. |
| `z` | `number` | Its offset in depth. |
| `motions` | `integer` | How many motions it has. |
| `id` *(optional)* | `string` | The text id, for a model a mod made (`rq.monster.model`). |

## Used by

[`rq.monster.models`](../api/rq.monster.md#rqmonstermodels)
