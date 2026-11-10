# Replacing music

`rq.music` (loader 2.4.0) plays a music file from your mod where the game plays one of its own
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
- **Volume:** the game's music volume and fades apply to your file. `volume` (0 to 100, default
  100) lowers a file that is louder than the game's tracks. Better still, make the file as loud
  as the game's music.

## Music for one quest, dungeon or fight

`rq.music.on_play` runs each time the game is about to change the music. `ctx:file` plays one of
your files this time only. `ctx:track` plays another game track instead.

```lua
local MY_QUEST = 42

rq.music.on_play(function(ctx)
  if ctx.quest ~= MY_QUEST then return end
  if ctx.kind == "dungeon" then
    ctx:file("music/my_dungeon.ogg")
  elseif ctx.kind == "fight" and ctx.no == rq.ids.music.BOSS_BATTLE_R8 then
    ctx:file("music/my_boss.ogg", { loop_start = 4.0 })
  end
end)
```

`ctx.kind` is "fight", "dungeon" or "other", `ctx.no` is the track the game asked for, and
`ctx.quest` is the quest in progress.

## When two mods replace the same track

The mod that loads later wins, and the log names both. Use `mod.json`'s load order when your pack
should come after another. A mod's `rq.music.restore(no)` takes back only its own replacement.

## Things to know

- **A path is looked up in the folder of the mod whose code calls `rq.music`.** A helper in a
  library mod uses the library's folder, also when it ends in `return rq.music.replace(...)`. Before
  loader 2.24.1 that tail call used the caller's folder ([Which mod is calling](sandbox.md#which-mod-is-calling)).
- The game's looped ambient sounds (rain, wind) are music tracks too. `replace` changes them;
  `on_play` does not see them.
- A wrong track number in `init.lua` is only found once the game has opened its music, at the
  first frame. It is logged and dropped, not raised.
