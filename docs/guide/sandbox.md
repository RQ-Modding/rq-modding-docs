# What a mod can reach

Mods run in Lua 5.4 with the standard libraries, the `rq` table, and a sandbox around files: a mod
reads, writes and loads files only inside its own folder. This keeps one mod from reading another's
files or touching the rest of the computer.

## Files

Paths are relative to the mod's folder. `..` and absolute paths that lead out of it are refused with
an error.

| Call | In the sandbox |
| --- | --- |
| `io.open`, `io.lines`, `io.input`, `io.output` | A file in the mod's folder. An absolute path works only when it is inside the folder. |
| `os.remove`, `os.rename` | Files in the mod's folder. |
| `dofile`, `loadfile` | A relative path in the mod's folder. Every absolute path is refused. |
| `load` | Works. The chunk belongs to the mod that loads it, whatever name it asks for, so its `rq.log` lines and `io` calls are that mod's. |
| `io.popen`, `io.tmpfile`, `os.tmpname`, `os.execute` | Not available: they raise an error. |
| `package.loadlib`, C modules | Not available. |
| `debug` | Not there. `rq.traceback` gives what `debug.traceback` would. |

For data a mod keeps between runs, `rq.store` is simpler than files: it lives with the save, and
`rq.store.global` lives with every save profile.

## require

`require` looks in the mod's own folder. Dots become folders:

```lua
local util = require("util")          -- util.lua
local draw = require("ui.draw")       -- ui\draw.lua, or ui\draw\init.lua
```

A module name with `:`, `/`, `\` or `..` is refused. `require("rq")` gives the `rq` table, and
`require("rq.hud")` gives `rq.hud`; both are also there as globals.

::: warning Mods share one Lua state
All mods run in the same Lua state, so they share global variables and `require`'s cache
(`package.loaded`). When two mods both `require("util")`, the second one gets the first one's module.
Keep your code in `local` variables, and put your modules in a folder named after your mod:

```lua
local util = require("hellomod.util")  -- hellomod\util.lua in your mod's folder
```
:::

## When code runs

`init.lua` runs once at startup, before the game runs. Register callbacks and definitions there:
`rq.on_frame`, the `on_*` calls, `define`, `edit`, `patch`, `rq.image.add`. Calls that read or change
the running game raise an error at that point. Among them:

- `rq.skill.get`, `rq.chara.get`, `rq.item.give`, `rq.party.*`
- `rq.hud.text_width`, `wrap`, `cg` and `text_begin`
- `rq.input.set_key`, `set_mouse`, `wheel` and `release`
- `rq.ui.get`, `aim`, `shot` and `shot_result`
- `rq.battle.start`, `rq.random.seed`

The queries `rq.units()`, `rq.items()`, `rq.quests()` and `rq.castle()` return empty lists there.
Make these calls from `rq.on_frame` or from a callback.

## Errors

An error in a callback is written to `logs\rqmod.log` with the mod's name, and the game goes on. An
error in `rq.on_frame` is logged once for each new error text, not on every frame.

An error at the top level of `init.lua` stops it there, with `run error <path>: <message>` in the
log, and the mod does not count as loaded. Callbacks it registered before the error stay
registered, so fix the error rather than rely on what ran.

## Saving under a Lua call

The game cannot save while a mod's Lua call waits inside the game (for example a scene that a mod
plays). The engine refuses such a save, and a load there ends the Lua call with an error instead of
crashing.
