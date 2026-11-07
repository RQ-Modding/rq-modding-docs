# rq.shop

`since 0.2.0`

Adds stock to Frostbuy, the item shop, and reports purchases.

The game refills the shop's stock in `Ｔアイテム屋` every time the shop opens. `rq.shop.install` wraps
the end of that function so `on_stock` callbacks run right after the game's own refill. Without a
hook the shop keeps only the game's stock. The calls take an item number or a text id.

```lua
rq.shop.install()
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

### rq.shop.install

```lua
rq.shop.install() -> boolean
```

`since 0.2.0`

Wraps the end of `Ｔアイテム屋` so `on_stock` callbacks run and `stock` works.

Calling it again is harmless.

| Returns | Type | Description |
| --- | --- | --- |
| `ok` | `boolean` | true when the hook is in place; false when a game function is missing (see the log). |

### rq.shop.in_stock

```lua
rq.shop.in_stock(no) -> boolean
```

`since 0.2.0` `changed 0.9.0`

Returns whether an item is already on sale in the shop.

It asks the game whether an instance of that item has the shop's existence value, 6.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | An item number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `stocked` | `boolean` | true when the shop already sells it. |

> Changed in 0.9.0: Accepts a text id.

### rq.shop.stock

```lua
rq.shop.stock(no) -> integer
```

`since 0.2.0` `changed 0.9.0` `changed 0.26.0`

Puts one item on sale, through the game's `Ｔアイテム屋／入荷品`.

Raises an error before `rq.shop.install`, for an unknown item, or for a value that is not a number
or a text id.

| Parameter | Type | Description |
| --- | --- | --- |
| `no` | `integer\|string` | An item number or text id. |

| Returns | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The new instance, or 0 when the shop already had the item or the game refused it. |

> Changed in 0.9.0: Accepts a text id.

> Changed in 0.26.0: An unknown item raises an error instead of closing the game.

## Events

| Name | Summary |
| --- | --- |
| [`rq.shop.on_stock`](#rqshopon_stock) | Registers a function that runs after the game refills the shop's stock. |
| [`rq.shop.on_buy`](#rqshopon_buy) | Registers a function that runs after each Frostbuy purchase. |

### rq.shop.on_stock

```lua
rq.shop.on_stock(fn) -> fun()
```

`since 0.2.0` `changed 0.9.0` `changed 0.23.0`

Registers a function that runs after the game refills the shop's stock.

It runs on every shop open, once `rq.shop.install` was called; before that it never runs. Up to 16
callbacks. An error in a callback is written to the log and the others still run.

| Parameter | Type | Description |
| --- | --- | --- |
| `fn` | `fun()` | Adds stock, usually with `rq.shop.stock`. |

| Returns | Type | Description |
| --- | --- | --- |
| `remove` | `fun()` | Removes this callback. |

> Changed in 0.9.0: Keeps every mod's callback (before, the last one replaced the others).

> Changed in 0.23.0: Returns a remover.

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
