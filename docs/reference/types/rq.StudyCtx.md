# rq.StudyCtx

`since 2.46.0`

What `rq.battle.on_study` gets for one Study that fired.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | Athena 2.0's roster slot. |
| `ally` | `integer` | The roster slot of the ally she studied: the one diagonally in front of her. |
| `stat` | `"attack"\|"accuracy"\|"speed"\|"hp"\|"critical"` | The stat the Study raises. |
| `skill` | `integer` | The Study's skill number, 336 to 340 in the order of `stat`'s names. |
| `base` | `integer` | The game's gain: 3 attack, 2 accuracy, 1 speed, 5 HP, 1 critical. |
| `gain` | `integer` | The gain the stat gets: the game's, then what the callback before left. |

## Used by

[`rq.battle.on_study`](../api/rq.battle.md#rqbattleon_study)
