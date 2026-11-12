# rq.QuestBonus

A quest bonus in `rq.QuestRun.bonuses`.

`feats` counts the adventure achievements found, `level_ups` the levels gained in the quest and
`enemies` the placed enemies beaten. Each stops at its maximum, and each at its maximum adds one
bonus to every rare item appraised at the end.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `count` | `integer` | The count, 0 to `max`. |
| `max` | `integer` | The maximum. |

## Used by

[`rq.QuestRun`](rq.QuestRun.md)
