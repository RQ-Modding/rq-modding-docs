# rq.loot

`since 0.2.0`

Chest loot: what the pools roll, and the items the player will find, known in advance.

A chest's loot comes from five pool functions: `item` (`持ち物を選ぶ`), `special` (`特殊を選ぶ`),
`rare` (`レアアイテムを選ぶ`), `ultra` (`ウルトラレアを選ぶ`) and `gear` (`武器防具を選ぶ`, weapons and
armor). `rq.loot.install` rolls each chest's item when it is placed, so `rq.loot.list` can show it.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.loot.add`](#rqlootadd) | Adds an item to the chest pools' rolls. |
| [`rq.loot.remove`](#rqlootremove) | Keeps an item from ever coming out of a chest. |
| [`rq.loot.install`](#rqlootinstall) | Rolls each chest's item when the chest is placed, so it is known in advance. |
| [`rq.loot.list`](#rqlootlist) | Lists the items waiting for the player: the Magnum's (when it holds one), then the locked chests'. |

### rq.loot.add

```lua
rq.loot.add(spec)
```

`since 0.9.0` `changed 0.15.0`

Adds an item to the chest pools' rolls.

Each roll of the pool has `chance` percent to give this item instead of the game's.

```lua
rq.loot.add({ item = "mymod:charm", pool = "rare", chance = 2.5, unique = true })
```

| Parameter | Type | Description |
| --- | --- | --- |
| `spec` | [`rq.LootAdd`](../types/rq.LootAdd.md) | The item and its chance. |

> Changed in 0.15.0: Added the "gear" pool; no `pool` includes it.

### rq.loot.remove

```lua
rq.loot.remove(who, opts)
```

`since 0.9.0`

Keeps an item from ever coming out of a chest.

The pool rolls 0 for it, so the game tries the next pool.

| Parameter | Type | Description |
| --- | --- | --- |
| `who` | `string\|integer` | An item number or text id. |
| `opts` *(optional)* | `{pool?: "item"\|"special"\|"rare"\|"ultra"}` | `pool`: only this pool. Default: every pool. |

### rq.loot.install

```lua
rq.loot.install() -> boolean
```

`since 0.2.0`

Rolls each chest's item when the chest is placed, so it is known in advance.

It skips the game's roll at opening and sets the map's chest flags. Red chests keep the game's
chance and still explode on a fail, which loses the item. It opens no screen.

It changes when the game rolls, so it stays a mod's own choice: `rq.loot.list`, which needs it,
does not make it.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the patch is in place. |

### rq.loot.list

```lua
rq.loot.list() -> rq.LootItem[]
```

`since 0.2.0`

Lists the items waiting for the player: the Magnum's (when it holds one), then the locked chests'.

Needs `rq.loot.install`; before it the list is empty.

| Returns | Type | Description |
| --- | --- | --- |
| `items` | [`rq.LootItem`](../types/rq.LootItem.md) `[]` | The items. |

## Events

| Name | Summary |
| --- | --- |
| [`rq.loot.on_pick`](#rqlooton_pick) | Calls `fn` after each roll of a chest pool, to replace the item. |

### rq.loot.on_pick

```lua
rq.loot.on_pick(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0`

Calls `fn` after each roll of a chest pool, to replace the item.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx: {pool: string, item: integer}): integer\|string\|nil` | Returns another item number or text id, 0 for nothing, or nil to keep it. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.
