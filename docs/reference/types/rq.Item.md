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

## Used by

[`rq.items.list`](../api/rq.items.md#rqitemslist), [`rq.uikit.item_filter`](../api/rq.uikit.md#rquikititem_filter), [`rq.uikit.item_sort`](../api/rq.uikit.md#rquikititem_sort)
