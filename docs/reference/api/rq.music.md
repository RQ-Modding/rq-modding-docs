# rq.music

`since 2.4.0`

Music from a mod's own file, in place of one of the game's tracks.

The game plays music by track number, and reads the number back: whether dungeon music plays,
what a save plays again on load, what the system bar goes back to. So a mod does not add new
numbers; it puts its file behind a game track's number (`replace`), everywhere the game plays
it, or for one time only (`on_play` with `ctx:file`). The game's own fades, crossfades and
Config's music volume apply to the file as to the game's tracks. `rq.ids.music` names the tracks.

**Files** can be OGG (Vorbis or Opus), FLAC, WAV or MP3, mono or stereo, at any sample rate.
They stream from the disk while they play. A file loops forever, as the game's tracks do, unless
the game plays the track once (`音楽１回再生`). It loops between its loop points: `loop_start` /
`loop_end` in seconds, else `LOOPSTART` with `LOOPLENGTH` or `LOOPEND` tags in the file (in
samples, as many music packs carry them), else the whole file.

**Two mods** that replace the same track: the later one in load order wins, and the log names
both. Each mod restores only its own.

The game's looped ambient sounds (rain, wind) are music tracks too: `replace` changes them, and
`on_play` does not see them.

```lua
-- A soundtrack pack: the everyday fight track and the indoor dungeon track.
rq.music.replace(rq.ids.music.BATTLE_2_R8, "music/battle.ogg", { name = "Battle (Remix)" })
rq.music.replace(rq.ids.music.INDOOR_CRAWL_R8, "music/indoor.ogg", { loop_start = 12.5 })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.music.replace`](#rqmusicreplace) | Plays a file wherever the game plays one of its tracks. |
| [`rq.music.restore`](#rqmusicrestore) | Undoes the calling mod's `rq.music.replace` on a track. |
| [`rq.music.info`](#rqmusicinfo) | Returns what is known of a track: its name, and the mod's file when one replaces it. |
| [`rq.music.current`](#rqmusiccurrent) | Returns the track that plays now. |
| [`rq.music.play`](#rqmusicplay) | Plays a game track, as the game does: with its crossfade, and a mod's file when one replaces it. |
| [`rq.music.stop`](#rqmusicstop) | Stops the music, with the game's fade. |

### rq.music.replace

```lua
rq.music.replace(no, path, opts) -> rq.MusicInfo
```

`since 2.4.0`

Plays a file wherever the game plays one of its tracks.

It starts the next time the game starts the track, or when a mod plays it (`rq.music.play`). A
replacement made while the track plays starts the next time the game asks for that track.

Raises an error for a number the game has not, a path out of the mod folder, a missing file, a
file that is not a sound with 1 or 2 channels, or an option of the wrong type or range. In
`init.lua` the game has not opened its music yet: the number is checked at the first frame, and a
wrong one is logged and dropped.

```lua
rq.music.replace(rq.ids.music.BATTLE_2_R8, "music/battle.ogg", { loop_start = 8.25, name = "Battle (Remix)" })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The game's track number. |
| `path` | `string` | A path inside the mod's folder. |
| `opts` *(optional)* | [`rq.MusicOpts`](../types/rq.MusicOpts.md) | Loop points, volume, name. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.MusicInfo`](../types/rq.MusicInfo.md) | What was set, with the loop points the file gave. |

See also: [`rq.music.restore`](rq.music.md#rqmusicrestore)

### rq.music.restore

```lua
rq.music.restore(no) -> boolean
```

`since 2.4.0`

Undoes the calling mod's `rq.music.replace` on a track.

It ends the next time the game starts the track. Another mod's replacement stays.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |

| Returns | Type | Description |
| --- | --- | --- |
| `restored` | `boolean` | false when the mod had not replaced it. |

### rq.music.info

```lua
rq.music.info(no) -> rq.MusicInfo
```

`since 2.4.0`

Returns what is known of a track: its name, and the mod's file when one replaces it.

A game track's length opens the track, so call it now and then, not every frame.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.MusicInfo`](../types/rq.MusicInfo.md) | The track. |

### rq.music.current

```lua
rq.music.current() -> rq.MusicNow|nil
```

`since 2.4.0`

Returns the track that plays now.

| Returns | Type | Description |
| --- | --- | --- |
| `now` | [`rq.MusicNow`](../types/rq.MusicNow.md) `\|nil` | The track, or nil when no music plays. |

### rq.music.play

```lua
rq.music.play(no, opts)
```

`since 2.4.0`

Plays a game track, as the game does: with its crossfade, and a mod's file when one replaces it.

When it already plays, nothing changes, unless `restart` is set or another file should play now.

Raises an error for a number the game has not.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |
| `opts` *(optional)* | `{restart?: boolean, once?: boolean}` | `restart`: from the start when it already plays. `once`: play it once, not in a loop. |

### rq.music.stop

```lua
rq.music.stop()
```

`since 2.4.0`

Stops the music, with the game's fade.

## Events

| Name | Summary |
| --- | --- |
| [`rq.music.on_play`](#rqmusicon_play) | Calls `fn` before the game starts a track. |

### rq.music.on_play

```lua
rq.music.on_play(fn) -> fun()
```

`since 2.4.0`

Calls `fn` before the game starts a track.

Each time the game changes the music (`SYS_PlayBGM`), with the track it asks for. `ctx:file`
plays a file of the mod's this time only, and `ctx:track` another game track. Callbacks run in
load order, and the last `ctx:file` wins. When the track already plays and nothing changes, the
game goes on with it. An error in a callback is logged and the next still runs.

```lua
-- Every boss fight of one quest gets the mod's theme.
rq.music.on_play(function(ctx)
  if ctx.kind == "fight" and ctx.no == rq.ids.music.BOSS_BATTLE_R8 and ctx.quest == 42 then
    ctx:file("music/boss42.ogg")
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.MusicPlayCtx`](../types/rq.MusicPlayCtx.md) `)` | Gets the track. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
