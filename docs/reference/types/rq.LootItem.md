# rq.LootItem

An item the player will find, from `rq.loot.list`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `integer` | The item instance. |
| `source` | `"magnum"\|"chest"` | Held by the Magnum, or locked in a chest on the map. |
| `seen` | `boolean` | The player knows the item: another instance with the same catalog number is identified. |
| `cg` | `integer` | The item's CG when seen, else the game's "?" CG. |
| `name` | `string` | The real name when seen, else "Unidentified item". |
| `comment` | `string` | The game's item text when seen, else a line saying it is not identified. |
| `overlay` | `integer` | 10403 when not seen, else 0. |
| `catalog` | `integer` | The catalog number. Do not show it for an item not seen. |
| `floor` | `integer` | The floor. |
| `x` | `integer` | The chest's cell. |
| `y` | `integer` | The chest's cell. |

## Used by

[`rq.loot.list`](../api/rq.loot.md#rqlootlist)
