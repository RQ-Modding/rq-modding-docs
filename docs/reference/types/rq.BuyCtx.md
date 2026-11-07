# rq.BuyCtx

What an `rq.shop.on_buy` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance that was bought. |
| `no` | `integer` | Its item number. |
| `id` *(optional)* | `string` | Its text id, when a mod defined the item. |
| `price` | `integer` | The price paid, in gold. |
| `name` | `string` | The item's name. |

## Used by

[`rq.shop.on_buy`](../api/rq.shop.md#rqshopon_buy)
