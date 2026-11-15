# rq.HasSkillCtx

`since 2.55.0`

What `rq.chara.on_has_skill` gets for one check.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `chara` | `integer` | The character number (`Ｃ番号`). |
| `skill` | `integer` | The skill asked for. |
| `mode` | `"held"\|"set"\|"unset"` | What the game asks: "held", whether the character has it; "set", whether it is in one of the action slots; "unset", whether it is held and not set. |
| `row` | `integer` | The game's answer: the skill row (1 and up) of the first copy that fits `mode`, 0 for none. |
| `caller` *(optional)* | `string` | The game function that asks, past the game's own helpers (`ＣＳ有無`, `ＣＳ有無／スタメン` and the like): `Ｃ再計算` for the stats, a scene's or a battle's function otherwise. |

## Used by

[`rq.chara.on_has_skill`](../api/rq.chara.md#rqcharaon_has_skill)
