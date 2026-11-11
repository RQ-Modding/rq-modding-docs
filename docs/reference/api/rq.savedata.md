# rq.savedata

`since 2.34.0`

Each mod's data that follows the game's save.

Kept in memory while the game runs: nothing is written on `set`. When the game writes its save (or
the suspend save) the data is written beside it, in `RanceQuestMagnum_030.rqmod.json` (`_930` for
the suspend save), and when the game loads a save the data comes back as it was then. So after a
quit without saving, or the load of an older save, a mod sees the data that matches the save. The
data is emptied at the title, so a new game starts with none, and data set at the title is dropped
by the next load. A save made before this version, or without the loader, has none.

At the top level of `init.lua` no save is loaded yet: read the data in `rq.saves.on_load`, or when
it is needed. Each mod sees only its own keys. The data of a mod that is not loaded now is kept and
written back, and the file is deleted with its save (the suspend save after a resume, both at the
title's Reset) and copied into the game's daily backup with it.

Values are numbers, strings, booleans and tables of them: a table has string keys, or is a list
(1 to n with no holes), up to 16 levels deep. A whole number comes back an integer (up to 2^53).
`set` copies a table and `get` returns a new copy, so changing one after does nothing until it is
set again. The whole file is written at every save: keep it small.

```lua
rq.shop.on_buy(function(ctx)
  if ctx.no == MY_ITEM then rq.savedata.set("bought", rq.savedata.get("bought", 0) + 1) end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.savedata.get`](#rqsavedataget) | Reads a key. |
| [`rq.savedata.set`](#rqsavedataset) | Writes a key. |
| [`rq.savedata.delete`](#rqsavedatadelete) | Deletes a key. |
| [`rq.savedata.keys`](#rqsavedatakeys) | Lists this mod's keys. |

### rq.savedata.get

```lua
rq.savedata.get(key, default) -> any
```

`since 2.34.0`

Reads a key.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |
| `default` *(optional)* | `any` | What to return when the key is not set. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `any` | The value (a copy for a table), or `default`. |

### rq.savedata.set

```lua
rq.savedata.set(key, value)
```

`since 2.34.0`

Writes a key.

Raises an error for a value that cannot be kept: a function, a table with both string keys and
list indexes, a list with holes, a table nested past 16 levels or inside itself, NaN, an infinite
number, an integer past 2^53, or a string with a zero byte.

```lua
rq.savedata.set("met", { "Sill", "Kanami" })
local met = rq.savedata.get("met", {})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |
| `value` | `any` | The value; nil deletes the key. |

### rq.savedata.delete

```lua
rq.savedata.delete(key)
```

`since 2.34.0`

Deletes a key.

| Parameter | Type | Description |
| --- | --- | --- |
| `key` | `string` | The key. |

### rq.savedata.keys

```lua
rq.savedata.keys() -> string[]
```

`since 2.34.0`

Lists this mod's keys.

| Returns | Type | Description |
| --- | --- | --- |
| `keys` | `string[]` | The keys. |
