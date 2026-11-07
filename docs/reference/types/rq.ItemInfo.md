# rq.ItemInfo

What `rq.item.get` returns.

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
| `place` | `integer` | 6 shop stock, 7 vault, 8 quest storage, or the owner's roster slot while equipped. |
| `locked` | `integer` | Non-zero when it cannot be taken off. |
| `vanishes` | `integer` | Non-zero when it vanishes. |
| `effects` | [`rq.ItemEffect`](rq.ItemEffect.md) `[]` | The effects. |

## Used by

[`rq.item.get`](../api/rq.item.md#rqitemget)
