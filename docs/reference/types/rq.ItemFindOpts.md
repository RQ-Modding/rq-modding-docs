# rq.ItemFindOpts

What `rq.item.find` and `rq.item.count` take.

A place is `"vault"` (7), `"storage"` (11), `"quest"` (8, quest storage), `"worn"` (on a
character: the game's place 20 and up), or the game's place number.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `place` *(optional)* | `string\|integer\|(string\|integer)[]` | One place or a list of up to 8. Default `{ "worn", "vault", "storage" }`, the places the game counts. |
| `lock` *(optional)* | `boolean` | false leaves out items locked in the vault, true keeps only those. Default: both. |

## Used by

[`rq.item.count`](../api/rq.item.md#rqitemcount), [`rq.item.find`](../api/rq.item.md#rqitemfind)
