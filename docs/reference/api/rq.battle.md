# rq.battle

`since 0.2.0`

Hooks into fights: events, ally skill select, marks and buffs on the cards, faces, states, drops,
and scripted fights.

Each event (`on_*`) installs its hook on first use; most hold up to 16 callbacks. The ally skill
select calls need `rq.battle.install`, `set_flame` and `set_mark` need `rq.battle.install_flame`,
and `set_state` needs `rq.battle.install_states`.

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
| [`rq.battle.set_face`](#rqbattleset_face) | Shows another face for an ally on the cards in a fight. |
| [`rq.battle.get_face`](#rqbattleget_face) | Returns what `rq.battle.set_face` set for a character. |
| [`rq.battle.in_ally_select`](#rqbattlein_ally_select) | Returns whether an ally is choosing a skill. |
| [`rq.battle.actor`](#rqbattleactor) | Returns the ally choosing a skill. |
| [`rq.battle.skill_usable`](#rqbattleskill_usable) | Returns whether a character can use a skill now. |
| [`rq.battle.start`](#rqbattlestart) | Opens a fight with the current party, using the game's scripted fight. |
| [`rq.battle.force_hit`](#rqbattleforce_hit) | Decides every accuracy check, of allies and enemies, until `force_hit(nil)`. |
| [`rq.battle.time`](#rqbattletime) | Returns the actions left in this fight, the number on the TIME REMAINING panel. |
| [`rq.battle.set_time`](#rqbattleset_time) | Sets the actions left in this fight. |
| [`rq.battle.snapshot`](#rqbattlesnapshot) | Returns a copy of what the fight screen shows. |

### rq.battle.install

```lua
rq.battle.install() -> boolean
```

`since 0.2.0`

Installs the ally skill select hooks.

It wraps `T_BattleSelect@select`, `@checkKey` and `@exec`, so a key that `on_select_key` claims
completes the select like a click on that skill: the key is swallowed (Space does not also
Cancel), and the skill runs on the actor itself.

Raises an error when the AIN is not loaded or a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

### rq.battle.install_flame

```lua
rq.battle.install_flame() -> boolean
```

`since 0.12.0`

Installs the hooks the flame, the buffs and the marks need.

It hooks the ally status refresh so `set_flame` sticks, and installs the fight start and end
events, which clear the flames and buffs. Call it once at the top of `init.lua`.

Raises an error when a hook cannot be placed.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

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

Raises an error before `rq.battle.install_flame`.

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
Needs `rq.battle.install_flame`.

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

`since 0.9.0`

Returns the item a won fight hands out (`◆戦闘後アイテム取得`).

Read it inside `rq.battle.on_end`.

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number; 0 for none. |

### rq.battle.set_drop

```lua
rq.battle.set_drop(who)
```

`since 0.9.0`

Sets the item a won fight hands out.

Set it inside `rq.battle.on_end`. The game then skips its own drop rules and puts the item in quest
storage, which goes to the vault after the result screen.

Raises an error for a value that is not a number, a text id, nil or false.

```lua
rq.battle.on_end(function(ctx)
  if ctx.boss then rq.battle.set_drop("mymod:crown") end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer\|nil\|false` | An item number or text id; nil or false clears it. |

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

It is true while `T_BattleSelect@select` is waiting. Needs `rq.battle.install`.

| Returns | Type | Description |
| --- | --- | --- |
| `selecting` | `boolean` | true during ally skill select. |

### rq.battle.actor

```lua
rq.battle.actor() -> rq.BattleActor|nil
```

`since 0.2.0`

Returns the ally choosing a skill.

Needs `rq.battle.install`.

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
rq.battle.start(opts) -> "won"|"lost"|"other"
```

`since 0.22.0`

Opens a fight with the current party, using the game's scripted fight.

It blocks until the fight and its result screens end, as `rq.scene` commands do, while
`rq.on_frame` keeps running; call it from a coroutine if the same mod plays the fight. It counts as
a fight of the current quest.

Raises an error for no enemies, an unknown monster, an empty party, or during a fight.

```lua
coroutine.wrap(function()
  local result = rq.battle.start({ enemies = { 0, boss_no, 0 } })
  rq.log("fight:", result)
end)()
```

| Parameter | Type | Description |
| --- | --- | --- |
| `opts` | `{enemies: integer[], exp?: integer}` | `enemies`: up to five monster numbers in rank order, 0 for an empty rank. `exp`: experience for the win. Default 0. |

| Returns | Type | Description |
| --- | --- | --- |
| `result` | `"won"\|"lost"\|"other"` | How the fight ended. |

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
| [`rq.battle.on_support`](#rqbattleon_support) | Calls `fn` at the start of every support (blue) skill action (`Ｔ補助行動`). |
| [`rq.battle.on_down`](#rqbattleon_down) | Calls `fn` when the game sets a character to downed (`Ｃ状態変化` 3). |
| [`rq.battle.on_switch`](#rqbattleon_switch) | Calls `fn` for each ally rank that holds someone else after a switch in a fight. |
| [`rq.battle.on_use`](#rqbattleon_use) | Calls `fn` each time a skill is carried out, before its effects. |
| [`rq.battle.on_hp`](#rqbattleon_hp) | Calls `fn` in a fight each time a character's HP changes. |

### rq.battle.on_select_key

```lua
rq.battle.on_select_key(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` for each key pressed while an ally chooses a skill.

Return a skill number (or `{ skill = n }`) to choose that skill, or nil to let the game handle the
key. Callbacks run in load order until one names a skill. Needs `rq.battle.install`.

```lua
rq.battle.install()
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

### rq.battle.on_start

```lua
rq.battle.on_start(fn) -> fun()
```

`since 0.5.0` `changed 0.23.0`

Calls `fn` once per fight, at the end of `Ｔ戦闘前初期化`.

Every start-of-fight effect of the game has already run (skills such as Cough, an ambush, poison
tea), so `rq.chara.get` and `set` on the lists see the real state.

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

### rq.battle.on_end

```lua
rq.battle.on_end(fn) -> fun()
```

`since 0.5.0` `changed 0.23.0`

Calls `fn` at the start of `戦闘後処理`, before the game cleans up the fight.

Set a drop here with `rq.battle.set_drop`.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BattleEndCtx`](../types/rq.BattleEndCtx.md) `)` | Gets the fight and its result. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

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
