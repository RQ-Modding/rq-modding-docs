# rq.music

`since 2.4.0` `changed 2.27.0`

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
both. Each mod restores only its own; the one below it in load order then plays again.

**Moments.** `on_play`'s `ctx.kind` tells which moment asks for the track: an everyday fight, a
boss fight, a dungeon, the town, Rance Castle, the opening, the results screen, the jingle, a scene
(with the game's scene function in `ctx.scene`), or the rest. The rain, wind and other sounds of
the scenes are music tracks too (201 to 213), played from scenes: `replace` and `on_play` take
them. The game has a channel for looped ambient sounds (`ループ効果音`) but never starts one.

**The player's switches.** `rq.music.page` gives a pack a page in Config's Mods tab: a switch for
each track it replaced and each moment it names, a play button, all on and all off. A track switched
off plays the game's file (or the next mod's below in load order). `rq.music.enabled` reads a
moment's switch in `on_play`. A mod with its own page puts the same rows on it with
`rq.uikit.music_list`.

ctx's `scene`, `boss`, `enemies`, `area`, `map_kind` and `world`, volume up to 200, the player's
switches (`page`, `enabled`, `rq.uikit.music_list`), and `restore` bringing back the mod below.

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
| [`rq.music.page`](#rqmusicpage) | Gives the calling mod a page in Config's Mods tab to turn its music on and off. |
| [`rq.music.enabled`](#rqmusicenabled) | Returns whether the player left one of the calling mod's switches on. |

### rq.music.replace

```lua
rq.music.replace(no, path, opts) -> rq.MusicInfo
```

`since 2.4.0`

Plays a file wherever the game plays one of its tracks.

It starts the next time the game starts the track, or when a mod plays it (`rq.music.play`). A
replacement made while the track plays starts the next time the game asks for that track. When
the player switched the track off on the mod's page (`rq.music.page`), the file is checked and
kept, `info.off` is true, and the game's plays until it is switched on.

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

See also: [`rq.music.restore`](rq.music.md#rqmusicrestore), [`rq.music.page`](rq.music.md#rqmusicpage)

### rq.music.restore

```lua
rq.music.restore(no) -> boolean
```

`since 2.4.0` `changed 2.27.0`

Undoes the calling mod's `rq.music.replace` on a track.

It ends the next time the game starts the track. Another mod's replacement stays, and one made
earlier in load order plays again.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The track number. |

| Returns | Type | Description |
| --- | --- | --- |
| `restored` | `boolean` | false when the mod had not replaced it. |

> Changed in 2.27.0: The replacement of the mod below in load order comes back (it was the game's).

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

### rq.music.page

```lua
rq.music.page(opts) -> string
```

`since 2.27.0`

Gives the calling mod a page in Config's Mods tab to turn its music on and off.

The page lists each track the mod replaced (`rq.music.replace`), by number with the mod's name
for it and the game's, then each moment in `opts.moments`. Each row has a switch; a track's row
has a play button that plays the mod's file while the page shows (the music that played before
comes back when the page goes away). "All on" and "All off" turn every switch. The page shows 8
rows at a time, with arrows for more.

A track switched off plays the game's file (or the replacement of the mod below in load order),
at once when it plays now. A moment switched off changes nothing by itself: the mod's `on_play`
asks `rq.music.enabled(key)`. The switches are kept for every save profile.

Agents see the rows as `check-music-t<no>` and `check-music-m-<key>`, the buttons as
`button-music-play-<no>`, `button-music-all-on` and `button-music-all-off`.

Raises an error for an option of the wrong type, or a moment with no `key`.

```lua
rq.music.replace(rq.ids.music.BATTLE_2_R8, "music/battle.ogg", { name = "Battle (Remix)" })
rq.music.page({ moments = { { key = "boss", name = "Boss fights" } } })
rq.music.on_play(function(ctx)
  if ctx.kind == "boss" and rq.music.enabled("boss") then ctx:file("music/boss.ogg") end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` *(optional)* | [`rq.MusicPageOpts`](../types/rq.MusicPageOpts.md) | The title, the id and the moments. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string` | The page's id. |

See also: [`rq.uikit.music_list`](rq.uikit.md#rquikitmusic_list)

### rq.music.enabled

```lua
rq.music.enabled(key) -> boolean
```

`since 2.27.0`

Returns whether the player left one of the calling mod's switches on.

Every switch is on until the player turns it off on the mod's page (`rq.music.page` or
`rq.uikit.music_list`).

Raises an error for a key that is not a string or a whole number.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string\|integer` | A moment's key, or a track number. |

| Returns | Type | Description |
| --- | --- | --- |
| `on` | `boolean` | true when on. |

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
  if ctx.kind == "boss" and ctx.quest == 42 then
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
