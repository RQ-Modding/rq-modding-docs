# rq.UnequipCtx

`since 2.57.0`

What `rq.item.on_unequip` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance that came off. With `vanished`, the game has already deleted it; after a Morurun absorbs a Special item, it deletes it right after the callbacks. |
| `no` | `integer` | The item number (`Ｉ固有番号`), read before it came off. |
| `id` *(optional)* | `string` | A mod item's text id, as `rq.item.define` named it; nil for a game item. |
| `iic` | `integer` | The character's roster slot. |
| `chara` | `integer` | The character number (`Ｃ番号`). |
| `slot` | `"special"\|"weapon"\|"armor"\|"item"` | The slot. |
| `kind` | `integer` | The slot as the game numbers it: 21 special, 1 weapon, 11 armor, 17 item. |
| `equip` | `boolean` | true when it came off through the game's equip call (`キャラ_装備設定`: REMOVE, a drag, a swap, `rq.item.equip`, and `rq.item.remove`, `sell` and `donate` on a worn item); false when the game took it off itself (a character removed, a Morurun absorbing it, a quest's event). |
| `by` | `integer` | The instance put on in its place by the same equip call, 0 for none. |
| `vanished` | `boolean` | true when the game deleted it as it came off: an item that vanishes when taken off (Rocky Chunk, `vanishes` in `rq.item.define`), through the equip call. |

## Used by

[`rq.item.on_unequip`](../api/rq.item.md#rqitemon_unequip)
