# rq.MusicPlayCtx

`since 2.4.0`

What `rq.music.on_play` gets: a track the game is about to play.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track the game asks for; `ctx:track` changes it for the callbacks after. |
| `playing` | `integer` | The track that plays now; 0 for none. |
| `kind` | `"fight"\|"dungeon"\|"other"` | "fight": a fight's track (`音楽_戦闘`). "dungeon": a dungeon map's (`迷宮音楽_再生`). "other": the town, scenes, events, the rest. |
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
