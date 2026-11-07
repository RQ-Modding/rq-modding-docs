# rq.BattleStartCtx

What `rq.battle.on_start` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `boss` | `boolean` | The fight is a boss fight. |
| `allies` | `integer[]` | The allies' roster slots. |
| `enemies` | `integer[]` | The enemies' slots, below 20. |
| `group` | `integer` | The fight group (`◆戦闘グループ`). Since 0.9.0. |
| `rank` | `integer` | The fight rank (`◆戦闘ランク`). Since 0.9.0. |

## Used by

[`rq.battle.on_start`](../api/rq.battle.md#rqbattleon_start)
