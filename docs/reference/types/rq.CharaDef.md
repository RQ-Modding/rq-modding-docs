# rq.CharaDef

A character template for `rq.chara.define`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The text id, such as "mymod:alice", under 64 bytes. |
| `lines` *(optional)* | `string[]` | Battle lines 1 to 6. |
| `on_create` *(optional)* | `fun(iic: integer)` | Runs when this character is created. |

## Used by

[`rq.chara.define`](../api/rq.chara.md#rqcharadefine)
