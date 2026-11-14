# Data that follows the save

A mod's variables start over every time the game starts. There are three places to keep a value
for longer. They differ in what happens when the player loads an older save, or quits without
saving.

| Call | Kept | Written | For |
| --- | --- | --- | --- |
| [`rq.savedata`](../reference/api/rq.savedata.md) (2.34.0) | With each save of the game, in a file beside it | When the game saves | Progress: what the player did in this playthrough |
| [`rq.store`](../reference/api/rq.store.md) | With the save profile | At once, on every `set` | Settings, and anything that must not go back with a load |
| `rq.store.global` | For every save profile | At once | Settings shared by every profile |

Each example on this page is a whole `init.lua`; set `loader` to `2.34.0` in its `mod.json`.

## rq.savedata

`rq.savedata` has the calls `rq.store` has: `get(key, default)`, `set(key, value)`, `delete(key)`
and `keys()`. Each mod sees only its own keys.

```lua
local LENS = 900 -- your item's number

rq.shop.on_buy(function(ctx)
  if ctx.no == LENS then
    rq.savedata.set("bought", rq.savedata.get("bought", 0) + 1)
  end
end)
```

The data follows the game's save:

- `set` keeps the value in memory. Nothing is written yet.
- When the game saves (before a quest, after it, the SYSTEM menu's Save), every mod's data is
  written beside the save, in `RanceQuestMagnum_030.rqmod.json`. The suspend save gets its own
  file, `_930`.
- When the game loads a save (Continue, the SYSTEM menu's Load, Resume), each mod's data comes back
  as it was at that save. So a purchase made after the last save is gone after a quit without
  saving, as the item is.
- At the title no save is loaded: the data is empty there, and a new game starts with none.
- When the game deletes a save, its file goes too, and the game's daily backup copies it with the
  save.
- The data of a mod that is not loaded is kept and written back: removing a mod for a while loses
  nothing.

With `rq.store` the counter above would keep the newer number after the player loads an older save,
so a price that rises with each purchase would stay high with the purchase undone.

Values are numbers, strings, booleans and tables of them. A table has string keys, or is a list
(1 to n with no holes), up to 16 levels deep. A whole number comes back an integer, up to 2^53.
`set` copies a table and `get` returns a new copy, so change the table, then `set` it again. A
function, a table with both kinds of keys, NaN or a string with a zero byte raises an error. The
whole file is written at every save: keep the data small.

## When the game saves and loads

[`rq.saves.on_save`](../reference/api/rq.saves.md#rqsaveson_save) runs just before the game writes
a save: the moment to put in `rq.savedata` what the mod keeps in its variables.
[`rq.saves.on_load`](../reference/api/rq.saves.md#rqsaveson_load) runs after a save has loaded, with
its data in: the moment to read it back. In both, `ctx.suspend` is true for the suspend save.

```lua
local met = {}

rq.saves.on_load(function()
  met = rq.savedata.get("met", {})
end)

rq.saves.on_save(function()
  rq.savedata.set("met", met)
end)

rq.battle.on_end(function(ctx)
  for _, iic in ipairs(ctx.allies) do met[rq.chara.get(iic).name] = true end
end)
```

At the top level of `init.lua` no save is loaded yet, so read the data in `on_load`, or when it is
needed.

A mod can also save now, as the game does when a quest is taken and when it ends:
[`rq.saves.autosave`](../reference/api/rq.saves.md#rqsavesautosave) (2.50.0) writes the game's
autosave, with its "Auto-Saving" message, on the hub only. A mod that gave the player something in
a scene saves it before anything else can happen; Pluepet Rare Contract does it after its delivery:

```lua
local save_after = false
rq.on_frame(function()
  if not save_after or rq.scene.active() or rq.ui.get().screen ~= "hub" then return end
  save_after = false
  local ok, why = rq.saves.autosave()
  if not ok then rq.log("no autosave: " .. why) end
end)
```

The game draws frames while its message shows, and `rq.on_frame` runs under them: a second
autosave there is refused, and `rq.scene.start` and `rq.ui.choose` wait for the save to end.

## Moving from rq.store

A mod that kept its progress in `rq.store` can move it over once, on the first load after the
update:

```lua
rq.saves.on_load(function()
  local old = rq.store.get("bought")
  if old == nil then return end
  if rq.savedata.get("bought") == nil then rq.savedata.set("bought", old) end
  rq.store.delete("bought")
end)
```

A save made before loader 2.34.0, or without the loader, has no data, so `get` gives the default
there.

## Not yet

- States made by mods (`rq.status`) that last until the save is loaded again.
- An event for a new game. A new game starts with empty data, as at the title.
- Which mods have data in a save, in the Save Profiles list.
