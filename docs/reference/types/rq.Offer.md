# rq.Offer

A row `rq.chara.on_offer` adds to the skill buy list.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number. |
| `cost` | `integer` | The cost the game's price curve starts from. |
| `level` | `integer` | The level needed to buy it; below it the row shows the game's "Cannot learn yet" text. |
| `points` *(optional)* | `integer` | The final price shown. It replaces the game's own price, its rise per use bought and its cap of 9. Since 0.13.0. |

## Used by

[`rq.chara.on_offer`](../api/rq.chara.md#rqcharaon_offer)
