# rq.shop

`since 0.2.0` `changed 2.35.0`

Adds stock to Frostbuy, the item shop, and reports purchases.

The game refills the shop's stock in `Ｔアイテム屋` every time the shop opens. The first `on_stock`,
`in_stock` or `stock` wraps the end of that function so `on_stock` callbacks run right after the
game's own refill. The calls take an item number or a text id.

```lua
rq.shop.on_stock(function()
  if not rq.shop.in_stock(306) then rq.shop.stock(306) end -- Skill Again
end)
```

## Functions

| Name | Summary |
| --- | --- |
| [`rq.shop.install`](#rqshopinstall) | Wraps the end of `Ｔアイテム屋` so `on_stock` callbacks run and `stock` works. |
| [`rq.shop.in_stock`](#rqshopin_stock) | Returns whether an item is already on sale in the shop. |
| [`rq.shop.stock`](#rqshopstock) | Puts one item on sale, through the game's `Ｔアイテム屋／入荷品`. |
| [`rq.shop.donations`](#rqshopdonations) | Returns the donations count and Frostbuy's reward goal (`◆寄付`, `◆寄付ボーナス`). |
| [`rq.shop.set_donations`](#rqshopset_donations) | Writes the donations count, and the reward goal when given. |

### rq.shop.install

```lua
rq.shop.install() -> boolean
```

`since 0.2.0` `changed 2.35.0`

Wraps the end of `Ｔアイテム屋` so `on_stock` callbacks run and `stock` works.

Not needed since 2.35.0: each call that needs it places it the first time, and raises this
call's error there when it cannot. Calling it still does no harm.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the hook is in place; a failure raises an error. |

> Changed in 2.35.0: Not needed: `on_stock`, `in_stock` and `stock` make it.

### rq.shop.in_stock

```lua
rq.shop.in_stock(no) -> boolean
```

`since 0.2.0` `changed 0.9.0` `changed 2.35.0`

Returns whether an item is already on sale in the shop.

It asks the game whether an instance of that item has the shop's existence value, 6.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | An item number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `stocked` | `boolean` | true when the shop already sells it. |

> Changed in 0.9.0: Accepts a text id.

> Changed in 2.35.0: Answers without `rq.shop.install`; before it, it always said false.

### rq.shop.stock

```lua
rq.shop.stock(no) -> integer
```

`since 0.2.0` `changed 0.9.0` `changed 0.26.0` `changed 2.35.0` `changed 2.47.0`

Puts one item on sale, through the game's `Ｔアイテム屋／入荷品`.

Raises an error for an unknown item, or for a value that is not a number or a text id.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | An item number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The new instance, or 0 when the shop already had the item or the game refused it. |

> Changed in 0.9.0: Accepts a text id.

> Changed in 0.26.0: An unknown item raises an error instead of closing the game.

> Changed in 2.35.0: No `rq.shop.install` needed; it raised an error before it.

> Changed in 2.47.0: While the shop shows, the item is on its list at once (it waited for the next visit).

### rq.shop.donations

```lua
rq.shop.donations() -> integer, integer
```

`since 2.23.0`

Returns the donations count and Frostbuy's reward goal (`◆寄付`, `◆寄付ボーナス`).

DONATE in the vault adds to the count. On a visit, when Frostbuy's talk about donations has been
seen and the count is at the goal or above, she gives one reward and the goal goes up by 25. A world
transfer sets the count to 0 and the goal to 25.

```lua
local count, goal = rq.shop.donations()
rq.log(("donated %d, next reward at %d"):format(count, goal))
```

| Returns | Type | Description |
| --- | --- | --- |
| `count` | `integer` | The donations count. |
| `goal` | `integer` | The count at which Frostbuy gives her next reward. |

See also: [`rq.shop.set_donations`](rq.shop.md#rqshopset_donations)

### rq.shop.set_donations

```lua
rq.shop.set_donations(count, goal)
```

`since 2.23.0`

Writes the donations count, and the reward goal when given.

Frostbuy reads both on a visit (see `rq.shop.donations`). Two things to know:
- A count at the goal or above gives a reward on the next visit. To set a count without one, set
  the goal above it, as `(count // 25 + 1) * 25` does.
- While her talk about donations has not been seen, a count other than 0 plays the talk on a visit
  and sets the goal to 25. Mark it seen with `rq.scene.seen` to skip it.

Raises an error for a count or goal that is not a whole number, 0 or more.

```lua
local count = 60
rq.shop.set_donations(count, (count // 25 + 1) * 25) -- 60, next reward at 75
```

| Parameter | Type | Description |
| --- | --- | --- |
| `count` | `integer` | The donations count. |
| `goal` *(optional)* | `integer` | The reward goal. Default: kept as it is. |

See also: [`rq.shop.donations`](rq.shop.md#rqshopdonations)

## Events

| Name | Summary |
| --- | --- |
| [`rq.shop.on_stock`](#rqshopon_stock) | Registers a function that runs after the game refills the shop's stock. |
| [`rq.shop.on_buy`](#rqshopon_buy) | Registers a function that runs after each Frostbuy purchase. |

### rq.shop.on_stock

```lua
rq.shop.on_stock(fn) -> fun()
```

`since 0.2.0` `changed 0.9.0` `changed 0.23.0` `changed 2.35.0`

Registers a function that runs after the game refills the shop's stock.

It runs on every shop open. Up to 16 callbacks. An error in a callback is written to the log and the
others still run.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Adds stock, usually with `rq.shop.stock`. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.9.0: Keeps every mod's callback (before, the last one replaced the others).

> Changed in 0.23.0: Returns a remover.

> Changed in 2.35.0: Wraps the shop itself; before `rq.shop.install` it never ran.

See also: [`rq.shop.stock`](rq.shop.md#rqshopstock)

### rq.shop.on_buy

```lua
rq.shop.on_buy(fn) -> fun()
```

`since 0.9.0` `changed 0.23.0`

Registers a function that runs after each Frostbuy purchase.

It wraps the end of `T_Shop@buyItem` the first time it is used, so it needs no `install`. Use it to
count purchases, and raise the next price in `on_stock`. Up to 16 callbacks; an error in one is
written to the log.

```lua
rq.shop.on_buy(function(ctx)
  rq.log("bought", ctx.name, "for", ctx.price)
end)
```

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun(ctx:` [`rq.BuyCtx`](../types/rq.BuyCtx.md) `)` | Gets the purchase. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.23.0: Returns a remover.
