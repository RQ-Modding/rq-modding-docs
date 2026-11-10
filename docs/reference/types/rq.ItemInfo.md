# rq.ItemInfo

What `rq.item.info` returns: an item number's row data, as `rq.uikit.item_data` gives it for an
instance, without the fields that belong to one instance (`ii`, `locked`, `place`). The kit's item
lists take it as a row.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `no` | `integer` | The item number (`固有番号`). |
| `id` *(optional)* | `string` | The text id, for an item a mod defined. |
| `name` | `string` | The name. |
| `info` | `string` | The description. |
| `type` | `integer` | The slot, as the game numbers it (see `rq.ItemDef.type`). |
| `type_name` | `string` | The slot's name. |
| `subtype` | `integer` | The detailed kind. |
| `rank` | `integer` | The kind rank. |
| `icon` | `integer` | The icon CG. |
| `price` | `integer` | The price. |
| `level` | `integer` | The level needed to equip it. |
| `rarity` | `integer` | The rarity. |
| `place` | `integer` | 6 shop stock, 7 vault, 8 quest storage, 11 storage, or the owner's roster slot (20 and up) while equipped. |
| `locked` | `integer` | Non-zero when it cannot be taken off. |
| `vanishes` | `integer` | Non-zero when it vanishes. |
| `effects` | [`rq.ItemEffect`](rq.ItemEffect.md) `[]` | The effects. |
| `no` | `integer` | The item number. |
| `name` | `string` | Its name. |
| `level` | `string` | The level line, or "". |
| `info` | `string` | The stats line, with the game's marks. |
| `icon` | `integer` | Its icon CG. |
| `rank` | `integer` | Its rarity rank. |
| `kind` | `integer` | Its kind: 21 special, 1 weapon, 11 armor, 17 item. |
| `price` | `integer` | Its price. |
| `discard` | `boolean` | It can be thrown away. |
| `classes` | `integer[]` | The class numbers that may equip it. |

## Used by

[`rq.item.get`](../api/rq.item.md#rqitemget), [`rq.item.info`](../api/rq.item.md#rqiteminfo)
