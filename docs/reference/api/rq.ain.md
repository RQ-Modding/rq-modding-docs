# rq.ain

`since 0.2.0`

Reaches into the game's own code (the AIN): call, hook and patch its functions, and read and write
its globals.

Names are the game's own, in UTF-8, such as `Ｔ戦闘前初期化` or `T_BattleSelect@select`; find them
with `rq.ain.find`. They can change with the game's data, so a mod that patches by number should
check the count it gets back.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.ain.patch_float`](#rqainpatch_float) | Replaces float constants in one AIN function. |
| [`rq.ain.patch_int`](#rqainpatch_int) | Replaces integer constants in one AIN function, such as a hard-coded skill number. |
| [`rq.ain.patch_int_after`](#rqainpatch_int_after) | Replaces the first integer constant `from` that follows a read of a global. |
| [`rq.ain.call`](#rqaincall) | Calls any AIN function by its name. |
| [`rq.ain.hook`](#rqainhook) | Runs Lua before and after any AIN function. |
| [`rq.ain.method`](#rqainmethod) | Calls a method of the game on the object a global reaches. |
| [`rq.ain.global`](#rqainglobal) | Reads a game global that holds an int, bool, float or string. |
| [`rq.ain.set_global`](#rqainset_global) | Writes a game global, as `rq.ain.global` reads it: `set_global(name, [step, ...,] value)`. |
| [`rq.ain.global_len`](#rqainglobal_len) | Returns the size of an array global. |
| [`rq.ain.set_global_len`](#rqainset_global_len) | Makes an array global longer or shorter, as the game's own `Realloc` does. |
| [`rq.ain.skip_msgbox`](#rqainskip_msgbox) | Removes the game's message boxes whose text contains `needle`. |
| [`rq.ain.skip_sdl_msgbox`](#rqainskip_sdl_msgbox) | Swallows the engine's own error boxes for the TADA and HTTP network checks (`getserverversion`). |
| [`rq.ain.find`](#rqainfind) | Writes the AIN functions whose name contains `needle` to the log. |

### rq.ain.patch_float

```lua
rq.ain.patch_float(name, from, to, n) -> integer
```

`since 0.2.0` `changed 1.3.0`

Replaces float constants in one AIN function.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `from` | `number` | The value to find. |
| `to` | `number` | The new value. |
| `n` *(optional)* | `integer` | Which occurrence, from 0. Default: all of them. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many constants were replaced. |

> Changed in 1.3.0: Reaches the game's code of a function the loader wraps (such as `Ｔ戦闘前初期化`); before, it patched only the wrapper and found nothing.

### rq.ain.patch_int

```lua
rq.ain.patch_int(name, from, to, n) -> integer
```

`since 0.17.0` `changed 1.3.0`

Replaces integer constants in one AIN function, such as a hard-coded skill number.

Occurrences count every constant of that value in the function, so they can differ between
versions of the game's AIN; to find one constant by what it follows, use `patch_int_after`.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `from` | `integer` | The value to find. |
| `to` | `integer` | The new value. |
| `n` *(optional)* | `integer` | Which occurrence, from 0. Default: all of them. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many constants were replaced. |

> Changed in 1.3.0: Reaches the game's code of a function the loader wraps.

See also: [`rq.ain.patch_int_after`](rq.ain.md#rqainpatch_int_after)

### rq.ain.patch_int_after

```lua
rq.ain.patch_int_after(name, global, from, to, nth_ref, window) -> integer
```

`since 1.3.0`

Replaces the first integer constant `from` that follows a read of a global.

It looks at the `window` instructions after the read, as for the 2 in
`if (◆２倍モード == 1) { x = x * 2; }`. A variable's index is never taken for the constant.

Raises an error for an unknown function or global.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `global` | `string` | The global's name. |
| `from` | `integer` | The value to find. |
| `to` | `integer` | The new value. |
| `nth_ref` *(optional)* | `integer` | Which read of the global in the function, from 0. Default: after every read. |
| `window` *(optional)* | `integer` | How many instructions to look at after the read. Default 8. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many constants were replaced. |

### rq.ain.call

```lua
rq.ain.call(name, ...) -> any
```

`since 0.18.0` `changed 0.26.0` `changed 0.27.0`

Calls any AIN function by its name.

The arguments must be int, bool, float or string, and all of them are needed. A scene command
blocks until it ends, so call it from a callback the game runs, not at the top level of a mod. A
function that reaches a save under this call gets the game's own "save failed" message and nothing
is written; one that reaches a load closes the game with an error. A bad index passed to a game
function is a fatal error in the game, and this call cannot check it.

Raises an error for an unknown name, a wrong number of arguments, a reference or struct argument, a
method (`Class@method`, which needs an object), or `SYS_セーブ実行` and `SYS_ロード実行`.

```lua
local name = rq.ain.call("クエスト_名前", 126)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `...` | `integer\|boolean\|number\|string` | The arguments. |

| Returns | Type | Description |
| --- | --- | --- |
| `result` | `any` | What the function returns; nil for none or a struct. |

> Changed in 0.26.0: Refuses `SYS_セーブ実行` and `SYS_ロード実行`.

> Changed in 0.27.0: A save under the call fails safely.

### rq.ain.hook

```lua
rq.ain.hook(name, opts) -> fun()
```

`since 0.18.0` `changed 0.23.0`

Runs Lua before and after any AIN function.

A method is named `Class@method`. Many hooks may sit on one function. The function does not fire
its hooks again while one of its callbacks runs. A table with neither side does nothing.

