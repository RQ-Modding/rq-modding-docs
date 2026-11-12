# rq.monster

`since 2.36.0` `changed 2.40.0`

The game's list of monsters: read a monster's data, change it each time the game builds it, and
change each enemy a fight builds. A mod's own monsters, enemy groups and models.

The game builds an enemy from its list each time a fight opens (`Ｃ敵登録`), then applies the
world's rules: in worlds 2 and 3 more HP, attack, defense and magic, a tier (×2 to ×7) and a
marked name; race 60 stronger; a boss fight's `strong` ×1.3. `get` and `edit` work on the list's
numbers, before those rules; `on_create` sees what was built, after them.

A mod's monster (`define`) is a game monster's data with the mod's changes, under a number of its
own: 1000 + a hash of its text id, so the same id gives the same number every run and in a save.
A mod's enemy group (`group`) is drawn on a quest's map like the game's (`rq.encounters.set_groups`)
or fought through `rq.battle.start`'s `group`. A save that holds the number of a mod that is no
longer loaded still works: an unknown monster is built as the game's Data-less Ghost, and an
unknown group in an area's list becomes the area's first game group (group 135 when it has none),
each with a line in the log.

```lua
rq.monster.edit(rq.ids.monster.COCKROACH, { name = "Big Cockroach", hp = 200 })
local KING = rq.monster.define({ id = "mymod:king_roach", base = rq.ids.monster.COCKROACH,
  name = "King Roach", hp = 900, level = 20 })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.monster.get`](#rqmonsterget) | Returns a monster's data from the game's list. |
| [`rq.monster.edit`](#rqmonsteredit) | Changes a monster each time the game builds it: in fights, as a familiar, in the game's name lookups and in `rq.monster.get`. |
| [`rq.monster.define`](#rqmonsterdefine) | Defines a monster of the mod's own, on a game monster's data. |
| [`rq.monster.group`](#rqmonstergroup) | Defines an enemy group of the mod's own. |
| [`rq.monster.models`](#rqmonstermodels) | Lists the game's model table, with the models mods made after it. |
| [`rq.monster.model`](#rqmonstermodel) | Makes a model of the game's at another size or place, for a monster's `model` field. |

### rq.monster.get

```lua
rq.monster.get(no) -> rq.Monster|nil
```

`since 2.36.0` `changed 2.40.0`

Returns a monster's data from the game's list.

The numbers are the list's, with every mod's `rq.monster.edit` applied, before the world's rules
and the fight's. Monsters 491 to 495 give what the current custom name builds (Kaito (True),
Prototype #1 and the others a scene names).

It builds the monster in a slot the game never uses (9) and empties it after; it draws no random
number for the world's tiers. It works anywhere a save is loaded, in a fight too.

Raises an error for a number that is not whole and 1 or more, a text id no mod defined, or before
the game runs.

```lua
local m = rq.monster.get(rq.ids.monster.COCKROACH)
rq.log(m.name, m.hp, m.atk, #m.skills, m.kills)
local king = rq.monster.get("mymod:king_roach")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The monster number (`rq.ids.monster`), or a mod's monster's text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `data` | [`rq.Monster`](../types/rq.Monster.md) `\|nil` | nil for a number the game's list does not have and no mod defined. |

> Changed in 2.40.0: A mod's monster, by number or text id; `id`, `base`, `kills` and `weak_known`.

### rq.monster.edit

```lua
rq.monster.edit(no, patch)
```

`since 2.36.0` `changed 2.40.0`

Changes a monster each time the game builds it: in fights, as a familiar, in the game's name
lookups and in `rq.monster.get`.

The patch replaces the list's numbers before the game applies the world's rules, so the world's
tiers, race 60 and a boss fight's `strong` scale the new numbers as they scale the game's. The
level and the lines are written after the build.

Each mod keeps one patch per monster: calling again replaces that mod's patch, and `nil` removes
it. The patches apply in load order, a later mod's field over an earlier one's. A change applies
from the next build; an enemy already in a fight keeps its numbers. A skill's `chance` changes how
often the game draws it in every fight; to choose a skill or a target turn by turn, use
`rq.battle.on_choose`.

A mod's monster (`rq.monster.define`) takes edits too, its own number's: an edit of the game
monster it is built on does not reach it.

`drops`: after a won fight with no item yet and room in the quest storage, each enemy defeated,
in rank order, rolls its drops in order, and the first that rolls is the fight's one item. It is
rolled before every mod's `rq.battle.on_end`, so `rq.battle.get_drop` sees it and `set_drop` can
change it. A fight that already has an item (a capture, a mod's `set_drop` in `on_start`) rolls
none; a drop that rolls takes the place of the game's own later drops (a signboard, the rare
groups). The last patch with `drops` in load order wins, over the definition's.

Raises an error for an unknown monster, an unknown field, a value of the wrong kind, a skill
position outside 1 to 5, or `drops` that are not a list of up to 8 items with a chance from 1 to
100.

```lua
rq.monster.edit(rq.ids.monster.COCKROACH, {
  name = "Big Cockroach", hp = 200,
  skills = { [1] = { chance = 50 }, [2] = false },
  lines = { attack = "Skitter!" },
  drops = { { item = "mymod:shell", chance = 25 } },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | The monster number (`rq.ids.monster`), or a mod's monster's text id. |
| `patch` | [`rq.MonsterEdit`](../types/rq.MonsterEdit.md) `\|nil` | The fields to change; nil removes this mod's patch. |

> Changed in 2.40.0: A mod's monster, by number or text id; `drops`.

See also: [`rq.battle.on_choose`](rq.battle.md#rqbattleon_choose)

### rq.monster.define

```lua
rq.monster.define(def) -> integer
```

`since 2.40.0`

Defines a monster of the mod's own, on a game monster's data.

The monster is `base` with the fields given, as `rq.monster.edit` would change it, under its own
number: 1000 + an FNV-1a hash of `id` modulo 9000, as an item's text id (`rq.item.define`), so it
is the same every run. The game builds it as it builds `base` (its look, its motions, the world's
rules) and counts it as its own: its kills and whether its weak point is known are kept in the
save under its id (`rq.monster.get`'s `kills` and `weak_known`). It fights through
`rq.battle.start`'s `enemies` (by number or id), a group of the mod's (`rq.monster.group`), or as
a familiar: an item with `subtype = 20` whose first effect is its number. An edit of `base` by
any mod does not reach it; an edit of its own number does.

`capture` lets the game's capture skills catch it under the game's own rules (its HP, the chance,
the quest storage not full, not in a boss fight), giving the item and showing the scene. Without
`capture` a capture always fails, as on a monster the game has no item for. `drops` are rolled as
`rq.monster.edit` says.

The mod that defined an id may define it again, which replaces the definition from the next
build. A mod's monster that is not loaded any more (a save that holds its number) is built as
the game's Data-less Ghost, with a line in the log.

Raises an error for a `def` that is not a table, an `id` that is not a text, a `base` that is not
a game monster, an unknown field, a value of the wrong kind (as `rq.monster.edit`), a bad
`capture`, an id whose number another id has, or an id another mod defined.

```lua
local CAN = rq.ids.monster.CAN_CAN
local JELLY = rq.monster.define({ id = "mymod:jelly", base = CAN, name = "Blue Jelly", hp = 300,
  lines = { wait = "Wobble." },
  drops = { { item = "mymod:jelly_drop", chance = 30 } },
  capture = { item = "mymod:jelly_familiar", cg = rq.image.add("mymod:jelly_cg", "cg/jelly.png"),
    text = "【Blue Jelly】$\"You caught me...\"" },
})
rq.item.define({ id = "mymod:jelly_familiar", name = "Blue Jelly", type = "item", subtype = 20,
  icon = 6500, effects = { { kind = 0, value = JELLY }, { kind = 0, value = 1 }, { kind = 0, value = 100 } } })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.MonsterDef`](../types/rq.MonsterDef.md) | The game monster to start from and the changes. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The monster's number, 1000 to 9999. |

### rq.monster.group

```lua
rq.monster.group(def) -> integer
```

`since 2.40.0`

Defines an enemy group of the mod's own.

A group is what the game draws on a quest's map: a line-up of up to five enemies, the fight's EXP
and its rank. Put it in an area's list with `rq.encounters.set_groups`, or fight it with
`rq.battle.start`'s `group`. Its number is 1000 + an FNV-1a hash of `id` modulo 9000.

The line-up is drawn as the game draws one: a number from 1 to 5, drawn again once when it is the
last fight's, picks `lineups[(n - 1) % #lineups + 1]`; an enemy standing on the map takes the 6th
one time in 3. So 5 line-ups are drawn evenly, and the 6th only for an enemy standing on the map.
The game still thins a line-up of 4 or more while its encounter flag says so, and plays its music.

The mod that defined an id may define it again, which replaces it. An area whose list holds a
group no mod defines (a save whose mod is gone) draws the area's first game group in its place,
group 135 when it has none, with a line in the log.

Raises an error for a `def` that is not a table, an `id` that is not a text, an unknown field, a
`name` that is not a text, an `exp` or `rank` that is not whole and 0 or more, `lineups` that are
not a list of 1 to 6 lists, a rank outside 1 to 5, a monster number the game's list does not have
(below 1000), a line-up with no monster, an id whose number another id has, or an id another mod
defined.

```lua
local R = rq.ids.monster.COCKROACH
local ROACHES = rq.monster.group({ id = "mymod:roaches", name = "Roach Swarm", exp = 120, rank = 5,
  lineups = { { 0, R, 0 }, { R, R }, { R, "mymod:king_roach", R } } })
rq.dungeon.on_area(function() rq.encounters.set_groups({ ROACHES, 12 }) end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.MonsterGroup`](../types/rq.MonsterGroup.md) | The group. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The group's number, 1000 to 9999. |

### rq.monster.models

```lua
rq.monster.models() -> rq.ModelInfo[]
```

`since 2.40.0`

Lists the game's model table, with the models mods made after it.

Raises an error when the table cannot be read.

```lua
for _, m in ipairs(rq.monster.models()) do rq.log(m.model, m.name, m.scale) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `models` | [`rq.ModelInfo`](../types/rq.ModelInfo.md) `[]` | In the table's order. |

### rq.monster.model

```lua
rq.monster.model(def) -> integer
```

`since 2.40.0`

Makes a model of the game's at another size or place, for a monster's `model` field.

It adds an entry after the game's model table, with the base's 3D file and motions, and returns its
number; the table is built again with it each time the game reads it. The number comes from the
order of the calls in a run, so give it to a monster (`rq.monster.define` or `edit`) at the top
level of the mod and do not keep it in a save. The mod that made an id may call again, which
changes the same model.

Raises an error for a `def` that is not a table, an `id` that is not a text, an unknown field, a
`base` that is not a game model, a `scale` that is not above 0 and at most 50, an offset that is
not a number, an id another mod made, or when the table cannot be read.

```lua
local ROACH_MODEL = 100122  -- rq.monster.get(rq.ids.monster.COCKROACH).model
local BIG = rq.monster.model({ id = "mymod:big_roach", base = ROACH_MODEL, scale = 2 })
rq.monster.define({ id = "mymod:big_roach", base = rq.ids.monster.COCKROACH, name = "Big Roach",
  model = BIG, hp = 1200 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.ModelDef`](../types/rq.ModelDef.md) | The base model and its size and place. |

| Returns | Type | Description |
| --- | --- | --- |
| `model` | `integer` | The model number. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.monster.on_create`](#rqmonsteron_create) | Calls `fn` after the game builds each enemy of a fight and the party's familiar, before the fight opens. |

### rq.monster.on_create

```lua
rq.monster.on_create(fn) -> fun()
```

`since 2.36.0` `changed 2.40.0`

Calls `fn` after the game builds each enemy of a fight and the party's familiar, before the fight
opens.

It runs for the enemies of every fight (ranks 1 to 5, from `ＰＴＢ登録`) and for the familiar of
the held item (`familiar` true). Not for `rq.monster.get` nor the game's name lookups.

The writable fields hold the built numbers, after the world's rules. Callbacks run in load order,
each reading what the ones before wrote; what they leave is written to the slot once after the
last one. A number is rounded down and kept from 0. After it the game still runs its own steps:
a boss fight's `double_hp`, `rq.battle.start`'s `names`, the familiar's growth and speed cap.

An error in a callback is logged once for each new error text; what it wrote before the error
stays.

```lua
--- Bosses a fifth stronger
rq.monster.on_create(function(ctx)
  if ctx.familiar or ctx.fight_rank ~= 2 then return end
  ctx.hp = ctx.hp * 1.2
  ctx.atk = ctx.atk * 1.2
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.MonsterCreateCtx`](../types/rq.MonsterCreateCtx.md) `)` | Reads and changes the enemy. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.40.0: `ctx.id` for a mod's monster.
