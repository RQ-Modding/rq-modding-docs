# rq.ForgetCtx

What `rq.chara.on_forget` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `iic` | `integer` | The character's roster slot. |
| `skill` | `integer` | The skill number. |
| `slot` | `integer` | The skill-list row. |
| `rank` | `integer` | The skill's rank. |
| `cost` | `integer` | The purchase record (since 2.45.0): the skill points paid for the row's bought steps, in the skill window or through `rq.chara.learn`; -1 for a skill a mod gave (`rq.chara.grant`, `edit`'s `learn`, `learn` with `pay = false`); 0 when nothing was recorded (a starting skill, or one bought before loader 2.45.0 and not upgraded since). Before 2.45.0 it was always 0. |
| `caller` | `string` | The AIN function that removed it, or "lua" for `rq.chara.forget`. |

## Used by

[`rq.chara.on_forget`](../api/rq.chara.md#rqcharaon_forget)
