# rq.BattleEndCtx

What `rq.battle.on_end` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `result` | `integer` | The game's result code. |
| `allies` | `integer[]` | The allies' roster slots. |
| `enemies` | `integer[]` | The enemies' slots. |
| `group` | `integer` | The fight group (`◆戦闘グループ`). Since 0.9.0. |
| `rank` | `integer` | The fight rank (`◆戦闘ランク`). Since 0.9.0. |

## Used by

[`rq.battle.on_end`](../api/rq.battle.md#rqbattleon_end)
