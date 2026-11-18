# rq.CombatRules

`since 2.44.0`

What a skill can do in a fight, from `rq.combat.rules`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `crit` | `boolean\|"sometimes"` | Can it deal a critical hit: true where the game rolls the attacker's chance; "sometimes" where the game zeroes that chance (a multiplier over 150, or skill 120) but still adds to it in two cases: an attacker with Low Blow (549) against a man or race 4, on half the rolls, and an enemy while character 91 (Kojika) is in the party; false for a skill that is not a physical attack. |
| `stun` | `boolean\|"sometimes"` | Can it stun: true for a physical attack, function 59 and the skills that stun in their own code (149, 183, 422, 507); false for the skills the game never stuns with (120, Fortune 448, 152) and the rest. |
| `poison` | `"own"\|"coat"\|"sometimes"\|false` | Can it poison: "own" with a rate of its own (`poison_rate`), "coat" only through the attacker's weapon 118 or Poison Attack (264) on a physical attack, false never. |
| `poison_rate` *(optional)* | `integer` | The skill's own poison chance, 0 to 100, when it has one the loader knows (the game's table in `毒計算`, or a mod's rule). |
| `accuracy` | `"ignores"\|"rolls"` | "ignores" for function 56 or 79, which never miss; "rolls" for the rest. |
| `set_by` *(optional)* | `table<string, string>` | For each rule a mod set (`crit`, `stun`, `poison`), the mod's id. nil when no mod set one. |

## Used by

[`rq.combat.rules`](../api/rq.combat.md#rqcombatrules), [`rq.combat.set_rules`](../api/rq.combat.md#rqcombatset_rules)
