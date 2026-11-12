# rq.QuestMap

A mod's quest's map, in `rq.QuestDef.map`.

The areas are cells of the game's 4 by 4 grid: area 1 at the north-west, 4 at the north-east, 13
at the south-west, 16 at the south-east. An exit to the north leads to the area 4 below in number,
south 4 above, east 1 above, west 1 below. Each area is a room of the tileset: drawn by the game from
the area's exits (`room` left out), one of the tileset's stock rooms by number, or one of the game's
fixed maps. The settings from `tileset` to `groups` are the map's, and an area may give its own.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `tileset` *(optional)* | `integer` | The tileset, a map kind (`rq.ids.map_kind`): the rooms' look, the fight background and the map music. The game's stock rooms are in 13 of them: Cave 1, Forest 2, Building 3, Snow 4, Castle 5, Field 6, Mountain 7, Water Cave 9, Burning Forest 10, Waterside 13, Malgrid 14, Malgrid X 20 and Malgrid X Deep 21; the others serve an area on a fixed map. Needed here or in each area. |
| `name` *(optional)* | `string` | The name on the map panel, up to 40 characters (about 15 fit). Default "". |
| `gold` *(optional)* | `integer` | The gold of a fight: the base the game draws from, 0 to 999999. Default 50. |
| `loot` *(optional)* | `"C"\|"B"\|"A"\|"C+"\|"B+"\|"A+"\|"A++"\|integer` | What the chests hold: equipment of rank C, B or A; with `+` also an item bonus; `"A++"` rank A with a superior item; or one of the game's chest types (0, 11 to 14, 21 to 24, 31 to 34, 40). The appraisal fee per item follows: 100, 300, 600 or 800 gold. Default: by Rance's level (the game's 0, a fee of 99). |
| `music` *(optional)* | `integer` | The map's music, one of the game's map tracks (`◆マップ曲`). Default: the track the game's quests on that tileset use most. |
| `background` *(optional)* | `integer` | The fight background (`rq.battle.backgrounds`). Default: the tileset's. |
| `traps` *(optional)* | `{shroom?: integer, shock?: integer, alarm?: integer, pit?: integer}` | The weights, 0 to 10, of the kinds a trap draws (`rq.dungeon.set_traps`). Default all 0: every trap is a shock, as in the game. |
| `groups` *(optional)* | `(integer\|string)[]` | The enemy groups of the random fights and the placed enemies, 1 to 5: the game's numbers or a mod's group ids (`rq.monster.group`). Needed here or in each area. |
| `bonuses` *(optional)* | `{feats?: integer, enemies?: integer, level_ups?: integer}` | The quest bonuses' goals, 0 to 99 (0 or left out: no such bonus): the achievements found, the placed enemies beaten, the levels gained (`rq.QuestBonus`). |
| `start` *(optional)* | `integer` | The area the party enters first, at the room's start. Default: the lowest area. |
| `chatter` *(optional)* | `boolean` | false holds back the game's party lines after new areas (a member's remark, a special event). Default true: they come as in the game's quests, but never on the Building, Snow, Water Cave, Burning Forest, Tower and Waterside tilesets. |
| `areas` | `table<integer,` [`rq.QuestArea`](rq.QuestArea.md) `>` | The areas by number, 1 to 16. Each exit leads to an area of the map that has the way back, and every area can be reached from `start`. |

## Used by

[`rq.QuestDef`](rq.QuestDef.md)
