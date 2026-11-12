# rq.TrapWeights

The weights of the trap kinds, from `rq.dungeon.traps()`: each 0 to 10.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `shroom` | `integer` | Sloth shrooms: a random member leaves the party (never with one member). |
| `shock` | `integer` | An electric current: the party loses 25% of its HP. |
| `alarm` | `integer` | An alarm: a fight follows. |
| `pit` | `integer` | A pitfall: the party falls (a floor down where the quest has floors). |

## Used by

[`rq.dungeon.traps`](../api/rq.dungeon.md#rqdungeontraps)
