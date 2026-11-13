# rq.BoostRow

`since 2.48.0`

One Boost, from `rq.chara.boosts`.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `skill` | `integer` | The skill number: Stamina, Attack and Magic Boost (276, 277, 278) and their second versions (455, 456, 457), then Accuracy, Evasion, Critical, Resilience and Stun Boost (279 to 283). |
| `step` | `integer` | 1 for a first version and the five alone, 2 for a second version. |
| `first` *(optional)* | `integer` | For a second version, the first one (457's is 278); nil for the rest. |
| `kept` | `boolean` | Whether the character keeps its effect without the skill now: its rank 4 was reached in the third world and the game's reset has not run since. Always false in another world. |

## Used by

[`rq.chara.boosts`](../api/rq.chara.md#rqcharaboosts)
