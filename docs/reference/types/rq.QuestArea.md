# rq.QuestArea

An area of a mod's quest's map, in `rq.QuestMap.areas`.

The room's spots hold its objects: first the counted ones (`enemies`, `chests`, `traps`, `feats`),
each on a spot the game draws, then `objects`. A room the game draws has 17 spots and 1 wide spot at
least. The stock rooms: 1 has 17 spots, 2 has 20 and 2 wide spots, 101 has 19, 102 has 21, 201 to
204 and 302 have 20, 301 has 18, and 401 to 409 have 24 or 25; each other one wide spot.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `exits` *(optional)* | `string` | The exits, as letters among N, S, E and W, such as "ES". Default none. |
| `room` *(optional)* | `integer` | A stock room of the tileset: 1 and 2 (east-west corridors), 101 and 102 (north-south rooms), 201 to 204, 301 and 302, or 401 to 409 (the Malgrid tilesets only). Left out, the game draws one from the exits, as for its own quests. Every stock room has the cells of the four exits, so any exits fit any room. |
| `fixed` *(optional)* | `integer` | One of the game's fixed maps, by the number its quests load it with (11 to 328), in place of a stock room: its own look and layout. The area's exits must be among the fixed map's. Not with `room`. |
| `enemies` *(optional)* | `integer` | Placed enemies, 0 to 25, on spots the game draws: each a fight of the area's groups. |
| `chests` *(optional)* | `integer` | Chest draws, 0 to 25, as the game draws them for its own rooms: each one a red chest or nothing, half and half (one more draw with Tomato in the party; all green, and no traps, when Biscutta cleans the area). They hold the map's `loot`. For a set number of chests, use `objects`. |
| `traps` *(optional)* | `integer` | Traps, 0 to 25. |
| `feats` *(optional)* | `integer` | Adventure achievements, 0 to 25. |
| `objects` *(optional)* | [`rq.QuestObject`](rq.QuestObject.md) `[]` | Objects placed on the area's first entry in a run, after the counted ones. |
| `setup` *(optional)* | `fun(ctx:` [`rq.QuestAreaCtx`](rq.QuestAreaCtx.md) `)` | Runs at each entry, after the area is set up and before it shows: for what the fields do not say, such as `rq.dungeon.place` or `rq.encounters.set_steps`. |
| `tileset` *(optional)* | `integer` | The area's own tileset. |
| `name` *(optional)* | `string` | The area's own name. |
| `gold` *(optional)* | `integer` | The area's own gold. |
| `loot` *(optional)* | `"C"\|"B"\|"A"\|"C+"\|"B+"\|"A+"\|"A++"\|integer` | The area's own loot. |
| `music` *(optional)* | `integer` | The area's own music. |
| `background` *(optional)* | `integer` | The area's own fight background. |
| `groups` *(optional)* | `(integer\|string)[]` | The area's own groups. |

## Used by

[`rq.QuestMap`](rq.QuestMap.md)
