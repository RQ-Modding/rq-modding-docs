# rq.OrderUnit

`since 2.37.0`

One unit of a fight, as `rq.battle.on_order` lists it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The unit's roster slot: an ally's, 1 to 5 for an enemy, 10 for the familiar. |
| `side` | `"ally"\|"enemy"\|"familiar"` | Its side. |
| `rank` | `integer` | Its rank, 1 to 5; 0 for the familiar. |
| `spd` | `integer` | The speed the game reads for the turn list (in `on_order`, after the earlier callbacks' `ctx:speed`). |
| `out` | `boolean` | true when the game gives it no turns now: down, or an ally with no skill use left. |
| `owner` *(optional)* | `integer` | The familiar's owner, an ally's roster slot. |
| `item` *(optional)* | `integer` | The familiar's item instance; nil when it cannot be found. |
| `own_spd` *(optional)* | `integer` | The familiar's speed as built, before the game holds it to the party's top speed. |

## Used by

[`rq.BattleOrderAfterCtx`](rq.BattleOrderAfterCtx.md), [`rq.BattleOrderCtx`](rq.BattleOrderCtx.md)
