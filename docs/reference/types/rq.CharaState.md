# rq.CharaState

Everything `rq.chara.get` returns about a character. `rq.chara.set` takes the same names.

Derived stats are rebuilt by each recalculation. `init_*` are the bonuses the recalculation adds;
for the game's own characters it writes them again first, so use `rq.chara.edit` to keep a change.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `id` *(optional)* | `string` | The text id, for a character a mod defined. |
| `name` | `string` | The full name. |
| `short` | `string` | The short name. |
| `face_name` | `string` | The face CG text. |
| `no` | `integer` | The character number. |
| `state` | `integer` | Where the character is (`登録状態`): 1 party, 2 reserve, 4 second string. |
| `guest` | `integer` | Non-zero for a guest. |
| `locked` | `integer` | Non-zero when the character cannot be removed. |
| `face` | `integer` | The face CG number. |
| `portrait` | `integer` | The standing-picture CG number. |
| `class` | `integer` | The class (see `rq.CharaFields.class`). |
| `sex` | `integer` | The sex. |
| `level` | `integer` | The level. |
| `level_max` | `integer` | The highest level, the talent limit (`ＣＬＶ最大`). It is kept in the save, and items and events raise it; `rq.chara.set(iic, { level_max = n })` changes it for good. The game ignores it for a character with `uncapped`. |
| `uncapped` | `boolean` | The game sets no level cap for this character (Rance, Reset Kalar and Dark Rance). Since 2.33.0. |
| `exp` | `integer` | Experience. |
| `exp_max` | `integer` | Experience for the next level. The game's recalculation sets it from the level; below the highest level the character has reached, it is at most 4980, so lost levels come back quickly. |
| `rebirths` | `integer` | Times reborn. |
| `hp` | `integer` | HP. |
| `hp_max` | `integer` | Most HP. |
| `spd` | `integer` | Speed. |
| `atk` | `integer` | Attack. |
| `def` | `integer` | Defense. |
| `hit` | `integer` | Accuracy. |
| `eva` | `integer` | Evasion. |
| `crit` | `integer` | Critical rate. |
| `impact` | `integer` | Impact rate. |
| `resist` | `integer` | Resistance. |
| `mag` | `integer` | Magic. |
| `mdef` | `integer` | Magic defense. |
| `fire_res` | `integer` | Fire resistance. |
| `ice_res` | `integer` | Ice resistance. |
| `thunder_res` | `integer` | Thunder resistance. |
| `light_res` | `integer` | Light resistance. |
| `dark_res` | `integer` | Dark resistance. |
| `weak_element` | `integer` | The weak element (`rq.ids.element`). |
| `weapon` | `integer` | The equipped weapon's item instance. |
| `armor` | `integer` | The equipped armor's item instance. |
| `item` | `integer` | The held item's instance. |
| `special` | `integer` | The option slot's item instance. |
| `skill_points` | `integer` | Free skill points. |
| `race` | `integer` | The race (`rq.ids.race`). |
| `type` | `integer` | The type value (`rq.ids.chara_type`). |
| `model` | `integer` | The 3D model. |
| `boss` | `integer` | Non-zero for a boss. |
| `weakness_known` | `boolean` | The player knows the weakness. |
| `status` | `integer` | Battle state: the status change, 1 poison, 0 none. Since 0.5.0. |
| `guard` | `integer` | Battle state: guard rate. Since 0.5.0. |
| `stealth` | `integer` | Battle state: stealth rate. Since 0.5.0. |
| `berserk` | `integer` | Battle state: berserk. Since 0.5.0. |
| `bless_all` | `integer` | Battle state: blessing on the whole party. Since 0.5.0. |
| `barrier` | `integer` | Battle state: barrier. Since 0.5.0. |
| `atk_buff` | `integer` | Battle state: attack buff. Since 0.5.0. |
| `def_buff` | `integer` | Battle state: defense buff. Since 0.5.0. |
| `charge` | `integer` | Battle state: charge. Since 0.5.0. |
| `init_hp` | `integer` | Bonus to most HP, in percent. |
| `init_spd` | `integer` | Bonus to speed, in points. |
| `init_atk` | `integer` | Bonus to attack, in percent. |
| `init_def` | `integer` | Bonus to defense, in percent. |
| `init_hit` | `integer` | Bonus to accuracy, in points. |
| `init_eva` | `integer` | Bonus to evasion, in points. |
| `init_crit` | `integer` | Bonus to critical rate, in points. |
| `init_impact` | `integer` | Bonus to impact rate, in points. |
| `init_resist` | `integer` | Bonus to resistance, in points. |
| `init_mag` | `integer` | Bonus to magic, in percent. |
| `init_mdef` | `integer` | Bonus to magic defense, in percent. |
| `init_sp` | `integer` | Starting skill points. |

## Used by

[`rq.chara.get`](../api/rq.chara.md#rqcharaget)
