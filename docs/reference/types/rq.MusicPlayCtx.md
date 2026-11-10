# rq.MusicPlayCtx

`since 2.4.0` `changed 2.27.0`

What `rq.music.on_play` gets: a track the game is about to play.

The moment (`kind`) is read from who called the game's music: its doors for fights, dungeons, the
town and the opening, and the function that asked for the track otherwise. The game's tracks for
each moment:

| `kind` | When | The game's tracks |
| --- | --- | --- |
| `"fight"` | An everyday fight starts | 51, 52, 55, 60 by the save's progress; 57 against Hannies |
| `"boss"` | A boss fight starts (`ボス戦闘処理`) | 53; 54, 58, 59 or 99 for some bosses |
| `"dungeon"` | A quest's map plays its track (`迷宮音楽_再生`) | 1 to 14 by the quest; 57 in quest 135 |
| `"town"` | The town, the shop, the Party and Quests screens (`システム曲_再生`) | 105 before Rance Castle opens, then 101, or 106 with the Magnum set |
| `"castle"` | Rance Castle | 89 |
| `"opening"` | The opening (`ＯＰ曲_再生`) | 103, or 107 with the Magnum set |
| `"result"` | The results screen after a quest | 102 |
| `"jingle"` | A girl monster joins | 108 |
| `"scene"` | A scene asks for it: the game's (`scene` names it) or a mod's (`rq.scene.play`) | Mostly 71 to 99; 201 to 213 for sounds |
| `"other"` | The extras, the system bar, a save's load, the title, a mod's `rq.music.play` | Any |

`boss`, `enemies`, `area`, `map_kind` and `world` are read when a callback reads them.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track the game asks for; `ctx:track` changes it for the callbacks after. |
| `playing` | `integer` | The track that plays now; 0 for none. |
| `kind` | `"fight"\|"boss"\|"dungeon"\|"town"\|"castle"\|"opening"\|"result"\|"jingle"\|"scene"\|"other"` | The moment, as in the table above. |
| `scene` *(optional)* | `string` | In a game scene, the game function of the scene that asks for the track, such as `"ランス／城汎用"`; nil in a mod's scene and at any other moment. Since 2.27.0. |
| `boss` *(optional)* | `integer` | In a boss fight, the boss's monster number (`rq.ids.monster`): the enemy in slot 2, else the first. Since 2.27.0. |
| `enemies` *(optional)* | `integer[]` | In a fight or a boss fight, the enemies' monster numbers, slot by slot. Since 2.27.0. |
| `area` *(optional)* | `integer` | On a quest's map, the area (1 to 16, as `rq.dungeon.info().area`). Since 2.27.0. |
| `map_kind` *(optional)* | `integer` | On a quest's map, the area's kind (`rq.ids.map_kind`). Since 2.27.0. |
| `world` *(optional)* | `integer` | The world, 1 to 3 (`rq.world.current()`). Since 2.27.0. |
| `quest` | `integer` | The quest in progress (`rq.quests.current()`); 0 for none. |
| `loops` | `integer` | 0 when it loops until changed, 1 when it plays once. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.MusicPlayCtx:file`](#rqmusicplayctxfile) | Plays a mod file for this track this time only. |
| [`rq.MusicPlayCtx:track`](#rqmusicplayctxtrack) | Plays another game track in place of this one. |

### rq.MusicPlayCtx:file

```lua
rq.MusicPlayCtx:file(path, opts)
```

`since 2.4.0`

Plays a mod file for this track this time only.

The path is in the mod folder of the mod whose callback calls it. The file is checked as in
`replace`. When the track already plays with another file, it starts again with this one.

Raises an error as `rq.music.replace` does.

```lua
rq.music.on_play(function(ctx)
  if ctx.kind == "dungeon" and ctx.quest == rq.ids.quest.MY_QUEST then
    ctx:file("music/my_dungeon.ogg")
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.MusicOpts`](rq.MusicOpts.md) | Loop points and volume; `name` is not used. |

### rq.MusicPlayCtx:track

```lua
rq.MusicPlayCtx:track(no)
```

`since 2.4.0`

Plays another game track in place of this one.

The game then counts that number as the one playing.

Raises an error for a number the game has not.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The game track to play. |

## Used by

[`rq.music.on_play`](../api/rq.music.md#rqmusicon_play)
