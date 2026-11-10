# rq.DungeonInfo

Where the party is in a dungeon, from `rq.dungeon.info()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `roomId` | `integer` | The map layout number (`◆ＭＡＰ番号`). |
| `roomName` | `string` | The area's name, as the map screen shows it. |
| `quest` | `integer` | The quest; 0 outside one. Since 2.24.0. |
| `area` | `integer` | The area, 1 to 16: a cell of the quest's 4 by 4 area map. 0 outside a quest. Since 2.24.0. |
| `row` | `integer` | The area's row on the area map, 1 to 4 from the top; 0 with no area. Since 2.24.0. |
| `col` | `integer` | The area's column on the area map, 1 to 4 from the left; 0 with no area. Since 2.24.0. |
| `kind` | `integer` | The map kind (`◆ＭＡＰ基礎型`), as in `rq.ids.map_kind`; 0 outside a quest. Since 2.24.0. |
| `stratum` | `integer\|nil` | The Malgrid Dungeon's stratum: 1 to 10 on its quests, the Xth Stratum's own count on quest 147; nil on any other quest. Since 2.24.0. |
| `mapX` | `integer` | The player's cell, x. |
| `mapZ` | `integer` | The player's cell, z. |
| `cell` | `{x: integer, z: integer}` | The same cell as `mapX` and `mapZ`. |
| `party` | `{slot: integer, id: integer, name: string}[]` | The dungeon party: party slot (1 to 6), roster slot and name. |

## Used by

[`rq.dungeon.info`](../api/rq.dungeon.md#rqdungeoninfo)
