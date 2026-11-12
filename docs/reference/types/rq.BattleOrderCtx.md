# rq.BattleOrderCtx

`since 2.37.0`

What `rq.battle.on_order` gets before the game builds the turn list.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `rebuild` | `boolean` | false at the fight's start, true when the game builds the list again after a switch, a shuffle (skill 530) or a revive. |
| `units` | [`rq.OrderUnit`](rq.OrderUnit.md) `[]` | Every unit in the fight: the allies by rank, the enemies by rank, then the familiar. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.BattleOrderCtx:speed`](#rqbattleorderctxspeed) | Sets one unit's speed for this build of the turn list only. |

### rq.BattleOrderCtx:speed

```lua
rq.BattleOrderCtx:speed(iic, n)
```

`since 2.37.0`

Sets one unit's speed for this build of the turn list only.

The game reads it in place of the unit's own; the own speed comes back right after the build,
so the status screens and the next build show it. The game counts a speed of 0 as 1.

Raises an error for a unit not in the fight or a speed that is not whole, 0 to 9999.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The unit's roster slot, from `ctx.units`. |
| `n` | `integer` | The speed, 0 to 9999. |

## Used by

[`rq.battle.on_order`](../api/rq.battle.md#rqbattleon_order)
