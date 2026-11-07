# Logs and debugging

## The log

`logs\rqmod.log`, in the folder next to `mods`, is the first place to look. It holds:

- what the engine found at startup: the folders, the loader version, each mod it loaded
  (`Loading <id> priority <n>`) or skipped and why;
- every `rq.log` line, starting with the mod's id: `[hello-mod] Hello Mod loaded`;
- every error in a mod's callback, with the mod's name and the Lua message.

The run before is kept as `rqmod.prev.log`. When the game crashes, the engine also writes
`rqmod-crash-<date>-<time>.log` (what happened, where, the game-script call stack and the last log
lines) and a small `.dmp`. A run that never closed cleanly leaves `rqmod-unclean-<date>-<time>.log`.

```lua
rq.log("rank", rank, "of", total)       -- values are joined with tabs, as print does
```

## The console

With `"terminal": true` in `xsystem4\config.json` (the default), a console window opens beside the
game and shows the same lines as the log while you play.

`"verbose": true` adds the engine's own event lines (settings, saves, the dungeon, the shop,
combat). Use it when you report an engine problem; it makes the log much longer.

## The F3 menu

Hold F3 in the game to see the engine's debug menu. Key 6 toggles Rendering Stats. A mod adds rows
with [`rq.debug.action`](../reference/api/rq.debug.md):

```lua
rq.debug.action({
  id = "hello-dump",
  label = "Log the party",
  key = "7",
  onPress = function()
    for _, u in ipairs(rq.units()) do rq.log(u.id, u.name, u.level) end
  end,
})
```

Rows can go on pages of their own with `page`. Keys 6, F3, `+`, `-` and M are the engine's.

## Errors in callbacks

An error inside a callback does not stop the game: it is logged and the other mods' callbacks still
run. An error in `rq.on_frame` is logged once for each new message, not on every frame. For a stack
trace, use `rq.traceback`, since the sandbox has no `debug` library:

```lua
local ok, err = xpcall(do_work, rq.traceback)
if not ok then rq.log(err) end
```

## Common problems

| What you see | Why |
| --- | --- |
| The mod does nothing, and the log has no `Loading <id>` line | It was skipped: look for its `skip` line ([mod.json](manifest.md#load-order)). |
| `run error ...\init.lua: ...` | An error at the top level of `init.lua`. |
| `rq.<call>: the game is not running yet` at startup | A call that reads the game ran at the top level. Move it into `rq.on_frame` or a callback ([When code runs](sandbox.md#when-code-runs)). |
| A HUD element flickers or shows once | HUD calls draw for one frame. Draw it on every `rq.on_frame`. |
| A timer runs out too soon | `rq.on_frame` runs per game update, which can be thousands of times a second on a still screen. Measure time with `rq.time_ms`. |
| Two mods fight over one thing | Load order decides who goes last: see `loadAfter` in [mod.json](manifest.md). |
