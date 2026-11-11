# rq.FightResult

How a fight from `rq.battle.start` ended, its second value.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `code` | `integer` | The game's end (`rq.battle.on_end`'s `result`): 1 won, 2 lost, 3 a draw (the enemies gone with no ally standing), 4 the actions ran out and the enemies left, 5 the party fled (Escape), 6 fled by skill 217. |
| `how` | `"won"\|"lost"\|"draw"\|"time"\|"fled"\|"other"` | The end in a word. |
| `exp` | `integer` | The fight's EXP the result screen showed, after every `rq.battle.on_reward` callback; 0 when the fight paid nothing. |
| `gold` | `integer` | The gold paid, after every `rq.battle.on_reward` callback; 0 when the fight paid nothing. |
| `kills` | `integer` | The enemies defeated. |
| `fallen` | `integer[]` | The allies' roster slots at 0 HP at the end. |

## Used by

[`rq.battle.start`](../api/rq.battle.md#rqbattlestart)
