# rq.StatusDef

`since 2.2.0`

What `rq.status.define` takes.

The callbacks get the instance `s` first. Their errors are logged with the mod and the id, and the
next callback still runs.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The name, for logs and other mods. Default the id. |
| `kind` *(optional)* | `"bad"\|"good"` | Bad states are cured by the game's cure skills, good ones taken by its dispels (see `cured_by`). Default "bad". |
| `turns` *(optional)* | `integer` | How many of the bearer's turns it lasts, 1 or more; `add` can give another. nil lasts the whole fight. |
| `stack` *(optional)* | `"refresh"\|"add"\|"keep"\|integer` | What adding it again does: "refresh" sets the new turns, "add" adds them, "keep" changes nothing, a number is the most stacks (the turns are set again). Default "refresh". |
| `cured_by` *(optional)* | `(string\|integer)[]` | What of the game takes it: "all" (Status Restore, Encourage, Self-Healing, skill 475, Am Powder), "poison" (First Aid), "dispel" (what takes the game's ▲), or support skill numbers; see `rq.status`. Default `{ "all" }` for a bad state, `{ "dispel" }` for a good one (since 2.26.0; `{}` before). `{}` keeps it from the game. |
| `tags` *(optional)* | `string[]` | Names for families of states, for `rq.status.cure(iic, { tag = ... })`. |
| `keep_on_down` *(optional)* | `boolean` | Stays when the bearer goes down, until the fight ends. Default false. |
| `lethal` *(optional)* | `boolean` | Its `on_turn` damage may bring the HP to 0 and down the bearer, with `source` as the killer; `ctx:damage(n, { lethal = false })` still stops at 1. Default false, as poison. Since 2.3.0. |
| `persevere` *(optional)* | `boolean` | With `lethal`, whether Persevere (skill 481, or 247 half the time once a fight) leaves the bearer 1 HP, as it does from a hit. Default true. Since 2.26.0. |
| `lasts` *(optional)* | `"fight"\|"quest"` | How long it can stay. "fight": until the fight ends. "quest": on an ally, from fight to fight until the quest ends, however it ends (reason "quest_end"); it can be added outside a fight during a quest and shows on the card when the next fight starts, and its turns count only in fights. On an enemy a "quest" state still ends with the fight. Default "fight". Since 2.26.0. |
| `immune` *(optional)* | [`rq.StatusImmune`](rq.StatusImmune.md) | Who cannot take it. Since 2.26.0. |
| `desc` *(optional)* | `string` | A few lines for players about what it does, given by `rq.status.info`. Since 2.26.0. |
| `icon` *(optional)* | [`rq.BuffDef`](rq.BuffDef.md) | The buff on the card; its `text` is set by `rq.status`. |
| `text` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `): string` | The icon's text, at most 15 bytes. Default the turns left, else the stacks when more than 1. |
| `on_turn` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `, ctx:` [`rq.BattleTurnCtx`](rq.BattleTurnCtx.md) `)` | Runs at each of the bearer's turn starts, as `rq.battle.on_turn`: damage, heal, skip, log. |
| `on_add` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `)` | Runs when it is put on someone who did not have it. |
| `on_remove` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `, reason: "expired"\|"cured"\|"down"\|"removed"\|"fight_end"\|"quest_end")` | Runs when it goes. |
| `physical` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `, side: "attacker"\|"defender", ctx:` [`rq.PhysicalCtx`](rq.PhysicalCtx.md) `): integer\|nil,` | integer\|nil For a physical hit by or on the bearer: returns as `rq.combat.on_physical`, an attack and a percent of the final damage. |
| `magic` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `, side: "attacker"\|"defender", ctx:` [`rq.MagicCtx`](rq.MagicCtx.md) `): integer\|nil` | For a spell by or on the bearer: a percent of its damage, as `rq.combat.on_magic`. |
| `accuracy` *(optional)* | `fun(s:` [`rq.StatusInstance`](rq.StatusInstance.md) `, side: "attacker"\|"defender", ctx:` [`rq.AccuracyCtx`](rq.AccuracyCtx.md) `): integer\|nil` | For an accuracy check by or on the bearer: points added to the hit chance, as `rq.combat.on_accuracy`. |

## Used by

[`rq.status.define`](../api/rq.status.md#rqstatusdefine)
