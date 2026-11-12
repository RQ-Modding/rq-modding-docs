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
| `ambush` | `"none"\|"surprise"\|"first_strike"\|"ambushed"` | The ambush the game decided: none, the party's surprise attack, a first strike, or the enemies' ambush. Change it with `rq.battle.set_ambush`. Since 2.37.0. |
| `first_striker` *(optional)* | `integer` | With "first_strike", the ally the game's notice names. Since 2.37.0. |

## Used by

[`rq.battle.on_start`](../api/rq.battle.md#rqbattleon_start)
