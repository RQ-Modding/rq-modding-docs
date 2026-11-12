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
| [`rq.quests.can_take`](#rqquestscan_take) | Returns whether a quest can be taken now: the game's `クエスト_有効`, which lights the quest list's Take button. |
| [`rq.quests.refresh`](#rqquestsrefresh) | Draws the quest list again, with the chosen quest's buttons as the game draws them. |
| [`rq.quests.get`](#rqquestsget) | Returns a quest's data, as the quest list shows it. |
| [`rq.quests.edit`](#rqquestsedit) | Changes a quest's name, text, place, difficulty or conditions while the mod runs. |
| [`rq.quests.run`](#rqquestsrun) | Returns the counters, bonuses and rules of the quest being played. |
| [`rq.quests.set_run`](#rqquestsset_run) | Changes the counters, bonuses and rules of the quest being played. |

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

`since 0.7.0` `changed 2.23.0`

Sets a quest's state, through the game's `Ｑ状態`.

State 2 also records a first clear. State 1 on a locked quest adds it to the "new quests" list of
the victory screen; on a quest already available or cleared, the game's `Ｑ状態` changes nothing, so
the call writes the state itself (a cleared quest can be taken again). Raises an error for a state
other than 0, 1 or 2.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |
| `state` | `integer` | 0 locked, 1 available, 2 cleared. |

> Changed in 2.23.0: State 1 on a cleared quest is written; before, the call did nothing there.

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

### rq.quests.can_take

```lua
rq.quests.can_take(no) -> boolean
```

`since 2.23.0` `changed 2.39.0`

Returns whether a quest can be taken now: the game's `クエスト_有効`, which lights the quest list's
Take button.

It is true when the party has at least one member, the quest exists and its conditions to take
part are met (an item it needs, a character, and the like). A mod's own condition
(`rq.quests.edit`'s `condition`) is asked first.

Raises an error when `no` is not a quest number.

```lua
if not rq.quests.can_take(80) then rq.log("Gem Lady needs a Jewel") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when Take would be lit for it. |

> Changed in 2.39.0: Asks the mods' own conditions (`rq.quests.edit`) first.

### rq.quests.refresh

```lua
rq.quests.refresh() -> boolean
```

`since 2.23.0` `changed 2.39.0`

Draws the quest list again, with the chosen quest's buttons as the game draws them.

After a change that the list shows (an item a quest needs, a state), the rows are made again and
the chosen quest's Take is lit or greyed by `rq.quests.can_take`, as the game does after the
favorite button (`T_Quest::remakeList`, then `T_Quest::lock`). With no quest chosen, only the rows.
The mods' own conditions (`rq.quests.edit`'s `condition`) are asked again first.

```lua
rq.item.remove(jewel)
rq.quests.refresh() -- Take greys if that was the last one
```

| Returns | Type | Description |
| --- | --- | --- |
| `done` | `boolean` | false when the quest list is not open. |

> Changed in 2.39.0: Asks the mods' own conditions (`rq.quests.edit`) again first.

### rq.quests.get

```lua
rq.quests.get(no) -> rq.QuestData
```

`since 2.39.0`

Returns a quest's data, as the quest list shows it.

It reads the game's data with every mod's `rq.quests.edit` on it. `rq.quests()` stays the short list
of every quest.

Raises an error for a number the game does not have (no quest has it, or it has no name), also
before a save is loaded.

```lua
local q = rq.quests.get(126)
rq.log(q.name, q.difficulty, q.fame, #q.conditions, q.can_take)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |

| Returns | Type | Description |
| --- | --- | --- |
| `data` | [`rq.QuestData`](../types/rq.QuestData.md) | The quest's data. |

See also: [`rq.quests.edit`](rq.quests.md#rqquestsedit)

### rq.quests.edit

```lua
rq.quests.edit(no, patch)
```

`since 2.39.0`

Changes a quest's name, text, place, difficulty or conditions while the mod runs.

The game writes every quest's data again when a game starts, after each load and at a world
transfer (`Ｑ起動時登録`), and the story's special conditions each time the quest menu opens
(`Ｑ特殊な条件の処理`). The patch is put back on top after each, and at once when the call is made
with a save loaded; made before (at a mod's top level), it applies when the game first writes its
data. Nothing stays in the save: without the mod, the game's next writing brings its own data back.

Each mod keeps one patch per quest: calling again replaces that mod's patch, and `nil` removes it,
bringing the game's data back. The patches apply in load order, a later mod's field over an
earlier one's. The fame a clear gives is not patched, since the game halves it after each clear;
to change what a run gives, use `rq.quests.set_run{ fame = ... }`.

A mod's own condition (`condition`): `ok(no)` is asked when the quest menu opens, at
`rq.quests.refresh` and at `rq.quests.can_take`. While it is not met, the quest takes the game's
special condition: the first free condition slot holds it, the quest list greys Take and shows
`text`. With the game's special condition already there, or the conditions of several mods, the
texts are joined with " / ". An error in `ok` is logged and counts as met. With the quest list open,
call `rq.quests.refresh` to show a change.

Raises an error for an unknown quest (once a save is loaded), an unknown field, a value of the
wrong kind or too long, more than 3 conditions, or `condition` with 3 `conditions`.

```lua
-- A harder quest that needs Kanami in the party and the three shrines found.
local function shrines() return rq.store.get("shrines") or 0 end
rq.quests.edit(126, {
  difficulty = 40,
  conditions = { { kind = "member", chara = rq.ids.chara.KANAMI_KENTOU } },
  condition = { text = "Find the three shrines", ok = function() return shrines() >= 3 end },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The quest number. |
| `patch` | [`rq.QuestEdit`](../types/rq.QuestEdit.md) `\|nil` | The fields to change; nil removes this mod's patch. |

See also: [`rq.quests.get`](rq.quests.md#rqquestsget)

### rq.quests.run

```lua
rq.quests.run() -> rq.QuestRun|nil
```

`since 2.39.0`

Returns the counters, bonuses and rules of the quest being played.

```lua
local run = rq.quests.run()
if run and run.bonuses.feats then
  rq.log("achievements", run.bonuses.feats.count, "of", run.bonuses.feats.max)
end
```

| Returns | Type | Description |
| --- | --- | --- |
| `run` | [`rq.QuestRun`](../types/rq.QuestRun.md) `\|nil` | nil in town. |

See also: [`rq.quests.set_run`](rq.quests.md#rqquestsset_run)

### rq.quests.set_run

```lua
rq.quests.set_run(fields)
```

`since 2.39.0`

Changes the counters, bonuses and rules of the quest being played.

The quest panel on the map is drawn again: the EXP bonus, the bonuses, AREA DISPLAY and the PARTY
button follow. A bonus that reaches its maximum shows the game's flash on the map, as a level-up or
a placed enemy does. The progress, the fights, the EXP total, the fee and the gold base are read
only: the game's systems make them. The quest's script sets its rules at the start and in some
areas, so a rule written early can be written again by the quest; set it from `rq.dungeon.on_area`
to keep it.

Raises an error outside a quest, for a field it does not write, or a value out of range.

```lua
-- Every quest gives twice the fame and starts with 10 more EXP bonus.
rq.quests.on_event_after(function(ev)
  if ev.kind ~= "start" then return end
  local run = rq.quests.run()
  rq.quests.set_run({ fame = run.fame * 2, exp_bonus = math.min(50, run.exp_bonus + 10) })
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fields` | [`rq.QuestRunEdit`](../types/rq.QuestRunEdit.md) | The fields to write. |

See also: [`rq.quests.run`](rq.quests.md#rqquestsrun)

## Events

| Name | Summary |
| --- | --- |
| [`rq.quests.on_clear`](#rqquestson_clear) | Registers a function that runs when a quest is cleared. |
| [`rq.quests.on_end`](#rqquestson_end) | Registers a function that runs when a quest ends, however it ends. |
| [`rq.quests.on_event`](#rqquestson_event) | Registers a function that runs before the game handles a quest moment. |
| [`rq.quests.on_event_after`](#rqquestson_event_after) | Registers a function that runs after the game handled a quest moment. |
| [`rq.quests.on_take`](#rqquestson_take) | Registers a function that runs when the player presses Take on the quest list. |

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
on `map_load`; the map is not ready. A mod's own map objects (`rq.dungeon.on_object`) do not reach it.

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

`ev.result` is what the game returned. Return a number to change it, or nothing to keep it. A mod's
own map objects (`rq.dungeon.on_object`) do not reach it.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.QuestEvent`](../types/rq.QuestEvent.md) `): integer\|nil` | Returns nil, or the result to use instead. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

See also: [`rq.quests.on_event`](rq.quests.md#rqquestson_event)

### rq.quests.on_take

```lua
rq.quests.on_take(fn) -> fun()
```

`since 2.23.0`

Registers a function that runs when the player presses Take on the quest list.

It runs before the game's "Take Quest?" question and before the autosave that comes with a Yes.
The callback may wait, for example on `rq.ui.ask` or `rq.ui.confirm`. What it returns decides:
- nil: the game goes on as usual, with its question unless the player turned it off.
- true: the quest is taken, with no question.
- false: the quest is not taken, and the list stays.

Callbacks run in the order they were added (mods in load order); the first one that returns
something other than nil decides, and the rest do not run. An error is logged and counts as nil.
Only the quest list's Take: not `rq.quests.start`, nor a quest the game starts by itself.

```lua
rq.quests.on_take(function(ctx)
  if ctx.quest ~= 80 then return nil end
  return rq.ui.confirm("Pay 100 gold to take it?") == true
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.TakeContext`](../types/rq.TakeContext.md) `): boolean\|nil` | nil for the game's way, true to take the quest, false not to. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
