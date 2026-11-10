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
| `dofile`, `loadfile` | A relative path in the mod's folder. Every absolute path is refused. The chunk runs with the mod's globals, unless `loadfile` is given an `env`. |
| `load` | Works. The chunk belongs to the mod that loads it, whatever name it asks for, so its `rq.log` lines and `io` calls are that mod's. It runs with the mod's globals, unless `load` is given an `env`. |
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
`require("rq.hud")` gives `rq.hud`; both are also there as globals. The standard libraries work
too: `require("string")` is `string`.

Each mod has its own cache (its `package.loaded`), so a module runs once per mod, and two mods that
each have a `util.lua` each get their own. The module runs with the mod's globals. As in Lua 5.4,
`require` also returns the module's file path the first time. A module file that does not compile
raises `error loading module ...` with the line.

## Globals

Each mod has its own global variables. A global set in one mod, with or without `_G.`, is not seen
by any other mod. Inside a mod, `_G` is the mod's own table, and `pairs(_G)` lists only what the
mod set. Names the mod did not set itself, such as `rq`, `string`, `pairs` or `print`, are found as
usual.

Everything the mod's code makes keeps its globals: functions defined in `init.lua`, callbacks given
to `rq.on_frame` and the `on_*` calls, modules from `require`, and chunks from `load`, `loadfile`
and `dofile`.

`setmetatable(_G, ...)` raises an error, so helpers that make undefined globals an error ("strict
mode") do not work. `local` is still the better habit: it is faster and easier to read.

::: warning Shared tables are still shared
The `rq` table and the standard library tables (`string`, `table`, `math`...) are the same tables
for every mod. A mod that writes `rq.log = f` or `string.trim = f` changes them for all mods.
Don't: keep your helpers in your own `local` table.

After each mod's `init.lua`, the loader writes a line to `logs\rqmod.log` for each field it added,
changed or removed in these tables:

```
[rqmod] my-mod added string.trim, in a table every mod shares
```

It only logs; the change stays. It looks three levels into `rq` (`rq.hud.box`, `rq.ids.skill.X`),
skips names that start with `_`, and writes at most 20 lines per mod. A change made later, in a
callback, is not logged.
:::

## Sharing with other mods

A mod shares only what its `init.lua` returns:

```lua
-- mods/ui-lib/init.lua   (mod.json: "id": "ui-lib")
local M = {}
function M.title(text) rq.log("title: " .. text) end
return M
```

Another mod that lists that id in `dependencies` in its [mod.json](manifest.md) gets it with
`require`:

```lua
-- mods/my-mod/init.lua   (mod.json: "dependencies": ["ui-lib"])
local ui = require("ui-lib")
ui.title("Hello")
```

- It is the same value, not a copy, so a library can keep state in it, and every mod sees that state.
- The library's own modules, globals and files stay its own, also when another mod calls its
  functions: inside `M.title`, `require("x")` and `io.open("x")` are the library's.
- `require` of a mod that is not in `dependencies` raises an error that says so. A file of that
  name in your own folder comes first.
- For optional support, without `dependencies`, use [`rq.mod.get`](../reference/api/rq.mod.md): it gives
  the value, or `nil` when that mod is not installed. List the mod in `loadAfter`, so it loads
  before yours when it is there.

```lua
-- mod.json: "loadAfter": ["ui-lib"]
local ui = rq.mod.get("ui-lib")
if ui then ui.title("Hello") end
```

`rq.mod.id()` gives your mod's id, and `rq.mod.list()` the ids of the mods that finished loading.

## Which mod is calling

The loader names the calling mod by the nearest code on the call stack that runs from a file in a
mod's folder. That is the mod behind `rq.mod.id`, the paths of `io`, `require` and `rq.music`, the
`rq.log` tag, and everything a mod adds under its id: game buttons, castle rooms, states, remembered
questions. It is the `id` in `mod.json`, also when the folder has another name. Code of a library mod
that your mod calls counts as the library's.

A tail call (`return f(...)`) into a function of another file is a plain call in RQ MOD, so your mod
stays on the stack: `return rq.ui.confirm(...)` asks your mod's question, and an error it raises
names your line. A tail call within one file stays a tail call, so a loop or recursion written that
way does not grow the stack. A chain of tail calls across files does grow it, as plain recursion
does: Lua stops it with "stack overflow" at about 499,000 levels. Since loader 2.24.1; before, such a
tail call counted as outside any mod.

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
