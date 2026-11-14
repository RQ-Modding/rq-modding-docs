# rq.ShopCopy

`since 2.49.0`

What `rq.shop.next` gives for each copy: `rq.item.info`'s row data and the copy's shop level.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ii` *(optional)* | `integer` | The instance on sale, on the first copy only. |
| `plus` | `integer` | The shop level at the end of the name, ① to ⑨ as 1 to 9; 0 for none. |

## Used by

[`rq.shop.next`](../api/rq.shop.md#rqshopnext)
