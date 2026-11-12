# rq.BattleOrderAfterCtx

`since 2.37.0`

What `rq.battle.on_order_after` gets after the game built the turn list.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `rebuild` | `boolean` | false at the fight's start, true after a switch, a shuffle or a revive. |
| `units` | [`rq.OrderUnit`](rq.OrderUnit.md) `[]` | Every unit in the fight, with their own speeds. |
| `order` | `integer[]` | The list, up to 50 roster slots in the order they act; after `ctx:set_order`, the list set. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.BattleOrderAfterCtx:set_order`](#rqbattleorderafterctxset_order) | Replaces the turn list the game built. |

### rq.BattleOrderAfterCtx:set_order

```lua
rq.BattleOrderAfterCtx:set_order(list)
```

`since 2.37.0`

Replaces the turn list the game built.

The fight goes through the list from the first entry and starts again at the first after the
last. A unit that cannot act when its entry comes (down, stunned, an ally with no skill use left)
is passed over, as in the game's list. A unit left out never acts until the list is built again.
The turn icons show the new list.

Raises an error for a list that is empty or longer than 50, or an entry that is not a unit of the
fight.

| Parameter | Type | Description |
| --- | --- | --- |
| `list` | `integer[]` | Roster slots, 1 to 50 of them, from `ctx.units`. |

## Used by

[`rq.battle.on_order_after`](../api/rq.battle.md#rqbattleon_order_after)
