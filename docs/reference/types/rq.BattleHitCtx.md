# rq.BattleHitCtx

`since 2.1.0`

What `rq.battle.on_hit` gets for one hit.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `attacker` | `integer` | The attacker's roster slot. |
| `defender` | `integer` | The defender's roster slot. |
| `skill` | `integer` | The skill number. |
| `kind` | `"physical"\|"magic"` | The kind of attack. |
| `damage` | `integer` | The HP the hit took; 0 for a miss, a barrier or an immune target. |
| `missed` | `boolean` | The hit missed (`◆攻撃外れた`). |
| `crit` | `boolean` | The hit was a critical. |
| `downed` | `boolean` | The defender is down after the hit. |
| `counter` | `boolean` | The hit is a counter. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.BattleHitCtx:log`](#rqbattlehitctxlog) | Adds text to this hit's battle log line, after the game's own (" X took 120 damage. (Stun)"). |

### rq.BattleHitCtx:log

```lua
rq.BattleHitCtx:log(text)
```

`since 2.1.0`

Adds text to this hit's battle log line, after the game's own (" X took 120 damage. (Stun)").

Start it with a space, as the game's suffixes do: `" (Burn)"`.

Raises an error for a value that is not a string.

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The text to add. |

## Used by

[`rq.battle.on_hit`](../api/rq.battle.md#rqbattleon_hit)
