# rq.TryEquipCtx

`since 2.58.0`

What `rq.item.on_try_equip` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance the player puts on. |
| `no` | `integer` | The item number (`Ｉ固有番号`). |
| `id` *(optional)* | `string` | A mod item's text id, as `rq.item.define` named it; nil for a game item. |
| `iic` | `integer` | The character's roster slot. |
| `chara` | `integer` | The character number (`Ｃ番号`). |
| `slot` | `"special"\|"weapon"\|"armor"\|"item"` | The slot. |
| `kind` | `integer` | The slot as the game numbers it: 21 special, 1 weapon, 11 armor, 17 item. |
| `old` | `integer` | The instance the slot holds now, 0 for none. |
| `from` | `"vault"\|"storage"\|"shop"\|"status"` | Where the player does it: a drag from the vault, from the storage screen or from the shop's rack onto a character's row, or a pick in the status page's item list. |

## Used by

[`rq.item.on_try_equip`](../api/rq.item.md#rqitemon_try_equip)
