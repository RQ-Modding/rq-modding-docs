# rq.speed

`since 1.2.0`

Runs the game clock faster or slower than real time.

The game clock drives the game's timers and waits, Flash and parts animations, the 3D map,
rain and snow, and battle effects. Real time stays real: sound and music, the frame cap,
`rq.time_ms`, the loader's own dialogs and the play time written to the save. The factor works
on top of the game's own battle speed setting.

The factor is 1 on every boot, so a mod that wants another speed sets it each time it loads.

Sounds still play at normal speed, so at 3x a voice can last longer than its animation. Frames
of a Flash animation that are skipped still start their sounds.

## Functions

| Name | Summary |
| --- | --- |
| [`rq.speed.set`](#rqspeedset) | Sets the game clock to `factor` times real time. |
| [`rq.speed.get`](#rqspeedget) | Returns the factor the game clock runs at. |

### rq.speed.set

```lua
rq.speed.set(factor) -> number
```

`since 1.2.0`

Sets the game clock to `factor` times real time.

The clock does not jump: game time goes on from where it was, at the new rate.

```lua
rq.speed.set(2)                -- twice as fast
local now = rq.speed.set(100)  -- clamped: now == 8
```

| Parameter | Type | Description |
| --- | --- | --- |
| `factor` | `number` | How many times faster than real time. Clamped to 0.25..8. |

| Returns | Type | Description |
| --- | --- | --- |
| `factor` | `number` | The factor now in use, after clamping. |

See also: [`rq.speed.get`](rq.speed.md#rqspeedget)

### rq.speed.get

```lua
rq.speed.get() -> number
```

`since 1.2.0`

Returns the factor the game clock runs at.

| Returns | Type | Description |
| --- | --- | --- |
| `factor` | `number` | 1 unless a mod called `rq.speed.set`. |

See also: [`rq.speed.set`](rq.speed.md#rqspeedset)
