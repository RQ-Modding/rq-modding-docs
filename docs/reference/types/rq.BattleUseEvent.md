# rq.BattleUseEvent

What `rq.battle.on_use` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |
| `user` | `integer` | The roster slot of who uses it. |
| `unit` | `integer` | The user's battle number. |
| `target` | `integer` | The target's roster slot; 0 when there is none. |
| `target_unit` | `integer` | The target's battle number. |
| `side` | `"ally"\|"enemy"\|"summon"` | Whose skill it is. |
| `counter` | `boolean` | true when the skill runs as a counter. |

## Used by

[`rq.battle.on_use`](../api/rq.battle.md#rqbattleon_use)
