# rq.BattleForecastCtx

`since 2.26.0`

What `rq.battle.on_forecast` gets for one forecast line.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The target's roster slot. |
| `skill` | `integer` | The skill number. |
| `text` | `string` | The game's line so far, such as "Battle Forecast:  Accuracy 85%  Stun 10%　△Medium damage"; "" for a skill the game makes no forecast for. |

## Used by

[`rq.battle.on_forecast`](../api/rq.battle.md#rqbattleon_forecast)
