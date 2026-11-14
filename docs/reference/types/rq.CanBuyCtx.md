# rq.CanBuyCtx

What an `rq.shop.on_can_buy` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` | `integer` | The item instance on the shop's rack. |
| `no` | `integer` | Its item number. |
| `id` *(optional)* | `string` | Its text id, when a mod defined the item. |
| `name` | `string` | The item's name. |
| `price` | `integer` | Its price, in gold. |
| `to` | `"vault"\|"character"` | Where it goes: the vault, or a party member it is dragged onto (`rq.item.buy`'s `chara`). |

## Used by

[`rq.shop.on_can_buy`](../api/rq.shop.md#rqshopon_can_buy)
