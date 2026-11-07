# rq.SkillInfo

What `rq.skill.get` returns.

It also holds every field `rq.SkillPatch` lists.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The skill number. |
| `name` | `string` | The name. |
| `kinou` | `integer` | The function code (`機能`). |
| `bairitsu` | `integer` | The multiplier (`倍率`). |
| `target` | `integer` | The target code (`対象`). |
| `koudou` | `integer` | The action kind (`行動種類`): 1 physical, 2 magic, 3 special, 4 support, 0 ability. |
| `kouka` | `integer` | The effect code (`効果`). |
| `desc1` | `string` | The raw description (`説明文１`); it may still hold `$`. |

## Used by

[`rq.skill.get`](../api/rq.skill.md#rqskillget)
