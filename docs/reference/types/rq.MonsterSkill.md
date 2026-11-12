# rq.MonsterSkill

A skill in a monster's list (`rq.Monster.skills`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | Its position, 1 to 5. |
| `id` | `integer` | The skill number (`rq.skill.get`). |
| `text` | `string` | The text the fight shows when the monster uses it. |
| `motion` | `integer` | The motion it plays. |
| `chance` | `integer` | How often the monster chooses it, as the game weighs it: the draw (0 to 99) takes the first skill whose chance is at least the number, so 50 then 100 is half each; below 5 on an ability, its rank. |

## Used by

[`rq.Monster`](rq.Monster.md)
