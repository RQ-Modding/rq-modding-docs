# rq.LearnCtx

What `rq.chara.on_learn` gets for one purchase.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `slot` | `integer` | The skill-list row, 1 to 20. |
| `points` | `integer` | The skill points this step cost; 0 for `rq.chara.learn` with `pay = false`. |
| `cost` | `integer` | The row's purchase record after this step, as `rq.ForgetCtx.cost`. |
| `new` | `boolean` | true for a new skill, false for one more use or rank. |
| `n` | `integer` | The skill's level now: most uses for a use skill (type 10), rank for a ranked one (20, 30). |
| `by` | `"game"\|"learn"` | "game" for the skill window, "learn" for `rq.chara.learn`. |

## Used by

[`rq.chara.on_learn`](../api/rq.chara.md#rqcharaon_learn)
