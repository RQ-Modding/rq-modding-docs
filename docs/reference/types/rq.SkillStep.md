# rq.SkillStep

`since 2.48.0` `changed 2.66.0`

A step for `rq.chara.learnable`'s `after`: a skill set to a level.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. When the character holds a form of it and not the skill, the step sets that row; the recalculation then picks its form. |
| `n` | `integer` | The level to set, as `rq.SkillLevel.n`; 0 erases the skill (or the form's row). |

## Used by

[`rq.chara.learnable`](../api/rq.chara.md#rqcharalearnable)
