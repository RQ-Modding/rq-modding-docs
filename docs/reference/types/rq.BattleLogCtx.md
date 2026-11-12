# rq.BattleLogCtx

`since 2.37.0`

What `rq.battle.on_log` gets for one line of the battle log.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `text` | `string` | The line; after a callback that replaced it, the new text. |
| `color` | `integer` | The game's color number (5 for every line the game writes). |
| `last` | `boolean` | true for the fight's end message (Victory, Defeat, Time exceeded, the flight). |

## Used by

[`rq.battle.on_log`](../api/rq.battle.md#rqbattleon_log)
