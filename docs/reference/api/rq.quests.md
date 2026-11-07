# rq.quests

`since 0.2.0`

Lists the quests and follows them: clears, endings, quest moments and state.

`rq.quests()` and `rq.quests.list()` list the quests that have a name, up to 512. `state`,
`set_state`, `unlock` and `start` raise an error for a quest number the game does not have. Characters recruited and quests unlocked
from `on_clear` show on the victory screen with the game's own animation, as the game does for
Tomato. Dialogue inside a quest is quest script and is not part of these hooks.

```lua
rq.chara.define{ id = "mymod:alice", name = "Alice", face = "faces/alice.png", class = 5 }
rq.quests.on_clear(function(ctx)
  if ctx.quest == 126 and ctx.first then
    rq.chara.recruit("mymod:alice", { state = 2 }) -- shown on the victory screen
    rq.quests.unlock(207)
  end
end)
```

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `list` | `fun():` [`rq.Quest`](../types/rq.Quest.md) `[]` | Lists the quests, as `rq.quests()` does. |

## Functions

| Name | Summary |
| --- | --- |
| [`rq.quests.state`](#rqquestsstate) | Returns a quest's state. |
| [`rq.quests.set_state`](#rqquestsset_state) | Sets a quest's state, through the game's `Ｑ状態`. |
| [`rq.quests.unlock`](#rqquestsunlock) | Makes a locked quest available. |
| [`rq.quests.current`](#rqquestscurrent) | Returns the quest being played. |
| [`rq.quests.start`](#rqquestsstart) | Starts a quest through the game's own flow, with no click on the quest list. |
| [`rq.quests.new_this_run`](#rqquestsnew_this_run) | Returns what the victory screen will show as new. |

### rq.quests.state

```lua
rq.quests.state(no) -> integer
```

`since 0.7.0`

Returns a quest's state.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |

### rq.quests.set_state

```lua
rq.quests.set_state(no, state)
```

`since 0.7.0`

Sets a quest's state, through the game's `Ｑ状態`.

State 2 also records a first clear. Raises an error for a state other than 0, 1 or 2.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |

See also: [`rq.quests.unlock`](rq.quests.md#rqquestsunlock)

### rq.quests.unlock

```lua
rq.quests.unlock(no) -> boolean
```

`since 0.7.0`

Makes a locked quest available.

It sets state 1 only when the quest is locked. A quest opened this way joins the "new quests" list
on the victory screen.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |

| Returns | Type | Description |
| --- | --- | --- |
| `unlocked` | `boolean` | false when the quest was not locked. |

### rq.quests.current

```lua
rq.quests.current() -> integer
```

`since 0.18.0`

Returns the quest being played.

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number, or 0 in town. |

### rq.quests.start

```lua
rq.quests.start(no)
```

`since 0.23.0`

Starts a quest through the game's own flow, with no click on the quest list.

It returns at once; the game moves on its next update, and `rq.quests.current()` gives the number
once the quest started. Any join dialog or scene of the quest plays as usual, and like a real start
it autosaves and counts as a try. A locked quest starts too, including the game's debug entries
(quest 10 goes straight back to town).

Raises an error for a value that is not a whole number, an unknown quest, a quest this party cannot
take, while a quest runs or another is starting, and on any screen but the hub or the quest list.
The game can still refuse after that with its own message, at 2500 items or more or when its Alice
event is due.

```lua
if rq.ui.get().screen == "hub" then rq.quests.start(126) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |

### rq.quests.new_this_run

```lua
rq.quests.new_this_run() -> rq.NewThisRun
```

`since 0.7.0`

Returns what the victory screen will show as new.

Recruiting a character and unlocking a quest add to these lists; the game empties both when a quest
ends.

| Returns | Type | Description |
| --- | --- | --- |
| `new` | [`rq.NewThisRun`](../types/rq.NewThisRun.md) | The new characters and quests. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.quests.on_clear`](#rqquestson_clear) | Registers a function that runs when a quest is cleared. |
| [`rq.quests.on_end`](#rqquestson_end) | Registers a function that runs when a quest ends, however it ends. |
| [`rq.quests.on_event`](#rqquestson_event) | Registers a function that runs before the game handles a quest moment. |
| [`rq.quests.on_event_after`](#rqquestson_event_after) | Registers a function that runs after the game handled a quest moment. |

### rq.quests.on_clear

```lua
rq.quests.on_clear(fn) -> fun()
```

`since 0.7.0` `changed 0.23.0`

Registers a function that runs when a quest is cleared.

It runs only for a clean clear, not for an abandon, an escape or a defeat, at the end of the game's
`クエスト終了処理／クリアフラグ` (wrapped the first time this is used). Characters recruited with
`rq.chara.recruit` and quests opened with `rq.quests.unlock` in the callback join the game's "new
this run" lists, so the victory screen shows them. Up to 16 callbacks; an error in one is written to
the log.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.QuestClearCtx`](../types/rq.QuestClearCtx.md) `)` | Gets the cleared quest. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

See also: [`rq.quests.on_end`](rq.quests.md#rqquestson_end)

### rq.quests.on_end

```lua
rq.quests.on_end(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0`

Registers a function that runs when a quest ends, however it ends.

It runs at the start of the game's `クエスト終了処理` (wrapped the first time this is used). Up to 16
callbacks; an error in one is written to the log.

```lua
rq.quests.on_end(function(ctx)
  if not ctx.cleared then rq.log("quest", ctx.quest, "ended with", ctx.result) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.QuestEndCtx`](../types/rq.QuestEndCtx.md) `)` | Gets the quest and how it ended. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

See also: [`rq.quests.on_clear`](rq.quests.md#rqquestson_clear)

### rq.quests.on_event

```lua
rq.quests.on_event(fn) -> fun()
```

`since 0.18.0` `changed 0.23.0`

Registers a function that runs before the game handles a quest moment.

It hooks the game's `クエスト処理`. Return nothing to let the game handle it, or a number to skip the
game's handling: 0 continues the quest, other values end it (1 returns to town). Do not play a scene
on `map_load`; the map is not ready.

```lua
rq.quests.on_event(function(ev)
  if ev.kind == "chest" then rq.log("chest at event", ev.no) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.QuestEvent`](../types/rq.QuestEvent.md) `): integer\|nil` | Returns nil, or the result that replaces the game's handling. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

See also: [`rq.quests.on_event_after`](rq.quests.md#rqquestson_event_after)

### rq.quests.on_event_after

```lua
rq.quests.on_event_after(fn) -> fun()
```

`since 0.18.0` `changed 0.23.0`

Registers a function that runs after the game handled a quest moment.

`ev.result` is what the game returned. Return a number to change it, or nothing to keep it.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.QuestEvent`](../types/rq.QuestEvent.md) `): integer\|nil` | Returns nil, or the result to use instead. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

See also: [`rq.quests.on_event`](rq.quests.md#rqquestson_event)
