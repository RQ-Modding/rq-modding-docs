# rq.SkillLevel

A skill and its level, as `rq.chara.base_skills` lists them and `edit`'s `learn` takes them.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The skill number. |
| `n` | `integer` | Most uses for a use skill (type 10), rank 1 to 4 for a ranked one (20, 30), 1 for the rest. |

## Used by

[`rq.LearnableRow`](rq.LearnableRow.md), [`rq.chara.base_skills`](../api/rq.chara.md#rqcharabase_skills)
