# rq.QuestMapShape

The shape of a mod's quest's map, in `rq.QuestData.map`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `start` | `integer` | The area the party enters first. |
| `tileset` *(optional)* | `integer` | The map's tileset (`rq.ids.map_kind`); nil when each area gives its own. |
| `areas` | `table<integer, {exits: string, room?: integer, fixed?: integer, tileset: integer}>` | The areas by number, 1 to 16: the exits as letters in the order N, S, E, W; the stock room or the fixed map asked for (both nil for the game's draw); the area's tileset. |

## Used by

[`rq.QuestData`](rq.QuestData.md)
