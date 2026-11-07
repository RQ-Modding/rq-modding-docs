# rq.HpEvent

What `rq.battle.on_hp` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's slot. |
| `unit` | `integer` | The card: 1 to 5 allies, 11 to 15 enemies. |
| `side` | `"ally"\|"enemy"` | Whose card it is. |
| `hp` | `integer` | HP now. |
| `max` | `integer` | Most HP. |
| `before` | `integer` | HP when last seen; `hp` itself the first time. |
| `first` | `boolean` | The first sight of this character on this card (the start of a fight, a switch). |

## Used by

[`rq.battle.on_hp`](../api/rq.battle.md#rqbattleon_hp)
