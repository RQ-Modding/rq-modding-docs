# rq.ElementCtx

`since 2.46.0`

What `rq.combat.on_element` gets for one physical hit.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `element` | `integer` | The hit's element (`rq.ids.element`: 0 none, 1 light, 2 darkness, 3 electric, 4 ice, 5 fire): the game's, then what the callback before left. |
| `weapon` | `integer` | The element of the attacker's weapon; 0 for none. |
| `weakness` | `integer` | The defender's weak element; 0 for none. |
| `known` | `boolean` | The player knows the defender's weakness (`weakness_known`). |
| `guarded` | `boolean` | A guard took the hit (`FA[77]`); the game's arrows then do not take the weakness. |
| `basic` | `boolean` | The skill is a basic attack (`基本技` 1), as Ranged Attack and Melee Attack are. |
| `forecast` | `boolean` | true when the game only works out the battle forecast, not a real hit. |

## Used by

[`rq.combat.on_element`](../api/rq.combat.md#rqcombaton_element)
