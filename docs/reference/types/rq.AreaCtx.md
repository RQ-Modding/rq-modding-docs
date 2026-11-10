# rq.AreaCtx

What `rq.dungeon.on_area` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `quest` | `integer` | The quest. |
| `cleared` | `boolean` | The quest was cleared before. |
| `party` | `integer[]` | The party's roster slots. |
| `area` | `integer` | The area, 1 to 16: a cell of the quest's 4 by 4 area map. |
| `row` | `integer` | The area's row on the area map, 1 to 4 from the top. |
| `col` | `integer` | The area's column on the area map, 1 to 4 from the left. |
| `name` | `string` | The area's name, as the map screen shows it; "" when the game gives none (all of the Malgrid Dungeon's areas). |
| `kind` | `integer` | The map kind (`◆ＭＡＰ基礎型`), as in `rq.ids.map_kind`. The kind belongs to the area: one quest can use several. |
| `map` | `integer` | The map layout number (`◆ＭＡＰ番号`). A random layout keeps its number for that quest and area. |
| `first` | `boolean` | The party had not been in this area yet in this run of the quest. |
| `stratum` | `integer\|nil` | The Malgrid Dungeon's stratum: 1 to 10 on its quests, the Xth Stratum's own count on quest 147; nil on any other quest. |

## Used by

[`rq.dungeon.on_area`](../api/rq.dungeon.md#rqdungeonon_area)
