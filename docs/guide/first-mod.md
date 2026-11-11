# Your first mod

This page builds a small mod step by step: text on the screen, a key on the debug menu, a change to
a skill's hover text, a line in the log for every skill an ally uses, and a value kept with the save. You need RQ MOD installed
([Install](install.md)) and a text editor; [Editor setup](editor-setup.md) adds completion for every
`rq.*` call.

## 1. The folder

A mod is a folder in `mods` with two files:

```text
mods/
└── hello-mod/
    ├── mod.json
    └── init.lua
```

`mod.json` says who the mod is and which loader it needs:

```json
{
  "id": "hello-mod",
  "name": "Hello Mod",
  "author": "You",
  "version": "1.0.0",
  "loader": "0.25.0"
}
```

`loader` is the lowest RQ MOD version that has every call the mod uses. Each entry in the
[API reference](../reference/index.md) says when it was added (`since`). This mod uses
`rq.battle.on_use`, added in 0.25.0. All fields are on the [mod.json](manifest.md) page.

## 2. Text on the screen

`init.lua` runs once, when the game starts. Put this in it:

```lua
rq.log("Hello Mod loaded")

rq.on_frame(function()
  rq.hud.text(10, 10, "Hello from my mod", { size = 18 })
end)
```

Start the game with `xsystem4\xsystem4.exe`. The text shows in the top left corner, and
`logs\rqmod.log` has the line `[hello-mod] Hello Mod loaded`.

`rq.on_frame` runs its function on every update of the game. The HUD is immediate mode: what you draw
shows for one frame, so you draw it again every frame. Coordinates are game pixels from the top left.
See [`rq.hud`](../reference/api/rq.hud.md) for boxes, CGs and clicks.

::: tip The top level runs before the game
Mods load before the game starts running. At the top level of `init.lua`, register callbacks and
definitions. Calls that read or change the game, such as `rq.chara.get` or `rq.hud.text_width`, raise
an error there; make them from `rq.on_frame` or a callback.
:::

## 3. A key on the debug menu

Hold F3 in the game to see the debug menu. A mod can add rows to it:

```lua
local shown = true

rq.debug.action({
  id = "hello-toggle",
  label = "Hello text on/off",
  key = "7",
  onPress = function() shown = not shown end,
})

rq.on_frame(function()
  if shown then
    rq.hud.text(10, 10, "Hello from my mod", { size = 18 })
  end
end)
```

Hold F3 and press 7. Keys 6, F3, `+`, `-` and M belong to the engine.

## 4. Change a skill's hover text

`rq.skill.on_describe` rewrites the text the game shows when the mouse is over a skill, on the
status and fight screens:

```lua
rq.skill.install()
rq.skill.on_describe(function(no, text)
  local s = rq.skill.get(no)
  return text .. " (skill " .. no .. ", x" .. s.bairitsu .. ")"
end)
```

Each callback gets the text the one before it left, so several mods can add to the same text.

## 5. Watch a fight

`rq.battle.on_use` reports every skill as it is carried out:

```lua
rq.battle.on_use(function(ev)
  if ev.side == "ally" then
    local who = rq.chara.get(ev.user)
    rq.log(who.name, "used skill", ev.skill)
  end
end)
```

Start a quest and fight. Each ally action adds a line to the log. `ev.user` is a roster slot; see
[Numbers and ids](ids.md) for what the numbers mean.

## 6. Remember something

A mod's variables start over every time the game starts. To keep a value with the save, use
[`rq.savedata`](../reference/api/rq.savedata.md). It is written when the game saves and comes back
when the game loads, so loading an older save brings back the older value too. It came in 2.34.0:
set `loader` in `mod.json` to `2.34.0` to use it.

```lua
rq.battle.on_end(function()
  rq.savedata.set("fights", rq.savedata.get("fights", 0) + 1)
end)
```

For settings, which should not go back with a load, there is `rq.store`. [Data that follows the
save](save-data.md) tells them apart.

::: tip Waiting
To do something later, `rq.after(3000, fn)` calls `fn` three seconds from now. For steps with
waits between them, run them in `rq.spawn` and wait inside with `rq.wait(ms)` or
`rq.wait_until(cond)`: the game goes on meanwhile. [Gold, encounters and
levels](game-state.md#waiting-and-timers) has examples, with the money, random fights and levels.
:::

## Changing the mod

Mods load once, when the game starts. After you change `init.lua`, restart the game. When something
does not work, look at `logs\rqmod.log` first: errors in callbacks are written there with the mod's
name. [Logs and debugging](debugging.md) has more.

## Next

- [mod.json](manifest.md): load order, dependencies and conflicts.
- [What a mod can reach](sandbox.md): files, `require` and what Lua libraries are there.
- [API reference](../reference/index.md): every `rq.*` call.
