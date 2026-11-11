# rq.LevelUpCtx

What `rq.chara.on_level_up` callbacks get.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `level` | `integer` | The new level. |
| `from` | `integer` | The level before. |
| `free` | `boolean` | true for a level from the game's other level-up, which sets the EXP back to 0 (the story, training, the reserve's share of a fight, `rq.chara.level_up`); false for one that keeps the EXP left over (the party in a fight's result, `rq.chara.add_exp`). |
| `battle` | `boolean` | true inside a fight's result, for the party and the reserve alike. |

## Used by

[`rq.chara.on_level_up`](../api/rq.chara.md#rqcharaon_level_up)
