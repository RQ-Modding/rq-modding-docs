# rq.MonsterDef

What `rq.monster.define` takes: a game monster to start from, then any field of `rq.MonsterEdit`
for the mod's monster.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The text id, such as "mymod:king_roach". It becomes the monster's number, from 1000 to 9999. |
| `base` | `integer` | The game monster whose data and look it starts from (`rq.ids.monster`), below 1000. |
| `capture` *(optional)* | [`rq.MonsterCapture`](rq.MonsterCapture.md) | What a capture skill gives; without it the monster always escapes a capture. |

## Used by

[`rq.monster.define`](../api/rq.monster.md#rqmonsterdefine)
