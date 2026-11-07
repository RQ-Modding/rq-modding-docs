# rq.LootAdd

An item for `rq.loot.add`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `item` | `string\|integer` | An item number or text id. |
| `pool` *(optional)* | `"item"\|"special"\|"rare"\|"ultra"\|"gear"` | The pool. Default: every pool. "gear" since 0.15.0. |
| `chance` *(optional)* | `number` | The percent chance on each roll of the pool; may be a fraction. Default 1. |
| `unique` *(optional)* | `boolean` | Skip it when the player already owns one. Default false. |

## Used by

[`rq.loot.add`](../api/rq.loot.md#rqlootadd)
