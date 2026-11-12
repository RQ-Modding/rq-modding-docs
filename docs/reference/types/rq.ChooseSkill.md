# rq.ChooseSkill

`since 2.38.0`

A skill in `rq.ChooseCtx.skills`: one slot of the actor's list as it is now.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | Its position in the list, 1 to 20 (a monster's own skills first). |
| `id` | `integer` | The skill number (`rq.skill.get`). |
| `text` | `string` | The text the fight shows when the actor uses it. |
| `motion` | `integer` | The motion an enemy plays for it. |
| `chance` | `integer` | The game's draw threshold: the draw (0 to 99) takes the first slot whose chance is at least the number, so 50 then 100 is half each. 0 for a once-only skill already used; below 5 on an ability, its rank. |
| `added` | `boolean` | true for a skill a mod's `on_choose` put in the list in this fight. |

## Used by

[`rq.ChooseCtx`](rq.ChooseCtx.md)
