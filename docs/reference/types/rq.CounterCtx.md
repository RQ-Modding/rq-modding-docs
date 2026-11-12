# rq.CounterCtx

`since 2.37.0`

What `rq.combat.on_counter` gets after a hit.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot: who the counter would hit. |
| `defender` | `integer` | The roster slot of the character that was hit: who would counter. |
| `skill` | `integer` | The skill of the hit. |
| `rate` | `integer` | The counter chance about to be rolled, 0 to 100: the game's, then what the callback before left. 0 without the Counter skill, or when `blocked`. |
| `base` | `integer` | The chance of the Counter skill (259) the defender learned, before the game's blocks; 0 without it. |
| `damage` | `integer` | The damage of the hit. |
| `guarded` | `boolean` | Ally Guard took the hit for the one it was aimed at (`FA[77]`). |
| `blocked` *(optional)* | `"familiar"\|"area"\|"stunned"\|"guard"` | Why the game does not counter: the familiar's attack, a skill on more than one target, a stunned defender, a hit Ally Guard took (unless `rq.counter.on_guard_counter` lets it through). nil otherwise. |
| `counter` | `boolean` | The hit is itself a counter. |

## Used by

[`rq.combat.on_counter`](../api/rq.combat.md#rqcombaton_counter)
