# rq.chara

`since 0.2.0` `changed 0.4.0` `changed 2.35.0`

Reads and changes characters: their skills, stats, the skill buy list, and the roster.

The calls work on a roster slot, the `iic` (the `id` of an entry in `rq.units()`), unless they say
`who`: those take a character number or a mod's text id. Base-game numbers include Rance 1, Kaoru
52, Onoha 62 and Rebecca 81.

**Skills and the buy list.** `grant`, `rank`, `slots`, `set_slot`, `set_flavor`, `weapon_detail`,
`apply_mod`, `on_recalc`, `on_offer`, `offers`, `set_offer`, `set_uses`, `set_bar`, `clear_slot` and
`max_uses` place the hooks they need the first time (`rq.chara.install`). Before 2.35.0 they needed
it first, and without it read 0 and wrote nothing.

**Roster.** `define` registers a template; the character exists, and joins the player's roster,
only when `recruit` runs, so a mod can give it from a quest or an event. `recruit` also works for
base-game characters. A text id such as `"mymod:alice"` becomes a number from 1000 up, the same
number every time, so saves stay valid. The roster has 181 slots (20 to 200). The roster calls
install what they need on first use.

**HP and heals.** `get` and `set` read and write `hp`, `hp_max` and `status`; `heal` is the
game's own heal. Where a character is (the party, the reserve) is `rq.party`'s.

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
| [`rq.chara.heal`](#rqcharaheal) | Heals one character as the game does: HP to the most, and with `skills` the skill uses too. |
| [`rq.chara.forget`](#rqcharaforget) | Removes a skill from a character (`ＣＳ削除`). |
| [`rq.chara.base_skills`](#rqcharabase_skills) | Returns the skills a character starts with, as Morurun's reset would give them back. |
| [`rq.chara.skill_points_max`](#rqcharaskill_points_max) | Returns the most skill points a character can have had (`Ｃ最大スキルポイント取得`). |
| [`rq.chara.learnable`](#rqcharalearnable) | Returns the skill buy list the game would make for a character, without opening the window. |
| [`rq.chara.boosts`](#rqcharaboosts) | Returns the Boosts and whether the character keeps each one's effect without the skill. |
| [`rq.chara.price`](#rqcharaprice) | Returns what the game charges a character for a skill from one level to another. |
| [`rq.chara.learn`](#rqcharalearn) | Buys a skill for a character as the skill window does, without its questions. |
| [`rq.chara.skill_room`](#rqcharaskill_room) | Returns how many more skills a character can learn, as the skill window counts its free rows. |
| [`rq.chara.add_exp`](#rqcharaadd_exp) | Gives a character EXP, as a fight's result does, and the levels it fills. |
| [`rq.chara.level_up`](#rqcharalevel_up) | Raises a character's level for free, as the game's story and training do. |

### rq.chara.install

```lua
rq.chara.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Installs the hooks the skill and buy-list calls need.

It hooks the end of `Ｃ再計算` (the recalculation, after the game's own spear rewrite) and of
`Ｔ購入スキル登録` (the buy list), and the combat sites `rq.combat` uses. Calling it again, or after
`rq.combat.install`, does nothing more.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

Raises an error when the AIN is not loaded or a hook cannot be placed (the reason is in the log).

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | Always true; a failure raises an error. |

> Changed in 2.35.0: Not needed: the calls that need it make it.

### rq.chara.grant

```lua
rq.chara.grant(iic, skillId, n) -> integer
```

`since 0.2.0` `changed 2.45.0`

Gives a character a skill (`ＣＳ追加`).

A new row is marked as given in the purchase record (its cost is -1), so `rq.chara.on_forget`
can tell it from a bought skill. A row that already holds a record keeps it.

Raises an error for a slot with no character or a skill number outside 1 to 1000.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skillId` | `integer` | The skill number. |
| `n` | `integer` | The rank for a knowledge skill (type 30), or the uses for an active skill (type 10). |

| Returns | Type | Description |
| --- | --- | --- |
| `slot` | `integer` | The skill-list row it went to. |

> Changed in 2.45.0: Marks the row as given in the purchase record.

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

`since 0.2.0` `changed 2.45.0`

Lists the rows of a character's skill list that hold a skill.

The game's screens show 6 hotbar positions, so a `slots` value above 6 adds rows but no positions.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `slots` | [`rq.CharaSlot`](../types/rq.CharaSlot.md) `[]` | The rows in order; empty when there is no character. |

> Changed in 2.45.0: Each row has the purchase record (`cost`) and the level (`n`).

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

### rq.chara.heal

```lua
rq.chara.heal(iic, opts) -> boolean
```

`since 2.35.0`

Heals one character as the game does: HP to the most, and with `skills` the skill uses too.

A downed character is left as it is, as in the game's party heals; set its `status` to 0 with
`rq.chara.set` first to raise it.

Raises an error for a slot with no character, or for `all` (that is `rq.party.heal`'s).

```lua
if rq.chara.heal(iic, { skills = true }) then rq.log("healed") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The roster slot. |
| `opts` *(optional)* | `{skills?: boolean, half?: boolean}` | `skills` fills the skill uses; `half` heals up to half the most HP. |

| Returns | Type | Description |
| --- | --- | --- |
| `healed` | `boolean` | false for a downed character. |

See also: [`rq.party.heal`](rq.party.md#rqpartyheal)

### rq.chara.forget

```lua
rq.chara.forget(iic, skill, opts) -> boolean, integer?, integer?
```

`since 0.4.0` `changed 2.45.0` `changed 2.51.0`

Removes a skill from a character (`ＣＳ削除`).

`rq.chara.on_forget` callbacks run, with `caller` "lua" and `mod` the calling mod's id. With
`player = true` the erasure is the player's own, as the skill window's ERASE: a mod that erases
for the player (a build it loads, a skill the player picked in its menu) sets it, and the
callbacks see `player`, so a mod that gives points back for ERASE (Skill Removal Payback) gives
them back here too. Without it the removal is the mod's own, as onoha-qol's head start, and such
a mod gives nothing. The third value is the points the callbacks gave back, already added to
the character.

Raises an error for a slot with no character, or for `iic`, `skill` or `opts` of the wrong type.

```lua
-- Erase a skill the player picked in the mod's menu, as ERASE would.
local removed, cost, back = rq.chara.forget(iic, skill, { player = true })
if removed then rq.log(("erased; it cost %d, %d back"):format(cost, back)) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `opts` *(optional)* | `{player?: boolean}` | `player`: the player chose this erasure (default false). |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when the character did not have the skill (the only value then). |
| `cost` | `integer?` | The purchase record, as `rq.ForgetCtx.cost`. |
| `back` | `integer?` | The skill points the `rq.chara.on_forget` callbacks gave back (since 2.51.0). |

> Changed in 2.45.0: `cost` is the purchase record.

> Changed in 2.51.0: `opts.player`, and the points given back.

### rq.chara.base_skills

```lua
rq.chara.base_skills(iic) -> rq.SkillLevel[]
```

`since 2.45.0`

Returns the skills a character starts with, as Morurun's reset would give them back.

The game rebuilds a character's skills for that reset (`Ｃスキルドレイン`) from the character's
own data (`Ｃ生成／キャラデータ`): Skill Slots, the class's skills, the character's own, the
Morurun marks, then the ones flags add (the familiar, a few story skills). This call runs that
same code on the character and puts everything back before it returns, so the character does not
change and `rq.chara.on_forget` does not run. A mod's character gives its definition's `skills`.
Skills a mod gives through `edit` are not part of it.

What a character has above this set was bought, or given by a story event or a mod; the
purchase record (`rq.ForgetCtx.cost`) tells which, for what was bought from loader 2.45.0 on.

Raises an error for a slot with no character.

```lua
for _, s in ipairs(rq.chara.base_skills(iic)) do
  rq.log(("starts with skill %d at %d"):format(s.id, s.n))
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `skills` | [`rq.SkillLevel`](../types/rq.SkillLevel.md) `[]` | The starting skills, in their rows' order. |

See also: [`rq.chara.price`](rq.chara.md#rqcharaprice)

### rq.chara.skill_points_max

```lua
rq.chara.skill_points_max(iic) -> integer
```

`since 2.45.0`

Returns the most skill points a character can have had (`Ｃ最大スキルポイント取得`).

It is the game's count: level - 1, 2 for each Morurun reset up to 5, one for each castle bonus up
to 3, and the bonuses of a few skills and flags. Minus the free points
(`rq.chara.skill_points`), it is what the character has spent, unless a mod gave points. The
game's function also clears a counter (`FA[33]`); this call leaves it as it was.

Raises an error for a slot with no character.

```lua
local spent = rq.chara.skill_points_max(iic) - rq.chara.skill_points(iic)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `points` | `integer` | The most points. |

### rq.chara.learnable

```lua
rq.chara.learnable(iic, opts) -> rq.LearnableRow[]?, integer
```

`since 2.45.0` `changed 2.48.0`

Returns the skill buy list the game would make for a character, without opening the window.

The game fills its list (`Ｔ購入スキル登録`) and the loader reads it, then puts the list back as
it was. `rq.chara.on_offer` callbacks run, so mods' offers are in it. A skill at its most uses
(99) or rank (4) is not listed.

A row the list shows but does not sell has the game's reason (`why`) and what its conditions
name: the skills and levels (`needs`) and the character level (`level`). The game names a skill
by its name only; the loader reads it back to a number, the list's and the character's skills
first.

`opts.after` is a list of steps, each a skill and a level (0 erases it), set in order on the
character before the list is made and undone after: the list as it would be after those
purchases or erasures, as Healing 3 for sale once Healing 2 is at 3, or Healing 2 off sale once
Healing 1 is erased. A step sets the level as it is, with no price and none of the game's
checks; a Boost set to rank 4 is kept as the game's recalculation would keep it
(`rq.chara.boosts`). When a step needs a new row and none is left, the call returns nil and the
step's index.

The second value is the free skill rows after the steps, as `rq.chara.skill_room` counts them.

Raises an error for a slot with no character, an `after` that is not a list, or a step that is
not `{ skill = number, n = level from 0 }`.

and `level`.

```lua
for _, row in ipairs(rq.chara.learnable(iic)) do
  if row.points > 0 then rq.log(("skill %d: %d points"):format(row.skill, row.points)) end
end
-- Healing 3's price once Healing 2 is at 3 and Healing 1 erased
local rows = rq.chara.learnable(iic, { after = { { skill = 221, n = 0 }, { skill = 222, n = 3 } } })
for _, row in ipairs(rows or {}) do
  if row.skill == 223 then rq.log("Healing 3: " .. row.points .. " points") end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `opts` *(optional)* | `{ after?:` [`rq.SkillStep`](../types/rq.SkillStep.md) `[] }` | `after`: the steps to set before the list is made. |

| Returns | Type | Description |
| --- | --- | --- |
| `rows` | [`rq.LearnableRow`](../types/rq.LearnableRow.md) `[]?` | The list, in the game's order; nil when a step found no free row. |
| `room` | `integer` | The free skill rows after the steps; with nil rows, the index of the step that found none. |

> Changed in 2.48.0: `opts.after`, the free rows as a second value, and each row's `step`, `needs`

See also: [`rq.chara.price`](rq.chara.md#rqcharaprice)

### rq.chara.boosts

```lua
rq.chara.boosts(iic) -> rq.BoostRow[], boolean
```

`since 2.48.0`

Returns the Boosts and whether the character keeps each one's effect without the skill.

In the third world only (`rq.world.current`), the game's recalculation marks a Boost raised to
rank 4 (`FA[38]` to `FA[45]`), and the character keeps its effect after the skill is erased:
+800 HP, +300 Attack or Magic, or +50 to a rate. The second version of Stamina, Attack and
Magic Boost (455, 456, 457) is sold only once the first is at rank 4 or kept, and is kept on top
of it. The game's reset of the skills (`Ｃスキルドレイン`: Morurun's reset, Skill Again) clears
the marks, and so does a recalculation in another world.

Raises an error for a slot with no character.

```lua
local boosts, keeps = rq.chara.boosts(iic)
for _, b in ipairs(boosts) do
  if b.kept then rq.log(("skill %d's effect stays"):format(b.skill)) end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `boosts` | [`rq.BoostRow`](../types/rq.BoostRow.md) `[]` | The eleven Boosts, firsts before seconds. |
| `keeps` | `boolean` | Whether this world keeps a Boost's effect (the third world). |

See also: [`rq.chara.on_forget`](rq.chara.md#rqcharaon_forget)

### rq.chara.price

```lua
rq.chara.price(iic, skill, from, to) -> integer?, string?, string?
```

`since 2.45.0`

Returns what the game charges a character for a skill from one level to another.

Each step is priced as the buy list prices it at that step: the skill is set to the step on the
character, the game fills its list, and the step's price is read; the character and the list are
put back before the call returns. So the game's rules hold: one more point at 3, 5 and 7 most
uses, the prices that change with the skill (Rance's 147), and a mod's `rq.chara.on_offer`.
A level is most uses for a use skill (type 10), the rank for a ranked one (20, 30). Skill 384
goes 3 uses a step, as the game sells it.

It returns nil and why when a step is not for sale: `"not sold"` (the character's list does not
have it, or the skill cannot be bought), `"condition"` with the game's text (a level it lacks),
`"max"` (past 99 uses or rank 4), `"room"` (no free skill row to price a new skill in).

Raises an error for a slot with no character, a skill number not in the game's table, or a
level below 0.

```lua
-- what a starting skill would cost from nothing
local points = rq.chara.price(iic, 100, 0, 3) or 1
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `from` | `integer` | The level to start from; 0 for a skill the character does not have. |
| `to` | `integer` | The level to reach; nothing to pay when it is not above `from`. |

| Returns | Type | Description |
| --- | --- | --- |
| `points` | `integer?` | The points, or nil when a step is not for sale. |
| `why` | `string?` | `"not sold"`, `"condition"`, `"max"` or `"room"`. |
| `text` | `string?` | The game's reason, for `"condition"`. |

See also: [`rq.chara.learnable`](rq.chara.md#rqcharalearnable)

### rq.chara.learn

```lua
rq.chara.learn(iic, skill, opts) -> boolean, integer|string, integer|string?
```

`since 2.45.0`

Buys a skill for a character as the skill window does, without its questions.

Each step goes through the game's own buy (`キャラスキル_新規追加`) or upgrade
(`キャラスキル_更新`) at the list's price, with the game's "Learn ...?" answered Yes, then the
character is recalculated (and refilled outside a quest, as the window does). The purchase
record grows and `rq.chara.on_learn` runs for each step. Before buying anything it checks the
whole price, the free points and a free skill row, and refuses with the reason:

- `"points"`, with how many points are missing
- `"room"`: no free skill row for a new skill
- `"not sold"`, `"condition"` (with the game's text) or `"max"`, as `rq.chara.price`
- `"refused"`: the game refused a step; the steps before it stay bought

Raises an error for a slot with no character, a skill number not in the game's table, `opts`
that is not a table, a `to` below 0, or a call from inside another `learn`.

```lua
local ok, why, detail = rq.chara.learn(iic, 100, { to = 5 })
if not ok and why == "points" then rq.log(detail .. " more points needed") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `opts` *(optional)* | `{to?: integer, pay?: boolean}` | `to`: the level to reach (default one step more). `pay`: false gives the steps for free and marks a new row as given in the record (default true). |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the skill reached `to`. |
| `spent_or_why` | `integer\|string` | The points paid when ok; otherwise the reason. |
| `detail` | `integer\|string?` | The missing points for `"points"`, the game's text for `"condition"`. |

See also: [`rq.chara.price`](rq.chara.md#rqcharaprice)

### rq.chara.skill_room

```lua
rq.chara.skill_room(iic) -> integer
```

`since 2.45.0`

Returns how many more skills a character can learn, as the skill window counts its free rows.

It is the game's check before a new skill (`キャラスキル_空き確認`) as a number: 17 rows, less
the rows the game keeps free for the character's story skills (`キャラ_スキル枠キープ数`), less
the skills the character has. A new skill from `rq.chara.learn` needs one; one more use or rank
needs none. `rq.chara.grant` does not check it.

Raises an error for a slot with no character.

```lua
if rq.chara.skill_room(iic) < 2 then rq.ui.notice("Erase a skill first.") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `rows` | `integer` | The free rows, 0 or more. |

See also: [`rq.chara.learn`](rq.chara.md#rqcharalearn)

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
| [`rq.chara.on_learn`](#rqcharaon_learn) | Calls `fn` after each skill purchase, once per step. |
| [`rq.chara.on_skill_reset`](#rqcharaon_skill_reset) | Calls `fn` after the game resets a character's skills, to give back what a mod gave. |
| [`rq.chara.on_level_up`](#rqcharaon_level_up) | Calls `fn` after a character goes up a level, whatever gave it. |

### rq.chara.on_recalc

```lua
rq.chara.on_recalc(fn) -> fun()
```

`since 0.2.0` `changed 0.14.0` `changed 0.23.0` `changed 2.35.0`

Calls `fn` after the game recalculates a character (`Ｃ再計算`).

Up to 16 callbacks in all.

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

> Changed in 2.35.0: Places its hook itself; before, it needed `rq.chara.install`.

### rq.chara.on_offer

```lua
rq.chara.on_offer(fn) -> fun()
```

`since 0.2.0` `changed 0.13.0` `changed 0.23.0`

Calls `fn` after the game filled a character's skill buy list, to add rows.

`fn` returns nil, one `rq.Offer`, or a list of them. Each row goes through the game's own level
check (`スキルレベル制限表示`). Up to 16 callbacks in all. Since 2.35.0 it places its hook itself.

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

`since 0.4.0` `changed 0.23.0` `changed 2.45.0` `changed 2.48.0` `changed 2.51.0`

Calls `fn` before a skill row is emptied, to give skill points back.

The points every callback returns are added up and given to the character. `player` tells the
erasures the player chose (the skill window's ERASE, and a mod's `rq.chara.forget` with
`player = true`) from the game's other removals (its recalculation, the story, the reset) and a
mod's own; `caller` names the AIN function, or "lua". `kept` tells a Boost whose effect the
character keeps once it is erased (`rq.chara.boosts`), so its points were not lost. Up to 16
callbacks in all.

```lua
-- Half the points back for each erasure the player chose.
rq.chara.on_forget(function(ctx)
  if ctx.player and ctx.cost > 0 then return ctx.cost // 2 end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.ForgetCtx`](../types/rq.ForgetCtx.md) `): integer\|nil` | Returns the points to give back. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.45.0: `cost` is the purchase record.

> Changed in 2.48.0: `kept`.

> Changed in 2.51.0: `player` and `mod`.

### rq.chara.on_learn

```lua
rq.chara.on_learn(fn) -> fun()
```

`since 2.45.0`

Calls `fn` after each skill purchase, once per step.

It runs for the skill window's buy and upgrade, and for each step of `rq.chara.learn`, after the
loader wrote the purchase record. The tutorial's purchases count too.

```lua
rq.chara.on_learn(function(ctx)
  rq.log(("%d paid %d for skill %d"):format(ctx.iic, ctx.points, ctx.skill))
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.LearnCtx`](../types/rq.LearnCtx.md) `)` | Gets the purchase. Its return value is not used. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.chara.on_forget`](rq.chara.md#rqcharaon_forget)

### rq.chara.on_skill_reset

```lua
rq.chara.on_skill_reset(fn) -> fun()
```

`since 2.46.0`

Calls `fn` after the game resets a character's skills, to give back what a mod gave.

The game resets them (`Ｃスキルドレイン`) for Morurun's reset and when Skill Again (item 306) is
equipped: the skills become the starting set (`rq.chara.base_skills`) and the free points the
game's own count, so the skills and points a mod gave are gone. `fn` can give the points back
with `rq.chara.add_skill_points`; skills from `edit`'s `learn` come back by themselves at the
next recalculation.

A callback's error is logged once per mod.

```lua
rq.chara.on_skill_reset(function(ctx)
  if ctx.no == 27 then rq.chara.add_skill_points(ctx.iic, rq.savedata.get("given", 0)) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.SkillResetCtx`](../types/rq.SkillResetCtx.md) `)` | Gets the character. Its return value is not used. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.chara.base_skills`](rq.chara.md#rqcharabase_skills)

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