```lua
rq.ain.hook("message", { before = function(h)
  h.args[3] = h.args[3]:gsub("Rance", "Ranse")  -- rewrite every line of text
end })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `opts` | `{before?: fun(h:` [`rq.AinHookCtx`](../types/rq.AinHookCtx.md) `), after?: fun(h:` [`rq.AinHookCtx`](../types/rq.AinHookCtx.md) `)}` | The callbacks. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes both sides of this hook. |

> Changed in 0.23.0: Returns a remover.

### rq.ain.method

```lua
rq.ain.method(path, name, ...) -> any
```

`since 2.16.0`

Calls a method of the game on the object a global reaches.

`path` is a global's name, then indexes and field names as `rq.ain.global` takes them, and it must
end on a struct: `{"g_sSystemMenu"}`, `{"g_sCastle", "m_sList"}`. The method's class must be that
struct's (`T_SystemMenu@createButton` on a `T_SystemMenu`). The arguments are as `rq.ain.call`'s:
int, bool, float or string, all of them. The same cautions hold: a method that draws or waits
runs inside this call, and a bad value passed to the game can be a fatal error there.

Raises an error for a path that is not a table, does not start with a known global or does not
reach a struct, an unknown function, a function that is not a method or not the struct's, a wrong
number of arguments, or a reference or struct argument.

```lua
local rows = rq.ain.method({ "g_sSystemMenu", "m_sButton" }, "T_ButtonGroup@getButtonCount")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | `(string\|integer)[]` | The global's name, then indexes and field names to the object. |
| `name` | `string` | The method, `Class@method`. |
| `...` | `integer\|boolean\|number\|string` | The arguments. |

| Returns | Type | Description |
| --- | --- | --- |
| `result` | `any` | What the method returns; nil for none or a struct. |

See also: [`rq.ain.call`](rq.ain.md#rqaincall)

### rq.ain.global

```lua
rq.ain.global(name, ...) -> integer|boolean|number|string
```

`since 0.22.0` `changed 0.24.0`

Reads a game global that holds an int, bool, float or string.

Give the game's own index for an array element, and a field name to go into a struct, mixed as the
game does.

Raises an error for an unknown name or field, an index out of range, a step that does not fit the
value, a whole array or a struct.

```lua
local fa = rq.ain.global("FA", 87)          -- FA[87]
local name = rq.ain.global("Ｑ", 126, "名前")  -- Ｑ[126].名前
```

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The global's name. |
| `...` | `integer\|string` | Indexes and field names. |

| Returns | Type | Description |
| --- | --- | --- |
| `value` | `integer\|boolean\|number\|string` | The value. |

> Changed in 0.24.0: Field names reach into structs.

### rq.ain.set_global

```lua
rq.ain.set_global(name, ...)
```

`since 0.22.0`

Writes a game global, as `rq.ain.global` reads it: `set_global(name, [step, ...,] value)`.

It is the game's own state and goes into the next save, so restore what a test changes.

Raises an error as `rq.ain.global` does.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The global's name. |
| `...` | `any` | Indexes and field names, then the value. |

### rq.ain.global_len

```lua
rq.ain.global_len(name, ...) -> integer
```

`since 0.22.0`

Returns the size of an array global.

Many game arrays start at 1 and leave 0 unused, so the size can be one more than the entries.

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The global's name. |
| `...` | `integer\|string` | Indexes and field names to reach an inner array. |

| Returns | Type | Description |
| --- | --- | --- |
| `size` | `integer` | The number of elements. |

### rq.ain.set_global_len

```lua
rq.ain.set_global_len(name, ...)
```

`since 2.18.0`

Makes an array global longer or shorter, as the game's own `Realloc` does.

Values that fit are kept; new elements are 0, false, an empty string or an empty struct. Only an
array of one dimension. The array is the game's own state and goes into the next save at its new
size, and a save made before brings back the old size, so grow it again where it is used (for
example in a `before` hook). It is there only once the game runs, not while `init.lua` loads.

Raises an error for an unknown name, a value that is not an array, more than one dimension, or a
size below 0 or above 65536.

```lua
if rq.ain.global_len("取得可能スキル") < 145 then rq.ain.set_global_len("取得可能スキル", 145) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `name` | `string` | The global's name. |
| `...` | `integer\|string` | Indexes and field names to reach an inner array, then the new size. |

### rq.ain.skip_msgbox

```lua
rq.ain.skip_msgbox(needle) -> integer
```

`since 0.2.0`

Removes the game's message boxes whose text contains `needle`.

Every `system.MsgBox` call that shows a string holding `needle` is taken out of the code.

Raises an error when the AIN is not loaded.

| Parameter | Type | Description |
| --- | --- | --- |
| `needle` | `string` | Part of the message, in UTF-8. |

| Returns | Type | Description |
| --- | --- | --- |
| `sites` | `integer` | How many calls were taken out. |

### rq.ain.skip_sdl_msgbox

```lua
rq.ain.skip_sdl_msgbox()
```

`since 1.0.0`

Swallows the engine's own error boxes for the TADA and HTTP network checks (`getserverversion`).

### rq.ain.find

```lua
rq.ain.find(needle) -> integer
```

`since 0.2.0` `changed 1.16.1`

Writes the AIN functions whose name contains `needle` to the log.

Each line is `find '<needle>' fno=<number> <name>`, and the name is what `rq.ain.call` and
`rq.ain.hook` take (a method as `Class@method`). The match is on the game's own spelling, so
case and full-width letters count. At most 40 are listed; a longer needle narrows the list.

Raises an error when the AIN is not loaded.

```lua
rq.ain.find("Encount")   -- [rqmod] find 'Encount' fno=... T_Player@checkEncount, ...
```

| Parameter | Type | Description |
| --- | --- | --- |
| `needle` | `string` | Part of a name, in UTF-8. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many were listed. |

> Changed in 1.16.1: Each line also gives the function's name.
