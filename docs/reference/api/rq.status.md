# rq.status

`since 2.2.0` `changed 2.3.0`

Battle states made by mods, such as a burn, a bleed, a regeneration, a freeze or a weaken, that
live beside the game's poison, stun and ▲▼, in one registry every mod shares.

A mod defines a state once (`define`, in `init.lua`) and adds it to a character in a fight
(`add`, often from `rq.battle.on_hit`). Any mod can add, read, cure or remove any mod's state by
its id. A state lives only in the fight: it goes when the fight ends, when its bearer goes down
(unless `keep_on_down`), when its turns run out, when it is cured, or when a mod removes it.

**Turns** are the bearer's own: `on_turn` runs at each of the bearer's turn starts, and the
count goes down at the end of each of the bearer's turns. A state added during its bearer's own
turn skips that turn's countdown, so a 3-turn burn an enemy puts on ticks three times, and a
2-turn buff a character gives itself lasts through its next two actions.

**Cures.** The game's cure skills cure mod states too, as the game names them by number: Status
Restore (227), Encourage (237) and Self-Healing (220), which clear every state of the game,
cure each state whose `cured_by` has `"all"`; First Aid (218 and 219), which cures only poison,
cures each state whose `cured_by` has `"poison"`. `cured_by` defaults to `{ "all" }` for a bad
state and `{}` for a good one. A skill number in `cured_by` makes that support skill cure it. A
mod's own medicine calls `rq.status.cure`, by id, by tag or by kind. The game's items in a fight
are skills too, and none of them cures a state.

**On the card** a state with an `icon` shows as a buff (`rq.battle.set_buff`), with the turns
left as its text, or its stacks when it has no turns. A character holds up to 8 buffs, the
mods' own and the states' together.

**Lethal.** A state's damage stops at 1 HP, as poison's does, unless its definition has
`lethal = true`: then `ctx:damage` in its `on_turn` may down the bearer, with the state's
`source` as the killer (see `BattleTurnCtx:damage`). Once the bearer is down, the states after
it do not tick that turn.

