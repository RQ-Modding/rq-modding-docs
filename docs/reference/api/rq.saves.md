# rq.saves

`since 0.3.0`

Save profiles: whole save folders the player can switch between.

The base profile is the engine's own `SaveData` folder and can never be deleted. Every other profile
is a full copy under `<parent of SaveData>\Profiles\<id>\save`, with a `profile.json`;
`Profiles\active.txt` holds the active id. The engine picks the folder at boot, so switching
restarts the game. Calls that fail return nil and a message. The vanilla game's own save is only
ever read.

```lua
if rq.saves.title() then
  for _, p in ipairs(rq.saves.list()) do
    rq.log(p.name, p.active and "(active)" or "", p.summary.gold)
  end
end
local id = rq.saves.clone("base", "Friend test")
if id then rq.saves.switch(id) end
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.saves.install`](#rqsavesinstall) | Wraps `T_Title@checkSelect` so `rq.saves.title` works. |
| [`rq.saves.title`](#rqsavestitle) | Returns whether the title screen waits for a choice. |
| [`rq.saves.active`](#rqsavesactive) | Returns the active profile's id. |
| [`rq.saves.list`](#rqsaveslist) | Lists the profiles: the base first, then the others by creation time. |
| [`rq.saves.current_mods`](#rqsavescurrent_mods) | Lists the mods loaded in this session. |
| [`rq.saves.vanilla`](#rqsavesvanilla) | Reads the vanilla game's save in `Documents\AliceSoft\<game>\SaveData`. |
| [`rq.saves.create`](#rqsavescreate) | Makes a new, empty profile. |
| [`rq.saves.clone`](#rqsavesclone) | Copies a whole profile into a new one. |
| [`rq.saves.import_vanilla`](#rqsavesimport_vanilla) | Copies the vanilla game's save folder into a new profile, byte for byte. |
| [`rq.saves.rename`](#rqsavesrename) | Renames a profile. |
| [`rq.saves.delete`](#rqsavesdelete) | Deletes a profile. |
| [`rq.saves.switch`](#rqsavesswitch) | Makes a profile active and restarts the game on it. |
| [`rq.saves.autosave`](#rqsavesautosave) | Saves to the game's autosave slot now, as the game does when a quest is taken and when it ends. |

### rq.saves.install

```lua
rq.saves.install() -> boolean
```

`since 0.3.0`

Wraps `T_Title@checkSelect` so `rq.saves.title` works.

The engine already calls it at boot; calling it again is harmless.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the hook is in place. |

### rq.saves.title

```lua
rq.saves.title() -> boolean
```

`since 0.3.0`

Returns whether the title screen waits for a choice.

It is false inside the title's sub-menus (load, config).

| Returns | Type | Description |
| --- | --- | --- |
| `waiting` | `boolean` | true on the title's main choice. |

### rq.saves.active

```lua
rq.saves.active() -> string
```

`since 0.3.0`

Returns the active profile's id.

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string` | "base" for the original save. |

### rq.saves.list

```lua
rq.saves.list() -> rq.SaveProfile[]
```

`since 0.3.0`

Lists the profiles: the base first, then the others by creation time.

It reads every profile's save file, so call it when a window opens, not every frame.

| Returns | Type | Description |
| --- | --- | --- |
| `profiles` | [`rq.SaveProfile`](../types/rq.SaveProfile.md) `[]` | The profiles. |

### rq.saves.current_mods

```lua
rq.saves.current_mods() -> rq.SaveMod[]
```

`since 0.3.0`

Lists the mods loaded in this session.

| Returns | Type | Description |
| --- | --- | --- |
| `mods` | [`rq.SaveMod`](../types/rq.SaveMod.md) `[]` | The mods. |

### rq.saves.vanilla

```lua
rq.saves.vanilla() -> rq.VanillaSave
```

`since 0.3.0`

Reads the vanilla game's save in `Documents\AliceSoft\<game>\SaveData`.

| Returns | Type | Description |
| --- | --- | --- |
| `save` | [`rq.VanillaSave`](../types/rq.VanillaSave.md) | What was found. |

### rq.saves.create

```lua
rq.saves.create(name) -> string|nil, string?
```

`since 0.3.0`

Makes a new, empty profile.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The name. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The new profile's id, or nil. |
| `err` | `string?` | Why it failed. |

### rq.saves.clone

```lua
rq.saves.clone(src_id, name) -> string|nil, string?
```

`since 0.3.0`

Copies a whole profile into a new one.

The game's own `Backup` folder is skipped.

| Parameter | Type | Description |
| --- | --- | --- |
| `src_id` | `string` | The profile to copy. |
| `name` | `string` | The new profile's name. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The new profile's id, or nil. |
| `err` | `string?` | Why it failed. |

### rq.saves.import_vanilla

```lua
rq.saves.import_vanilla(name) -> string|nil, string?
```

`since 0.3.0`

Copies the vanilla game's save folder into a new profile, byte for byte.

It never writes to the source.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The new profile's name. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The new profile's id, or nil. |
| `err` | `string?` | Why it failed. |

### rq.saves.rename

```lua
rq.saves.rename(id, name) -> boolean|nil, string?
```

`since 0.3.0`

Renames a profile.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The profile. |
| `name` | `string` | The new name, up to 40 bytes. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean\|nil` | true, or nil. |
| `err` | `string?` | Why it failed. |

### rq.saves.delete

```lua
rq.saves.delete(id) -> boolean|nil, string?
```

`since 0.3.0`

Deletes a profile.

It refuses "base" and the active profile.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The profile. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean\|nil` | true, or nil. |
| `err` | `string?` | Why it failed. |

### rq.saves.switch

```lua
rq.saves.switch(id) -> nil, string?
```

`since 0.3.0`

Makes a profile active and restarts the game on it.

It records the choice, starts a new process (which waits for this one to exit) and exits this one.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The profile. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `nil` | Nothing: on success it does not return. |
| `err` | `string?` | Why the choice could not be recorded. |

### rq.saves.autosave

```lua
rq.saves.autosave() -> boolean, string?
```

`since 2.50.0`

Saves to the game's autosave slot now, as the game does when a quest is taken and when it ends.

It calls the game's own autosave (`自動セーブ(1)`): its "Auto-Saving" message shows for 700 ms and
the save goes to the slot the title's Continue loads, with the `rq.saves.on_save` callbacks and
`rq.savedata`. It saves on the hub only, where the SYSTEM menu's Save is on too (the footer's hub
mode, outside a quest): a mod that changed the player's things in a scene can save them before
anything else happens. The game draws frames while its message shows, so `rq.on_frame` runs under
it; a call from there while the game saves is refused. `rq.scene.start` and `rq.ui.choose` wait
for the save to end.

```lua
local save_after = false
rq.on_frame(function()
  if save_after and not rq.scene.active() and rq.ui.get().screen == "hub" then
    save_after = false
    local ok, why = rq.saves.autosave()
    if not ok then rq.log("no autosave: " .. why) end
  end
end)
```

| Returns | Type | Description |
| --- | --- | --- |
| `saved` | `boolean` | true when the game wrote the save. |
| `why` | `string?` | Why it did not save: "a quest is running", "only on the hub", "the game is saving" or "the game could not save". |

See also: [`rq.saves.on_save`](rq.saves.md#rqsaveson_save)

## Events

| Name | Summary |
| --- | --- |
| [`rq.saves.on_save`](#rqsaveson_save) | Calls `fn` just before the game writes its save. |
| [`rq.saves.on_load`](#rqsaveson_load) | Calls `fn` after the game has loaded a save. |

### rq.saves.on_save

```lua
rq.saves.on_save(fn) -> fun()
```

`since 2.34.0`

Calls `fn` just before the game writes its save.

The game saves before a quest starts, when one ends, from the SYSTEM menu's Save, and on Suspend
(then `ctx.suspend` is true and the game closes). Put a mod's last numbers into `rq.savedata` here;
`rq.savedata` is written with the save right after. An error is logged once for each new error
text.

```lua
local steps = 0
rq.saves.on_save(function()
  rq.savedata.set("steps", steps)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.SaveCtx`](../types/rq.SaveCtx.md) `)` | Runs before the save is written. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.savedata`](rq.savedata.md)

### rq.saves.on_load

```lua
rq.saves.on_load(fn) -> fun()
```

`since 2.34.0`

Calls `fn` after the game has loaded a save.

It runs for the title's Continue, the SYSTEM menu's Load and the title's Resume, after the game's
own after-load step, with `rq.savedata` holding that save's data. For the suspend save it runs
before the map shows again. A new game loads nothing, and starts with no `rq.savedata`.
`rq.on_reset("load")` runs before the load instead. An error is logged once for each new error
text.

```lua
local steps = 0
rq.saves.on_load(function()
  steps = rq.savedata.get("steps", 0)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.SaveCtx`](../types/rq.SaveCtx.md) `)` | Runs after the save is loaded. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.savedata`](rq.savedata.md)
