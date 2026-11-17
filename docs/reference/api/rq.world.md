# rq.world

The world and the game's world transfer.

The game has three worlds. At the end of a world it sets the new world, then resets much of the run
(`ワールド切り替え処理`): every quest and its map flags, the shop's stock and the quest list made
again, the quest storage emptied, every event, three skills of three characters, ten key items
(255 to 263 and 267), in world 3 the "cannot be taken off" mark on every item, the fame rank divided
by 3 and the fame points, the donations count (0) and Frostbuy's goal (25), the count of cleared
quests, Rance Castle closed, and about 40 of the game's flags. Characters, their levels and skills,
gold and the items in the vault and the storage stay.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.world.current`](#rqworldcurrent) | Returns the world being played. |

### rq.world.current

```lua
rq.world.current() -> integer|nil
```

`since 2.23.0` `changed 2.56.1`

Returns the world being played.

```lua
if rq.world.current() == 3 then rq.log("last world") end
```
title, and this answered 1 there. A save counts as loaded from the game's load (the autosave or
the suspend save) or a new game's first quest until the title shows again.

| Returns | Type | Description |
| --- | --- | --- |
| `world` | `integer\|nil` | 1 to 3, or nil before a save is loaded (at the title too). |

> Changed in 2.56.1: nil at the title: the game sets the world to 1 when it starts, before the

## Events

| Name | Summary |
| --- | --- |
| [`rq.world.on_transfer`](#rqworldon_transfer) | Registers a function that runs at a world transfer, before the game's reset. |
| [`rq.world.on_transfer_after`](#rqworldon_transfer_after) | Registers a function that runs at a world transfer, after the game's reset. |

### rq.world.on_transfer

```lua
rq.world.on_transfer(fn) -> fun()
```

`since 2.23.0`

Registers a function that runs at a world transfer, before the game's reset.

The old values are still there: read here what a mod wants to keep, and write it back in
`rq.world.on_transfer_after`. A write made here is reset with the rest. An error is logged.

```lua
local kept
rq.world.on_transfer(function(ctx) kept = rq.shop.donations() end)
rq.world.on_transfer_after(function(ctx) rq.shop.set_donations(kept, (kept // 25 + 1) * 25) end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.TransferContext`](../types/rq.TransferContext.md) `)` | Runs before the reset. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.world.on_transfer_after`](rq.world.md#rqworldon_transfer_after)

### rq.world.on_transfer_after

```lua
rq.world.on_transfer_after(fn) -> fun()
```

`since 2.23.0`

Registers a function that runs at a world transfer, after the game's reset.

Values written here last into the new world. An error is logged.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.TransferContext`](../types/rq.TransferContext.md) `)` | Runs after the reset. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

See also: [`rq.world.on_transfer`](rq.world.md#rqworldon_transfer)
