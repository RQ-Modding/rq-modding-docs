# rq.SkillResetCtx

`since 2.46.0`

What `rq.chara.on_skill_reset` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `no` | `integer` | The character number (`Ｃ番号`). |
| `points` | `integer` | The free skill points after the reset: the game's own count (`rq.chara.skill_points_max`). |

## Used by

[`rq.chara.on_skill_reset`](../api/rq.chara.md#rqcharaon_skill_reset)
