# rq.CharaFields

The fields `rq.chara.define` and `rq.chara.edit` share.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | `string` | The full name. |
| `short` *(optional)* | `string` | The short name. |
| `face` *(optional)* | `integer\|string` | A game face CG number, or an image path inside the mod's folder (shown at 196×232, proportions kept). Default 2916. A GIF or an animated WebP moves wherever the game shows the face (2.25.0). |
| `face_name` *(optional)* | `string` | The face CG text (`顔ＣＧ文字列`). |
| `portrait` *(optional)* | `integer\|string` | A standing-picture CG number, or an image path inside the mod's folder (on a 1024×768 canvas, proportions kept). A GIF or an animated WebP moves in scenes (2.25.0). |
| `class` *(optional)* | `integer` | 1 Fighter, 2 Guard, 3 Gunner, 4 Sorcerer, 5 Healer, 6 Ranger, 7 Brawler, 8 Civilian. |
| `sex` *(optional)* | `integer` | The sex, as the game numbers it. |
| `level` *(optional)* | `integer` | The level. `define` only. |
| `level_max` *(optional)* | `integer` | The highest level. `define` only. |
| `slots` *(optional)* | `integer` | Skill rows the character can equip. The hotbar has 6 positions. |
| `type` *(optional)* | `integer` | The game's type value (`タイプ`, `rq.ids.chara_type`). Also `race`, `model`, `boss` and any other `rq.CharaState` name. |
| `init` *(optional)* | [`rq.CharaInit`](rq.CharaInit.md) | Bonuses each recalculation adds. |
| `skills` *(optional)* | [`rq.CharaSkillGrant`](rq.CharaSkillGrant.md) `[]` | Skills learned when the character is created. `define` only. |
| `weapon` *(optional)* | `integer\|string` | An item number or text id, created and equipped when the character is created, before `on_create`. An item of the wrong kind is logged and not given. Since 0.15.0. |
| `armor` *(optional)* | `integer\|string` | As `weapon`, for the armor. Since 0.15.0. |
| `item` *(optional)* | `integer\|string` | As `weapon`, for the held item. Since 0.15.0. |
| `special` *(optional)* | `integer\|string` | As `weapon`, for the option slot. Since 0.15.0. |