```lua
local BURN_ICON = rq.image.add("burn", "burn.png", { fit = "contain", w = 56, h = 56 })
rq.status.define("mymod:burn", {
  name = "Burn", turns = 3, tags = { "fire" }, icon = { icon = BURN_ICON },
  on_turn = function(s, ctx)
    ctx:damage(math.max(1, rq.chara.get(s.iic).hp_max * s.power // 100))
    ctx:log(" " .. rq.chara.get(s.iic).short .. " burns.")
  end,
})
rq.battle.on_hit(function(ctx)
  if ctx.skill == FIRE_SLASH and not ctx.missed and not ctx.downed then
    rq.status.add(ctx.defender, "mymod:burn", { power = 5, source = ctx.attacker })
    ctx:log(" (Burn)")
  end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.status.define`](#rqstatusdefine) | Defines a state that every mod can then add. |
| [`rq.status.info`](#rqstatusinfo) | Returns what is known of a definition, for any mod. |
| [`rq.status.add`](#rqstatusadd) | Puts a state on a character in a fight, or adds to it. |
| [`rq.status.get`](#rqstatusget) | Returns a character's instance of a state. |
| [`rq.status.list`](#rqstatuslist) | Returns every state on a character, in the order they came. |
| [`rq.status.remove`](#rqstatusremove) | Removes a state from a character, with the reason "removed". |
| [`rq.status.cure`](#rqstatuscure) | Cures states of a character, with the reason "cured": a mod's medicine. |

### rq.status.define

```lua
rq.status.define(id, def) -> string
```

`since 2.2.0`

Defines a state that every mod can then add.

Call it in `init.lua`. The first definition with an `icon` installs the buff marks
(`rq.battle.install_flame`), and the first with `physical` or `accuracy` the combat hooks
(`rq.combat.install`).

Raises an error for an id that is not `"<mod>:<name>"` (letters, digits, `_` and `-` on each side),
an id already defined by any mod, or a field of the wrong type or range.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The state's id, `"<mod>:<name>"`, such as `"mymod:burn"`. |
| `def` | [`rq.StatusDef`](../types/rq.StatusDef.md) | The definition. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string` | The id. |

### rq.status.info

```lua
rq.status.info(id) -> rq.StatusInfo|nil
```

`since 2.2.0`

Returns what is known of a definition, for any mod.

Raises an error for an id that is not `"<mod>:<name>"`.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The state's id. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.StatusInfo`](../types/rq.StatusInfo.md) `\|nil` | A copy, or nil when no mod defined it. |

### rq.status.add

```lua
rq.status.add(iic, id, opts) -> rq.StatusInstance|nil, boolean|nil
```

`since 2.2.0`

Puts a state on a character in a fight, or adds to it.

When the character already has it, the definition's `stack` says what changes, and `power` and
`source` are set again when given. Not in a fight, or on someone down, it does nothing.

Raises an error for an id no mod defined, or an option of the wrong type or range.

```lua
local s, new = rq.status.add(target, "mymod:burn", { turns = 2, power = 5, source = user })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot, ally or enemy. |
| `id` | `string` | The state's id. |
| `opts` *(optional)* | `{turns?: integer, stacks?: integer, power?: number, source?: integer, data?: table}` | `turns`: in place of the definition's, 1 or more. `stacks`: how many to add, default 1. `power`, `source`, `data`: stored on the instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `s` | [`rq.StatusInstance`](../types/rq.StatusInstance.md) `\|nil` | The instance, or nil when nothing was put on. |
| `new` | `boolean\|nil` | true when the character did not have it before. |

### rq.status.get

```lua
rq.status.get(iic, id) -> rq.StatusInstance|nil
```

`since 2.2.0`

Returns a character's instance of a state.

Raises an error for an id no mod defined.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `id` | `string` | The state's id. |

| Returns | Type | Description |
| --- | --- | --- |
| `s` | [`rq.StatusInstance`](../types/rq.StatusInstance.md) `\|nil` | The live instance, or nil. |

### rq.status.list

```lua
rq.status.list(iic) -> rq.StatusInstance[]
```

`since 2.2.0`

Returns every state on a character, in the order they came.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `list` | [`rq.StatusInstance`](../types/rq.StatusInstance.md) `[]` | The live instances; empty when none. |

### rq.status.remove

```lua
rq.status.remove(iic, id) -> boolean
```

`since 2.2.0`

Removes a state from a character, with the reason "removed".

Raises an error for an id no mod defined.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `id` | `string` | The state's id. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when the character did not have it. |

### rq.status.cure

```lua
rq.status.cure(iic, what) -> integer
```

`since 2.2.0`

Cures states of a character, with the reason "cured": a mod's medicine.

It takes no notice of `cured_by`, which is for the game's skills.

Raises an error for anything else as `what`, or an id no mod defined.

```lua
rq.status.cure(target, { tag = "fire" })  -- a burn salve
rq.status.cure(target, "bad")             -- a cure-all of the mod's own
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `what` | `string\|{tag: string}` | A state's id, "bad", "good", "all", or `{ tag = name }`. |

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | How many states went. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.status.on_add`](#rqstatuson_add) | Calls `fn` each time any mod's state is put on someone who did not have it. |
| [`rq.status.on_remove`](#rqstatuson_remove) | Calls `fn` each time any mod's state goes from someone. |

### rq.status.on_add

```lua
rq.status.on_add(fn) -> fun()
```

`since 2.2.0`

Calls `fn` each time any mod's state is put on someone who did not have it.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(s:` [`rq.StatusInstance`](../types/rq.StatusInstance.md) `)` | Gets the new instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.status.on_remove

```lua
rq.status.on_remove(fn) -> fun()
```

`since 2.2.0`

Calls `fn` each time any mod's state goes from someone.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(s:` [`rq.StatusInstance`](../types/rq.StatusInstance.md) `, reason: "expired"\|"cured"\|"down"\|"removed"\|"fight_end")` | Gets the instance and why it went. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
