# rq.CanEquipCtx

`since 2.46.0`

What `rq.item.on_can_equip` gets for one item and one character.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance. |
| `no` | `integer` | The item number (`Ｉ固有番号`). |
| `iic` | `integer` | The character's roster slot. |
| `chara` | `integer` | The character number (`Ｃ番号`). |
| `allowed` | `boolean` | The answer so far: the game's, then what the callback before returned. |
| `reason` *(optional)* | `"level"\|"chara"\|"class"` | The first reason the game says no, in its order; nil when it says yes. "level": the character's level is below the item's. "chara": the item names the characters who may wear it, and not this one. "class": it names none, and the character's class may not wear it. |
| `reasons` | `("level"\|"chara"\|"class")[]` | Every reason the game says no, in its order: "level" first, then "chara" or "class". Empty when it says yes. |
| `level` | `integer` | The level the item needs (`Ｉ装備ＬＶ`); 0 for none. |
| `chara_level` | `integer` | The character's level. |

## Used by

[`rq.item.on_can_equip`](../api/rq.item.md#rqitemon_can_equip)
