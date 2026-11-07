# rq.CounterGuardCtx

What `rq.counter.on_guard_counter` gets.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `guarded` | `boolean` | Ally Guard redirected this hit (the game's `FA[77]` is 1). |
| `defender` | `integer` | The roster slot that took the hit: the guard when redirected. |
| `attacker` | `integer` | The attacker's roster slot. |
| `skill` | `integer` | The incoming skill number. |
| `rate` | `integer` | The Counter rate before the game's guard check clears it. |

## Used by

[`rq.counter.on_guard_counter`](../api/rq.counter.md#rqcounteron_guard_counter)
