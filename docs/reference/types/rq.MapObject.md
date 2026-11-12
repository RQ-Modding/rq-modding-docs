# rq.MapObject

An object on the current map, from `rq.dungeon.objects()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `x` | `integer` | The cell, east, as in `rq.dungeon.grid`. |
| `z` | `integer` | The cell, north. |
| `kind` | `"chest"\|"red-chest"\|"warp"\|"achievement"\|"trap"\|"event"\|"spring"\|"escape"\|"enemy"\|"gold"\|"exp"\|"custom"\|"other"` | What it is. |
| `code` | `integer` | The game's object code (`maptt`). |
| `number` | `integer` | The game's number on it (`maptz`): a chest's fixed item (with `rq.loot.install` in place, as Loot Preview puts it, 10000 + the item instance rolled for the chest when it was placed), a map event's number, a warp's direction. |
| `rank` *(optional)* | `integer` | The game's third number (`maptv`): a chest's rank. nil on a `custom` object. |
| `id` *(optional)* | `string` | A `custom` object's id; nil when no loaded mod placed it or registered its id. |
| `look` *(optional)* | `string` | A `custom` object's look. |
| `keep` *(optional)* | `boolean` | A `custom` object comes back after each step. |

## Used by

[`rq.dungeon.objects`](../api/rq.dungeon.md#rqdungeonobjects)
