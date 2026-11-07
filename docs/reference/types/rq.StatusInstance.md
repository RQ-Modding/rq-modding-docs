# rq.StatusInstance

`since 2.2.0`

A state on one character, from `rq.status.add`, `get` and `list`.

It is the live record: a mod may change `turns`, `power` and `data`. The icon shows a change of
`turns` the next time `rq.status` touches the state.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | The state's id. |
| `iic` | `integer` | The bearer's roster slot. |
| `kind` | `"bad"\|"good"` | From the definition. |
| `turns` *(optional)* | `integer` | The bearer's turns left; nil for the whole fight. |
| `stacks` | `integer` | How many stacks, 1 or more. |
| `power` | `number` | What `add` gave in `opts.power`, for the definition's callbacks. Default 0. |
| `source` | `integer` | Who put it on (`opts.source`); 0 when not given. |
| `data` | `table` | A table for the mod's own values. |

## Used by

[`rq.StatusDef`](rq.StatusDef.md), [`rq.status.add`](../api/rq.status.md#rqstatusadd), [`rq.status.get`](../api/rq.status.md#rqstatusget), [`rq.status.list`](../api/rq.status.md#rqstatuslist), [`rq.status.on_add`](../api/rq.status.md#rqstatuson_add), [`rq.status.on_remove`](../api/rq.status.md#rqstatuson_remove)
