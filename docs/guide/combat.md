# Combat rules

Loader 2.37.0 lets a mod change the rules of a fight. A mod can set the chance of a stun, a poison,
a counter or an escape, and how much HP a heal gives. It can also change the speeds the turn list is
built from, the list itself, the ambush, and each line of the battle log. Since 2.38.0 it can also
choose what an enemy or the familiar does on its turn, and since 2.44.0 read and change what a skill
can do (its crit, stun and poison rules). Since 2.46.0 it can change a hit's damage limit and a
physical hit's element, and show the game's Weakness Search. Every mod's callbacks run in turn on
the same fight, and the game shows the result as its own: the forecast, the log, the numbers and the
turn icons.

## What a skill can do: the rules

The game decides some things by skill number, in its combat code: Assassinate (120) never crits,
Fortune (448) never stuns, a few skills have a poison chance of their own. It keeps them in no
table. The loader does, and `rq.combat.rules(skill)` answers with them, joined to the skill's data
as it is then (a `rq.skill.patch` shows) and to what mods set:

```lua
local r = rq.combat.rules(448) -- Fortune
-- r.crit = "sometimes", r.stun = false, r.poison = "coat", r.accuracy = "ignores"
```

- `crit` and `stun` are true, false or `"sometimes"`. "sometimes" is the game's exceptions: a skill
  whose crit chance the game sets to 0 (a multiplier above 150, or Assassinate) still crits with
  skill 549 or party item 91.
- `poison` is `"own"` (with `poison_rate`), `"coat"` (only through the weapon or Poison Effect, as
  most physical attacks), `"sometimes"` or false.
- `accuracy` is `"ignores"` for the skills that never miss, else `"rolls"`.

