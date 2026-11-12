# rq.battle

`since 0.2.0`

Hooks into fights: events, ally skill select, marks and buffs on the cards, faces, states, drops,
and scripted fights.

Each call places the hooks it needs the first time; most events hold up to 16 callbacks. Only
`set_state` needs a call first, `rq.battle.install_states`, since it changes the game's rules.

A card goes by battle number: 1 to 5 are the ally ranks, 11 to 15 the enemy ranks. Characters are
roster slots (`iic`); enemy slots are below 20.

```lua
rq.battle.on_start(function(ctx)
  for _, e in ipairs(ctx.enemies) do
    rq.chara.set(e, { weakness_known = true })  -- reveal every enemy's weakness
  end
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.battle.install`](#rqbattleinstall) | Installs the ally skill select hooks. |
| [`rq.battle.familiar`](#rqbattlefamiliar) | Returns the familiar in the current fight. |
| [`rq.battle.escape`](#rqbattleescape) | Returns the escape chance of the current fight. |
| [`rq.battle.set_escape`](#rqbattleset_escape) | Sets the escape chance of the current fight. |
| [`rq.battle.set_ambush`](#rqbattleset_ambush) | Changes the fight's ambush, from `rq.battle.on_start`. |
| [`rq.battle.log`](#rqbattlelog) | Adds a line to the battle log now. |
| [`rq.battle.install_flame`](#rqbattleinstall_flame) | Installs the hooks the flame, the buffs and the marks need. |
| [`rq.battle.set_flame`](#rqbattleset_flame) | Shows or hides the enemies' "charging" flame on an ally. |
| [`rq.battle.set_buff`](#rqbattleset_buff) | Adds, changes or removes a mod's buff on a character. |
| [`rq.battle.set_rank_buff`](#rqbattleset_rank_buff) | Adds, changes or removes a buff that stays on a card, whoever stands there. |
| [`rq.battle.set_mark`](#rqbattleset_mark) | Changes how one of the game's marks shows, until changed again, also in later fights. |
| [`rq.battle.install_states`](#rqbattleinstall_states) | Lets poison and stun be on one character at once, and ▲ and ▼ of one stat, until the game closes. |
| [`rq.battle.states`](#rqbattlestates) | Returns every state of a character, also without `install_states`. |
| [`rq.battle.set_state`](#rqbattleset_state) | Adds or takes one state, by the rules of `install_states`, and the card shows it. |
| [`rq.battle.buffs`](#rqbattlebuffs) | Lists the marks a card shows in turn. |
| [`rq.battle.get_drop`](#rqbattleget_drop) | Returns the item a won fight hands out (`◆戦闘後アイテム取得`). |
| [`rq.battle.set_drop`](#rqbattleset_drop) | Sets the item a won fight hands out. |
| [`rq.battle.bags`](#rqbattlebags) | Lists the gold bags of the fight's enemies. |
| [`rq.battle.set_bag`](#rqbattleset_bag) | Gives an enemy a gold bag, or takes its bag away, before it falls. |
| [`rq.battle.set_face`](#rqbattleset_face) | Shows another face for an ally on the cards in a fight. |
| [`rq.battle.get_face`](#rqbattleget_face) | Returns what `rq.battle.set_face` set for a character. |
| [`rq.battle.in_ally_select`](#rqbattlein_ally_select) | Returns whether an ally is choosing a skill. |
| [`rq.battle.actor`](#rqbattleactor) | Returns the ally choosing a skill. |
| [`rq.battle.skill_usable`](#rqbattleskill_usable) | Returns whether a character can use a skill now. |
| [`rq.battle.start`](#rqbattlestart) | Opens a fight with the current party, using the game's scripted fight or its boss fight. |
| [`rq.battle.backgrounds`](#rqbattlebackgrounds) | Lists the game's fight backgrounds, in the game's order. |
| [`rq.battle.force_hit`](#rqbattleforce_hit) | Decides every accuracy check, of allies and enemies, until `force_hit(nil)`. |
| [`rq.battle.time`](#rqbattletime) | Returns the actions left in this fight, the number on the TIME REMAINING panel. |
| [`rq.battle.set_time`](#rqbattleset_time) | Sets the actions left in this fight. |
| [`rq.battle.snapshot`](#rqbattlesnapshot) | Returns a copy of what the fight screen shows. |

### rq.battle.install

```lua
rq.battle.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Installs the ally skill select hooks.

It wraps `T_BattleSelect@select`, `@checkKey` and `@exec`, so a key that `on_select_key` claims
completes the select like a click on that skill: the key is swallowed (Space does not also
Cancel), and the skill runs on the actor itself.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

Raises an error when the AIN is not loaded or a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

> Changed in 2.35.0: Not needed: `on_select_key`, `in_ally_select`, `actor` and `skill_usable` make it.

### rq.battle.familiar

```lua
rq.battle.familiar() -> rq.BattleFamiliar|nil
```

`since 2.37.0`

Returns the familiar in the current fight.

An ally holding a familiar item may call its familiar at a fight's start (the item's class,
Familiar Knowledge), and a strong familiar from the vault sometimes jumps in. It is built from its
monster in slot 10, with its attack and magic raised by its growth.

```lua
local f = rq.battle.familiar()
if f then rq.log("familiar " .. f.no .. " beside " .. rq.chara.get(f.owner).name) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `familiar` | [`rq.BattleFamiliar`](../types/rq.BattleFamiliar.md) `\|nil` | The familiar, or nil outside a fight or with none. |

### rq.battle.escape

```lua
rq.battle.escape() -> integer|nil
```

`since 2.37.0`

Returns the escape chance of the current fight.

The game sets it at a fight's start to 20, or the party's Escape Boost (268) if higher, 0 in a
boss fight. It grows by 5 at each ally's turn while it is not 0, and by 5 after a failed Escape,
up to 100. Escape (211) works when a roll of 1 to 100 is at most the chance.

| Returns | Type | Description |
| --- | --- | --- |
| `chance` | `integer\|nil` | 0 to 100; nil outside a fight. |

See also: [`rq.battle.set_escape`](rq.battle.md#rqbattleset_escape), [`rq.combat.on_escape`](rq.combat.md#rqcombaton_escape)

### rq.battle.set_escape

```lua
rq.battle.set_escape(n) -> integer
```

`since 2.37.0`

Sets the escape chance of the current fight.

It is the game's own setter: a boss fight keeps 0. A chance of 0 stays 0, as the game's growth
adds only to a chance that is not 0. Set it from `rq.battle.on_start` for the whole fight, or any
time in it. `rq.battle.start`'s `escape` sets it too, before every `on_start` callback.

Raises an error for a chance that is not whole, 0 to 100, or outside a fight.

```lua
rq.battle.on_start(function(ctx)
  if has_smoke_bomb() then rq.battle.set_escape(80) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The chance, 0 to 100. |

| Returns | Type | Description |
| --- | --- | --- |
| `chance` | `integer` | The chance now, after the game's rule. |

See also: [`rq.battle.escape`](rq.battle.md#rqbattleescape)

### rq.battle.set_ambush

```lua
rq.battle.set_ambush(kind, iic)
```

`since 2.37.0`

Changes the fight's ambush, from `rq.battle.on_start`.

The game decides the ambush before `on_start` (`ctx.ambush`): "surprise" gives every ally the
first entries of the turn list, "first_strike" gives the Gunners of the party two first entries
each and names the ally in the notice, "ambushed" gives every enemy the first entries. The notice
shows after the setup. The game's other effects of an ambush it rolled stay (an ambush by the
enemies gives the fight one more action per enemy).

Raises an error for an unknown kind, an ally not in the fight, an ally with another kind, or a
call outside the setup of a fight (`rq.battle.on_start`).

```lua
rq.battle.on_start(function(ctx)
  if ctx.ambush == "ambushed" and has_lookout() then rq.battle.set_ambush("none") end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `kind` | `"none"\|"surprise"\|"first_strike"\|"ambushed"` | The ambush. |
| `iic` *(optional)* | `integer` | For "first_strike", the ally the notice names. Default: the first ally. |

### rq.battle.log

```lua
rq.battle.log(text) -> boolean
```

`since 2.37.0`

Adds a line to the battle log now.

It goes through `rq.battle.on_log` as the game's lines do, in the game's color. Write a whole
line; the game's own start with the turn's number or "→".

Raises an error for a value that is not a string, or outside a fight.

```lua
rq.battle.on_start(function()
  rq.battle.log("→The air is thick with spores.")
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `text` | `string` | The line. An empty line adds nothing. |

| Returns | Type | Description |
| --- | --- | --- |
| `added` | `boolean` | false when the game added nothing. |

See also: [`rq.battle.on_log`](rq.battle.md#rqbattleon_log)

### rq.battle.install_flame

```lua
rq.battle.install_flame() -> boolean
```

`since 0.12.0` `changed 2.35.0`

Installs the hooks the flame, the buffs and the marks need.

It hooks the ally status refresh so `set_flame` sticks, and installs the fight start and end
events, which clear the flames and buffs. The engine also makes it once the mods have loaded.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

Raises an error when a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

> Changed in 2.35.0: Not needed: `set_flame` and `set_mark` make it.

### rq.battle.set_flame

```lua
rq.battle.set_flame(iic, on) -> boolean
```

`since 0.12.0` `changed 0.29.0`

Shows or hides the enemies' "charging" flame on an ally.

The flame goes with the character when the party changes places in a switch, and ends when they
leave the party. It is forgotten at the start and end of a fight. The ally's card shows one mark
at a time, so the flame takes turns with Protect, Berserk, Stealth and Barrier. Attack and defense
arrows are separate: `rq.chara.set(iic, { atk_buff = 1 })`.

The first call places the hooks (`rq.battle.install_flame`); before 2.35.0 a call before them
raised an error.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The ally's roster slot. |
| `on` | `boolean` | true shows it, false hides it. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the character is not in the party. |

> Changed in 0.29.0: The flame follows the character in a switch.

### rq.battle.set_buff

```lua
rq.battle.set_buff(iic, key, def) -> boolean
```

`since 0.16.0` `changed 0.28.0` `changed 0.29.0`

Adds, changes or removes a mod's buff on a character.

The buff belongs to the character: it leaves the card with them, shows again when they come back,
and can be changed or removed while they are out. On an enemy the spot is over the card's second
line, and the game hides the marks of a dead enemy. Up to 8 per character, cleared at the start
and end of a fight. Up to 128 different icons and GIFs, together.

Raises an error for a def with neither icon nor anim, a number that is no CG, an unknown anim, an
`x`, `y`, `layer` or `order` out of range or not whole, a too long key, or a 9th buff.

```lua
local ICON = rq.image.add("shield", "shield.png", { fit = "contain", w = 56, h = 56 })
rq.battle.set_buff(iic, "my-shield", { icon = ICON, text = "3" })
rq.battle.set_buff(iic, "my-shield")  -- remove it
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `key` | `string` | The buff's name, unique per character. |
| `def` *(optional)* | [`rq.BuffDef`](../types/rq.BuffDef.md) | The buff; nil removes it. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the character has not stood on a card in this fight. |

> Changed in 0.28.0: Enemies too.

> Changed in 0.29.0: The buff follows the character.

See also: [`rq.battle.set_rank_buff`](rq.battle.md#rqbattleset_rank_buff)

### rq.battle.set_rank_buff

```lua
rq.battle.set_rank_buff(rank, key, def) -> boolean
```

`since 0.29.0`

Adds, changes or removes a buff that stays on a card, whoever stands there.

It works as `rq.battle.set_buff`, and comes after the character's own buffs. An empty rank can
hold one; it shows when someone comes in. Up to 8 per rank, cleared at the start and end of a
fight.

| Parameter | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | The battle number: 1 to 5 for allies, 11 to 15 for enemies. |
| `key` | `string` | The buff's name, unique per rank. |
| `def` *(optional)* | [`rq.BuffDef`](../types/rq.BuffDef.md) | The buff; nil removes it. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false for any other number. |

### rq.battle.set_mark

```lua
rq.battle.set_mark(mark, def, who) -> boolean
```

`since 0.30.0` `changed 1.5.0`

Changes how one of the game's marks shows, until changed again, also in later fights.

Without `who` it is for every card. `who = { iic = n }` is for one character, wherever they stand,
and `who = { no = n }` for one card, whoever stands there. A character's def wins over its card's,
which wins over the one for every card, and replaces it whole: an empty table `{}` for one
character shows the game's own mark there while the other cards show a mod's icon. A hidden or
moved mark keeps its place in the game's stack. Up to 64 defs for characters and cards together.
The first call places the hooks (`rq.battle.install_flame`, needed before 2.35.0).

Raises an error for a bad `who`, a card number that is not 1 to 5 or 11 to 15, a number that is
no CG, an unknown anim, or a 65th def.

```lua
rq.battle.set_mark(21, { icon = POISON_ICON })   -- poison, on every card
rq.battle.set_mark(21, {}, { iic = rq.chara.find(1) })  -- but the game's own on Rance
```

| Parameter | Type | Description |
| --- | --- | --- |
| `mark` | `integer` | 1 attack ▲, 2 attack ▼, 11 defense ▲, 12 defense ▼, 21 poison, 22 stun, 23 near death, 31 flame, 32 guard, 33 berserk, 34 stealth, 35 protect, 36 barrier. |
| `def` *(optional)* | [`rq.MarkDef`](../types/rq.MarkDef.md) | How it shows; nil goes back to the game's (for that `who`). |
| `who` *(optional)* | `{iic?: integer, no?: integer}` | One character or one card. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false for any other mark number. |

> Changed in 1.5.0: Added `who`.

### rq.battle.install_states

```lua
rq.battle.install_states() -> boolean
```

`since 0.31.0`

Lets poison and stun be on one character at once, and ▲ and ▼ of one stat, until the game closes.

It changes the game's rules, so it stays a mod's own choice: `set_state`, which needs it, raises an
error before it.

Without it the game's own rule stays, where a new state replaces the old. With it: poison does its
damage on the turn a character only recovers from stun; ▲ and ▼ both apply and cancel out;
recovering from stun takes only stun, First Aid only poison, and a cure of ▼ or a removal of ▲ only
its own side; Encourage, Self-Healing and Status Restore take both poison and stun, and death takes
everything. Barrier still blocks poison, a stun still cancels a charge, no two stuns in a row.

The second state of a stat is not in the save and is forgotten when the fight ends. `rq.chara`'s
`status`, `atk_buff` and `def_buff` still show one value each, the one that came first, and stun
over poison; the second state shows as a pinned mark, listed by `buffs`. Use
`rq.battle.states` for all of them.

Raises an error when a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

### rq.battle.states

```lua
rq.battle.states(iic) -> rq.BattleStates|nil
```

`since 0.31.0`

Returns every state of a character, also without `install_states`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `states` | [`rq.BattleStates`](../types/rq.BattleStates.md) `\|nil` | nil for a number that is no character. |

### rq.battle.set_state

```lua
rq.battle.set_state(iic, state, on) -> boolean
```

`since 0.31.0`

Adds or takes one state, by the rules of `install_states`, and the card shows it.

Taking stun from someone also poisoned does the poison's damage, because it counts as the stun
ending.

Raises an error for an unknown state, or before `rq.battle.install_states`.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's slot. |
| `state` | `"poison"\|"stun"\|"atk_up"\|"atk_down"\|"def_up"\|"def_down"` | The state. |
| `on` | `boolean` | true adds it, false takes it. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false for a number that is no character, or someone dead. |

### rq.battle.buffs

```lua
rq.battle.buffs(iic) -> rq.BuffInfo[]
```

`since 0.16.0` `changed 0.28.0`

Lists the marks a card shows in turn.

They come by `order`, then the pinned ones. For someone switched out it lists their own buffs that
wait for their return. A game mark hidden by `set_mark` is not listed.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `marks` | [`rq.BuffInfo`](../types/rq.BuffInfo.md) `[]` | The marks in turn order. |

> Changed in 0.28.0: Enemies too.

### rq.battle.get_drop

```lua
rq.battle.get_drop() -> integer
```

`since 0.9.0` `changed 2.34.0`

Returns the item a won fight hands out (`◆戦闘後アイテム取得`).

Read it inside `rq.battle.on_end` or `rq.battle.on_reward`: the game chooses it before the fight.

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number; 0 for none. |

> Changed in 2.34.0: Also in `rq.battle.on_reward`.

### rq.battle.set_drop

```lua
rq.battle.set_drop(who)
```

`since 0.9.0` `changed 2.34.0`

Sets the item a won fight hands out.

Set it inside `rq.battle.on_end` or `rq.battle.on_reward`. The game then skips its own drop rules
and puts the item in quest storage, which goes to the vault after the result screen.

Raises an error for a value that is not a number, a text id, nil or false.

```lua
rq.battle.on_end(function(ctx)
  if ctx.boss then rq.battle.set_drop("mymod:crown") end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer\|nil\|false` | An item number or text id; nil or false clears it. |

> Changed in 2.34.0: Also in `rq.battle.on_reward`.

### rq.battle.bags

```lua
rq.battle.bags() -> rq.BagInfo[]
```

`since 2.34.0`

Lists the gold bags of the fight's enemies.

At a fight's start the game gives each enemy a bag at 50%. When an enemy with a bag falls, the bag
shows where it stood and is picked up; the bags picked set the fight's gold (`rq.battle.on_reward`'s
`bags`). The game rolls the bags after `rq.battle.on_start`, so there the list shows only the bags a
mod set with `rq.battle.set_bag`.

Raises an error at the top level of a mod.

| Returns | Type | Description |
| --- | --- | --- |
| `bags` | [`rq.BagInfo`](../types/rq.BagInfo.md) `[]` | One entry per enemy, in the game's order; empty outside a fight. |

### rq.battle.set_bag

```lua
rq.battle.set_bag(iic, carries) -> boolean
```

`since 2.34.0`

Gives an enemy a gold bag, or takes its bag away, before it falls.

The bag shows where the enemy stood when it falls, as the game's, and the gold follows the game's
table for the bags picked: one bag a quarter of the quest's gold, two a half, three all of it, four
twice, five four times. Called in `rq.battle.on_start`, it is kept and written over the game's roll.

Raises an error for a slot that is not an enemy of this fight, for `carries` that is not a
boolean, and at the top level of a mod.

```lua
--- Every enemy carries a bag
rq.battle.on_start(function(ctx)
  for _, e in ipairs(ctx.enemies) do rq.battle.set_bag(e, true) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The enemy's slot. |
| `carries` | `boolean` | true for a bag, false for none. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false for an enemy that already fell, or whose bag was picked up. |

### rq.battle.set_face

```lua
rq.battle.set_face(iic, face, opts) -> boolean
```

`since 1.12.0`

Shows another face for an ally on the cards in a fight.

Only the fight's cards change; the party bar, the status pages and the scenes keep the game's. The
face lasts until changed, also in later fights. With `opts.ms` it is a face for a while, over the
lasting one, and it ends with the fight; nil with `ms` shows the game's own for a while. The game's
face sprite is drawn over, so the fight's moves, shakes, flashes and fades still show on it, and
the dead mark still covers it. The game's own faces are CGs too (Rance 2000, Lia 2150). Up to 64
characters.

Raises an error for a character, CG or GIF that is not there, an `ms` of 0 or less, or a 65th
character.

```lua
local HURT = rq.image.add("hurt", "hurt.png")
rq.battle.on_hp(function(ev)
  if ev.iic == rq.chara.find("mymod:alice") then  -- half HP or less: another face
    rq.battle.set_face(ev.iic, ev.hp > 0 and ev.hp * 2 <= ev.max and HURT or nil)
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The ally's roster slot. |
| `face` | `integer\|string\|nil` | A CG number, a GIF file in the mod's folder or an `rq.image.add_gif` key, stretched to 196×232; nil for the game's face. |
| `opts` *(optional)* | `{ms?: number, fps?: number, clock?: "game"\|"real"}` | `ms`: how long, for a face for a while. `fps`: GIF speed, as on a sprite. `clock`: "game" (default) or "real" time. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true. |

See also: [`rq.battle.get_face`](rq.battle.md#rqbattleget_face)

### rq.battle.get_face

```lua
rq.battle.get_face(iic) -> {face?: integer|string, temp?: integer|string, temp_ms?: integer, card?: integer, drawn: boolean}|nil
```

`since 1.12.0`

Returns what `rq.battle.set_face` set for a character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The ally's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `face` | `{face?: integer\|string, temp?: integer\|string, temp_ms?: integer, card?: integer, drawn: boolean}\|nil` | `face` the lasting face and `temp` the one for a while (a CG number or the GIF's name; left out for the game's), `temp_ms` the ms left, `card` the card (1 to 5) in a fight, `drawn` whether it was drawn in the last 250 ms; nil when nothing is set. |

### rq.battle.in_ally_select

```lua
rq.battle.in_ally_select() -> boolean
```

`since 0.2.0`

Returns whether an ally is choosing a skill.

It is true while `T_BattleSelect@select` is waiting. The first call places the hooks
(`rq.battle.install`): a select that was already open then is not seen.

| Returns | Type | Description |
| --- | --- | --- |
| `selecting` | `boolean` | true during ally skill select. |

### rq.battle.actor

```lua
rq.battle.actor() -> rq.BattleActor|nil
```

`since 0.2.0`

Returns the ally choosing a skill.

The first call places the hooks (`rq.battle.install`): a select that was already open then is not
seen.

| Returns | Type | Description |
| --- | --- | --- |
| `actor` | [`rq.BattleActor`](../types/rq.BattleActor.md) `\|nil` | The acting ally, or nil outside skill select. |

### rq.battle.skill_usable

```lua
rq.battle.skill_usable(actor, skill_no) -> boolean
```

`since 0.2.0` `changed 1.0.0`

Returns whether a character can use a skill now.

The skill must be equipped, have uses left and not be locked. While skill select is open it
answers like the skill's button: false when the button is greyed out, also for a front-row skill
from the back.

| Parameter | Type | Description |
| --- | --- | --- |
| `actor` | [`rq.BattleActor`](../types/rq.BattleActor.md) `\|integer` | An actor table (`chara` or `no`), or a roster slot. |
| `skill_no` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `usable` | `boolean` | true when the skill can be chosen. |

> Changed in 1.0.0: Answers like the button during skill select.

### rq.battle.start

```lua
rq.battle.start(opts) -> "won"|"lost"|"other", rq.FightResult
```

`since 0.22.0` `changed 2.22.1` `changed 2.36.0`

Opens a fight with the current party, using the game's scripted fight or its boss fight.

It blocks until the fight and its result screens end, as `rq.scene` commands do, while
`rq.on_frame` keeps running; call it from a job (`rq.spawn`) or a coroutine if the same mod plays
the fight. It counts as a fight of the current quest.

It may start from any screen with a footer: a quest's map, the town, Rance Castle, the Party
screen, Quests. While it runs, `rq.ui.get` says `battle`; after it, the screen it started from is
drawn again with its footer.

A won fight and one whose actions ran out pay (`rq.battle.on_reward`); a lost or fled one pays
nothing. The enemies are built as in any fight: `rq.monster.edit` and `rq.monster.on_create`
apply.

Raises an error for an unknown option or a value of the wrong kind, no enemies, an unknown
monster, `strong` or `double_hp` without `boss`, an unknown background or track, a music file
that is missing or outside the mod's folder, an empty party, or during a fight.

its footer, and `rq.ui.get` named that screen during the fight, not `battle`.
`escape` and `gold`, and the second value. An unknown option raises an error (it was ignored).

```lua
rq.spawn(function()
  local r, info = rq.battle.start({
    enemies = { 0, rq.ids.monster.COCKROACH, 0 }, exp = 500,
    boss = true, strong = true, names = { [2] = "The Shadow" },
    background = "bgA_00_douk", music = "music/shadow.ogg", gold = 1000,
  })
  rq.log(r, info.how, info.exp, info.gold, #info.fallen)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | [`rq.FightOpts`](../types/rq.FightOpts.md) | The fight. |

| Returns | Type | Description |
| --- | --- | --- |
| `result` | `"won"\|"lost"\|"other"` | How the fight ended: "other" for a draw, the actions run out or a flight. |
| `info` | [`rq.FightResult`](../types/rq.FightResult.md) | The end in detail and what the fight paid. Since 2.36.0. |

> Changed in 2.22.1: Away from a quest's map, the screen under the fight came back black and without

> Changed in 2.36.0: The options `boss`, `strong`, `double_hp`, `names`, `background`, `music`,

### rq.battle.backgrounds

```lua
rq.battle.backgrounds() -> rq.FightBackground[]
```

`since 2.36.0`

Lists the game's fight backgrounds, in the game's order.

Each map sets the background of its fights when it loads, by the map's kind;
`rq.battle.start`'s `background` chooses one for its own fight.

Raises an error before the game runs.

```lua
for _, b in ipairs(rq.battle.backgrounds()) do rq.log(b.no, b.name) end
```

| Returns | Type | Description |
| --- | --- | --- |
| `list` | [`rq.FightBackground`](../types/rq.FightBackground.md) `[]` | The backgrounds. |

### rq.battle.force_hit

```lua
rq.battle.force_hit(mode)
```

`since 0.22.0`

Decides every accuracy check, of allies and enemies, until `force_hit(nil)`.

The rest of the check runs as usual, so a miss still shows in the log, and a hit can still do 0
damage. The game keeps the last result in the global `◆攻撃外れた` (1 is a miss).

Raises an error for any other mode.

| Parameter | Type | Description |
| --- | --- | --- |
| `mode` | `"hit"\|"miss"\|nil` | The result every check gives; nil goes back to rolling. |

See also: [`rq.random.fix`](rq.random.md#rqrandomfix)

### rq.battle.time

```lua
rq.battle.time() -> integer
```

`since 0.26.0`

Returns the actions left in this fight, the number on the TIME REMAINING panel.

| Returns | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The actions left; 999 means no limit, 0 outside a fight. |

### rq.battle.set_time

```lua
rq.battle.set_time(n)
```

`since 0.26.0`

Sets the actions left in this fight.

The game sets the count again when a fight opens, so a value set outside one is lost.

Raises an error for a number that is not whole or not 0 to 999.

| Parameter | Type | Description |
| --- | --- | --- |
| `n` | `integer` | The actions left, 0 to 999; 999 means no limit. |

### rq.battle.snapshot

```lua
rq.battle.snapshot() -> rq.BattleSnap
```

`since 0.2.0`

Returns a copy of what the fight screen shows.

| Returns | Type | Description |
| --- | --- | --- |
| `snap` | [`rq.BattleSnap`](../types/rq.BattleSnap.md) | The allies, enemies, the actor's skills and the log. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.battle.on_select_key`](#rqbattleon_select_key) | Calls `fn` for each key pressed while an ally chooses a skill. |
| [`rq.battle.on_start`](#rqbattleon_start) | Calls `fn` once per fight, at the end of `Ｔ戦闘前初期化`. |
| [`rq.battle.on_end`](#rqbattleon_end) | Calls `fn` at the start of `戦闘後処理`, before the game cleans up the fight. |
| [`rq.battle.on_reward`](#rqbattleon_reward) | Calls `fn` once per fight that pays, after the game has summed the gold and EXP and before the result screen shows them. |
| [`rq.battle.on_support`](#rqbattleon_support) | Calls `fn` at the start of every support (blue) skill action (`Ｔ補助行動`). |
| [`rq.battle.on_down`](#rqbattleon_down) | Calls `fn` when the game sets a character to downed (`Ｃ状態変化` 3). |
| [`rq.battle.on_switch`](#rqbattleon_switch) | Calls `fn` for each ally rank that holds someone else after a switch in a fight. |
| [`rq.battle.on_use`](#rqbattleon_use) | Calls `fn` each time a skill is carried out, before its effects. |
| [`rq.battle.on_turn`](#rqbattleon_turn) | Calls `fn` at the start of every turn in a fight, for allies, enemies and familiars. |
| [`rq.battle.on_hit`](#rqbattleon_hit) | Calls `fn` after each attack or special skill on a target, with its result. |
| [`rq.battle.on_forecast`](#rqbattleon_forecast) | Calls `fn` each time the game builds a battle forecast line, to add text to it. |
| [`rq.battle.on_order`](#rqbattleon_order) | Calls `fn` each time the game builds the turn list, to change the speeds it is built from. |
| [`rq.battle.on_order_after`](#rqbattleon_order_after) | Calls `fn` each time the game has built the turn list, to read or replace it. |
| [`rq.battle.on_log`](#rqbattleon_log) | Calls `fn` for each line before it goes into the battle log, to drop or change it. |
| [`rq.battle.on_hp`](#rqbattleon_hp) | Calls `fn` in a fight each time a character's HP changes. |

### rq.battle.on_select_key

```lua
rq.battle.on_select_key(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0` `changed 2.35.0`

Calls `fn` for each key pressed while an ally chooses a skill.

Return a skill number (or `{ skill = n }`) to choose that skill, or nil to let the game handle the
key. Callbacks run in load order until one names a skill.

```lua
rq.battle.on_select_key(function(ctx)
  if ctx.key ~= 32 then return nil end
  local a = rq.battle.actor()
  if a and rq.battle.skill_usable(a, 384) then return 384 end  -- Space: Standby
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleSelectKeyCtx`](../types/rq.BattleSelectKeyCtx.md) `): integer\|{skill: integer}\|nil` | Returns the skill to choose. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs until one names a skill (before, the last one won).

> Changed in 0.23.0: Returns a remover.

> Changed in 2.35.0: Places its hooks itself; before, it needed `rq.battle.install`.

### rq.battle.on_start

```lua
rq.battle.on_start(fn) -> fun()
```

`since 0.5.0` `changed 0.23.0` `changed 2.37.0`

Calls `fn` once per fight, at the end of `Ｔ戦闘前初期化`.

Every start-of-fight effect of the game has already run (skills such as Cough, an ambush, poison
tea), so `rq.chara.get` and `set` on the lists see the real state. The enemies were built before
it: change how they are built with `rq.monster.on_create`. In a fight of `rq.battle.start`, its
`escape` is written before the first callback.

The ambush is decided by then (`ctx.ambush`); `rq.battle.set_ambush` changes it here, before the
turn list is built. The escape chance is `rq.battle.escape` and `set_escape`.

```lua
rq.battle.on_start(function(ctx)
  for _, a in ipairs(ctx.allies) do rq.chara.set(a, { status = 0 }) end  -- clear poison
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleStartCtx`](../types/rq.BattleStartCtx.md) `)` | Gets the fight. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.37.0: `ctx.ambush` and `first_striker`.

### rq.battle.on_end

```lua
rq.battle.on_end(fn) -> fun()
```

`since 0.5.0` `changed 0.23.0`

Calls `fn` at the start of `戦闘後処理`, before the game cleans up the fight.

Set a drop here with `rq.battle.set_drop`. The fight's gold has been paid and the party's EXP
given by then: change them in `rq.battle.on_reward`, which the result screen shows.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleEndCtx`](../types/rq.BattleEndCtx.md) `)` | Gets the fight and its result. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

### rq.battle.on_reward

```lua
rq.battle.on_reward(fn) -> fun()
```

`since 2.34.0`

Calls `fn` once per fight that pays, after the game has summed the gold and EXP and before the result screen shows them.

What the callbacks leave is what the result screen shows, what the party gets and the gold paid.
In a fight of `rq.battle.start` with `gold`, `ctx.gold` holds that gold when the first callback runs.
Callbacks run in load order, each one reading what the ones before wrote. A fight the enemies ran
from pays as a won one does (`ctx.result` 4); a fight lost pays nothing and calls nothing.

The rest follows the new numbers: the quest's EXP total (a twentieth of which goes to the
characters in training at the quest's end) moves with `ctx.exp`, an ally the new EXP levels up
counts toward the quest's level-up bonus, and the reserve gets `ctx.reserve` with the game's own
free level for a full bar (`rq.chara.on_level_up` reports it with `battle` and `free`). An ally
at 0 HP or at the cap gets no level, as with `rq.chara.add_exp`. The item a fight drops was chosen
before it: `rq.battle.get_drop` and `set_drop` work here too.

An error in a callback is logged once for each new error text; what it wrote before the error
stays.

```lua
--- Twice the EXP and half again the gold, on the result screen too
rq.battle.on_reward(function(ctx)
  ctx.exp = ctx.exp * 2
  ctx.gold = ctx.gold * 1.5
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.RewardCtx`](../types/rq.RewardCtx.md) `)` | Reads and changes the fight's rewards. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.battle.bags`](rq.battle.md#rqbattlebags)

### rq.battle.on_support

```lua
rq.battle.on_support(fn) -> fun()
```

`since 0.13.0` `changed 0.23.0`

Calls `fn` at the start of every support (blue) skill action (`Ｔ補助行動`).

It runs before the game applies its own effects. A skill a mod defined has no effect of its own,
so this is where Lua gives it one.

```lua
rq.battle.on_support(function(ctx)
  if ctx.skill == MY_SKILL then rq.chara.set(ctx.target, { status = 0 }) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleSupportCtx`](../types/rq.BattleSupportCtx.md) `)` | Gets the action. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

### rq.battle.on_down

```lua
rq.battle.on_down(fn) -> fun()
```

`since 0.12.0` `changed 0.23.0` `changed 1.3.1`

Calls `fn` when the game sets a character to downed (`Ｃ状態変化` 3).

Any cause counts: damage, poison, capture, instant death. It runs once per fall. A revive is not
reported.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleDownCtx`](../types/rq.BattleDownCtx.md) `)` | Gets the character. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 1.3.1: Once per fall; before, it could run again for a character already down.

### rq.battle.on_switch

```lua
rq.battle.on_switch(fn) -> fun()
```

`since 0.29.0`

Calls `fn` for each ally rank that holds someone else after a switch in a fight.

The new cards are already on screen. Someone who only moved shows up as `left` on one rank and
`came_in` on the other.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleSwitchCtx`](../types/rq.BattleSwitchCtx.md) `)` | Gets one rank. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.battle.on_use

```lua
rq.battle.on_use(fn) -> fun()
```

`since 0.25.0`

Calls `fn` each time a skill is carried out, before its effects.

It runs for allies, enemies and summons, once per hit of a multi-hit skill, and for a counter
too. It only reports: it cannot change or stop the skill.

```lua
rq.battle.on_use(function(ev)
  if ev.side == "enemy" then rq.log("enemy used", ev.skill) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.BattleUseEvent`](../types/rq.BattleUseEvent.md) `)` | Gets the action. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

### rq.battle.on_turn

```lua
rq.battle.on_turn(fn) -> fun()
```

`since 2.1.0` `changed 2.3.0`

Calls `fn` at the start of every turn in a fight, for allies, enemies and familiars.

It runs after the game's own start of a turn (`Ｔ行動開始`): the stun has ended, the poison and
regeneration have been done, and nothing is shown yet. Damage and healing from `ctx` then show
with the game's own number and effect, as poison and regeneration do. It also runs on the turn a
stun ends, and for a petrified Kaloria, with `ctx.passing` true. A familiar's turn has no card,
so its damage and healing are not shown. Callbacks run in load order; an error in one is logged
and the next still runs.

This is where a mod state does its work each turn: a burn's damage, a regeneration, a freeze
that skips the turn. A lethal `ctx:damage` may down the character (see `BattleTurnCtx:damage`).

```lua
local burning = {}  -- iic -> turns left
rq.battle.on_turn(function(ctx)
  local left = burning[ctx.iic]
  if not left then return end
  local hp_max = rq.chara.get(ctx.iic).hp_max
  ctx:damage(math.max(1, hp_max // 20))
  ctx:log(" " .. rq.chara.get(ctx.iic).short .. " is burning.")
  burning[ctx.iic] = left > 1 and left - 1 or nil
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleTurnCtx`](../types/rq.BattleTurnCtx.md) `)` | Gets the turn. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.3.0: Lethal damage, and `ctx.downed`.

See also: [`rq.battle.on_hit`](rq.battle.md#rqbattleon_hit)

### rq.battle.on_hit

```lua
rq.battle.on_hit(fn) -> fun()
```

`since 2.1.0` `changed 2.26.0`

Calls `fn` after each attack or special skill on a target, with its result.

It runs once per target and per hit: each hit of a multi-hit skill, each target of a skill on
many, and a counter, for allies, enemies and familiars. A miss is reported too, with `missed`
true. The damage is already taken from the HP, and the hit is not shown yet. The turn a skill
only starts to charge is not a hit and is not reported. Special skills (action kind 3: the
taunt, stuns, poisons and captures, and a mod's skill patched to `action = 3`) come with `kind`
"special", so a debuff skill that does no damage can put a state on. Support skills do not; use
`rq.battle.on_support` or `rq.battle.on_use` for them.

This is where a hit gives a mod state.

```lua
rq.battle.on_hit(function(ctx)
  if ctx.skill == FIRE_SLASH and not ctx.missed and not ctx.downed and math.random(100) <= 40 then
    burning[ctx.defender] = 3
    ctx:log(" (Burn)")
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleHitCtx`](../types/rq.BattleHitCtx.md) `)` | Gets the hit. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.26.0: Special skills, with `kind` "special".

See also: [`rq.battle.on_turn`](rq.battle.md#rqbattleon_turn), [`rq.battle.on_use`](rq.battle.md#rqbattleon_use)

### rq.battle.on_forecast

```lua
rq.battle.on_forecast(fn) -> fun()
```

`since 2.26.0`

Calls `fn` each time the game builds a battle forecast line, to add text to it.

With Battle Forecast (488) in the party, the game shows the line when the player points a skill
at a target: the hit chance, the stun chance and a damage word for an attack, the capture rate
for a capture. The line is built again on every hover, so `fn` must be quick and roll no dice.
The strings of every callback are added in load order. The damage word already counts mod states
and the `rq.combat` callbacks, which run with `ctx.forecast` true.

Raises an error, logged, for a return that is not a string or nil.

```lua
rq.battle.on_forecast(function(ctx)
  if ctx.skill == FIRE_SLASH then return "  Burn 40%" end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleForecastCtx`](../types/rq.BattleForecastCtx.md) `): string\|nil` | Returns text to add, starting with spaces as the game's parts do, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.combat.on_physical`](rq.combat.md#rqcombaton_physical)

### rq.battle.on_order

```lua
rq.battle.on_order(fn) -> fun()
```

`since 2.37.0`

Calls `fn` each time the game builds the turn list, to change the speeds it is built from.

The game builds the whole list of a fight's turns at its start (`Ｔ順番生成`) and again after a
switch, a shuffle or a revive, reading each unit's speed there and nowhere else in a fight.
`ctx:speed` sets a speed for that build only. Each round of the list every unit takes its speed,
with chance, from a box of 300 and gets an entry when it is empty; a unit far faster gets
several entries a round. The game's other rules stay: Head Start, the first entries of an ambush,
the catch-up of a unit with no turn yet, an enemy far slower than the party sped up half the time.

The familiar's unit has `owner`, `item` and `own_spd`: the game holds a familiar's speed to the
party's top speed when it builds it, and `own_spd` is the speed before that.

```lua
rq.battle.on_order(function(ctx)
  for _, u in ipairs(ctx.units) do
    if hasted[u.iic] then ctx:speed(u.iic, u.spd * 6 // 5) end -- a fifth faster
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleOrderCtx`](../types/rq.BattleOrderCtx.md) `)` | Gets the units before the build. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.battle.on_order_after`](rq.battle.md#rqbattleon_order_after)

### rq.battle.on_order_after

```lua
rq.battle.on_order_after(fn) -> fun()
```

`since 2.37.0`

Calls `fn` each time the game has built the turn list, to read or replace it.

It runs after `rq.battle.on_order`'s build, before the turn icons are made from the list. Each
callback sees in `ctx.order` the list the one before left.

```lua
rq.battle.on_order_after(function(ctx)
  if not ctx.rebuild and first_mover then
    local list = ctx.order
    table.insert(list, 1, first_mover) -- one more turn for them, first
    if #list > 50 then list[51] = nil end
    ctx:set_order(list)
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleOrderAfterCtx`](../types/rq.BattleOrderAfterCtx.md) `)` | Gets the list. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.battle.on_order`](rq.battle.md#rqbattleon_order)

### rq.battle.on_log

```lua
rq.battle.on_log(fn) -> fun()
```

`since 2.37.0`

Calls `fn` for each line before it goes into the battle log, to drop or change it.

Every line goes through it: a turn's two lines (with the text of `rq.battle.on_turn`'s and
`on_hit`'s `ctx:log` in them), the game's notices at a fight's start (terrain, a familiar called,
Cough-Cough Disease), a familiar's cut-in, the end message, and `rq.battle.log`. `fn` returns false
to drop the line, a string to put in its place, or nil to keep it. After a false the later
callbacks do not see the line. A line added with `rq.battle.log` from inside `fn` goes into the
log without passing through `on_log` again. An empty line is never added.

Raises an error, logged, for a return that is not false, a string or nil.

```lua
rq.battle.on_log(function(ctx)
  return (ctx.text:gsub("Poison", "Venom")) -- the game's word in this mod's world
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleLogCtx`](../types/rq.BattleLogCtx.md) `): string\|false\|nil` | Returns false, a new line, or nil. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.battle.log`](rq.battle.md#rqbattlelog)

### rq.battle.on_hp

```lua
rq.battle.on_hp(fn) -> fun()
```

`since 1.12.0`

Calls `fn` in a fight each time a character's HP changes.

Damage, healing, revival and a mod's `rq.chara.set` all count, for allies and enemies. It also runs
once with `first = true` when a character is first seen on a card, so one callback can set the
first face too. HP is read once a frame, so two changes in one frame come as one. Up to 64
callbacks.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ev:` [`rq.HpEvent`](../types/rq.HpEvent.md) `)` | Gets the change. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
