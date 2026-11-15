# rq.ForgetCtx

What `rq.chara.on_forget` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `slot` | `integer` | The skill-list row. |
| `rank` | `integer` | The skill's rank. |
| `cost` | `integer` | The purchase record (since 2.45.0): the skill points paid for the row's bought steps, in the skill window or through `rq.chara.learn`; -1 for a skill a mod gave (`rq.chara.grant`, `edit`'s `learn`, `learn` with `pay = false`); 0 when nothing was recorded (a starting skill, or one bought before loader 2.45.0 and not upgraded since). Before 2.45.0 it was always 0. |
| `caller` | `string` | The AIN function that removed it, or "lua" for `rq.chara.forget`. |
| `kept` | `boolean` | Whether the skill is a Boost whose effect the character keeps without it (since 2.48.0), as `rq.BoostRow.kept`: erasing it loses nothing until the game's reset. false for every other skill. |
| `player` | `boolean` | Whether the player chose this erasure (since 2.51.0): the skill window's ERASE (`caller` "キャラスキル_消去"), or a mod's `rq.chara.forget` with `player = true`. false for the game's other removals (its recalculation, the story, the reset) and a plain `rq.chara.forget`. |
| `mod` *(optional)* | `string` | The id of the mod that called `rq.chara.forget` or `rq.chara.forget_points` (since 2.51.0), as `rq.mod.id` gives it; nil for the game's own removals. |
| `n` | `integer` | The skill's level in its row (since 2.52.0), as `rq.chara.slots`' `n`: most uses for a use-count skill, rank for a ranked one, 1 for the rest; in a preview, the level asked about. |
| `preview` | `boolean` | true when `rq.chara.forget_points` asks what the callback would give back (since 2.52.0): nothing is erased and the points are not given, so do nothing but count (no log, no state). false for an erasure. |

## Used by

[`rq.chara.on_forget`](../api/rq.chara.md#rqcharaon_forget)