`rq.combat.set_rules(skill, rules)` changes a rule in the fight and in `rules` together, so a hover
that reads `rules` (Better Explained's) can never disagree with the fight. Copandon Dot QoL lets
Fortune crit and stun:

```lua
rq.combat.set_rules(rq.ids.skill.FORTUNE, { crit = true, stun = true })
```

- `crit = true` rolls the game's chance where the game zeroes it, with the game's other rules
  (halved on all enemies, +30 while hidden); `false` never crits.
- `stun = true` stuns at the game's formula where the game never does; `false` never stuns.
- `poison = 30` gives the skill its own chance (the weapon's or the coat's when higher); `false`
  never poisons.
- `"sometimes"` leaves the fight alone and only changes what `rules` says, for a mod whose change
  depends on the fight and stays in a callback. `"game"` puts the game's rule back.

The rules act where the game works those rolls out, on physical attacks. The callbacks below run
after a rule and see its chance.

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

- A stun: `"skill"` for the skills that never stun (120, Fortune 448, 152, or a skill a mod's
  `set_rules` gave `stun = false`), or `"repeat"` for a target stunned in the turn before.
- A counter: `"familiar"` (the familiar's attack), `"area"` (a skill on more than one target),
  `"stunned"` (a stunned defender) or `"guard"` (a hit Ally Guard took).
- An escape: `"enemy"` (an enemy with skill 437 in the fight), `"rank"` or `"quest"` (for "Relax,
  relax").

Skill 152 stunning at the formula's chance, in a callback:

```lua
rq.combat.on_stun(function(ctx)
  if ctx.skill == 152 and ctx.blocked == "skill" then return ctx.base end
end)
```

For a rule that holds on every hit, `set_rules` is shorter and shows in `rules` too. A callback
fits a rule that depends on the fight: Copandon Dot QoL keeps one that holds Fortune's stun at 0 on
Bad Luck.

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

## The damage limit

Many skills hold their damage to a limit (500 for Ranged Attack 1): damage over it is halved, and
over twice it quartered. Damage Maximum raises the limit by its percent. Since 2.46.0
`rq.combat.on_cap` runs where the game works the limit out, for each physical hit, spell and
forecast, after Damage Maximum. `ctx.base` is the skill's own limit, `ctx.damage_max` Damage
Maximum's percent and `ctx.limit` the limit so far. Return a new limit (0 for none) or nil. Athena
QoL's Athena Maximum adds +100% to Damage Maximum's percent:

```lua
rq.combat.on_cap(function(ctx)
  if ctx.base > 0 and has_maximum(ctx.attacker) then
    return ctx.base * (100 + ctx.damage_max + 100) // 100
  end
end)
```

## A hit's element

`rq.combat.on_element` (2.46.0) runs once the game has picked a physical hit's element: the
weapon's, then the skill's, then the game's arrows (Fire, Ice and Electric Arrows on a basic
attack, and skill 145), which take the target's weakness when it is known and no guard took the
hit. Return an element ([`rq.ids.element`](ids.md)) or nil. The game goes on with it: the weakness
bonus, " (Attribute weakness)" in the log, the effect's look and the knowledges. A spell's element
is the spell's own and does not go through here. Calculated Shot on a known weakness, as the game's
arrows:

```lua
rq.combat.on_element(function(ctx)
  if ctx.skill == SHOT and ctx.known and not ctx.guarded and ctx.weakness ~= 0 then
    return ctx.weakness
  end
end)
```

## Weakness Search from a mod

`rq.battle.reveal_weakness(enemies, opts)` (2.46.0) does what the game's Weakness Search does: each
enemy's weakness becomes known (the hits see it at once, and the game keeps it for the monster),
the effect plays over the enemies and their marks blink. From `rq.battle.on_start` it waits for the
fight to show, after any ambush notice; from `rq.on_frame` or a timer, for the next turn; from the
fight's own flow (`rq.battle.on_turn`, `on_hit`) it plays at once. Rebecca Copley QoL plays it in
every fight Rebecca starts in:

```lua
rq.battle.on_start(function(ctx)
  if rebecca_in(ctx.allies) then
    rq.battle.reveal_weakness(nil, { log = "→Rebecca observed the enemies' weaknesses." })
  end
end)
```

`opts.effect = false` shows the marks without the effect and the blinking.

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

## What enemies choose

On an enemy's turn the game draws a skill from the monster's list. Each skill has a chance, read as
a threshold: the draw, 0 to 99, takes the first skill whose chance is at least the number, so 50
then 100 is half each. An enemy in the back row whose skill reaches only the front row stands by
(Standby, 384) while an enemy stands in the front row. The familiar always uses its first skill.
The game then rolls the target among the units the skill can reach.

`rq.battle.on_choose` (2.38.0) runs after both, before the enemy acts. `ctx.skill` and `ctx.target`
hold the game's choice, and a mod writes them to change it. `ctx.skills` is the actor's list, and
`ctx:targets(skill)` the units a skill may aim at. A boss that heals when its HP is low, and
otherwise hits whoever has the least HP:

```lua
local HEAL = 1234 -- a support skill on its own side

rq.battle.on_choose(function(ctx)
  if ctx.side ~= "enemy" or rq.chara.get(ctx.iic).no ~= MY_BOSS then return end
  local me = rq.chara.get(ctx.iic)
  if me.hp * 3 < me.hp_max then
    ctx.skill, ctx.target = HEAL, ctx.iic
    return
  end
  local weakest
  for _, iic in ipairs(ctx:targets()) do
    if not weakest or rq.chara.get(iic).hp < rq.chara.get(weakest).hp then weakest = iic end
  end
  ctx.target = weakest
end)
```

The loader checks what a callback writes, and keeps the value before it when a check fails, with a
line in the log:

- A skill must act (physical, magic, special or support, not an ability), and cannot be Escape or
  "Relax, relax". It goes through the Standby rule. A skill the actor does not have is put at the
  end of its list for the rest of the fight, with chance 0 so the game never draws it. The game
  shows the skill's own log text, and the enemy plays the motion of its first skill.
- A target must be one of `ctx:targets(ctx.skill)`: standing, on the side the skill aims at, not a
  hidden ally, and in the front row for a melee skill while one stands there. An attack on the
  enemy's own side is refused: the game draws an enemy's attack only on the party's side.
- A callback that writes a new skill and leaves the target gets the game's roll for the new skill,
  unless a mod set the target and it still fits. `nil` lets the game roll again.

A target a mod set takes every hit of a multi-hit skill while it stands; writing the unit the game
rolled counts as setting it. On the turn a charged
skill is released, `ctx.charged` is true and only the target can change.

The familiar's turns come here too, with `ctx.side == "familiar"`: a familiar that uses its second
skill on the enemy with the most HP is a few lines. The allies' turns do not: the player chooses
them, and AUTO is the game's.

### The taunt

The game has a taunt of its own: a skill that "got the enemy's attention" names an ally, and the
enemies' rolls take that ally first while it stands, is not hidden and is in the rows the skill
reaches. `rq.battle.taunt()` reads it and `rq.battle.set_taunt(iic)` sets it (nil clears it). It
lasts until it changes or the fight ends. A taunt state is in [Battle states](states.md#a-state-that-changes-the-rules).

## Not yet

These are on the [Roadmap](../roadmap.md):

- The allies' AUTO choices, an ally's turn taken by a state (charm, berserk), and confusion (an
  attack on the attacker's own side).
- The skill a counter uses (always Counter Attack).
- The turn list read at any time, with the turn the fight is on.
- The game's own ambush chances.
