# rq.ForgetCtx

What `rq.chara.on_forget` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `slot` | `integer` | The skill-list row. |
| `rank` | `integer` | The skill's rank. |
| `cost` | `integer` | The skill points the character paid for it; 0 when the game did not record it. |
| `caller` | `string` | The AIN function that removed it, or "lua" for `rq.chara.forget`. |

## Used by

[`rq.chara.on_forget`](../api/rq.chara.md#rqcharaon_forget)
