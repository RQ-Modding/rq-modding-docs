# rq.MapCtx

What `rq.dungeon.on_map` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest being entered (its `Ｑ` index). |
| `cleared` | `boolean` | The quest was cleared before. |
| `map` | `integer` | The map layout number (`◆ＭＡＰ番号`), the same as `rq.DungeonInfo.roomId`. |
| `party` | `integer[]` | The party's roster slots. |
| `area` | `integer` | The area, 1 to 16: a cell of the quest's 4 by 4 area map. 0 outside a quest. Since 2.24.0. |
| `row` | `integer` | The area's row on the area map, 1 to 4 from the top; 0 with no area. Since 2.24.0. |
| `col` | `integer` | The area's column on the area map, 1 to 4 from the left; 0 with no area. Since 2.24.0. |
| `name` | `string` | The area's name, as the map screen shows it; "" when the game gives none (all of the Malgrid Dungeon's areas). Since 2.24.0. |
| `kind` | `integer` | The map kind (`◆ＭＡＰ基礎型`), as in `rq.ids.map_kind`. Since 2.24.0. |
| `first` | `boolean` | The party had not been in this area yet in this run of the quest. Since 2.24.0. |
| `stratum` | `integer\|nil` | The Malgrid Dungeon's stratum: 1 to 10 on its quests, the Xth Stratum's own count on quest 147; nil on any other quest. Since 2.24.0. |

## Used by

[`rq.dungeon.on_map`](../api/rq.dungeon.md#rqdungeonon_map)
