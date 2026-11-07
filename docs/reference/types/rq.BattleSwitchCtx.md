# rq.BattleSwitchCtx

What `rq.battle.on_switch` gets for one rank.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `left` | `integer` | The roster slot of who stood on the rank; 0 for nobody. |
| `came_in` | `integer` | The roster slot of who stands there now; 0 for nobody. |
| `rank` | `integer` | The ally rank, 1 to 5. |

## Used by

[`rq.battle.on_switch`](../api/rq.battle.md#rqbattleon_switch)
