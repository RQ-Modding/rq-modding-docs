# rq.CharaEdit

A patch for `rq.chara.edit`. `level`, `level_max`, `skills` and `lines` do not apply.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `learn` *(optional)* | [`rq.CharaSkillGrant`](rq.CharaSkillGrant.md) `[]` | Makes sure the character has these skills: raises a rank, never lowers it, and does not stack the uses of a use skill twice. A skill it adds or raises is marked as given in the purchase record (cost -1) when the row had no record (since 2.45.0). |
| `on_recalc` *(optional)* | `fun(iic: integer): boolean\|nil` | Runs after each recalculation of this character; return true to ask for one more. |

## Used by

[`rq.chara.edit`](../api/rq.chara.md#rqcharaedit)
