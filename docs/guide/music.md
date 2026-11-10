# Replacing music

`rq.music` (loader 2.4.0, moments and the Config page 2.27.0) plays a music file from your mod where the game plays one of its own
tracks. Use it for a soundtrack pack, a new theme for one fight, or music of your own for one
quest's dungeon.

## How the game picks music

The game plays music by **track number**. A fight plays its fight track, a dungeon its map's track,
the town and the scenes their own. The game also reads the number back. It checks it to know
whether dungeon music plays, saves it with the game, and plays it again on load.

So a mod does not add new tracks. It puts its file **behind a game track's number**. Everything
the game does with that number goes on as before: the crossfade between tracks, Config's music
volume, saves. Only the sound is yours.

## A soundtrack pack

Put the files in your mod folder and replace the tracks in `init.lua`:

```lua
rq.music.replace(rq.ids.music.BATTLE_2_R8, "music/battle.ogg", { name = "Battle (Remix)" })
rq.music.replace(rq.ids.music.INDOOR_CRAWL_R8, "music/indoor.ogg")
```

`rq.ids.music` names the tracks; the Music table under Game data lists them all, with their
numbers. `name` is what the extras' music room shows for the track.

The file plays from the next time the game starts the track. To hear it at once while you test:

```lua
rq.music.play(rq.ids.music.BATTLE_2_R8, { restart = true })
```

**Which track plays where?** Log each one the game asks for while you play, then look in
`logs\rqmod.log`:

```lua
rq.music.on_play(function(ctx)
  rq.log("music", ctx.no, rq.ids.name("music", ctx.no), ctx.kind)
end)
```

`rq.music.current()` gives the track that plays now, with the file when a mod's plays.

Everyday fights don't always use the same track: the game picks one by how far the story is (51,
52, 55 or 60, and 57 against Hannies). Boss fights have their own. A pack that wants every fight
replaces each of them.

## Files and loops

- **Formats:** OGG (Vorbis or Opus), FLAC, WAV or MP3, mono or stereo, any sample rate. Files
  stream from the disk, so a long track costs no memory.
- **Loops:** a track loops until the game changes it, as the game's own do. By default the whole
  file loops. Most music has an intro that should not repeat. Give the loop points in seconds:

  ```lua
  rq.music.replace(no, "music/town.ogg", { loop_start = 12.5, loop_end = 98.0 })
  ```

  Or leave them out and put `LOOPSTART` and `LOOPLENGTH` (or `LOOPEND`) tags in the OGG file, in
  samples. That is how many music packs made for other games already come, and RQ MOD reads them.
  `rq.music.info(no)` shows the loop points it found.
- **Volume:** the game's music volume and fades apply to your file. `volume` (0 to 200, default
  100) lowers a file that is louder than the game's tracks, or raises a quiet one (above 100 a
  loud file clips). Better still, make the file as loud as the game's music.

## Music for one quest, dungeon or fight

`rq.music.on_play` runs each time the game is about to change the music. `ctx:file` plays one of
your files this time only. `ctx:track` plays another game track instead.

```lua
local MY_QUEST = 42

rq.music.on_play(function(ctx)
  if ctx.quest ~= MY_QUEST then return end
  if ctx.kind == "dungeon" then
    ctx:file("music/my_dungeon.ogg")
  elseif ctx.kind == "boss" then
    ctx:file("music/my_boss.ogg", { loop_start = 4.0 })
  end
end)
```

`ctx.no` is the track the game asked for, `ctx.quest` the quest in progress, and `ctx.kind` the
moment:

| `kind` | When | The game's tracks |
| --- | --- | --- |
| `"fight"` | An everyday fight | 51, 52, 55, 60 by the save's progress; 57 against Hannies |
| `"boss"` | A boss fight | 53; 54, 58, 59 or 99 for some bosses |
| `"dungeon"` | A quest's map | 1 to 14 by the quest; 57 in quest 135 |
| `"town"` | The town, the shop, the Party and Quests screens | 105 before Rance Castle opens, then 101, or 106 with the Magnum set |
| `"castle"` | Rance Castle | 89 |
| `"opening"` | The opening | 103, or 107 with the Magnum set |
| `"result"` | The results screen after a quest | 102 |
| `"jingle"` | A girl monster joins | 108 |
| `"scene"` | A scene: the game's or a mod's | Mostly 71 to 99; 201 to 213 for sounds |
| `"other"` | The extras, the system bar, a save's load, the title, a mod's `rq.music.play` | Any |

More on the ctx: in a fight, `ctx.enemies` lists the monster numbers and, in a boss fight,
`ctx.boss` is the boss. On a quest's map, `ctx.area` and `ctx.map_kind` say where
(`rq.ids.map_kind`). `ctx.world` is the world.

### One scene's music

In a game scene, `ctx.scene` names the game's scene function, so one scene can have its own track:

```lua
rq.music.on_play(function(ctx)
  if ctx.scene == "ランス／城汎用" then ctx:file("music/rance_room.ogg") end
end)
```

To find a scene's name, log it while you play: `rq.log(tostring(ctx.scene))`.

## Let the player choose

`rq.music.page()` gives your pack a page in Config's Mods tab. It lists every track you replaced,
with a switch to turn it off (the game's track plays again) and a button to hear yours. "All on"
and "All off" switch everything. The choice is kept for every save profile.

For the moments your `on_play` picks, name them, and ask their switch in the callback:

```lua
rq.music.page({ moments = { { key = "boss", name = "Boss fights" } } })

rq.music.on_play(function(ctx)
  if ctx.kind == "boss" and rq.music.enabled("boss") then ctx:file("music/boss.ogg") end
end)
```

If your mod already has a Config page, draw the same rows on it with `rq.uikit.music_list`:

```lua
rq.config.page({ id = "my-pack", title = "My Pack", draw = function(ui, box)
  rq.uikit.music_list({ w = box.w, moments = { { key = "boss", name = "Boss fights" } } })
end })
```

## When two mods replace the same track

The mod that loads later wins, and the log names both. Use `mod.json`'s load order when your pack
should come after another. A mod's `rq.music.restore(no)` takes back only its own replacement;
the one below it in load order then plays again. A track the player switched off on the winning
mod's page also falls back to the one below.

## Things to know

- **A path is looked up in the folder of the mod whose code calls `rq.music`.** A helper in a
  library mod uses the library's folder, also when it ends in `return rq.music.replace(...)`. Before
  loader 2.24.1 that tail call used the caller's folder ([Which mod is calling](sandbox.md#which-mod-is-calling)).
- The rain, wind and other sounds of the game's scenes are music tracks too (201 to 213): `replace`
  and `on_play` take them like any track. The game has a channel for looped ambient sounds, but
  never starts one. For a looped sound of your own beside the music, use
  `rq.sound.play(path, { loop = 0 })`.
- A wrong track number in `init.lua` is only found once the game has opened its music, at the
  first frame. It is logged and dropped, not raised.
