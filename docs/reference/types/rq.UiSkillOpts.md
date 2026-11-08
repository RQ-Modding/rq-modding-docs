# rq.UiSkillOpts

`since 2.15.0`

What `rq.uikit.skill_button` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `rank` *(optional)* | `integer` | The skill's rank: a mark for each rank above 1, after the name. Default 1, or the character's with `chara`. |
| `chara` *(optional)* | `integer` | A character number: the rank, and for a skill that is an action its uses, are the character's (`キャラスキル_ランク`, `キャラスキル_使用回数`), as the status page shows them. |
| `long` *(optional)* | `boolean` | The long tile, 167 wide, of a red, blue or item skill (`延長スキルボタン_ＣＧ番号`). The game draws it 25 to the left of the normal tile's place. |
| `count` *(optional)* | `integer\|false` | The uses, in the level digits at the tile's x + 120, two digits padded with zeros, 99 at most. Default: the character's with `chara`. false: none. |
| `count_max` *(optional)* | `integer\|false` | On a long tile: the most uses, at x + 145. Default: the character's with `chara`. |
| `disabled` *(optional)* | `boolean` | Darkened as the game greys a skill: the tile and its uses at half, the name's color halved. It cannot be clicked; under the mouse it gets the game's red frame, and its tip still shows. |
| `slot` *(optional)* | `integer` | With `skill` nil: the empty slot, with this number on it. |

## Used by

[`rq.uikit.skill_button`](../api/rq.uikit.md#rquikitskill_button)
