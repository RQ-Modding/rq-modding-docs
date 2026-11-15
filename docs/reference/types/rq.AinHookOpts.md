# rq.AinHookOpts

What `rq.ain.hook` takes.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `before` *(optional)* | `fun(h:` [`rq.AinHookCtx`](rq.AinHookCtx.md) `)` | Runs before the function, with its arguments. |
| `after` *(optional)* | `fun(h:` [`rq.AinHookCtx`](rq.AinHookCtx.md) `)` | Runs after it, with its return value. |
| `only` *(optional)* | `table<integer, integer\|integer[]>` | Argument positions (1 for the first) to a whole number or a list of 1 to 16: the callbacks run only for a call whose int argument at each position holds one of its values. At most 4 positions. Default: every call (since 2.55.0). |

## Used by

[`rq.ain.hook`](../api/rq.ain.md#rqainhook)
