# Combat rules

Loader 2.37.0 lets a mod change the rules of a fight. A mod can set the chance of a stun, a poison,
a counter or an escape, and how much HP a heal gives. It can also change the speeds the turn list is
built from, the list itself, the ambush, and each line of the battle log. Every mod's callbacks run
in turn on the same fight, and the game shows the result as its own: the forecast, the log, the
numbers and the turn icons.

## A chance: stun, poison, counter, escape

`rq.combat.on_stun`, `on_poison`, `on_counter` and `on_escape` run just before the game rolls. The
callback returns the chance, or nil to leave it:

| Return | Chance |
| --- | --- |
| `nil` | as it was |
| a number | rounded down, held from 0 to 100 |
| `true` | 100 |
| `false` | 0 |

`ctx.rate` is the chance the callback before left, so two mods can both add to it. Some mods want
the game's own number. For them, `ctx.base` gives the formula's number for a stun, and the Counter
skill's number for a counter.

A venom blade poisons three hits in ten (most hits have no poison chance in the game):

```lua
local VENOM_BLADE = 1234

rq.combat.on_poison(function(ctx)
  local weapon = rq.item.equipped(ctx.attacker).weapon
  if weapon and rq.item.number(weapon) == VENOM_BLADE then
    return math.max(ctx.rate, 30)
  end
end)
```

The game blocks some rolls, and the callbacks still run there with `ctx.blocked` saying why. Return
a chance to lift the block:

- A stun: `"skill"` for the skills that never stun (120, Fortune 448, 152), or `"repeat"` for a
  target stunned in the turn before.
- A counter: `"familiar"` (the familiar's attack), `"area"` (a skill on more than one target),
  `"stunned"` (a stunned defender) or `"guard"` (a hit Ally Guard took).
- An escape: `"enemy"` (an enemy with skill 437 in the fight), `"rank"` or `"quest"` (for "Relax,
  relax").

Copandon Dot QoL lets Fortune stun this way:

```lua
rq.combat.on_stun(function(ctx)
  if ctx.skill == 448 and ctx.blocked == "skill" then return ctx.base end
end)
```

The stun callbacks also run for the battle forecast, with `ctx.forecast` true. A callback that
counts or rolls dice should do nothing then.

A counter does not need the Counter skill. `on_counter` runs after every hit that leaves the target
standing, for allies, enemies and familiars. The counter is the game's own Counter Attack. Thorns
for a state:

```lua
rq.combat.on_counter(function(ctx)
  if rq.status.get(ctx.defender, "mymod:thorns") and not ctx.counter then
    return math.max(ctx.rate, 50)
  end
end)
```

A counter can be countered, as in the game. After 10 counters in a row the loader grants no more,
so two mods that always counter cannot loop. `rq.counter.on_guard_counter` (the counter after Ally
Guard) still decides first.

Escape (211) and "Relax, relax" (217) end a fight. Neither does in a boss fight, and `on_escape`
does not run there.

## Heals

`rq.combat.on_heal` runs for every heal a skill gives in a fight: a support skill's heal
(`kind = "skill"`), a revive (`"revive"`), and HP absorb from a hit (`"absorb"`). Write
`ctx.amount` to change it. The HP, the number on the screen and the log's " recovered N HP." follow
the new amount. A curse that halves healing, and a state with no healing at all:

```lua
rq.combat.on_heal(function(ctx)
  if rq.status.get(ctx.target, "mymod:no_heal") then
    ctx.amount = ctx.kind == "revive" and 1 or 0 -- a revive still stands them up
  elseif rq.status.get(ctx.target, "mymod:curse") then
    ctx.amount = ctx.amount // 2
  end
end)
```

Regeneration at a turn's start is not a skill: change it with `rq.battle.on_turn`'s `ctx:heal`
([Battle states](states.md)). Outside fights, the game's heals are `rq.chara.heal` and
`rq.party.heal`.

## The turn list: Haste and Slow

The game builds the whole list of a fight's turns at the start, from each unit's speed. It builds
it again after a switch, a shuffle or a revive, and reads speed nowhere else in a fight.
`rq.battle.on_order` runs just before each build. `ctx:speed` sets a unit's speed for that build
only, so the status screens keep the real one. Haste and Slow as states:

```lua
rq.battle.on_order(function(ctx)
  for _, u in ipairs(ctx.units) do
    if rq.status.get(u.iic, "mymod:haste") then
      ctx:speed(u.iic, math.min(9999, u.spd * 3 // 2))
    elseif rq.status.get(u.iic, "mymod:slow") then
      ctx:speed(u.iic, u.spd // 2)
    end
  end
end)
```

The list is built only at those times, so a state put on in the middle of a fight changes the
order at the next rebuild. A state that has to act at once can rebuild the list itself in
`rq.battle.on_order_after`. That callback reads `ctx.order`, up to 50 roster slots, and can put a
list of its own in place with `ctx:set_order(list)`.

The familiar's unit has its `owner`, its `item` and `own_spd`: the game holds a familiar's speed to
the party's top speed, and `own_spd` is its speed before that. `rq.battle.familiar()` gives the same
at any time in a fight. Onoha QoL gives Onoha's familiar her speed this way.

## The escape chance and the ambush

`rq.battle.escape()` is the fight's escape chance. It starts at 20, or at the party's Escape Boost
if that is higher, and grows by 5 at each ally's turn. `rq.battle.set_escape(n)` sets it. A boss fight keeps 0.

`rq.battle.on_start`'s `ctx.ambush` is the ambush the game rolled: `"none"`, `"surprise"`,
`"first_strike"` or `"ambushed"`. `rq.battle.set_ambush` changes it there, before the turn list is
built:

```lua
rq.battle.on_start(function(ctx)
  if ctx.ambush == "ambushed" and party_has_lookout() then
    rq.battle.set_ambush("none")
  end
end)
```

## The battle log

`rq.battle.on_log` sees every line before it goes into the log. The callback returns false to drop
the line, a string to put in its place, or nil to keep it. `rq.battle.log(text)` adds a line of
your own. Nozomi Okita QoL drops the disease's line for a character who wears the Poison Mask:

```lua
rq.battle.on_log(function(ctx)
  if ctx.text:find("is poisoned by cough-cough disease", 1, true) and masked(ctx.text) then
    return false
  end
end)
```

`ctx.last` is true for the fight's end message: Victory, Defeat, Time exceeded, or the flight.

## Not yet

These are on the [Roadmap](../roadmap.md):

- What an enemy or a familiar does on its turn.
- The skill a counter uses (always Counter Attack).
- The turn list read at any time, with the turn the fight is on.
- The game's own ambush chances.
