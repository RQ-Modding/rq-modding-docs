# rq.StunCtx

`since 2.37.0`

What `rq.combat.on_stun` gets where the game works out a stun.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `rate` | `integer` | The stun chance about to be rolled, 0 to 100: the game's, then what the callback before left. 0 when `blocked`. |
| `base` | `integer` | The chance of the game's formula (impact, the skill, hiding, a charging target, the target's resilience, at most 75, and its other rules), also where the game does not stun. |
| `blocked` *(optional)* | `"skill"\|"repeat"` | Why the game does not stun here: "skill" for the skills that never stun (120, Fortune 448, 152), "repeat" for a target stunned in the turn before. nil when the game rolls. |
| `forecast` | `boolean` | true when the game only works out the battle forecast: count nothing and roll no dice then. |

## Used by

[`rq.combat.on_stun`](../api/rq.combat.md#rqcombaton_stun)
