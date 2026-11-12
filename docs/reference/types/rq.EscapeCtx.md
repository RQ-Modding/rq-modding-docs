# rq.EscapeCtx

`since 2.37.0`

What `rq.combat.on_escape` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot of the ally who used the skill. |
| `skill` | `integer` | 211 for Escape, 217 for "Relax, relax". |
| `rate` | `integer` | The chance it works, 0 to 100: for Escape the fight's escape chance (`rq.battle.escape`), for 217 100 or 0; then what the callback before left. 0 when `blocked`. |
| `blocked` *(optional)* | `"enemy"\|"rank"\|"quest"` | Why the game says no: an enemy standing with skill 437 (Escape), fight rank 2 or the quest's rule (217). nil otherwise. |

## Used by

[`rq.combat.on_escape`](../api/rq.combat.md#rqcombaton_escape)
