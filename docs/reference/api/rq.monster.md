# rq.monster

`since 2.36.0`

The game's list of monsters: read a monster's data, change it each time the game builds it, and
change each enemy a fight builds.

The game builds an enemy from its list each time a fight opens (`Ｃ敵登録`), then applies the
world's rules: in worlds 2 and 3 more HP, attack, defense and magic, a tier (×2 to ×7) and a
marked name; race 60 stronger; a boss fight's `strong` ×1.3. `get` and `edit` work on the list's
numbers, before those rules; `on_create` sees what was built, after them.

```lua
rq.monster.edit(rq.ids.monster.COCKROACH, { name = "Big Cockroach", hp = 200 })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.monster.get`](#rqmonsterget) | Returns a monster's data from the game's list. |
| [`rq.monster.edit`](#rqmonsteredit) | Changes a monster each time the game builds it: in fights, as a familiar, in the game's name lookups and in `rq.monster.get`. |

### rq.monster.get

```lua
rq.monster.get(no) -> rq.Monster|nil
```

`since 2.36.0`

Returns a monster's data from the game's list.

The numbers are the list's, with every mod's `rq.monster.edit` applied, before the world's rules
and the fight's. Monsters 491 to 495 give what the current custom name builds (Kaito (True),
Prototype #1 and the others a scene names).

It builds the monster in a slot the game never uses (9) and empties it after; it draws no random
number for the world's tiers. It works anywhere a save is loaded, in a fight too.

Raises an error for a number that is not whole and 1 or more, or before the game runs.

```lua
local m = rq.monster.get(rq.ids.monster.COCKROACH)
rq.log(m.name, m.hp, m.atk, #m.skills)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The monster number (`rq.ids.monster`). |

| Returns | Type | Description |
| --- | --- | --- |
| `data` | [`rq.Monster`](../types/rq.Monster.md) `\|nil` | nil for a number the game's list does not have. |

### rq.monster.edit

```lua
rq.monster.edit(no, patch)
```

`since 2.36.0`

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

Raises an error for an unknown monster, an unknown field, a value of the wrong kind, or a skill
position outside 1 to 5.

```lua
rq.monster.edit(rq.ids.monster.COCKROACH, {
  name = "Big Cockroach", hp = 200,
  skills = { [1] = { chance = 50 }, [2] = false },
  lines = { attack = "Skitter!" },
})
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The monster number (`rq.ids.monster`). |
| `patch` | [`rq.MonsterEdit`](../types/rq.MonsterEdit.md) `\|nil` | The fields to change; nil removes this mod's patch. |

See also: [`rq.battle.on_choose`](rq.battle.md#rqbattleon_choose)

## Events

| Name | Summary |
| --- | --- |
| [`rq.monster.on_create`](#rqmonsteron_create) | Calls `fn` after the game builds each enemy of a fight and the party's familiar, before the fight opens. |

### rq.monster.on_create

```lua
rq.monster.on_create(fn) -> fun()
```

`since 2.36.0`

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
