# rq.MonsterSkill

A skill in a monster's list (`rq.Monster.skills`).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | Its position, 1 to 5. |
| `id` | `integer` | The skill number (`rq.skill.get`). |
| `text` | `string` | The text the fight shows when the monster uses it. |
| `motion` | `integer` | The motion it plays. |
| `chance` | `integer` | How often the monster chooses it, as the game weighs it. |

## Used by

[`rq.Monster`](rq.Monster.md)
