# rq.OfferCtx

What `rq.chara.on_offer` gets for the character whose buy list the game just filled.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `no` | `integer` | The character number (`Ｃ番号`). |
| `level` | `integer` | The character's level. |
| `class` | `integer` | The character's class (see `rq.CharaFields.class`). |
| `preview` | `boolean` | true when the list is made inside a try on a kept character (`rq.chara.learnable`'s `after`, `rq.chara.price`), which the loader puts back after. Since 2.66.0. |

## Used by

[`rq.chara.on_offer`](../api/rq.chara.md#rqcharaon_offer)
