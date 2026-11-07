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
growth. Its icon must be 6500 to 6516 or 6632, or the familiar never takes a turn.

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
| [`rq.item.set`](#rqitemset) | Writes an instance's fields. |
| [`rq.item.transform`](#rqitemtransform) | Turns an instance into another item, keeping its place and owner. |
| [`rq.item.edit`](#rqitemedit) | Patches an item number, for every new instance and the ones in the save. |
| [`rq.item.equip`](#rqitemequip) | Equips an existing instance on a character (`キャラ_装備設定`). |
| [`rq.item.remove`](#rqitemremove) | Deletes an instance (`Ｉ削除`), taking it off its owner first. |
| [`rq.item.equipped`](#rqitemequipped) | Returns the instances a character has equipped. |
| [`rq.item.number`](#rqitemnumber) | Returns the item number of an instance. |
| [`rq.item.id_of`](#rqitemid_of) | Returns the text id of a defined item number. |

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

## Events

| Name | Summary |
| --- | --- |
| [`rq.item.on_create`](#rqitemon_create) | Calls `fn` after any item instance is created (`Ｉ生成`), game or mod. |

### rq.item.on_create

```lua
rq.item.on_create(fn) -> fun()
```

`since 0.8.0` `changed 0.23.0`

Calls `fn` after any item instance is created (`Ｉ生成`), game or mod.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx: {ii: integer, no: integer, id?: string})` | Gets the instance, its number, and its text id for a mod's item. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.
