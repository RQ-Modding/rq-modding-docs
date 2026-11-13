# rq.CapCtx

`since 2.46.0`

What `rq.combat.on_cap` gets for one hit.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `magic` | `boolean` | true for a spell (action kind 2), false for a physical hit. |
| `base` | `integer` | The skill's own limit (`ダメージ上限`), in damage points; 0 for none. |
| `damage_max` | `integer` | The percent Damage Maximum (289) adds to it, by the attacker's rank in it; 0 without it or with no limit. |
| `limit` | `integer` | The limit the hit is held to, in damage points: `base` raised by `damage_max` as the game raises it, then what the callback before left. 0 for none. |
| `forecast` | `boolean` | true when the game only works out the battle forecast, not a real hit. |

## Used by

[`rq.combat.on_cap`](../api/rq.combat.md#rqcombaton_cap)
