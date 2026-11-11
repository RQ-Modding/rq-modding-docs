# rq.FightOpts

What `rq.battle.start` takes. Only `enemies` is needed.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `enemies` | `integer[]` | Up to five monster numbers (`rq.ids.monster`) in rank order, 0 for an empty rank. |
| `exp` *(optional)* | `integer` | Experience for the win. Default 0. |
| `boss` *(optional)* | `boolean` | The game's boss fight: fight rank 2, no escape, 999 actions, no ambush, no capture, the fight lost when no ally can act, the boss music (53, or the boss's own) and the `boss` moment of `rq.music.on_play`. Since 2.36.0. |
| `strong` *(optional)* | `boolean` | Needs `boss`. The game's stronger boss (`◆敵強化率` 130): a "+" on the name and ×1.3 in world 1; HP ×2 and ×1.3 in worlds 2 and 3. Since 2.36.0. |
| `double_hp` *(optional)* | `boolean` | Needs `boss`. Each enemy's HP twice (four times in world 3), after `rq.monster.on_create`. With `strong`, both apply. Since 2.36.0. |
| `names` *(optional)* | `table<integer, string>` | A name per rank, 1 to 5, shown in the fight in place of the monster's; `""` keeps the monster's. Since 2.36.0. |
| `background` *(optional)* | `integer\|string` | A background for this fight: a number or a name from `rq.battle.backgrounds`. The map's own is put back after. Since 2.36.0. |
| `music` *(optional)* | `integer\|string` | The fight's music: a game track (`rq.ids.music`) or a file in the calling mod's folder. It plays over the game's choice and over `rq.music.on_play`'s callbacks, which still see the game's track. Since 2.36.0. |
| `escape` *(optional)* | `integer` | The escape chance, 0 to 100, in a boss fight too. It is written after the game's own and before every `rq.battle.on_start` callback. Since 2.36.0. |
| `gold` *(optional)* | `integer` | The gold the fight pays, 0 or more: `rq.battle.on_reward`'s `ctx.gold` before the mods' callbacks, which may still change it. Default: the game's. Since 2.36.0. |

## Used by

[`rq.battle.start`](../api/rq.battle.md#rqbattlestart)
