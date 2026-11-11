# rq.RewardAlly

One ally in `rq.battle.on_reward`'s `ctx.allies`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The ally's roster slot. |
| `exp` | `integer` | What the ally gets, after its own items and skills. Write a number (rounded down, kept from 0); a fallen or capped ally keeps the game's 0 whatever is written. |
| `down` | `boolean` | The ally fell in the fight: the game gives none. |
| `capped` | `boolean` | The ally is at its level cap: the game gives none and shows "talent limit". |

## Used by

[`rq.RewardCtx`](rq.RewardCtx.md)
