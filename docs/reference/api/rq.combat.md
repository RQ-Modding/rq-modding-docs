# rq.combat

`since 0.2.0`

Changes physical damage, accuracy and criticals.

Physical attacks keep the game's own path: defense, variance, cap, then the usual multipliers. Lua
can replace the attack before defense, scale the final damage, add to the hit chance at the same
place as the game's own -5 and -10 for some skills, and force or deny a critical. The callbacks
hold up to 16 each, and the first one places the hooks (`rq.combat.install`, needed before 2.35.0).

They also run when the game works out the battle forecast, so the forecast shows what they
change; `ctx.forecast` is then true (since 2.26.0), and a callback that counts hits or rolls dice
should do nothing.

```lua
rq.combat.on_physical(function(ctx)
  if ctx.race == 8 then return nil, 50 end  -- half damage to a hanny
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.combat.install`](#rqcombatinstall) | Installs the hooks the combat callbacks need. |
| [`rq.combat.rules`](#rqcombatrules) | Returns what a skill can do in a fight: crit, stun, poison and accuracy. |
| [`rq.combat.set_rules`](#rqcombatset_rules) | Changes what a skill can do in a fight: its crit, stun or poison rule, in the fight and in `rq.combat.rules` together. |

### rq.combat.install

```lua
rq.combat.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Installs the hooks the combat callbacks need.

It is the same call as `rq.chara.install`; calling either again does nothing more.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

Raises an error when the AIN is not loaded or a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

> Changed in 2.35.0: Not needed: the callbacks make it.

### rq.combat.rules

```lua
rq.combat.rules(skill) -> rq.CombatRules|nil
```

`since 2.44.0`

Returns what a skill can do in a fight: crit, stun, poison and accuracy.

Worked out at each call from the skill's data as it is now (`rq.skill.get`: its action kind,
multiplier and function, so a `rq.skill.patch` shows), the game's rules by skill number, which
the game keeps only in its combat code (the loader knows them), and the rules mods set with
`rq.combat.set_rules`. For a skill's hover text, as Better Explained writes it.

The game's own exceptions show as "sometimes": a skill whose crit chance the game zeroes can
still crit with skill 549 or item 91. A rule a mod changes through a callback (`on_crit`,
`on_stun`, `on_poison`) does not show here unless that mod also calls `set_rules`.

Raises an error when `skill` is not a whole number.

```lua
rq.skill.on_describe(function(no, text)
  local r = rq.combat.rules(no)
  if r and r.crit == false then return text .. "\nCan't Crit" end
  return text
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `rules` | [`rq.CombatRules`](../types/rq.CombatRules.md) `\|nil` | What it can do; nil when there is no such skill, and before the game runs (at a mod's top level). |

See also: [`rq.combat.set_rules`](rq.combat.md#rqcombatset_rules)

### rq.combat.set_rules

```lua
rq.combat.set_rules(skill, rules) -> rq.CombatRules|nil
```

`since 2.44.0`

Changes what a skill can do in a fight: its crit, stun or poison rule, in the fight and in
`rq.combat.rules` together.

Each field of `rules` sets one rule; the fields left out keep theirs:

- `crit = true`: the skill rolls the attacker's crit chance even where the game zeroes it (a
  multiplier over 150, or skill 120), with the game's other rules (+30 hidden, halved for all
  enemies). `false`: it never crits.
- `stun = true`: it stuns at the chance of the game's formula even where the game never stuns
  (skills 120, Fortune 448 and 152; `rq.combat.on_stun`'s `base`). `false`: it never stuns.
- `poison = N` (0 to 100): its own poison chance, as the game's poison skills have; the
  weapon's or the coat's chance when higher, and a target the game shields (a barrier, character
  22, skill 502, item 195) is not poisoned. `false`: it never poisons.
- `"sometimes"`: the fight is left as it is, and `rules` says "sometimes", for a mod whose change
  depends on the fight and stays in its own callback.
- `"game"`: back to the game's rule.

In the fight the rules act where the game works out those rolls: on physical attacks
(`クリティカル計算`, `衝撃計算`, `毒計算`). The callbacks (`on_crit`, `on_stun`, `on_poison`) run
after the rule and see its chance. The last call for a skill wins, whichever mod made it.

A mod sets its rules from `init.lua`, before the game's skills are read: the skill is not checked
then, and the call returns nil until the game runs.

Raises an error when `skill` is not a whole number above 0, `rules` is not a table, or a field is
not one of the three or has another value.

```lua
rq.combat.set_rules(rq.ids.skill.FORTUNE, { crit = true, stun = true }) -- Fortune crits and stuns
rq.combat.set_rules(MY_SKILL, { poison = 40 })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |
| `rules` | `{crit?: boolean\|"sometimes"\|"game", stun?: boolean\|"sometimes"\|"game", poison?: integer\|false\|"sometimes"\|"game"}` | The rules to change. |

| Returns | Type | Description |
| --- | --- | --- |
| `rules` | [`rq.CombatRules`](../types/rq.CombatRules.md) `\|nil` | What the skill can do now; nil before the game runs, or for no such skill. |

See also: [`rq.combat.rules`](rq.combat.md#rqcombatrules)

## Events

| Name | Summary |
| --- | --- |
| [`rq.combat.on_physical`](#rqcombaton_physical) | Calls `fn` for each physical hit, to change the attack and the final damage. |
| [`rq.combat.on_accuracy`](#rqcombaton_accuracy) | Calls `fn` for each accuracy check, to add to the hit chance. |
| [`rq.combat.on_crit`](#rqcombaton_crit) | Calls `fn` where the game rolls a critical (the `確率演算` call in `クリティカル計算`). |
| [`rq.combat.on_magic`](#rqcombaton_magic) | Calls `fn` for each magic hit, to change its final damage by a percent. |
| [`rq.combat.on_stun`](#rqcombaton_stun) | Calls `fn` where the game works out a stun, to change its chance. |
| [`rq.combat.on_poison`](#rqcombaton_poison) | Calls `fn` after each hit on a target with no status, to change the chance it is poisoned. |
| [`rq.combat.on_counter`](#rqcombaton_counter) | Calls `fn` after each hit that leaves the character hit standing, to change the chance it counters. |
| [`rq.combat.on_heal`](#rqcombaton_heal) | Calls `fn` when a skill gives HP in a fight, to change how much. |
| [`rq.combat.on_escape`](#rqcombaton_escape) | Calls `fn` when an ally uses Escape or "Relax, relax", to change the chance it ends the fight. |
| [`rq.combat.on_cap`](#rqcombaton_cap) | Calls `fn` where the game holds a hit's damage to the skill's limit, to change the limit. |
| [`rq.combat.on_element`](#rqcombaton_element) | Calls `fn` where the game picks a physical hit's element, to change it. |

### rq.combat.on_physical

```lua
rq.combat.on_physical(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` for each physical hit, to change the attack and the final damage.

`fn` returns nothing to keep the game's numbers, a new attack before defense, or an attack (nil
keeps it) and a percent of the final damage, applied after `最終ダメージ計算` (100 is unchanged, 50
half). Each callback sees the attack the one before left, and the percents multiply.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.PhysicalCtx`](../types/rq.PhysicalCtx.md) `): integer\|nil,` | integer\|nil Returns the attack, then the percent. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs (before, the last one won).

> Changed in 0.23.0: Returns a remover.

### rq.combat.on_accuracy

```lua
rq.combat.on_accuracy(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` for each accuracy check, to add to the hit chance.

The returned numbers of every callback add up; nil counts as 0. The game's own limits come after
them: the chance is at most 100; an ally's attack hits at least 20% of the time; an enemy's at
least 40% (20% or 60% by the target's class, more after the target dodged several times in a
row) and at most 80% to 100% by the target's evasion.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.AccuracyCtx`](../types/rq.AccuracyCtx.md) `): integer\|nil` | Returns points to add to the hit chance; negative lowers it. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs and the numbers add up (before, the last one won).

> Changed in 0.23.0: Returns a remover.

### rq.combat.on_crit

```lua
rq.combat.on_crit(fn) -> fun()
```

`since 0.12.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` where the game rolls a critical (the `確率演算` call in `クリティカル計算`).

Return true to force the critical, false to deny it, nil to roll as the game does. The first
callback that returns a boolean decides. A forced critical still adds the game's +30 to the damage
multiplier, and it also happens for skills whose multiplier is above 150, which never roll one in
the game.

```lua
rq.combat.on_crit(function(ctx)
  if ctx.defender_type == 22 then return true end  -- humanoids always take a critical
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CritCtx`](../types/rq.CritCtx.md) `): boolean\|nil` | Returns true, false, or nil to roll. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs until one decides.

> Changed in 0.23.0: Returns a remover.

See also: [`rq.combat.on_stun`](rq.combat.md#rqcombaton_stun)

### rq.combat.on_magic

```lua
rq.combat.on_magic(fn) -> fun()
```

`since 2.1.0` `changed 2.26.0`

Calls `fn` for each magic hit, to change its final damage by a percent.

`fn` returns a percent of the final damage (100 is unchanged, 50 half, 0 none) or nil to keep it.
The percents of every callback multiply, and the damage is rounded down. It runs after the game's
last damage step (`最終ダメージ計算`), so the barrier, immunities and the game's magic resistance
are already in `damage`; a spell that does 0 is not reported. It also runs for the battle
forecast, with `ctx.forecast` true, so the forecast's damage word shows the percent. It is the
magic twin of the final percent of `rq.combat.on_physical`.

Raises an error, logged, for a return that is not a whole number of 0 or more.

```lua
rq.combat.on_magic(function(ctx)
  if weakened[ctx.attacker] then return 70 end  -- a weakened caster does 70%
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.MagicCtx`](../types/rq.MagicCtx.md) `): integer\|nil` | Returns the percent, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.26.0: Runs for the battle forecast too, with `ctx.forecast`.

See also: [`rq.combat.on_physical`](rq.combat.md#rqcombaton_physical)

### rq.combat.on_stun

```lua
rq.combat.on_stun(fn) -> fun()
```

`since 2.37.0`

Calls `fn` where the game works out a stun, to change its chance.

It runs in `衝撃計算` for each hit of an attack, and for the battle forecast with `ctx.forecast`
true. `fn` returns the chance, 0 to 100, or nil to keep it; true is 100 and false is 0, and a
number past either end is held there. Each callback sees in `ctx.rate` what the one before left.
The game then rolls the last chance with its own roll (`確率演算`): the forecast's "Stun N%" and
the log's " (Stun rate = N)" show it.

It also runs for the hits the game never stuns with: the skills 120, Fortune (448) and 152, and a
target stunned in the turn before (the game's rule against a stun every turn). There `ctx.rate`
is 0 and `ctx.blocked` says why; `ctx.base` is what the formula gives, so a mod can let one of
them stun.

A stunned target loses its next turn and stops charging, as with the game's own stun. A target
that is already stunned, or a hit that does no damage, is the game's to judge as before.

Raises an error, logged, for a return that is not a number, a boolean or nil.

```lua
rq.combat.on_stun(function(ctx)
  if ctx.skill == FORTUNE and ctx.blocked == "skill" then return ctx.base end -- Fortune stuns
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.StunCtx`](../types/rq.StunCtx.md) `): integer\|boolean\|nil` | Returns the chance, true, false or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.combat.on_crit`](rq.combat.md#rqcombaton_crit)

### rq.combat.on_poison

```lua
rq.combat.on_poison(fn) -> fun()
```

`since 2.37.0`

Calls `fn` after each hit on a target with no status, to change the chance it is poisoned.

It runs in `毒計算`, after the stun, for each hit of an attack on a target that is not poisoned,
stunned or down. `fn` returns the chance, 0 to 100, or nil to keep it; true is 100 and false is
0. Most hits have a chance of 0 in the game, so a mod can give one to any attack. The log's first
line shows " (Poison = N)", as for the game's own poison (the game shows no word when it takes).
The game makes no forecast for a poison.

Raises an error, logged, for a return that is not a number, a boolean or nil.

```lua
rq.combat.on_poison(function(ctx)
  if rq.item.number(rq.item.equipped(ctx.attacker).weapon or 0) == VENOM_BLADE then return 30 end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.PoisonCtx`](../types/rq.PoisonCtx.md) `): integer\|boolean\|nil` | Returns the chance, true, false or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.combat.on_stun`](rq.combat.md#rqcombaton_stun)

### rq.combat.on_counter

```lua
rq.combat.on_counter(fn) -> fun()
```

`since 2.37.0`

Calls `fn` after each hit that leaves the character hit standing, to change the chance it counters.

It runs in `ダメージ後計算`, for allies, enemies and familiars, whether or not the one hit has the
Counter skill (259), a yellow skill of any class that learned it. `fn` returns the chance, 0 to
100, or nil to keep it; true is 100 and false is 0. A counter is the game's: the one hit uses
Counter Attack (116) on the attacker, with " (counter)" in the log, and `rq.battle.on_hit` and
`on_use` see it with `counter` true. A counter can be countered, as in the game; after 10 counters
in a row the loader grants no more, so two callbacks that always counter cannot loop.

`rq.counter.on_guard_counter` still decides first whether Ally Guard clears the Counter skill's
chance; `ctx.rate` is then what it left.

Raises an error, logged, for a return that is not a number, a boolean or nil.

```lua
rq.combat.on_counter(function(ctx)
  if thorns[ctx.defender] and not ctx.counter then return math.max(ctx.rate, 50) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CounterCtx`](../types/rq.CounterCtx.md) `): integer\|boolean\|nil` | Returns the chance, true, false or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.counter.on_guard_counter`](rq.counter.md#rqcounteron_guard_counter)

### rq.combat.on_heal

```lua
rq.combat.on_heal(fn) -> fun()
```

`since 2.37.0` `changed 2.56.1`

Calls `fn` when a skill gives HP in a fight, to change how much.

It runs after a support skill's heal or revive (`Ｔ補助行動`: First Aid, the Healing spells,
Recovery Rain, Maiden's Spirit, Bishamonten, Am Powder, Epinephrend, Status Restore, Full Revive,
and a mod skill patched to one of them) and after a hit with HP absorb (`ダメージ後計算`), before
anything shows. Each callback sees in `ctx.amount` what the one before left. The HP given, the
number shown and the number in the log's " recovered N HP." follow the last amount. A revive
gives at least 1 HP. A heal the game makes 0 (a downed target, Medicine on Suzume, skill 366) is
not reported.

A skill on the whole party (Recovery Rain) gives one heal to each ally in the fight, a downed one
too; the party's empty places get none.

Regeneration at a turn start is not a skill: give or take it with `rq.battle.on_turn`'s
`ctx:heal`. Outside fights the game's heals are `rq.chara.heal` and `rq.party.heal`.

the five places, not the place, so an empty place was healed too: a callback with `target` 0 and
a line with no name in the log. The loader makes it check the place.

```lua
rq.combat.on_heal(function(ctx)
  if cursed[ctx.target] then ctx.amount = ctx.amount // 2 end -- a curse halves healing
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.HealCtx`](../types/rq.HealCtx.md) `)` | Gets the heal; writes `ctx.amount` to change it. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.56.1: The game's whole-party support (`戦闘味方_全体補助`) checked its user at each of

See also: [`rq.battle.on_turn`](rq.battle.md#rqbattleon_turn)

### rq.combat.on_escape

```lua
rq.combat.on_escape(fn) -> fun()
```

`since 2.37.0`

Calls `fn` when an ally uses Escape or "Relax, relax", to change the chance it ends the fight.

Escape (211) flees the fight (the result "fled"): the game rolls the fight's escape chance. "Relax,
relax" (217) ends it as the enemies leave (the game's result 6), always, but not at fight rank 2
or under the quest's rule. `fn` returns the chance, 0 to 100, or nil to keep it; true is 100 and
false is 0. When the last chance differs from the game's, the loader rolls it with the game's
roll. A failed Escape still raises the chance by 5, as the game does.

It does not run in a boss fight, where nothing ends the fight but a win or a loss.

Raises an error, logged, for a return that is not a number, a boolean or nil.

```lua
rq.combat.on_escape(function(ctx)
  if ctx.skill == 211 and has_smoke_bomb(ctx.iic) then return 100 end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.EscapeCtx`](../types/rq.EscapeCtx.md) `): integer\|boolean\|nil` | Returns the chance, true, false or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.battle.set_escape`](rq.battle.md#rqbattleset_escape)

### rq.combat.on_cap

```lua
rq.combat.on_cap(fn) -> fun()
```

`since 2.46.0`

Calls `fn` where the game holds a hit's damage to the skill's limit, to change the limit.

It runs in `最終ダメージ計算`, for every physical hit and spell and for the battle forecast. The
limit is the skill's (500 for Ranged Attack 1), raised by the attacker's Damage Maximum. Damage over
the limit is halved, and over twice the limit quartered, as before. `fn` returns the new limit in
damage points, 0 for none, or nil to keep it; a negative number is 0. Each callback sees in
`ctx.limit` what the one before left.

A skill with no limit (`base` 0) gets one when a callback returns a number above 0. Skill 460 in
world 3 still has no limit on half its hits, as in the game.

A callback's error, or a return that is not a number or nil, is logged once and changes nothing.

```lua
rq.combat.on_cap(function(ctx)
  -- +100% more, added to Damage Maximum's percent
  if ctx.base > 0 and has_mark(ctx.attacker) then
    return ctx.base * (100 + ctx.damage_max + 100) // 100
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CapCtx`](../types/rq.CapCtx.md) `): integer\|nil` | Returns the limit, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.combat.on_physical`](rq.combat.md#rqcombaton_physical)

### rq.combat.on_element

```lua
rq.combat.on_element(fn) -> fun()
```

`since 2.46.0`

Calls `fn` where the game picks a physical hit's element, to change it.

It runs in `物理属性計算` for each physical hit and for the battle forecast, once the game has
picked: the weapon's element, the skill's over it, then the game's arrows over both (Fire, Ice and
Electric Arrows on a basic attack, and skill 145's five, which take the weakness when it is known
and no guard took the hit). `fn` returns an element 0 to 5, or nil to keep it. Each callback sees
in `ctx.element` what the one before left.

The game then goes on with the element: a hit on the weakness gets +50% damage, " (Attribute
weakness)" in the log and the big number; the effect gets the element's look; the knowledges
(Fire Knowledge and the rest) add their percent. A spell's element is the spell's and does not go
through here.

A callback's error, or a return that is not a whole number 0 to 5 or nil, is logged once and
changes nothing.

```lua
rq.combat.on_element(function(ctx)
  -- like the game's arrows: the weakness, when it is known and no guard took the hit
  if ctx.basic and ctx.known and not ctx.guarded and ctx.weakness ~= 0 and has_arrows(ctx.attacker) then
    return ctx.weakness
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.ElementCtx`](../types/rq.ElementCtx.md) `): integer\|nil` | Returns the element, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.ids`](rq.ids.md)
