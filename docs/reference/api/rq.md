# rq

`since 0.2.0`

The global table every mod uses to reach the game.

The engine builds `rq` before any mod runs. Mods load before the game starts, so at the top level
of `init.lua` register callbacks and definitions (`rq.on_frame`, `on_*`, `define`, `edit`,
`patch`, `rq.image.add`). Calls that read or change game state, such as `rq.skill.get`,
`rq.chara.get`, `rq.item.give`, `rq.party.*` or `rq.hud.text_width`, raise an error there: make
them from `rq.on_frame` or a callback. The queries `rq.units()`, `rq.items()`, `rq.quests()` and
`rq.castle()` return empty results at that point.

Every `on_*` call, `rq.on_frame` and `rq.ain.hook` return a function that removes the callback.
It works at once, also from inside the callback, and calling it twice is harmless. Definitions
(`define`, `edit`) are not callbacks and have no remover.

```lua
local remove
remove = rq.battle.on_end(function(ev)
  rq.log("the first fight ended")
  remove()
end)
```

## Namespaces

| Namespace | Summary |
| --- | --- |
| [`rq`](rq.md) | The global table every mod uses to reach the game. |
| [`rq.agent`](rq.agent.md) | Lets the test pipe (`rqmod-ctl`) see and press a mod's controls. |
| [`rq.ain`](rq.ain.md) | Reaches into the game's own code (the AIN): call, hook and patch its functions, and read and write its globals. |
| [`rq.battle`](rq.battle.md) | Hooks into fights: events, ally skill select, marks and buffs on the cards, faces, states, drops, and scripted fights. |
| [`rq.castle`](rq.castle.md) | Reads the castle: whether it is open, its rooms and who is in them. |
| [`rq.chara`](rq.chara.md) | Reads and changes characters: their skills, stats, the skill buy list, and the roster. |
| [`rq.chest`](rq.chest.md) | The chance of opening a red chest. |
| [`rq.combat`](rq.combat.md) | Changes physical damage, accuracy and criticals. |
| [`rq.config`](rq.config.md) | A Mods tab in the game's Config screen. |
| [`rq.counter`](rq.counter.md) | Lets the Counter skill (259) work after Ally Guard. |
| [`rq.debug`](rq.debug.md) | Adds rows to the engine's F3 debug menu. |
| [`rq.dungeon`](rq.dungeon.md) | Reads and changes the dungeon: the map, the player's place, objects on it, and the camera. |
| [`rq.hud`](rq.hud.md) | Draws text, boxes and CGs over the game, and reads clicks on them. |
| [`rq.ids`](rq.ids.md) | The game's numbers by name: characters, items, monsters, quests, skills, and the small lists the game names (classes, states, races, character types, elements, item kinds, skill targets). |
| [`rq.image`](rq.image.md) | Images from a mod's folder, shown by the game as CGs. |
| [`rq.input`](rq.input.md) | Reads the mouse and keyboard, and drives them for the game. |
| [`rq.item`](rq.item.md) | Defines, gives and changes items. |
| [`rq.items`](rq.items.md) | Lists the item instances the player owns. |
| [`rq.loot`](rq.loot.md) | Chest loot: what the pools roll, and the items the player will find, known in advance. |
| [`rq.mod`](rq.mod.md) | Finds out about other mods, and reaches what they share. |
| [`rq.music`](rq.music.md) | Music from a mod's own file, in place of one of the game's tracks. |
| [`rq.orb`](rq.orb.md) | The blue Recovery Spring on the map (`回復の泉`, object 203). |
| [`rq.party`](rq.party.md) | Reads and changes who is in the party. |
| [`rq.quests`](rq.quests.md) | Lists the quests and follows them: clears, endings, quest moments and state. |
| [`rq.random`](rq.random.md) | Controls the random number generator the game and the loader share. |
| [`rq.saves`](rq.saves.md) | Save profiles: whole save folders the player can switch between. |
| [`rq.scene`](rq.scene.md) | Plays scenes with the game's own commands, so a mod can do anything a game scene does. |
| [`rq.shop`](rq.shop.md) | Adds stock to Frostbuy, the item shop, and reports purchases. |
| [`rq.skill`](rq.skill.md) | Reads, defines and patches skills, and rewrites their hover text. |
| [`rq.skilllist`](rq.skilllist.md) | Pages the Potential Skills grid, 36 skills a page. |
| [`rq.sound`](rq.sound.md) | Plays sounds: a game sound number, a file in the mod folder, or a sound inside a game Flash file. |
| [`rq.speed`](rq.speed.md) | Runs the game clock faster or slower than real time. |
| [`rq.sprite`](rq.sprite.md) | Sprites a mod makes once and changes later, drawn among the game's own in z order. |
| [`rq.status`](rq.status.md) | Battle states made by mods, such as a burn, a bleed, a regeneration, a freeze or a weaken, that live beside the game's poison, stun and ▲▼, in one registry every mod shares. |
| [`rq.store`](rq.store.md) | Small key and value storage for each mod and each save. |
| [`rq.ui`](rq.ui.md) | Reads what is on the screen and saves screenshots. |
| [`rq.uikit`](rq.uikit.md) | Widgets in the look of the game's Config screen and, since 2.6.0, of its hub. |
| [`rq.units`](rq.units.md) | Lists the recruited characters. |

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `version` | `string` | The loader version, such as "1.16.0". A mod whose `mod.json` asks for a newer `loader` is not loaded. |
| `game_dir` | `string` | The game folder (where the AIN is). |
| `mods_dir` | `string` | The `mods` folder, ending in a backslash. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.log`](#rqlog) | Writes a line to the console and to the log. |
| [`rq.time_ms`](#rqtime_ms) | Returns the time since the game started, in real milliseconds. |
| [`rq.traceback`](#rqtraceback) | Returns a stack trace, of the current code or of a coroutine. |

### rq.log

```lua
rq.log(...)
```

`since 0.2.0` `changed 1.1.0`

Writes a line to the console and to the log.

The line goes to `logs\rqmod.log` (the `logs` folder beside `mods`) and, when `config.json` has
`"terminal": true`, to the console window. It starts with the name of the mod and file that
called it, such as `[loot-preview] Detected 2 items`. Arguments are turned into text as `tostring`
does and joined with tabs, as `print` does.

| Parameter | Type | Description |
| --- | --- | --- |
| `...` | `any` | The values to write. |

> Changed in 1.1.0: The log moved from `mods` to the `logs` folder.

### rq.time_ms

```lua
rq.time_ms() -> integer
```

`since 0.20.0`

Returns the time since the game started, in real milliseconds.

It keeps counting at real speed whatever `rq.speed` is set to.

| Returns | Type | Description |
| --- | --- | --- |
| `ms` | `integer` | Milliseconds since the game started. |

### rq.traceback

```lua
rq.traceback(co, msg) -> string
```

`since 0.20.0`

Returns a stack trace, of the current code or of a coroutine.

The sandbox has no `debug` library; this gives what `debug.traceback` would.

| Parameter | Type | Description |
| --- | --- | --- |
| `co` *(optional)* | `thread\|string` | The coroutine to trace, or the message when no coroutine is given. |
| `msg` *(optional)* | `string` | A message put before the trace. |

| Returns | Type | Description |
| --- | --- | --- |
| `trace` | `string` | The stack trace. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.on_frame`](#rqon_frame) | Calls `fn` once on every game update. |
| [`rq.on_reset`](#rqon_reset) | Calls `fn` after a load or after going to the title, once the game runs again. |

### rq.on_frame

```lua
rq.on_frame(fn) -> fun()
```

`since 0.2.0` `changed 0.3.0`

Calls `fn` once on every game update.

Draw with `rq.hud.*` here, and check input or game state. Every mod may register callbacks; they
run in load order. An update is not a drawn frame: on a screen that does not redraw it can run
thousands of times per second, so use `rq.time_ms` for anything that must last a real time. An
error in `fn` is logged once for each new error text, not on every update.

```lua
rq.on_frame(function()
  rq.hud.text(10, 10, "Hello from my mod")
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Runs on every update. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.3.0: Every mod keeps its own callback (before, the last mod replaced the others).

### rq.on_reset

```lua
rq.on_reset(fn) -> fun()
```

`since 1.13.0`

Calls `fn` after a load or after going to the title, once the game runs again.

Use it to clear a mod's own flags, such as "a scene is playing". These are the same callbacks as
`rq.sprite.on_reset`, and they run after every mod sprite is gone. On the title, every Lua call
that was waiting in the game (a scene, a fight from `rq.battle.start`) has already ended with the
error "rq: the game went to the title".

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(why: "load"\|"title")` | `why` says which one happened. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
