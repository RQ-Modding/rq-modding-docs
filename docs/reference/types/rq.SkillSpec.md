# rq.SkillSpec

A new skill for `rq.skill.define`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer\|string` | A number 1 to 1000, or a text id. |
| `kind` | `"physical"\|"knowledge"` | "physical": an active attack (type 10, action 1, panel 100). "knowledge": a passive (type 30, action 0, panel 105). |
| `name` *(optional)* | `string` | The name. |
| `flavor` *(optional)* | `string` | The battle-log verb (`Ｓ表示文`). |
| `desc` *(optional)* | `string` | The hover text; `$` is a line break. |
| `target` *(optional)* | `integer` | 1 melee (front row), 2 ranged, 3 all enemies, 4 needs two or more front-row enemies (`rq.ids.target`). |
| `bairitsu` *(optional)* | `integer` | The multiplier (`倍率`). |
| `flat` *(optional)* | `integer` | Added damage (`付与ダメージ`). |
| `kinou` *(optional)* | `integer` | The function code (`機能`). |
| `kouka` *(optional)* | `integer` | The effect code (`効果`). |
| `kouka2` *(optional)* | `integer` | The second effect code. |
| `kouka3` *(optional)* | `integer` | The third effect code. |
| `kouka4` *(optional)* | `integer` | The fourth effect code. |
| `cap` *(optional)* | `integer` | The damage cap (`ダメージ上限`); 0 for none. |
| `basic` *(optional)* | `integer` | The basic-skill flag (`基本技`). |
| `weapon` *(optional)* | `integer` | The weapon it needs (`発動条件／武器`). |
| `ef` *(optional)* | `string` | The game's effect text (`ＳＥＦ`). |

## Used by

[`rq.skill.define`](../api/rq.skill.md#rqskilldefine)
