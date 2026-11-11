# rq.chara

`since 0.2.0` `changed 0.4.0`

Reads and changes characters: their skills, stats, the skill buy list, and the roster.

The calls work on a roster slot, the `iic` (the `id` of an entry in `rq.units()`), unless they say
`who`: those take a character number or a mod's text id. Base-game numbers include Rance 1, Kaoru
52, Onoha 62 and Rebecca 81.

**Skills and the buy list.** `grant`, `rank`, `slots`, `set_slot`, `set_flavor`, `weapon_detail`,
`apply_mod`, `on_recalc`, `on_offer`, `offers`, `set_offer`, `set_uses`, `set_bar`, `clear_slot` and
`max_uses` need `rq.chara.install` first.

**Roster.** `define` registers a template; the character exists, and joins the player's roster,
only when `recruit` runs, so a mod can give it from a quest or an event. `recruit` also works for
base-game characters. A text id such as `"mymod:alice"` becomes a number from 1000 up, the same
number every time, so saves stay valid. The roster has 181 slots (20 to 200). The roster calls
install what they need on first use.

```lua
-- Create now, provide later
rq.chara.define({ id = "mymod:alice", name = "Alice", class = 1, level = 5, slots = 4,
  init = { atk = 10 }, skills = { { id = 100, n = 8 } } })
if rq.store.get("alice_joined") ~= true then
  local iic = rq.chara.recruit("mymod:alice", { state = 2 })
  if iic then rq.store.set("alice_joined", true) end
end

-- Edit a base-game character, also in old saves: Onoha gets Head Start 2 (skill 246)
rq.chara.edit(62, { init = { eva = 50, spd = 25 }, learn = { { id = 246, n = 2 } } })
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.chara.install`](#rqcharainstall) | Installs the hooks the skill and buy-list calls need. |
| [`rq.chara.grant`](#rqcharagrant) | Gives a character a skill (`ＣＳ追加`). |
| [`rq.chara.rank`](#rqchararank) | Returns a character's rank in a skill (`ＣＳ有無／ランク`). |
| [`rq.chara.slots`](#rqcharaslots) | Lists the rows of a character's skill list that hold a skill. |
| [`rq.chara.set_slot`](#rqcharaset_slot) | Writes the skill number of a skill-list row (`ＣＳ番号`). |
| [`rq.chara.set_flavor`](#rqcharaset_flavor) | Copies the battle-log line (`Ｓ表示文`) of a row's current skill to the character. |
| [`rq.chara.weapon_detail`](#rqcharaweapon_detail) | Returns the weapon kind of the character's equipped weapon (`Ｉ種類詳細`). |
| [`rq.chara.apply_mod`](#rqcharaapply_mod) | Applies a stat change the way the game's own skills do (`Ｃ機能適応`). |
| [`rq.chara.offers`](#rqcharaoffers) | Lists the rows of the skill buy list that hold a skill. |
| [`rq.chara.set_offer`](#rqcharaset_offer) | Replaces the skill in a buy-list row. |
| [`rq.chara.set_uses`](#rqcharaset_uses) | Sets the uses left and the most uses of a skill-list row. |
| [`rq.chara.set_bar`](#rqcharaset_bar) | Puts a skill-list row on the hotbar, or takes it off (`ＣＳ実装中`). |
| [`rq.chara.clear_slot`](#rqcharaclear_slot) | Empties a skill-list row (`ＣＳ初期化`). |
| [`rq.chara.max_uses`](#rqcharamax_uses) | Returns the most uses a character has of a skill (`ＣＳ有無／最大回数`). |
| [`rq.chara.define`](#rqcharadefine) | Registers a character template. |
| [`rq.chara.recruit`](#rqchararecruit) | Creates a character in the roster (`Ｃ生成`), or finds the one already there. |
| [`rq.chara.find`](#rqcharafind) | Returns the roster slot of a character (`Ｃ番号取得`). |
| [`rq.chara.is_recruited`](#rqcharais_recruited) | Returns whether a character is in the roster. |
| [`rq.chara.recalc`](#rqchararecalc) | Recalculates a character now (`Ｃ再計算`). |
| [`rq.chara.absorbed`](#rqcharaabsorbed) | Returns the five items a Morurun absorbed: item numbers, 0 for an empty slot. |
| [`rq.chara.set_absorbed`](#rqcharaset_absorbed) | Changes one of the five absorbed items, then recalculates the character. |
| [`rq.chara.dismiss`](#rqcharadismiss) | Removes a character from the roster (`Ｃ削除`). |
| [`rq.chara.number`](#rqcharanumber) | Returns the character number in a roster slot. |
| [`rq.chara.id_of`](#rqcharaid_of) | Returns the text id of a defined character number. |
| [`rq.chara.edit`](#rqcharaedit) | Patches a character, again at the end of every recalculation, so it covers old saves too. |
| [`rq.chara.get`](#rqcharaget) | Returns everything known about a character. |
| [`rq.chara.set`](#rqcharaset) | Writes character fields by the names `rq.chara.get` uses. |
| [`rq.chara.skill_points`](#rqcharaskill_points) | Returns a character's free skill points. |
| [`rq.chara.add_skill_points`](#rqcharaadd_skill_points) | Adds to a character's free skill points. |
| [`rq.chara.forget`](#rqcharaforget) | Removes a skill from a character (`ＣＳ削除`). |
| [`rq.chara.add_exp`](#rqcharaadd_exp) | Gives a character EXP, as a fight's result does, and the levels it fills. |
| [`rq.chara.level_up`](#rqcharalevel_up) | Raises a character's level for free, as the game's story and training do. |

### rq.chara.install

```lua
rq.chara.install() -> boolean
```

`since 0.2.0`

Installs the hooks the skill and buy-list calls need.

It hooks the end of `Ｃ再計算` (the recalculation, after the game's own spear rewrite) and of
`Ｔ購入スキル登録` (the buy list), and the combat sites `rq.combat` uses. Calling it again, or after
`rq.combat.install`, does nothing more. Call it at the top of `init.lua`.

Raises an error when the AIN is not loaded or a hook cannot be placed (the reason is in the log).

```lua
rq.chara.install()
```

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

### rq.chara.grant

```lua
rq.chara.grant(iic, skillId, n) -> integer
```

`since 0.2.0`

Gives a character a skill (`ＣＳ追加`).

Raises an error for a slot with no character or a skill number outside 1 to 1000.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skillId` | `integer` | The skill number. |
| `n` | `integer` | The rank for a knowledge skill (type 30), or the uses for an active skill (type 10). |

| Returns | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | The skill-list row it went to. |

### rq.chara.rank

```lua
rq.chara.rank(iic, skillId) -> integer
```

`since 0.2.0`

Returns a character's rank in a skill (`ＣＳ有無／ランク`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skillId` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `rank` | `integer` | 1 to 4 (no star through three stars); 0 when the character does not have the skill or there is no character. |

### rq.chara.slots

```lua
rq.chara.slots(iic) -> rq.CharaSlot[]
```

`since 0.2.0`

Lists the rows of a character's skill list that hold a skill.

The game's screens show 6 hotbar positions, so a `slots` value above 6 adds rows but no positions.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `slots` | [`rq.CharaSlot`](../types/rq.CharaSlot.md) `[]` | The rows in order; empty when there is no character. |

### rq.chara.set_slot

```lua
rq.chara.set_slot(iic, slot, skillId)
```

`since 0.2.0`

Writes the skill number of a skill-list row (`ＣＳ番号`).

Only the number changes; the uses and the battle-log line stay. See `rq.chara.set_flavor`.

Raises an error for a slot with no character or a skill number outside 0 to 1000.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | The skill-list row. |
| `skillId` | `integer` | The skill number; 0 empties the number. |

### rq.chara.set_flavor

```lua
rq.chara.set_flavor(iic, slot)
```

`since 0.2.0`

Copies the battle-log line (`Ｓ表示文`) of a row's current skill to the character.

The game's own slot swaps skip this, so call it after `rq.chara.set_slot`.

Raises an error for a slot with no character or a row under 1.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | The skill-list row. |

### rq.chara.weapon_detail

```lua
rq.chara.weapon_detail(iic) -> integer
```

`since 0.2.0`

Returns the weapon kind of the character's equipped weapon (`Ｉ種類詳細`).

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `kind` | `integer` | Sword 2, spear or naginata 7, glove 9; 0 when there is no character. |

### rq.chara.apply_mod

```lua
rq.chara.apply_mod(iic, kind, amount, scale)
```

`since 0.2.0`

Applies a stat change the way the game's own skills do (`Ｃ機能適応`).

Call it from `rq.chara.on_recalc`, so it is applied on every recalculation.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `kind` | `integer` | The stat, as the game numbers it: accuracy 8, magic 14. |
| `amount` | `integer` | How much to add. |
| `scale` *(optional)* | `integer` | The percent of `amount` applied. Default 100. |

### rq.chara.offers

```lua
rq.chara.offers() -> rq.OfferRow[]
```

`since 0.2.0` `changed 2.18.0`

Lists the rows of the skill buy list that hold a skill.

They are the game's `取得可能スキル`: rows 1 to 60, or 1 to 144 with `rq.skilllist` on.

| Returns | Type | Description |
| --- | --- | --- |
| `rows` | [`rq.OfferRow`](../types/rq.OfferRow.md) `[]` | The rows in order; empty when there is no buy list. |

> Changed in 2.18.0: With `rq.skilllist`, the game's own arrays (made longer) instead of the engine's copy.

### rq.chara.set_offer

```lua
rq.chara.set_offer(index, skillId, points)
```

`since 0.2.0`

Replaces the skill in a buy-list row.

It writes the game's list. The row's level text stays as it is.

Raises an error for an index outside the list, or for `points` when the game has no price list.

| Parameter | Type | Description |
| --- | --- | --- |
| `index` | `integer` | The row's index, as `rq.chara.offers` gives it. |
| `skillId` | `integer` | The skill number. |
| `points` *(optional)* | `integer` | The new price in skill points. Default: the price stays. |

### rq.chara.set_uses

```lua
rq.chara.set_uses(iic, slot, uses, max)
```

`since 0.2.0`

Sets the uses left and the most uses of a skill-list row.

The most uses is written first; the game caps it at 99.

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | The skill-list row. |
| `uses` | `integer` | Uses left. |
| `max` | `integer` | Most uses. |

### rq.chara.set_bar

```lua
rq.chara.set_bar(iic, slot, pos)
```

`since 0.2.0`

Puts a skill-list row on the hotbar, or takes it off (`ＣＳ実装中`).

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | The skill-list row. |
| `pos` | `integer` | The hotbar position, 1 to 6; 0 takes it off. |

### rq.chara.clear_slot

```lua
rq.chara.clear_slot(iic, slot)
```

`since 0.2.0`

Empties a skill-list row (`ＣＳ初期化`).

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | The skill-list row. |

### rq.chara.max_uses

```lua
rq.chara.max_uses(iic, skillId) -> integer
```

`since 0.2.0`

Returns the most uses a character has of a skill (`ＣＳ有無／最大回数`).

This is what the game's price (`スキルポン`) reads when it raises the cost of another use.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skillId` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `max` | `integer` | The most uses; 0 when the character does not have the skill or there is no character. |

### rq.chara.define

```lua
rq.chara.define(def) -> integer
```

`since 0.4.0`

Registers a character template.

Nothing joins the roster until `rq.chara.recruit`. Defining the same id again replaces the
template. Up to 96 templates.

Raises an error for a missing or too long id, an id whose number another id already has, or a
97th template.

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.CharaDef`](../types/rq.CharaDef.md) | The template. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The character number the id maps to, 1000 or more. |

See also: [`rq.chara.recruit`](rq.chara.md#rqchararecruit)

### rq.chara.recruit

```lua
rq.chara.recruit(who, opts) -> integer|nil, string?
```

`since 0.4.0` `changed 0.6.0`

Creates a character in the roster (`Ｃ生成`), or finds the one already there.

Works for a defined id and for a base-game number. `opts` applies also to a character already in
the roster. The Party tab's list is refreshed.

Raises an error for a number of 1000 or more that no template has.

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | A text id or a character number. |
| `opts` *(optional)* | [`rq.RecruitOpts`](../types/rq.RecruitOpts.md) | Where the new character goes. |

| Returns | Type | Description |
| --- | --- | --- |
| `iic` | `integer\|nil` | The roster slot, or nil when the game refused. |
| `err` | `string?` | Why the game refused, such as a full roster. |

> Changed in 0.6.0: Refreshes the Party tab's list.

### rq.chara.find

```lua
rq.chara.find(who) -> integer|nil
```

`since 0.4.0`

Returns the roster slot of a character (`Ｃ番号取得`).

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | A text id or a character number. |

| Returns | Type | Description |
| --- | --- | --- |
| `iic` | `integer\|nil` | The roster slot, or nil when the character is not in the roster. |

### rq.chara.is_recruited

```lua
rq.chara.is_recruited(who) -> boolean
```

`since 0.4.0`

Returns whether a character is in the roster.

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | A text id or a character number. |

| Returns | Type | Description |
| --- | --- | --- |
| `recruited` | `boolean` | true when the character is in the roster. |

### rq.chara.recalc

```lua
rq.chara.recalc(iic, heal)
```

`since 0.5.0`

Recalculates a character now (`Ｃ再計算`).

Pending `rq.chara.edit` patches and `init` changes show at once.

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `heal` *(optional)* | `boolean` | true also refills HP and uses (`Ｃ補給`). Default false. |

### rq.chara.absorbed

```lua
rq.chara.absorbed(iic) -> integer[]
```

`since 2.23.0`

Returns the five items a Morurun absorbed: item numbers, 0 for an empty slot.

The game fills these slots when a Morurun takes in a special item (`Ｃ体内特殊アイテムの取得処理`):
kind 21 only, never 304 to 307, 309 or 310; the first empty slot; with all five full, a higher rank
replaces the first slot that holds a rank-1 item, and a rank-1 item is not taken. Every character
has the slots; in play only Morurun fill them.

Raises an error for a slot with no character.

```lua
for slot, no in ipairs(rq.chara.absorbed(iic)) do
  if no ~= 0 then rq.log(slot, rq.ids.name("item", no)) end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `items` | `integer[]` | Five item numbers, in slot order; 0 is empty. |

See also: [`rq.chara.set_absorbed`](rq.chara.md#rqcharaset_absorbed)

### rq.chara.set_absorbed

```lua
rq.chara.set_absorbed(iic, slot, no)
```

`since 2.23.0`

Changes one of the five absorbed items, then recalculates the character.

Only the slot changes: taking an instance from the vault, giving the old item back, drawing the
status page again (`rq.statuspage.refresh`) and a sound are the mod's. The recalculation also
refills HP and uses outside a quest. It does not check that the character is a Morurun.

Raises an error for a slot with no character, a slot outside 1 to 5, an item that is not a special
item (kind 21) or one the game never absorbs (304 to 307, 309, 310).

```lua
rq.chara.set_absorbed(iic, 1, 0)   -- empty slot 1
rq.chara.set_absorbed(iic, 2, 274) -- put item 274 in slot 2
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `slot` | `integer` | 1 to 5. |
| `no` | `integer` | The item number, or 0 to empty the slot. |

See also: [`rq.chara.absorbed`](rq.chara.md#rqcharaabsorbed)

### rq.chara.dismiss

```lua
rq.chara.dismiss(iic)
```

`since 0.4.0` `changed 0.6.0`

Removes a character from the roster (`Ｃ削除`).

The character leaves the party first. The Party tab's list is refreshed.

Raises an error for an empty slot or a slot under 20.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

> Changed in 0.6.0: Refreshes the Party tab's list.

### rq.chara.number

```lua
rq.chara.number(iic) -> integer|nil
```

`since 0.4.0`

Returns the character number in a roster slot.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer\|nil` | The character number, or nil when the slot is empty. |

### rq.chara.id_of

```lua
rq.chara.id_of(no) -> string|nil
```

`since 0.4.0`

Returns the text id of a defined character number.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The character number. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The text id, or nil when no mod defined that number. |

### rq.chara.edit

```lua
rq.chara.edit(who, patch)
```

`since 0.4.0` `changed 1.2.1`

Patches a character, again at the end of every recalculation, so it covers old saves too.

Each mod keeps one patch per character; calling again replaces it. Every edited character is
recalculated once right after a save loads. A patch made later, with the save already loaded,
waits for the character's next recalculation; `rq.chara.recalc` applies it now. `weapon`, `armor`,
`item` and `special` apply only when the character is created. Up to 192 patches.

```lua
rq.chara.edit("mymod:alice", { init = { spd = 10 }, weakness_known = true })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | A text id or a character number (not a roster slot). |
| `patch` | [`rq.CharaEdit`](../types/rq.CharaEdit.md) | The fields to set. |

> Changed in 1.2.1: Edited characters are recalculated once after a save loads.

### rq.chara.get

```lua
rq.chara.get(iic) -> rq.CharaState|nil
```

`since 0.4.0` `changed 0.5.0`

Returns everything known about a character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `state` | [`rq.CharaState`](../types/rq.CharaState.md) `\|nil` | A copy of the character's fields, or nil when there is no character. |

> Changed in 0.5.0: Added the battle-state fields.

### rq.chara.set

```lua
rq.chara.set(iic, fields)
```

`since 0.4.0`

Writes character fields by the names `rq.chara.get` uses.

`slots`, `name`, `short` and `face_name` work too, and `face` and `portrait` take an image path
inside the mod's folder. A change to a derived stat (`hp_max`, `atk`, ...) lasts only until the
next recalculation: use `init_*`, or `rq.chara.edit` to keep it.

Raises an error for a slot with no character or an unknown field.

```lua
rq.chara.set(iic, { hp = 1, weakness_known = true })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `fields` | `table` | Field names and new values. |

### rq.chara.skill_points

```lua
rq.chara.skill_points(iic) -> integer
```

`since 0.4.0`

Returns a character's free skill points.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `points` | `integer` | The free skill points; 0 when there is no character. |

### rq.chara.add_skill_points

```lua
rq.chara.add_skill_points(iic, delta) -> integer
```

`since 0.4.0`

Adds to a character's free skill points.

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `delta` | `integer` | Points to add; negative takes away. |

| Returns | Type | Description |
| --- | --- | --- |
| `total` | `integer` | The new total, never below 0. |

### rq.chara.forget

```lua
rq.chara.forget(iic, skill) -> boolean, integer?
```

`since 0.4.0`

Removes a skill from a character (`ＣＳ削除`).

`rq.chara.on_forget` callbacks run, with `caller` "lua".

Raises an error for a slot with no character.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when the character did not have the skill. |
| `cost` | `integer?` | The skill points the character had paid for it. |

### rq.chara.add_exp

```lua
rq.chara.add_exp(iic, n) -> integer
```

`since 2.33.0`

Gives a character EXP, as a fight's result does, and the levels it fills.

The EXP is added, then the character goes up one level each time the bar is full, with the game's
own level-up (`キャラ_レベルアップ`): the stats grow, skill points come, the bar's EXP is used,
and what is left carries over to the next level. EXP over the last level's bar is cut to that bar.
A character at the highest level (`level_max` in `rq.chara.get`; none for a character with
`uncapped`) gets nothing, as in the game, and so does Athena 2.0 (character 27), whom the game
keeps at level 1. A character at 0 HP gets the EXP but no level, since the game's level-up wants
HP: the bar stays full (EXP over it is cut) and the level comes with the next EXP once the
character has HP. `rq.chara.on_level_up` runs for each level, with `free` false.

Raises an error for a slot with no character, for an amount that is not a whole number of 0 or
more, and at the top level of a mod.

```lua
local iic = rq.party.get()[1]
local gained = rq.chara.add_exp(iic, 500)
rq.log("levels gained: " .. gained)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `n` | `integer` | The EXP to add, 0 or more. |

| Returns | Type | Description |
| --- | --- | --- |
| `gained` | `integer` | The levels gained; 0 at the cap. |

See also: [`rq.chara.level_up`](rq.chara.md#rqcharalevel_up)

### rq.chara.level_up

```lua
rq.chara.level_up(iic, n) -> integer
```

`since 2.33.0`

Raises a character's level for free, as the game's story and training do.

Uses the game's free level-up (`レベルアップ処理`): the stats grow and the EXP goes back to 0 for
the new level. It stops at `level_max`, also for a character with `uncapped`, as the game's own
does, and Athena 2.0 (character 27) stays at level 1. `rq.chara.on_level_up` runs for each level,
with `free` true.

Raises an error for a slot with no character, for a count that is not a whole number of 1 or
more, and at the top level of a mod.

```lua
rq.chara.level_up(iic, 5)  -- five levels, or fewer at the cap
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `n` *(optional)* | `integer` | The levels to add, 1 or more. Default 1. |

| Returns | Type | Description |
| --- | --- | --- |
| `gained` | `integer` | The levels gained; fewer than `n` at the cap. |

See also: [`rq.chara.add_exp`](rq.chara.md#rqcharaadd_exp)

## Events

| Name | Summary |
| --- | --- |
| [`rq.chara.on_recalc`](#rqcharaon_recalc) | Calls `fn` after the game recalculates a character (`Ｃ再計算`). |
| [`rq.chara.on_offer`](#rqcharaon_offer) | Calls `fn` after the game filled a character's skill buy list, to add rows. |
| [`rq.chara.on_create`](#rqcharaon_create) | Calls `fn` after any character is created (`Ｃ生成`), base game or mod. |
| [`rq.chara.on_forget`](#rqcharaon_forget) | Calls `fn` before a skill row is emptied, to give skill points back. |
| [`rq.chara.on_level_up`](#rqcharaon_level_up) | Calls `fn` after a character goes up a level, whatever gave it. |

### rq.chara.on_recalc

```lua
rq.chara.on_recalc(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0`

Calls `fn` after the game recalculates a character (`Ｃ再計算`).

Needs `rq.chara.install`. Up to 16 callbacks in all.

```lua
rq.chara.on_recalc(function(iic)
  if rq.chara.weapon_detail(iic) == 7 then rq.chara.apply_mod(iic, 8, 10) end  -- spear: accuracy
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(iic: integer)` | Gets the character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.14.0: Every mod's callback runs (before, the last one won).

> Changed in 0.23.0: Returns a remover.

### rq.chara.on_offer

```lua
rq.chara.on_offer(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` after the game filled a character's skill buy list, to add rows.

`fn` returns nil, one `rq.Offer`, or a list of them. Each row goes through the game's own level
check (`スキルレベル制限表示`). Needs `rq.chara.install`. Up to 16 callbacks in all.

```lua
rq.chara.on_offer(function(ctx)
  if ctx.class == 4 then return { skill = 246, cost = 2, level = 10, points = 3 } end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.OfferCtx`](../types/rq.OfferCtx.md) `):` [`rq.Offer`](../types/rq.Offer.md) `\|` [`rq.Offer`](../types/rq.Offer.md) `[]\|nil` | Returns the rows to add. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.13.0: Every mod's callback runs (before, the last one won); a list adds several rows; added `points`.

> Changed in 0.23.0: Returns a remover.

### rq.chara.on_create

```lua
rq.chara.on_create(fn) -> fun()
```

`since 0.4.0` `changed 0.23.0`

Calls `fn` after any character is created (`Ｃ生成`), base game or mod.

The engine then recalculates and heals the character. Up to 16 callbacks in all.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CreateCtx`](../types/rq.CreateCtx.md) `)` | Gets the new character. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

### rq.chara.on_forget

```lua
rq.chara.on_forget(fn) -> fun()
```

`since 0.4.0` `changed 0.23.0`

Calls `fn` before a skill row is emptied, to give skill points back.

The points every callback returns are added up and given to the character. Use `caller` to skip
the removals the game makes inside its recalculation. Up to 16 callbacks in all.

```lua
rq.chara.on_forget(function(ctx)
  if ctx.caller:find("Ｃ再計算") then return 0 end
  return ctx.cost > 0 and ctx.cost or 1
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.ForgetCtx`](../types/rq.ForgetCtx.md) `): integer\|nil` | Returns the points to give back. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

### rq.chara.on_level_up

```lua
rq.chara.on_level_up(fn) -> fun()
```

`since 2.33.0`

Calls `fn` after a character goes up a level, whatever gave it.

It runs for the game's level-ups (a fight's result, the story, training, the reserve's share) and
for `rq.chara.add_exp` and `level_up`, once per level. The game shows its own level-up on the
result screen; this only tells a mod. An error is logged once for each new error text.

```lua
rq.chara.on_level_up(function(ctx)
  if ctx.level % 10 == 0 then rq.chara.add_skill_points(ctx.iic, 1) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.LevelUpCtx`](../types/rq.LevelUpCtx.md) `)` | Runs after each level. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |
