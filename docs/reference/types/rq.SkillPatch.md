# rq.SkillPatch

Fields for `rq.skill.patch`, named after the game's.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The name. |
| `flavor` *(optional)* | `string` | The battle-log verb. |
| `desc` *(optional)* | `string` | The hover text; `$` is a line break. |
| `ef` *(optional)* | `string` | The game's effect text. |
| `basic` *(optional)* | `integer` | `基本技`. |
| `big` *(optional)* | `integer` | `大技`. |
| `kinou` *(optional)* | `integer` | `機能`, the function code. |
| `kouka` *(optional)* | `integer` | `効果`, the effect code. |
| `kouka2` *(optional)* | `integer` | `効果２`. |
| `kouka3` *(optional)* | `integer` | `効果３`. |
| `kouka4` *(optional)* | `integer` | `効果４`. |
| `locked` *(optional)* | `integer` | `削除不可`: cannot be removed. |
| `type` *(optional)* | `integer` | `タイプ`: 10 active, 30 knowledge. |
| `action` *(optional)* | `integer` | `行動種類`, the action kind. |
| `panel` *(optional)* | `integer` | `パネル色`, the panel color. |
| `target` *(optional)* | `integer` | `対象`, the target code (`rq.ids.target`). |
| `bairitsu` *(optional)* | `integer` | `倍率`, the multiplier. |
| `cap` *(optional)* | `integer` | `ダメージ上限`, the damage cap. |
| `element` *(optional)* | `integer` | `属性`, the element (`rq.ids.element`). |
| `flat` *(optional)* | `integer` | `付与ダメージ`, added damage. |
| `no_first_turn` *(optional)* | `integer` | `初ターン使用禁止技`: not on the first turn. |
| `once_per_battle` *(optional)* | `integer` | `同一戦闘一度のみ技`: once per fight. |
| `needs_charge` *(optional)* | `integer` | `要溜め`: needs a charge. |
| `efa` *(optional)* | `integer` | `ＥＦＡ`. |
| `efb` *(optional)* | `integer` | `ＥＦＢ`. |
| `weapon` *(optional)* | `integer` | `発動条件／武器`, the weapon it needs. |

## Used by

[`rq.skill.patch`](../api/rq.skill.md#rqskillpatch)
