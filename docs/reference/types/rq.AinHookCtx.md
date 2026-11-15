# rq.AinHookCtx

What an `rq.ain.hook` callback gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `name` | `string` | The function's name. |
| `args` | `table` | The arguments by position; change one to change what the function gets. References and structs are nil. |
| `skip` *(optional)* | `boolean` | `before` only: true keeps the function from running. |
| `result` *(optional)* | `any` | In `before`: what a skipped function returns. In `after`: the return value, which may be changed. |

## Used by

[`rq.AinHookOpts`](rq.AinHookOpts.md), [`rq.scene.after`](../api/rq.scene.md#rqsceneafter), [`rq.scene.before`](../api/rq.scene.md#rqscenebefore), [`rq.scene.replace`](../api/rq.scene.md#rqscenereplace)
