# rq.DungeonInfo

Where the party is in a dungeon, from `rq.dungeon.info()`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `roomId` | `integer` | The map number. |
| `roomName` | `string` | The map's name. |
| `mapX` | `integer` | The player's cell, x. |
| `mapZ` | `integer` | The player's cell, z. |
| `cell` | `{x: integer, z: integer}` | The same cell as `mapX` and `mapZ`. |
| `party` | `{slot: integer, id: integer, name: string}[]` | The dungeon party: party slot (1 to 6), roster slot and name. |

## Used by

[`rq.dungeon.info`](../api/rq.dungeon.md#rqdungeoninfo)
