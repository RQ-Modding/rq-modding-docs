# rq.SpawnHandle

What `rq.spawn` returns, to follow or stop the job.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `done` | `boolean` | true once the job has ended, by returning, by an error or by `cancel`. |
| `ok` *(optional)* | `boolean` | Once done: true when the function returned, false on an error or a cancel. |
| `value` *(optional)* | `any` | Once done and ok: the first value the function returned. |
| `values` *(optional)* | `table` | Once done and ok: every value it returned, with `n` their count. |
| `error` *(optional)* | `any` | Once done and not ok: the error, or "cancelled". |
| `cancel` | `fun()` | Stops the job at its next wait; it never runs again. Does nothing once it is done. |

## Used by

[`rq.spawn`](../api/rq.md#rqspawn)
