# rq.Item

An owned item instance, from `rq.items()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The instance (ii). |
| `name` | `string` | The name. |
| `type` | `string` | "weapon", "armor", "special" or "item". |
| `typeId` | `integer` | The game's item kind: 1 weapon, 11 armor, 21 special; other values are items. |
| `class` | `string` | The name of the first class that can equip it. |
| `classId` | `integer` | That class's number, 0 when none is set. |
| `level` | `integer` | The level needed to equip it. |
| `description` | `string` | The item's text. |
| `no` | `integer` | The item number (`固有番号`), as `rq.ids.item` names it. Since 2.23.0. |
| `place` | `integer` | Where it is (`存在`): 7 the vault, 11 the storage, 8 quest storage, or the owner's roster slot (20 and up) while worn. Since 2.23.0. |
| `lock` | `boolean` | Locked in the vault (`アイテム_ＬＯＣＫ中`): the vault's LOCK, which keeps it from SELL and DONATE. Not `rq.item.get`'s `locked` (cannot be taken off). Since 2.23.0. |

## Used by

[`rq.items.list`](../api/rq.items.md#rqitemslist), [`rq.uikit.item_filter`](../api/rq.uikit.md#rquikititem_filter), [`rq.uikit.item_sort`](../api/rq.uikit.md#rquikititem_sort)
