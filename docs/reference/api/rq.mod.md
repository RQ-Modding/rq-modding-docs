# rq.mod

`since 2.0.0`

Finds out about other mods, and reaches what they share.

Every mod has its own global variables and its own `require` cache: a global set in one mod
is not seen by another, and two mods that each have a `util.lua` each get their own. A mod
shares only what its `init.lua` returns. A mod that lists that mod's id in `dependencies` in
`mod.json` gets it with `require("<id>")`; any mod can get it with `rq.mod.get`.

What is shared is the same value, not a copy, so a library mod can keep state in it. The
library's own modules, globals and files stay its own, also when another mod calls its
functions.

```lua
-- mods/ui-lib/init.lua (mod.json: "id": "ui-lib")
local M = {}
function M.title(text) rq.log("title: " .. text) end
return M

-- mods/my-mod/init.lua (mod.json: "dependencies": ["ui-lib"])
local ui = require("ui-lib")
ui.title("Hello")
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.mod.get`](#rqmodget) | Returns what a loaded mod's `init.lua` returned. |
| [`rq.mod.id`](#rqmodid) | Returns the id of the mod whose code calls it. |
| [`rq.mod.list`](#rqmodlist) | Returns the ids of the mods that finished loading, in load order. |

### rq.mod.get

```lua
rq.mod.get(id) -> any
```

`since 2.0.0`

Returns what a loaded mod's `init.lua` returned.

For optional support of another mod, without listing it in `dependencies`. A mod's value is
there once its `init.lua` has finished, so during your own `init.lua` you see only the mods
loaded before yours: list the other mod in `loadAfter` to be sure, or call this later (in a
callback). To need a mod, list it in `dependencies` and use `require("<id>")` instead.

```lua
-- mod.json: "loadAfter": ["ui-lib"], so ui-lib loads first when it is installed
local ui = rq.mod.get("ui-lib")    -- nil when ui-lib is not installed
if ui then ui.title("Hello") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The mod's `id` in its `mod.json`. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `any` | What its `init.lua` returned; `nil` when that mod is not loaded, did not finish loading, or returned nothing. |

See also: [`rq.mod.list`](rq.mod.md#rqmodlist)

### rq.mod.id

```lua
rq.mod.id() -> string|nil
```

`since 2.0.0` `changed 2.24.1`

Returns the id of the mod whose code calls it.

It is the `id` in that mod's `mod.json`. When a mod calls a function of another mod, the code
running is the other mod's, so that mod's id is returned.

The mod is found on the call stack: the nearest code that runs from a file in a mod's folder. A
tail call into another file's function, such as `return rq.ui.confirm(...)` in a callback, is a
plain call in RQ MOD, so your mod stays on the stack. A tail call within one file stays a tail call.

the top of a coroutine counted as outside any mod.

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The calling mod's id; `nil` outside any mod's code. |

> Changed in 2.24.1: Found through a tail call. Before, `return rq.ui.confirm(...)` in a callback or at

### rq.mod.list

```lua
rq.mod.list() -> string[]
```

`since 2.0.0`

Returns the ids of the mods that finished loading, in load order.

A mod whose `init.lua` raised an error is not in the list, nor is one that is still loading
(your own mod, during its `init.lua`).

```lua
for _, id in ipairs(rq.mod.list()) do rq.log(id) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `ids` | `string[]` | The mods' `id`s, in the order they loaded. |

See also: [`rq.mod.get`](rq.mod.md#rqmodget)
