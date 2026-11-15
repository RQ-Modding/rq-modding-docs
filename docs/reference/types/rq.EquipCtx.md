# rq.EquipCtx

`since 2.55.0`

What `rq.item.on_equip` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance put on. |
| `no` | `integer` | The item number (`Ｉ固有番号`). |
| `id` *(optional)* | `string` | A mod item's text id, as `rq.item.define` named it; nil for a game item. |
| `iic` | `integer` | The character's roster slot. |
| `chara` | `integer` | The character number (`Ｃ番号`). |
| `slot` | `"special"\|"weapon"\|"armor"\|"item"` | The slot. |
| `kind` | `integer` | The slot as the game numbers it: 21 special, 1 weapon, 11 armor, 17 item. |
| `old` | `integer` | The instance the slot held before, 0 for none. One that vanishes when taken off is already deleted. |

## Used by

[`rq.item.on_equip`](../api/rq.item.md#rqitemon_equip)
