# rq.RewardCtx

What `rq.battle.on_reward` callbacks get. Fields marked writable change what the game gives.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `result` | `integer` | The game's result code, as in `rq.battle.on_end`: 1 for a fight won, 4 for one the enemies ran from (the two that pay; `rq.battle.start` returns "other" for 4). |
| `group` | `integer` | The fight group (`◆戦闘グループ`). |
| `rank` | `integer` | The fight rank (`◆戦闘ランク`): 1 an enemy standing on the map, 2 a boss. |
| `kills` | `integer` | The enemies defeated, as the result screen counts them. |
| `bags` | `integer` | The gold bags picked up, 0 to 5. |
| `enemies` | `integer[]` | The enemies' slots. |
| `gold` | `integer` | Writable. The gold, after all of the game's rules. A number, rounded down, kept from 0; the result screen shows it and it is paid as the screen closes. |
| `base` | `integer` | The fight's base EXP, the result screen's top number. |
| `exp` | `integer` | Writable. The fight's EXP after the fight's bonuses (enemies defeated, the quest's EXP bonus, a small party), the result screen's second number. Writing it scales every ally's `exp` by the same ratio at once, so the next callback reads the new numbers. |
| `allies` | [`rq.RewardAlly`](rq.RewardAlly.md) `[]` | The party, in the result screen's order. Change the entries' `exp`, not the list. |
| `reserve` | `integer` | Writable. What each reserve character gets. Until a callback writes it, it reads the game's rule from the allies as they stand: the smallest `exp` that is not 0, divided by 20. |

## Used by

[`rq.battle.on_reward`](../api/rq.battle.md#rqbattleon_reward)
