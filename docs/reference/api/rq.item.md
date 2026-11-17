# rq.item

`since 0.8.0`

Defines, gives and changes items.

Items work like characters: define a template, then something provides it (a shop, a chest, a drop,
a quest, a character that starts with it). The game keeps item instances (`ii`, up to 3000) that
point to an item number (`no`). The calls take a number or a text id where they say `who`. The first
call grows the game's restock array (`◆アイテム補充数`) so numbers above 348 are safe. Effects are the
game's own codes; a mod that needs behavior of its own checks for its item with `rq.item.equipped`
and does the work in Lua.

A familiar is an item in the item slot with `subtype = 20`; its owner needs Familiar Knowledge
(321). The game reads three effects by place: the monster number, the class (1 to 4) and the
growth. Its icon must be 6500 to 6516 or 6632, or the familiar never takes a turn. The monster may
be a mod's (`rq.monster.define`), whose `capture` gives such an item (`rq.MonsterCapture`).

```lua
local broken = rq.item.define({ id = "mymod:broken_lens", name = "Broken Lens", price = 10,
  info = "Cracked. It no longer magnifies anything." })
rq.item.define({ id = "mymod:lens", name = "Lens", price = 2000, icon = "icons/lens.png",
  info = "Zoom out on a dungeon.$Breaks when the dungeon ends." })
local ii = rq.item.give("mymod:lens", { to = rq.chara.find(1) })  -- equip it on Rance
rq.item.transform(ii, "mymod:broken_lens")                       -- later, it breaks
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.item.define`](#rqitemdefine) | Registers an item template. |
| [`rq.item.give`](#rqitemgive) | Creates an instance (`Ｉ生成`) and puts it in the vault, in quest storage, or on a character. |
| [`rq.item.get`](#rqitemget) | Returns an instance's fields. |
| [`rq.item.appraise`](#rqitemappraise) | Appraises an unidentified item for free, as the game's appraisal does. |
| [`rq.item.set`](#rqitemset) | Writes an instance's fields. |
| [`rq.item.transform`](#rqitemtransform) | Turns an instance into another item, keeping its place and owner. |
| [`rq.item.edit`](#rqitemedit) | Patches an item number, for every new instance and the ones in the save. |
| [`rq.item.equip`](#rqitemequip) | Equips an existing instance on a character (`キャラ_装備設定`). |
| [`rq.item.remove`](#rqitemremove) | Deletes an instance (`Ｉ削除`), taking it off its owner first. |
| [`rq.item.equipped`](#rqitemequipped) | Returns the instances a character has equipped. |
| [`rq.item.number`](#rqitemnumber) | Returns the item number of an instance. |
| [`rq.item.id_of`](#rqitemid_of) | Returns the text id of a defined item number. |
| [`rq.item.lock`](#rqitemlock) | Locks an item in the vault or the storage, or unlocks it, as the vault's LOCK and UNDO LOCK do (`アイテム_ＬＯＣＫ`, `アイテム_ＵＮＬＯＣＫ`). |
| [`rq.item.sell`](#rqitemsell) | Sells an item from the vault, the storage or a character's gear, as the vault's SELL does (`アイテム_売却`): the game asks "Sell ...?" first, and on Yes the item goes, the shop restocks it, and you get 100 gold for an item priced over 1000, else 10. |
| [`rq.item.donate`](#rqitemdonate) | Donates an item from the vault, the storage or a character's gear, as the vault's DONATE does (`アイテム_寄付`): the game asks "Donate ...?" first, and on Yes the item goes, the shop restocks it, and the donations count goes up by one. |
| [`rq.item.store`](#rqitemstore) | Moves an item between the vault and the storage, as dragging a row on the game's storage screen does (`アイテム_存在設定` 7 or 11). |
| [`rq.item.buy`](#rqitembuy) | Buys an item from the shop's stock, as the shop's drag of a row onto the vault or a party member does (`T_EquitItem::setItem`): the game asks "Purchase ...?" first, and on Yes the item goes into the vault, its price comes off the money, and the shop's spent total goes up by it. |
| [`rq.item.info`](#rqiteminfo) | Returns an item number's row data, with no instance of it in the game. |
| [`rq.item.find`](#rqitemfind) | Lists the instances of an item number, by place. |
| [`rq.item.count`](#rqitemcount) | Counts the instances of an item number, by place. |

### rq.item.define

```lua
rq.item.define(def) -> integer
```

`since 0.8.0`

Registers an item template.

No instance exists until it is given or stocked.

Raises an error for a text id whose number another id already has.

| Parameter | Type | Description |
| --- | --- | --- |
| `def` | [`rq.ItemDef`](../types/rq.ItemDef.md) | The template. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number. |

### rq.item.give

```lua
rq.item.give(who, opts) -> integer|nil, string?
```

`since 0.8.0`

Creates an instance (`Ｉ生成`) and puts it in the vault, in quest storage, or on a character.

Raises an error for an unknown item.

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | An item number or text id. |
| `opts` *(optional)* | `{to?: integer, place?: "vault"\|"quest"}` | `to`: a roster slot to equip it on. `place`: "vault" (default) or "quest" storage. |

| Returns | Type | Description |
| --- | --- | --- |
| `ii` | `integer\|nil` | The new instance, or nil. |
| `err` | `string?` | Why it failed, or that the character cannot equip it. |

### rq.item.get

```lua
rq.item.get(ii) -> rq.ItemInfo|nil
```

`since 0.8.0`

Returns an instance's fields.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.ItemInfo`](../types/rq.ItemInfo.md) `\|nil` | A copy of the fields, or nil when there is no such instance. |

### rq.item.appraise

```lua
rq.item.appraise(ii, opts) -> boolean
```

`since 2.47.0`

Appraises an unidentified item for free, as the game's appraisal does.

It runs the game's `Ｉ鑑定` on the instance: a rare item gets the bonuses of the quest being
played, the effects 21 to 25 stop at 99, and the name, icon and description become the item
number's. The item stays where it is. The game appraises the quest storage's items itself after
a quest's success; this is for an item it never reaches, such as one a mod kept in the storage.

Raises an error for an instance that is not a whole number, `opts` that is not a table, or a
`sound` that is not true or false.

```lua
for _, row in ipairs(rq.items()) do
  if row.place == 11 and not rq.item.get(row.id).identified then rq.item.appraise(row.id) end
end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `opts` *(optional)* | `{sound?: boolean}` | `sound`: play the game's appraisal sound. Default false. |

| Returns | Type | Description |
| --- | --- | --- |
| `appraised` | `boolean` | true when it was unidentified and is now identified; false for no such instance, or one already identified. |

### rq.item.set

```lua
rq.item.set(ii, fields)
```

`since 0.8.0`

Writes an instance's fields.

The fields are `name`, `info`, `effects`, `price`, `rarity`, `level`, `icon`, `rank`, `subtype`,
`type`, `locked`, `vanishes` and `place`. After changing the effects of an equipped item, call
`rq.chara.recalc` on its owner.

Raises an error for an unknown field.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `fields` | `table` | The fields to write. |

### rq.item.transform

```lua
rq.item.transform(ii, who) -> boolean
```

`since 0.8.0`

Turns an instance into another item, keeping its place and owner.

Name, price, effects and description change, as for a "broken" version of an item.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `who` | `string\|integer` | The new item number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when it could not change. |

### rq.item.edit

```lua
rq.item.edit(who, patch)
```

`since 0.8.0` `changed 0.15.0`

Patches an item number, for every new instance and the ones in the save.

The patch takes the same fields as `rq.item.set`. It applies to every new instance, and to the ones
already in the save after each load, or on the next frame when called later (all fields but `place`
and `no`; an equipped item recalculates its owner). The save then keeps those values, also when the
mod is removed. Each mod keeps one patch per item.

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | An item number or text id. |
| `patch` | `table` | The fields to set. |

> Changed in 0.15.0: Reaches instances already in the save.

### rq.item.equip

```lua
rq.item.equip(ii, iic) -> boolean
```

`since 0.11.0`

Equips an existing instance on a character (`キャラ_装備設定`).

The old item of that slot is replaced, and the character is recalculated.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | false when the character cannot wear it. |

### rq.item.remove

```lua
rq.item.remove(ii) -> boolean
```

`since 0.10.0`

Deletes an instance (`Ｉ削除`), taking it off its owner first.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `removed` | `boolean` | false when there is no such instance. |

### rq.item.equipped

```lua
rq.item.equipped(iic) -> {weapon?: integer, armor?: integer, item?: integer, special?: integer}
```

`since 0.8.0`

Returns the instances a character has equipped.

| Parameter | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |

| Returns | Type | Description |
| --- | --- | --- |
| `gear` | `{weapon?: integer, armor?: integer, item?: integer, special?: integer}` | The instance in each slot; an empty slot is left out. |

### rq.item.number

```lua
rq.item.number(ii) -> integer|nil
```

`since 0.8.0`

Returns the item number of an instance.

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |

| Returns | Type | Description |
| --- | --- | --- |
| `no` | `integer\|nil` | The item number, or nil when there is no such instance. |

### rq.item.id_of

```lua
rq.item.id_of(no) -> string|nil
```

`since 0.8.0`

Returns the text id of a defined item number.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number. |

| Returns | Type | Description |
| --- | --- | --- |
| `id` | `string\|nil` | The text id, or nil when no mod defined that number. |

### rq.item.lock

```lua
rq.item.lock(ii, on) -> boolean
```

`since 2.9.0`

Locks an item in the vault or the storage, or unlocks it, as the vault's LOCK and UNDO LOCK do
(`アイテム_ＬＯＣＫ`, `アイテム_ＵＮＬＯＣＫ`).

A locked item cannot be sold or donated. `rq.uikit` rows show the change at once.

Raises an error when `ii` is not a whole number.

```lua
rq.item.lock(ii)        -- lock
rq.item.lock(ii, false) -- unlock
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `on` *(optional)* | `boolean` | false unlocks; default true. |

| Returns | Type | Description |
| --- | --- | --- |
| `done` | `boolean` | false when there is no such instance, it is not in the vault or the storage, or it already was. |

### rq.item.sell

```lua
rq.item.sell(ii, opts) -> boolean
```

`since 2.9.0` `changed 2.10.0`

Sells an item from the vault, the storage or a character's gear, as the vault's SELL does
(`アイテム_売却`): the game asks "Sell ...?" first, and on Yes the item goes, the shop restocks it,
and you get 100 gold for an item priced over 1000, else 10.

The game's question waits inside the call: call it from a callback, not in a loop. While it asks,
another `sell`, `donate` or `buy` returns false. With `ask = false` it sells at once, with the
game's sound and the same steps. An item the game will not let go (a quest item) gets the game's
"cannot be sold" notice, or false without asking. The money on the system bar updates.

An item a character wears comes off first (`キャラ_装備設定` with 0), after the question. One the
game will not take off gets its "cannot be removed" notice (or false without asking), and one
that vanishes when taken off is refused. The game never sells worn gear itself; this is the
vault's steps on an item taken off.

Raises an error when `ii` is not a whole number, or `opts` is not a table.

```lua
if rq.item.sell(ii, { ask = false }) then rq.log("sold", ii) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `opts` *(optional)* | `{ask?: boolean}` | `ask` (default true): the game's question first. |

| Returns | Type | Description |
| --- | --- | --- |
| `sold` | `boolean` | false when it was not sold: no such instance, not in the vault, the storage or a character's gear, locked, a quest item, one that cannot come off or vanishes when it does, No, or another question showing. |

> Changed in 2.10.0: Items a character wears.

### rq.item.donate

```lua
rq.item.donate(ii, opts) -> boolean
```

`since 2.9.0` `changed 2.10.0`

Donates an item from the vault, the storage or a character's gear, as the vault's DONATE does
(`アイテム_寄付`): the game asks "Donate ...?" first, and on Yes the item goes, the shop restocks
it, and the donations count goes up by one.

The game's question waits inside the call, as with `sell`. With `ask = false` it donates at once.
An item the game will not let go gets its "cannot be donated" notice, or false without asking. An
item a character wears comes off first, as with `sell`.

Raises an error when `ii` is not a whole number, or `opts` is not a table.

```lua
rq.item.donate(ii)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `opts` *(optional)* | `{ask?: boolean}` | `ask` (default true): the game's question first. |

| Returns | Type | Description |
| --- | --- | --- |
| `donated` | `boolean` | false when it was not donated, as with `sell`. |

> Changed in 2.10.0: Items a character wears.

### rq.item.store

```lua
rq.item.store(ii, where) -> boolean
```

`since 2.9.0`

Moves an item between the vault and the storage, as dragging a row on the game's storage screen
does (`アイテム_存在設定` 7 or 11).

Raises an error when `ii` is not a whole number, or `where` is not "vault" or "storage".

```lua
rq.item.store(ii, "storage")
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance. |
| `where` | `"vault"\|"storage"` | Where it goes. |

| Returns | Type | Description |
| --- | --- | --- |
| `moved` | `boolean` | false when there is no such instance or it is in neither. |

### rq.item.buy

```lua
rq.item.buy(ii, opts) -> boolean, string?
```

`since 2.10.0` `changed 2.49.0` `changed 2.50.0`

Buys an item from the shop's stock, as the shop's drag of a row onto the vault or a party member
does (`T_EquitItem::setItem`): the game asks "Purchase ...?" first, and on Yes the item goes into
the vault, its price comes off the money, and the shop's spent total goes up by it.

With `chara` the item is bought onto that character and equipped (`キャラ_装備設定`), as the drag
onto a party member does: the character must be able to wear it ("Unable to equip."), and the
slot's old item must come off, with the game's notice or questions for one that cannot or that
vanishes. Short of money, the game says "Not enough money.". The notices show only when asking;
with `ask = false` it buys at once and returns false where the game would have said no, and an
old item that vanishes when taken off also stops it. The question waits inside the call, as with
`sell`. The money on the system bar updates, and the `rq.shop.on_buy` callbacks run, as for the
shop's drag. Buying does not restock the shop: `rq.shop.restock` does what the next visit would.

The `rq.shop.on_can_buy` callbacks run first: a refusal returns false and its text, which the
game's notice shows when asking.

Raises an error when `ii` or `chara` is not a whole number, or `opts` is not a table.

```lua
local ii = rq.uikit.item_picker({ x = 538, y = 0, id = "shop", where = "shop" })
if ii and rq.item.buy(ii) then rq.log("bought", ii) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The instance, in the shop's stock (place 6). |
| `opts` *(optional)* | `{ask?: boolean, chara?: integer}` | `ask` (default true): the game's question and notices. `chara`: a roster slot to buy onto. |

| Returns | Type | Description |
| --- | --- | --- |
| `bought` | `boolean` | false when it was not bought: not in the shop's stock, refused by an `rq.shop.on_can_buy` callback, not enough money, a character who cannot wear it, an old item that cannot come off, No, or another question showing. |
| `why` | `string?` | A refusal's text from `rq.shop.on_can_buy`, when it gave one. |

> Changed in 2.49.0: Runs the `rq.shop.on_buy` callbacks (only the game's drag did).

> Changed in 2.50.0: Runs the `rq.shop.on_can_buy` callbacks, and returns a refusal's text.

### rq.item.info

```lua
rq.item.info(no) -> rq.ItemInfo?
```

`since 2.20.0`

Returns an item number's row data, with no instance of it in the game.

Read as the game's own lookups by number read it (`Ｉ固有名前`): a temporary instance, read and
deleted. The item's own definition runs (a mod item's `on_create` and `rq.item.edit` changes), but
`rq.item.on_create` listeners do not see that instance. An item whose data the game makes from the
moment (a few read Rance's level) gives the data of the moment. Kept for a second per number.

Raises an error when `no` is not an integer.

```lua
local it = rq.item.info(274)
if it then rq.log(it.name, it.info) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number. |

| Returns | Type | Description |
| --- | --- | --- |
| `info` | [`rq.ItemInfo`](../types/rq.ItemInfo.md) `?` | The data, or nil for 0 or a number the game does not have. |

### rq.item.find

```lua
rq.item.find(no, opts) -> integer[]
```

`since 2.23.0`

Lists the instances of an item number, by place.

The list comes in the order of `opts.place`, then by instance, so `{ "vault", "storage" }` gives
the vault's first. One pass over the game's item slots per place; it builds no rows, so it is
quicker than going through `rq.items()`. Shop stock (6) and instances being made (9) are only
found when asked for by number.

Raises an error for an unknown place name, a place that is not a whole number above 0, or more
than 8 places.

```lua
local JEWEL = 258
local ii = rq.item.find(JEWEL, { place = { "vault", "storage" }, lock = false })[1]
if ii then rq.item.remove(ii) end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number. |
| `opts` *(optional)* | [`rq.ItemFindOpts`](../types/rq.ItemFindOpts.md) | Which places, and the vault lock. |

| Returns | Type | Description |
| --- | --- | --- |
| `instances` | `integer[]` | The instances (ii); empty when there are none. |

See also: [`rq.item.count`](rq.item.md#rqitemcount)

### rq.item.count

```lua
rq.item.count(no, opts) -> integer
```

`since 2.23.0`

Counts the instances of an item number, by place.

It counts what `rq.item.find` would list. With no `opts` it gives the game's own count
(`Ｉ総数取得／固有番号(no, 0)`): worn, in the vault and in the storage.

Raises an error as `rq.item.find` does.

```lua
if rq.item.count(rq.ids.item.SKILL_AGAIN) >= 3 then rq.log("a set of three") end
```

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer` | The item number. |
| `opts` *(optional)* | [`rq.ItemFindOpts`](../types/rq.ItemFindOpts.md) | Which places, and the vault lock. |

| Returns | Type | Description |
| --- | --- | --- |
| `n` | `integer` | How many. |

See also: [`rq.item.find`](rq.item.md#rqitemfind)

## Events

| Name | Summary |
| --- | --- |
| [`rq.item.on_create`](#rqitemon_create) | Calls `fn` after any item instance is created (`Ｉ生成`), game or mod. |
| [`rq.item.on_can_equip`](#rqitemon_can_equip) | Calls `fn` where the game decides whether a character can equip an item, to change the answer. |
| [`rq.item.on_equip`](#rqitemon_equip) | Calls `fn` each time an item is put on a character. |
| [`rq.item.on_unequip`](#rqitemon_unequip) | Calls `fn` each time an item comes off a character. |

### rq.item.on_create

```lua
rq.item.on_create(fn) -> fun()
```

`since 0.8.0` `changed 0.23.0` `changed 2.20.0`

Calls `fn` after any item instance is created (`Ｉ生成`), game or mod.

It is not called for the temporary instance of `rq.item.info`, which never enters the game.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx: {ii: integer, no: integer, id?: string})` | Gets the instance, its number, and its text id for a mod's item. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.

> Changed in 2.20.0: Not called for `rq.item.info`'s lookup.

### rq.item.on_can_equip

```lua
rq.item.on_can_equip(fn) -> fun()
```

`since 2.46.0` `changed 2.55.0`

Calls `fn` where the game decides whether a character can equip an item, to change the answer.

It runs in `アイテム_装備可能`, the one check behind the vault, the status page, the shop, the
storage screen's filters, the list of who can wear an item, and `rq.item.buy` with a `chara`.
`fn` returns true to let the character equip it, false to refuse, or nil to keep the answer. Each
callback sees in `ctx.allowed` what the one before left.

A refusal can say why: `return false, "No free skill slot."`. The text of the last callback that
refused with one counts, unless a later one returns true. The game shows it in its notice where
a player tries to equip the item: a drop on a greyed character in the vault's or the storage
screen's equip list shows it instead of the game's "Unable to equip.". The status page's item
list greys only what the game itself refuses, so an item only a mod refuses with a text stays
bright there, and picking it shows the text and equips nothing. With no text, the game's own
behavior stays: "Unable to equip." in the vault, a grey row on the status page.

The game checks the level first and stops there, so `ctx.reasons` says whether the item's
characters or class would refuse it too: a mod that lifts only the level returns true only when
"level" is the one reason. `reason`, `reasons` and the levels are worked out when a callback
first reads them.

A callback's error, or a return that is not a boolean or nil, is logged once and changes nothing.

```lua
local BAG = rq.item.define({ id = "mymod:bag", name = "Bag", type = "special" })
rq.item.on_can_equip(function(ctx)
  -- Athena 2.0 (27) wears any bow (subtype 5) whatever its level.
  if ctx.chara == 27 and #ctx.reasons == 1 and ctx.reason == "level"
    and rq.item.get(ctx.ii).subtype == 5 then
    return true
  end
  -- The bag gives a skill: refused, with the reason, when there is no row for it.
  if ctx.no == BAG and rq.chara.skill_room(ctx.iic) < 1 then
    return false, "No free skill slot."
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.CanEquipCtx`](../types/rq.CanEquipCtx.md) `): (boolean\|nil, string?)` | Returns true, false or nil; with false, the text the game shows (since 2.55.0). |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 2.55.0: A refusal's text, shown in the vault and on the status page.

See also: [`rq.item.on_equip`](rq.item.md#rqitemon_equip)

### rq.item.on_equip

```lua
rq.item.on_equip(fn) -> fun()
```

`since 2.55.0`

Calls `fn` each time an item is put on a character.

It runs in `キャラ_装備設定`, the one call the game equips through: the vault's and the storage
screen's drag, the status page, buying onto a character in the shop, `rq.item.give` with `to`
and `rq.item.equip`. It runs once the slot holds the item, after the game has worked out the
stats again and, for a Special item, done its own effects (Skill Again, a Morurun). Putting the
same instance on again does not call it. An item taken off calls `rq.item.on_unequip` instead.

This is the place for an item that does something once, when equipped: give a skill, then
`rq.chara.recalc`. With `vanishes = true` in `rq.item.define`, the game deletes the item when it
comes off, as it does Rocky Chunk, and what it did stays.

A callback's error is logged once per mod.

```lua
local BAG = rq.item.define({ id = "mymod:bag", name = "Bag", type = "special", icon = 6331,
  price = 100, vanishes = true, info = "Equip: the wearer learns Immature." })
rq.item.on_equip(function(ctx)
  if ctx.no == BAG then
    rq.chara.grant(ctx.iic, 373, 0)
    rq.chara.recalc(ctx.iic)
  end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.EquipCtx`](../types/rq.EquipCtx.md) `)` | Gets the item and the character. Its return value is not used. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.item.on_can_equip`](rq.item.md#rqitemon_can_equip), [`rq.item.on_unequip`](rq.item.md#rqitemon_unequip)

### rq.item.on_unequip

```lua
rq.item.on_unequip(fn) -> fun()
```

`since 2.57.0`

Calls `fn` each time an item comes off a character.

It runs for every way an item leaves a character's slot: the vault's and the status page's REMOVE,
a drag to another place, a swap for another item (`by`), `rq.item.equip`, `rq.item.remove`,
`sell` and `donate` on a worn item, and the game's own (a character removed from the roster, a Morurun absorbing a Special item, a
quest's event that takes an item off). They all go through `Ｃアイテム外す`. Through the game's
equip call (`equip` true) it runs once that call has ended, before `rq.item.on_equip` for the item
put in its place; otherwise it runs as the item comes off. Putting the same instance on again does
not call it.

This is the place for what an item gives only while it is worn: take it back here. The stats are
worked out again after the equip call; for the game's own removals, call `rq.chara.recalc`.

A callback's error is logged once per mod.

```lua
local SKILL = 373 -- a skill the ring gives while it is worn
local RING = rq.item.define({ id = "mymod:ring", name = "Ring", type = "special", icon = 6331,
  price = 500, info = "Worn: the wearer knows the skill." })
rq.item.on_equip(function(ctx)
  if ctx.no == RING then rq.chara.grant(ctx.iic, SKILL, 0) rq.chara.recalc(ctx.iic) end
end)
rq.item.on_unequip(function(ctx)
  if ctx.no == RING then rq.chara.forget(ctx.iic, SKILL) rq.chara.recalc(ctx.iic) end
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.UnequipCtx`](../types/rq.UnequipCtx.md) `)` | Gets the item and the character. Its return value is not used. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.item.on_equip`](rq.item.md#rqitemon_equip)
